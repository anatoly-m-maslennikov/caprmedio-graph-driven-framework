"""Safe transport adapters for the shared Project gateway."""

from __future__ import annotations

import asyncio
import json
from concurrent.futures import CancelledError as FutureCancelledError
from typing import Any

from mcp import types

from operation_error_boundary import FailureRecord
from runtime_failure_diagnostics import report_failure


def refusal(code: str, root: Any = None) -> types.CallToolResult:
    """Encode a fixed, safe refusal without exposing diagnostic internals."""
    failure, secondary = report_failure(
        root,
        FailureRecord("WARNING", code, "shared MCP request refused"),
        component="SHARED_MCP_GATEWAY",
        operation="shared_dispatch",
    )
    diagnostics = [failure.code]
    if secondary is not None:
        diagnostics.append("technical_diagnostics_unavailable")
    value = {"outcome": "rejected", "diagnostics": diagnostics}
    return types.CallToolResult(
        content=[types.TextContent(type="text", text=json.dumps(value))],
        structured_content=value,
        is_error=True,
    )


def record_observation(
    observer: Any,
    name: Any,
    arguments: Any,
    response: Any,
    error: BaseException | None,
    *,
    root: Any,
    project_prefix: str | None,
    project_instance_id: str | None,
) -> None:
    """Keep a successful native result when bounded health recording fails."""
    try:
        observer.record(
            name,
            arguments,
            response,
            error=error,
            project_prefix=project_prefix,
            project_instance_id=project_instance_id,
        )
    except asyncio.CancelledError, FutureCancelledError:
        raise
    except Exception:
        report_failure(
            root,
            FailureRecord(
                "WARNING", "health_observation_failed", "health observations unavailable"
            ),
            component="SHARED_MCP_GATEWAY",
            operation="health_observations",
        )


__all__ = ["record_observation", "refusal"]
