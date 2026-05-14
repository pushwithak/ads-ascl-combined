"""Stage-5 Experiment Analysis Agent (closed-loop).

Stage 5 is a thin orchestrator:

1.  Call ``job_status`` (deterministic, no LLM).  If the job is not
    complete, return a free-form ``TextOutput`` with the status.
2.  Call ``job_plot`` to get ``{experiment_id: [url, ...]}``.
3.  Build context: Stage-1 hypothesis + Stage-3 experiment spec +
    an **experiment–figure mapping** that tells the analyzer which
    image slugs belong to which experiment.
4.  Hand the (flattened) URLs + context to the generic
    :class:`~akd_ext.agents.image_analyzer.ImageAnalyzerAgent`.
5.  Wrap the analyzer's output in a :class:`ExperimentAnalysisOutputSchema`.

The agent itself never invokes the LLM — all "intelligence" lives in
:class:`ImageAnalyzerAgent`.  Stage 5's job is the deterministic MCP I/O
and the completion-status branching around it.
"""

from __future__ import annotations

import json
import os
from collections.abc import AsyncIterator
from typing import Any, Literal, cast

import httpx
from loguru import logger
from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client
from pydantic import Field

from akd._base import (
    CompletedEvent,
    CompletedEventData,
    InputSchema,
    OutputSchema,
    PartialOutputEvent,
    RunContext,
    RunningEvent,
    StartingEvent,
    StartingEventData,
    StreamEvent,
    TextOutput,
)
from akd_ext.agents._base import OpenAIBaseAgent
from akd_ext.agents.closed_loop._base import ClosedLoopStageConfig
from akd_ext.agents.image_analyzer import (
    ImageAnalyzerAgent,
    ImageAnalyzerConfig,
    ImageAnalyzerInputSchema,
    ImageAnalyzerOutputSchema,
)

__all__ = [
    "ExperimentAnalysisAgent",
    "ExperimentAnalysisConfig",
    "ExperimentAnalysisInputSchema",
    "ExperimentAnalysisOutputSchema",
]

_COMPLETE = {"completed", "finished", "done", "success"}
_FAILED = {"failed", "cancelled", "canceled", "error"}


# -----------------------------------------------------------------------------
# Configuration / Schemas
# -----------------------------------------------------------------------------


class ExperimentAnalysisConfig(ClosedLoopStageConfig):
    """Configuration for the Stage-5 Data Analysis Agent."""

    mcp_url: str = Field(
        default_factory=lambda: os.environ.get("CM1_MCP_URL", "https://fm.prism.nasa-impact.net/akd/cm1-mcp"),
        description="CM1 Temporal MCP server URL for job_status / job_plot calls.",
    )
    default_user_name: str = Field(
        default="igurung",
        description="Fallback user_name passed to job_plot when not provided in the input.",
    )
    plot_read_timeout_seconds: float = Field(
        default=600.0,
        description="Read timeout (s) for job_plot — plot generation can be slow.",
    )
    analyzer_config: ImageAnalyzerConfig = Field(
        default_factory=ImageAnalyzerConfig,
        description="Forwarded to the underlying ImageAnalyzerAgent.",
    )


class ExperimentAnalysisInputSchema(InputSchema):
    """Input schema for the Stage-5 Data Analysis Agent."""

    job_id: str = Field(..., description="Job ID returned by Stage 4.")
    workspace_name: str | None = Field(
        default=None,
        description="Workspace name. If omitted, derived from the job_status payload.",
    )
    user_name: str | None = Field(
        default=None,
        description="Optional user name. Falls back to config.default_user_name.",
    )
    hypothesis: str = Field(
        default="",
        description="Stage-1 feasibility report (CapabilityFeasibilityMapper output).",
    )
    experiment_spec: str = Field(
        default="",
        description="Stage-3 implementation report (ExperimentImplementation output).",
    )
    skip_status_check: bool = Field(
        default=False,
        description="Skip job_status check and go straight to job_plot.",
    )


