"""CM1-specific MCP tool factory functions.

These functions create HostedMCPTool instances configured for the CM1
experiment management MCP server.
"""

from __future__ import annotations

import os

from agents import HostedMCPTool

from akd_ext._types import OpenAITool


def get_default_impl_tools() -> list[OpenAITool]:
    """Default MCP tools for Stage 4A — uses the CM1 Temporal MCP server.

    Allowed tools:
      - ``job_submit``: push an experiment batch onto the Temporal workflow queue
      - ``jobs_list``: list previously submitted jobs (useful for dedup / resume checks)
    """
    api_key = os.environ.get("CM1_MCP_API_KEY")
    if not api_key:
        return []  # No API key configured — Phase 2 will be skipped
    url = os.environ.get("CM1_MCP_URL", "https://fm.prism.nasa-impact.net/akd/cm1-mcp")
    return [
        HostedMCPTool(
            tool_config={
                "type": "mcp",
                "server_label": "CM1_Temporal_MCP_Server",
                "allowed_tools": ["job_submit", "jobs_list"],
                "require_approval": "never",
                "server_description": "CM1 Temporal workflow MCP server — submit jobs and list job history.",
                "server_url": url,
                "headers": {"X-API-Key": api_key},
            }
        ),
    ]


def get_default_report_tools() -> list[OpenAITool]:
    """Default tools for the Research Report Generator. Uses job management MCP server."""
    return [
        HostedMCPTool(
            tool_config={
                "type": "mcp",
                "server_label": "Job_Management_Server",
                "allowed_tools": [
                    "job_status",
                    "job_plot",
                ],
                "require_approval": "never",
                "server_description": "MCP server for checking CM1 experiment job status and fetching result figures",
                "server_url": os.environ.get(
                    "EXPERIMENT_STATUS_MCP_URL",
                    "",  # No default — must be configured
                ),
                "authorization": os.environ.get("EXPERIMENT_STATUS_MCP_KEY"),
            }
        ),
    ]
