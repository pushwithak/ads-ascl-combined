"""FM_Prithvi_EO-specialized closed-loop workflow agents.

Each agent is a subclass of the generic stage agent with FM_Prithvi_EO-specific
system prompts, context files, tools, and descriptions pre-configured.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from pydantic import Field

from akd_ext.agents.closed_loop.prithvi.prompts import (
    CAPABILITY_FEASIBILITY_MAPPER_SYSTEM_PROMPT,
    EXPERIMENT_ANALYSIS_SYSTEM_PROMPT,
    EXPERIMENT_IMPLEMENTER_SYSTEM_PROMPT,
    GAP_AGENT_SYSTEM_PROMPT,
    RESEARCH_REPORT_GENERATOR_SYSTEM_PROMPT,
    WORKFLOW_SPEC_BUILDER_SYSTEM_PROMPT,
)
from akd_ext.agents.closed_loop.prithvi.tools import (
    get_default_impl_tools,
    get_default_report_tools,
    get_default_spec_builder_tools,
)
from akd_ext.agents.gap import (
    GapAgent,
    GapAgentConfig,
)
from akd_ext.agents.closed_loop.stages.capability_feasibility_mapper import (
    CapabilityFeasibilityMapperAgent,
    CapabilityFeasibilityMapperConfig,
)
from akd_ext.agents.closed_loop.stages.workflow_spec_builder import (
    WorkflowSpecBuilderAgent,
    WorkflowSpecBuilderConfig,
)
from akd_ext.agents.closed_loop.stages.experiment_implementation import (
    ExperimentImplementationAgent,
    ExperimentImplementationConfig,
)
from akd_ext.agents.closed_loop.stages.experiment_analysis import (
    ExperimentAnalysisAgent,
    ExperimentAnalysisConfig,
)
from akd_ext.agents.closed_loop.stages.research_report_generator import (
    ResearchReportGeneratorAgent,
    ResearchReportGeneratorConfig,
)


_CONTEXT_DIR = Path(__file__).parent / "context"


def _load_prithvi_gap_agent_context() -> dict[str, str]:
    """Load Prithvi Gap Agent context files."""
    return {
        "Gap Detection Process": (_CONTEXT_DIR / "gap_detection_process.md").read_text(),
        "Pipeline Capabilities": (_CONTEXT_DIR / "pipeline_capabilities.md").read_text(),
    }


def _load_prithvi_feasibility_context() -> dict[str, str]:
    """Load Prithvi Capability & Feasibility Mapper context files."""
    return {
        "Pipeline Capabilities": (_CONTEXT_DIR / "pipeline_capabilities.md").read_text(),
        "Feasibility Mapper Reference": (_CONTEXT_DIR / "feasibility_mapper_reference.md").read_text(),
        "Ancillary Dataset Inventory": (_CONTEXT_DIR / "ancillary_dataset_inventory.md").read_text(),
        "Feasibility Mapper Governance": (_CONTEXT_DIR / "feasibility_mapper_governance.md").read_text(),
    }


def _load_prithvi_workflow_spec_context() -> dict[str, str]:
    """Load Prithvi Workflow Spec Builder context files."""
    return {
        "Workflow Spec Builder Reference": (_CONTEXT_DIR / "workflow_spec_builder_reference.md").read_text(),
        "Workflow Spec Config Schema": (_CONTEXT_DIR / "workflow_spec_config_schema.md").read_text(),
        "Pipeline Capabilities": (_CONTEXT_DIR / "pipeline_capabilities.md").read_text(),
        "Ancillary Dataset Inventory": (_CONTEXT_DIR / "ancillary_dataset_inventory.md").read_text(),
        "Workflow Spec Builder Governance": (_CONTEXT_DIR / "workflow_spec_builder_governance.md").read_text(),
    }


# -----------------------------------------------------------------------------
# Stage 1: Gap Agent
# -----------------------------------------------------------------------------


class FMPrithviGapAgentConfig(GapAgentConfig):
    """FM_Prithvi_EO-specific configuration for Gap Agent."""

    system_prompt: str = Field(default=GAP_AGENT_SYSTEM_PROMPT)
    context_files: dict[str, str] = Field(default_factory=_load_prithvi_gap_agent_context)
    description: str = Field(
        default="Stage-1 Research Gap Detection & Synthesis agent for the FM_Prithvi_EO pipeline. Identifies "
        "defensible research gaps, contradictions, and candidate research questions strictly within a "
        "user-provided corpus of academic papers, with paragraph-level traceability and explicit uncertainty. "
        "Frames RQs concretely enough (variables, proxies, spatial/temporal scope) for the downstream "
        "Capability & Feasibility Mapper, but does not assess feasibility or filter by pipeline capability."
    )


class FMPrithviGapAgent(GapAgent):
    """FM_Prithvi_EO-specialized Gap Agent."""

    config_schema = FMPrithviGapAgentConfig


# -----------------------------------------------------------------------------
# Stage 2: Capability & Feasibility Mapper
# -----------------------------------------------------------------------------


class FMPrithviCapabilityFeasibilityMapperConfig(CapabilityFeasibilityMapperConfig):
    """FM_Prithvi_EO-specific configuration for Capability & Feasibility Mapper."""

    system_prompt: str = Field(default=CAPABILITY_FEASIBILITY_MAPPER_SYSTEM_PROMPT)
    context_files: dict[str, str] = Field(default_factory=_load_prithvi_feasibility_context)
    description: str = Field(
        default="Capability & Feasibility Assessment agent for the Prithvi geospatial foundation-model "
        "pipeline. Maps approved research questions to atomic capability requirements across 5 dimensions, "
        "matches each requirement to a specific tool from the Pipeline Capabilities (Prithvi Tier 1 "
        "downstreams, region-aware baselines, NDVI severity, ancillary datasets, 86 statistical tests), "
        "and produces Go / Conditional-Go / No-Go recommendations with execution checklists."
    )


class FMPrithviCapabilityFeasibilityMapperAgent(CapabilityFeasibilityMapperAgent):
    """FM_Prithvi_EO-specialized Capability & Feasibility Mapper Agent."""

    config_schema = FMPrithviCapabilityFeasibilityMapperConfig


# -----------------------------------------------------------------------------
# Stage 3: Workflow Spec Builder
# -----------------------------------------------------------------------------


class FMPrithviWorkflowSpecBuilderConfig(WorkflowSpecBuilderConfig):
    """FM_Prithvi_EO-specific configuration for Workflow Spec Builder."""

    system_prompt: str = Field(default=WORKFLOW_SPEC_BUILDER_SYSTEM_PROMPT)
    context_files: dict[str, str] = Field(default_factory=_load_prithvi_workflow_spec_context)
    tools: list[Any] = Field(default_factory=get_default_spec_builder_tools)
    description: str = Field(
        default="Stage-3 Workflow Spec Builder for the Prithvi geospatial foundation-model pipeline. "
        "Translates approved research questions and feasibility handoff packages into atomic, ordered "
        "workflow steps, region-aware data acquisition plans, and validation strategies, then compiles "
        "them into an execution-ready Markdown spec plus a machine-readable pipeline config YAML matching "
        "the executor schema."
    )


class FMPrithviWorkflowSpecBuilderAgent(WorkflowSpecBuilderAgent):
    """FM_Prithvi_EO-specialized Workflow Spec Builder Agent."""

    config_schema = FMPrithviWorkflowSpecBuilderConfig


# -----------------------------------------------------------------------------
# Stage 4: Experiment Implementation
# -----------------------------------------------------------------------------


class FMPrithviExperimentImplementationConfig(ExperimentImplementationConfig):
    """FM_Prithvi_EO-specific configuration for Stage-4 Controlled Execution Loop."""

    system_prompt: str = Field(default=EXPERIMENT_IMPLEMENTER_SYSTEM_PROMPT)
    context_files: dict[str, str] = Field(default_factory=dict)
    tools: list[Any] = Field(default_factory=get_default_impl_tools)
    description: str = Field(
        default="Stage-4 Pipeline Executor agent for the FM_Prithvi_EO pipeline. Validates the "
        "Stage-3 YAML config (required sections, Prithvi task flags, event definitions) and "
        "submits it via the ``job_submit`` MCP tool to the Temporal workflow on HPC. The config "
        "drives event screening and full pipeline execution. "
        "Returns job_id, workspace_name, and a brief submission report."
    )


class FMPrithviExperimentImplementationAgent(ExperimentImplementationAgent):
    """FM_Prithvi_EO-specialized Stage-4 Pipeline Executor Agent."""

    config_schema = FMPrithviExperimentImplementationConfig


# -----------------------------------------------------------------------------
# Stage 5: Experiment Analysis (deterministic — polls job, fetches figures)
# -----------------------------------------------------------------------------


class FMPrithviExperimentAnalysisConfig(ExperimentAnalysisConfig):
    """FM_Prithvi_EO-specific configuration for the Stage-5 Experiment Analysis Agent.

    Overrides the MCP URL, system prompt, and default user_name for the Prithvi pipeline.
    """

    system_prompt: str = Field(default=EXPERIMENT_ANALYSIS_SYSTEM_PROMPT)
    tools: list[Any] = Field(default_factory=get_default_report_tools)
    mcp_url: str = Field(
        default_factory=lambda: os.environ.get("PRITHVI_MCP_URL", ""),
        description="Prithvi Temporal MCP server URL for job_status / job_plot calls.",
    )
    default_user_name: str = Field(
        default="",
        description="Fallback user_name passed to job_plot when not provided in the input.",
    )
    description: str = Field(
        default="Stage-5 experiment analysis agent for Prithvi-EO-2.0 pipelines. Checks "
        "job_status via MCP; when complete, fetches all result artifacts (figures, CSVs, "
        "reports) via job_plot, delegates image analysis to ImageAnalyzerAgent (GPT vision), "
        "and returns structured FigureAnalysis data + fetched text content for Stage 6."
    )


class FMPrithviExperimentAnalysisAgent(ExperimentAnalysisAgent):
    """FM_Prithvi_EO-specialized Stage-5 Experiment Analysis Agent.

    Overrides ``_api_key`` to use ``PRITHVI_MCP_API_KEY``.
    """

    config_schema = FMPrithviExperimentAnalysisConfig

    @property
    def _api_key(self) -> str:
        key = os.environ.get("PRITHVI_MCP_API_KEY")
        if not key:
            raise RuntimeError("PRITHVI_MCP_API_KEY is not set; cannot reach the Prithvi MCP.")
        return key


# -----------------------------------------------------------------------------
# Stage 6: Research Report Generator
# -----------------------------------------------------------------------------


class FMPrithviResearchReportGeneratorConfig(ResearchReportGeneratorConfig):
    """FM_Prithvi_EO configuration for Stage-6 Research Report Generator."""

    system_prompt: str = Field(default=RESEARCH_REPORT_GENERATOR_SYSTEM_PROMPT)
    description: str = Field(
        default="Stage-6 Research Report Generator for Prithvi-EO-2.0 pipelines. Receives "
        "Stage 1 research question, Stage 3 workflow spec, and Stage 5 figure analyses + "
        "pipeline text output. Produces a publication-style Markdown report. No tools — all "
        "context is passed from upstream stages."
    )


class FMPrithviResearchReportGeneratorAgent(ResearchReportGeneratorAgent):
    """FM_Prithvi_EO Stage-6 Research Report Generator Agent."""

    config_schema = FMPrithviResearchReportGeneratorConfig