class ExperimentAnalysisOutputSchema(OutputSchema):
    """Stage-5 structured output (only emitted when the job is complete).

    Stage 5's contract is "give me the report" — so the deliverable is
    ``markdown``.  ``status`` and ``message`` are kept as a marker channel
    so callers can short-circuit on ``status != "completed"`` without
    string-parsing the markdown.  Per-figure structured analyses are not
    surfaced — they live inside the rendered Markdown and would otherwise
    duplicate the same data twice.
    """

    __response_field__ = "markdown"

    status: Literal["completed"] = Field(default="completed")
    message: str = Field(default="Experiment Finished and Analysis is ready")
    markdown: str = Field(default="")


# -----------------------------------------------------------------------------
# MCP helper — single function, called twice (job_status, job_plot)
# -----------------------------------------------------------------------------


async def _mcp_call(
    *,
    url: str,
    api_key: str,
    tool: str,
    args: dict[str, Any],
    read_timeout: float,
) -> dict[str, Any]:
    """Invoke an MCP tool via streamable-HTTP and return the parsed JSON dict.

    Falls back to the structuredContent dict when present, otherwise parses
    the concatenated text content. Returns ``{}`` if neither yields a dict.
    Tolerates servers that wrap the real payload as a JSON string under
    ``"payload"`` — that gets unwrapped into ``"payload_parsed"``.
    """
    timeout = httpx.Timeout(connect=30.0, read=read_timeout, write=60.0, pool=60.0)
    async with httpx.AsyncClient(headers={"X-API-Key": api_key}, timeout=timeout) as http_client:
        async with streamable_http_client(url=url, http_client=http_client) as (read, write, _):
            async with ClientSession(read, write) as session:
                await session.initialize()
                res = await session.call_tool(tool, args)

    structured = getattr(res, "structuredContent", None)
    if isinstance(structured, dict):
        return structured

    text = "".join(getattr(b, "text", "") or "" for b in (getattr(res, "content", None) or [])).strip()
    if not text:
        return {}
    try:
        obj = json.loads(text)
    except json.JSONDecodeError:
        return {"raw": text}
    if isinstance(obj, dict) and isinstance(obj.get("payload"), str):
        try:
            obj["payload_parsed"] = json.loads(obj["payload"])
        except json.JSONDecodeError:
            pass
    return obj if isinstance(obj, dict) else {}


# -----------------------------------------------------------------------------
# Experiment Analysis Agent
# -----------------------------------------------------------------------------


