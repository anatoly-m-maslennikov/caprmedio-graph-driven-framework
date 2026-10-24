"""Durable selected-dispatch state and its failure boundary."""

from __future__ import annotations

from collections.abc import Mapping
from concurrent.futures import CancelledError as FutureCancelledError
from pathlib import Path
import sys
from typing import Any

from selected_evidence_io import atomic_write
from selected_execution_contracts import ActionHandler
from selected_run_session import RunSupport, shared_dispatch


def uncertain_dispatch_failure(
    root: Path,
    folder: Path,
    run_id: str,
    error: Exception,
) -> dict[str, Any]:
    """Retain uncertain intent after a failure without authorizing replay."""
    tools_root = str(Path(__file__).resolve().parents[2] / "201_TOOLS")
    if tools_root not in sys.path:
        sys.path.insert(0, tools_root)
    from runtime_failure_diagnostics import report_failure

    failure, secondary = report_failure(
        root,
        error,
        component="WORKFLOW_ORCHESTRATOR",
        operation="selected_execution.dispatch",
        correlation_id=run_id,
    )
    failure_payload = {
        "severity": getattr(failure, "severity", "WARNING"),
        "code": getattr(failure, "code", "internal_failure"),
        "message": getattr(failure, "message", "operation failure"),
    }
    diagnostic = secondary or getattr(failure, "diagnostic_error", None)
    if diagnostic:
        failure_payload["diagnostic_error"] = diagnostic
    atomic_write(
        folder / "dispatch_uncertain.json",
        {
            "run_id": run_id,
            "reason": "uncertain selected dispatch intent retained; no replay",
            "failure": failure_payload,
        },
    )
    return {
        "disposition": "recording_pending",
        "outcome": "interrupted_pending",
        "workflow_run_id": run_id,
        "reason": "uncertain selected dispatch intent retained; no replay",
        "failure": failure_payload,
        "retry_disposition": "inspect-or-recover-only",
    }


def dispatch_admitted_with_failure_boundary(
    root: Path,
    handlers: Mapping[str, ActionHandler],
    frozen: Mapping[str, Any],
    request: Mapping[str, Any],
    run_id: str,
    folder: Path,
    accepted: Path,
    intent: Path,
    run_support: RunSupport | None,
) -> dict[str, Any]:
    """Commit accepted result or retain uncertain intent after dispatch failure."""
    try:
        result = shared_dispatch(
            root,
            handlers,
            frozen,
            run_support=run_support,
        )
        value = dict(result)
        atomic_write(accepted, {"result": value})
        intent.unlink(missing_ok=True)
        return value
    except FutureCancelledError:
        raise
    except Exception as error:
        return uncertain_dispatch_failure(root, folder, run_id, error)
