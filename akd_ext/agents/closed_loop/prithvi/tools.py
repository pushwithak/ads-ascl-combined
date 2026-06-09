"""Prithvi-specific MCP tool wiring for closed-loop stages.

All tools are served by the hosted MCP server (PRITHVI_MCP_URL).
Each stage gets a filtered view via ``allowed_tools``:

- Stage 3: geocode, reverse_geocode
- Stage 4: screen_events, check_screening, job_submit
- Stage 5: job_status, job_plot
"""

from __future__ import annotations

import os

from agents import HostedMCPTool

from akd_ext._types import OpenAITool


# ---------------------------------------------------------------------------
# Public API — tool lists for each stage (all tools served by hosted MCP)
# ---------------------------------------------------------------------------


def get_default_impl_tools() -> list[OpenAITool]:
    """Default tools for Stage 4 (Experiment Implementation).

    Conditionally includes (when ``PRITHVI_MCP_API_KEY`` is set), all served
    by the hosted MCP server:
      - ``screen_events``: start async event screening (returns a task_id)
      - ``check_screening``: poll a screening job by task_id
      - ``job_submit``: push a pipeline config onto the Temporal workflow queue

    Note: the local ``screen_events``/``geocode``/``reverse_geocode`` function
    tools still exist in this module but are not attached to the agent — event
    screening runs on the MCP server so the slow NOAA/HLS crawl doesn't block
    the agent loop.
    """
    tools: list[OpenAITool] = []

    api_key = os.environ.get("PRITHVI_MCP_API_KEY")
    if api_key:
        url = os.environ.get("PRITHVI_MCP_URL", "")
        tools.append(
            HostedMCPTool(
                tool_config={
                    "type": "mcp",
                    "server_label": "Prithvi_Temporal_MCP_Server",
                    "allowed_tools": [
                        "screen_events",
                        "check_screening",
                        "job_submit",
                    ],
                    "require_approval": "never",
                    "server_description": (
                        "Prithvi pipeline Temporal workflow MCP server — screen flood/burn "
                        "events (screen_events starts a job, check_screening polls until "
                        "done), submit pipeline configs, and list job history."
                    ),
                    "server_url": url,
                    "headers": {"Authorization": f"Bearer {api_key}"},
                }
            ),
        )
    return tools


def get_default_spec_builder_tools() -> list[OpenAITool]:
    """Default tools for Stage 3 (Workflow Spec Builder).

    Conditionally includes (when ``PRITHVI_MCP_API_KEY`` is set), served by the
    hosted MCP server:
      - ``geocode``: resolve a place name / AOI description → bbox
      - ``reverse_geocode``: resolve a bbox → US state / county

    Used when the user names a region or supplies a custom AOI while the spec
    is being built. Returns an empty list when no MCP key is configured.
    """
    tools: list[OpenAITool] = []

    api_key = os.environ.get("PRITHVI_MCP_API_KEY")
    if api_key:
        url = os.environ.get("PRITHVI_MCP_URL", "")
        tools.append(
            HostedMCPTool(
                tool_config={
                    "type": "mcp",
                    "server_label": "Prithvi_Temporal_MCP_Server",
                    "allowed_tools": ["geocode", "reverse_geocode"],
                    "require_approval": "never",
                    "server_description": (
                        "Prithvi pipeline MCP server — geocode (place name → bbox) "
                        "and reverse_geocode (bbox → US state/county) for resolving "
                        "regions and custom AOIs while building the workflow spec."
                    ),
                    "server_url": url,
                    "headers": {"Authorization": f"Bearer {api_key}"},
                }
            ),
        )
    return tools


def get_default_report_tools() -> list[OpenAITool]:
    """Default tools for Stage 5 (report/analysis). Uses the same MCP server."""
    api_key = os.environ.get("PRITHVI_MCP_API_KEY")
    if not api_key:
        return []
    url = os.environ.get("PRITHVI_MCP_URL", "")
    return [
        HostedMCPTool(
            tool_config={
                "type": "mcp",
                "server_label": "Prithvi_Temporal_MCP_Server",
                "allowed_tools": [
                    "job_status",
                    "job_plot",
                ],
                "require_approval": "never",
                "server_description": (
                    "Prithvi pipeline MCP server for checking job status "
                    "and fetching result figures/tables/maps."
                ),
                "server_url": url,
                "headers": {"Authorization": f"Bearer {api_key}"},
            }
        ),
    ]