class ExperimentAnalysisAgent(
    OpenAIBaseAgent[ExperimentAnalysisInputSchema, ExperimentAnalysisOutputSchema],
):
    """Stage-5 orchestrator. Status check → URL fetch → delegate to ImageAnalyzerAgent."""

    input_schema = ExperimentAnalysisInputSchema
    output_schema = ExperimentAnalysisOutputSchema | TextOutput
    config_schema = ExperimentAnalysisConfig

    # -- Helpers -------------------------------------------------------

    @property
    def _api_key(self) -> str:
        key = os.environ.get("CM1_MCP_API_KEY")
        if not key:
            raise RuntimeError("CM1_MCP_API_KEY is not set; cannot reach the CM1 MCP.")
        return key

    @staticmethod
    def _workspace_from(payload: dict[str, Any]) -> str | None:
        """Extract workspace_name from a job_status payload, top-level or wrapped."""
        for blob in (payload, payload.get("payload_parsed") or {}):
            if isinstance(blob, dict):
                ws = blob.get("workspace_name")
                if isinstance(ws, str) and ws:
                    return ws
        return None

    @staticmethod
    def _flatten(plot_urls: dict[str, list[str]]) -> list[str]:
        """``{exp_id: [urls]}`` → flat list, preserving order."""
        return [u for urls in plot_urls.values() for u in urls if isinstance(u, str)]

    @staticmethod
    def _build_experiment_map_context(experiment_urls: dict[str, list[str]]) -> str:
        """Build a markdown section mapping experiment IDs → figure slugs.

        This is injected into the ImageAnalyzer context so the LLM knows
        which figures belong to which experiment.
        """
        if not experiment_urls:
            return ""
        lines = [
            "## Experiment–Figure Mapping",
            "",
            "Each figure belongs to a specific experiment.  Use this mapping",
            "to identify which experiment produced each figure and label your",
            "analysis accordingly.",
            "",
        ]
        for exp_id, urls in experiment_urls.items():
            slugs = [url.rstrip("/").split("/")[-1].split("?")[0] for url in urls if isinstance(url, str)]
            lines.append(f"- **{exp_id}** ({len(slugs)} figures): {', '.join(slugs)}")
        return "\n".join(lines)

    @staticmethod
    def _build_context(
        params: ExperimentAnalysisInputSchema,
        experiment_urls: dict[str, list[str]] | None = None,
    ) -> str:
        """Concatenate hypothesis + experiment_spec + experiment–figure map."""
        parts: list[str] = []
        if params.hypothesis.strip():
            parts.append(f"## Hypothesis / Feasibility Report\n\n{params.hypothesis.strip()}")
        if params.experiment_spec.strip():
            parts.append(f"## Experiment Specification\n\n{params.experiment_spec.strip()}")
        if experiment_urls:
            exp_map = ExperimentAnalysisAgent._build_experiment_map_context(experiment_urls)
            if exp_map:
                parts.append(exp_map)
        return "\n\n---\n\n".join(parts)

    @staticmethod
    def _extract_status(payload: dict[str, Any]) -> str:
        """Extract status from top-level or wrapped payload_parsed."""
        for blob in (payload, payload.get("payload_parsed") or {}):
            if isinstance(blob, dict):
                s = blob.get("status")
                if isinstance(s, str) and s:
                    return s.lower()
        return "unknown"

    async def _check_job(self, job_id: str) -> dict[str, Any] | TextOutput:
        """MCP job_status → payload dict, or TextOutput on error / not-complete."""
        try:
            payload = await _mcp_call(
                url=self.config.mcp_url, api_key=self._api_key,
                tool="job_status", args={"job_id": job_id}, read_timeout=60.0,
            )
        except Exception as exc:
            logger.warning(f"[Stage5] job_status failed: {exc!r}")
            return TextOutput(content=f"Could not reach CM1 MCP for `{job_id}`: {exc}")

        logger.info(f"[Stage5] job_status payload keys: {list(payload.keys())}")
        status = self._extract_status(payload)
        if status in _FAILED:
            return TextOutput(content=f"Job `{job_id}` failed (status=`{status}`). No analysis.")
        if status not in _COMPLETE:
            return TextOutput(
                content=f"Job `{job_id}` is still running (status=`{status}`). "
                "Re-run Stage 5 once the batch completes."
            )
        return payload

    def _resolve_workspace(
        self, params: ExperimentAnalysisInputSchema, payload: dict[str, Any],
    ) -> tuple[str, str] | TextOutput:
        """Return ``(workspace, user)`` or a TextOutput error."""
        workspace = params.workspace_name or self._workspace_from(payload)
        if not workspace:
            return TextOutput(
                content=f"Could not determine `workspace_name` for `{params.job_id}`. "
                "Pass it explicitly via the input schema."
            )
        return workspace, params.user_name or self.config.default_user_name

    async def _fetch_plot_urls(self, job_id: str, workspace: str, user: str) -> dict[str, list[str]] | TextOutput:
        """MCP job_plot → ``{experiment_id: [urls]}`` dict, or TextOutput on error / empty.

        The keys are experiment IDs (e.g. ``EXP_stability_baseline``).
        Callers use :meth:`_flatten` when they need a plain URL list.
        """
        try:
            plot_payload = await _mcp_call(
                url=self.config.mcp_url, api_key=self._api_key,
                tool="job_plot",
                args={"job_id": job_id, "workspace_name": workspace, "user_name": user},
                read_timeout=self.config.plot_read_timeout_seconds,
            )
        except Exception as exc:
            logger.warning(f"[Stage5] job_plot failed: {exc!r}")
            return TextOutput(content=f"Failed to fetch plots for `{job_id}`: {exc}")

        plot_urls = {
            k: v for k, v in plot_payload.items()
            if isinstance(v, list) and not k.startswith("_") and k != "payload"
        }
        n_figures = len(self._flatten(plot_urls))
        if not n_figures:
            return TextOutput(content=f"Job `{job_id}` is complete but `job_plot` returned no figures.")
        logger.info(f"[Stage5] job_id={job_id} workspace={workspace!r} figures={n_figures} groups={list(plot_urls.keys())}")
        return plot_urls

    # -- Pipeline (_arun) ----------------------------------------------

    async def _arun(
        self, params: ExperimentAnalysisInputSchema, run_context: RunContext, **kwargs: Any
    ) -> ExperimentAnalysisOutputSchema | TextOutput:
        if params.skip_status_check:
            payload: dict[str, Any] = {}
            logger.info(f"[Stage5] Skipping status check for {params.job_id}")
        else:
            payload = await self._check_job(params.job_id)
            if isinstance(payload, TextOutput):
                return payload

        ws = self._resolve_workspace(params, payload)
        if isinstance(ws, TextOutput):
            return ws
        workspace, user = ws

        experiment_urls = await self._fetch_plot_urls(params.job_id, workspace, user)
        if isinstance(experiment_urls, TextOutput):
            return experiment_urls

        urls = self._flatten(experiment_urls)
        context = self._build_context(params, experiment_urls)
        result = await ImageAnalyzerAgent(self.config.analyzer_config).arun(
            ImageAnalyzerInputSchema(urls=urls, context=context),
        )
        if not isinstance(result, ImageAnalyzerOutputSchema):
            return cast(TextOutput, result)
        return ExperimentAnalysisOutputSchema(markdown=result.markdown)

    # -- Pipeline (_astream) -------------------------------------------

    async def _astream(
        self, params: ExperimentAnalysisInputSchema, run_context: RunContext, **kwargs: Any
    ) -> AsyncIterator[StreamEvent]:
        cn = self.__class__.__name__

        yield StartingEvent(
            source=cn, message=f"Starting {cn}",
            data=StartingEventData[ExperimentAnalysisInputSchema](params=params),
            run_context=run_context,
        )
        # 1. job_status
        if params.skip_status_check:
            payload: dict[str, Any] = {}
            logger.info(f"[Stage5] Skipping status check for {params.job_id}")
            yield RunningEvent(source=cn, message="Skipping status check…", run_context=run_context)
        else:
            yield RunningEvent(source=cn, message="Checking job status…", run_context=run_context)
            payload = await self._check_job(params.job_id)
            if isinstance(payload, TextOutput):
                yield CompletedEvent(source=cn, message=f"Completed {cn}", data=CompletedEventData(output=payload), run_context=run_context)
                return

        # 2. workspace + user
        ws = self._resolve_workspace(params, payload)
        if isinstance(ws, TextOutput):
            yield CompletedEvent(source=cn, message=f"Completed {cn}", data=CompletedEventData(output=ws), run_context=run_context)
            return
        workspace, user = ws

        yield RunningEvent(source=cn, message=f"Job complete. Fetching plots for {workspace}…", run_context=run_context)

        # 3. job_plot
        experiment_urls = await self._fetch_plot_urls(params.job_id, workspace, user)
        if isinstance(experiment_urls, TextOutput):
            yield CompletedEvent(source=cn, message=f"Completed {cn}", data=CompletedEventData(output=experiment_urls), run_context=run_context)
            return

        urls = self._flatten(experiment_urls)
        yield RunningEvent(source=cn, message=f"Got {len(urls)} figures across {len(experiment_urls)} experiments. Analyzing…", run_context=run_context)

        # 4. Delegate — forward ImageAnalyzerAgent's streaming events
        context = self._build_context(params, experiment_urls)
        analyzer = ImageAnalyzerAgent(self.config.analyzer_config)
        result: ImageAnalyzerOutputSchema | TextOutput | None = None

        async for event in analyzer.astream(ImageAnalyzerInputSchema(urls=urls, context=context)):
            if isinstance(event, PartialOutputEvent):
                yield PartialOutputEvent(source=cn, message=event.message, data=event.data, run_context=run_context)
            elif isinstance(event, CompletedEvent):
                result = event.data.output

        # 5. Wrap
        if isinstance(result, ImageAnalyzerOutputSchema):
            final = ExperimentAnalysisOutputSchema(markdown=result.markdown)
        elif result is not None:
            final = cast(TextOutput, result)
        else:
            final = TextOutput(content="ImageAnalyzerAgent returned no output.")

        yield CompletedEvent(source=cn, message=f"Completed {cn}", data=CompletedEventData(output=final), run_context=run_context)

    # -- Output validation ---------------------------------------------

    def check_output(self, output) -> str | None:
        if isinstance(output, ExperimentAnalysisOutputSchema) and not output.markdown.strip():
            return "Markdown report is empty — the image analyzer produced no content."
        return super().check_output(output)
