"""Bounded, process-local observations of actual MCP calls."""

from __future__ import annotations

from collections.abc import Mapping
from datetime import datetime, timezone
import re
import threading
from typing import Any


MAX_OBSERVATIONS = 32
_TOOL_NAME = re.compile(r"^[A-Za-z0-9_.-]{1,128}$")
_RUN_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}$")
_TOOL_OUTCOMES = frozenset({
    "accepted", "applied", "assessed", "blocked", "canceled", "cancelled", "completed",
    "duplicate", "failed", "implementation_gap", "input_required", "interrupted",
    "interrupted_pending", "no-op", "no_op", "partial", "pending", "pending_recording",
    "prepared", "preview", "published", "publication_recovery_required", "queued",
    "recorded", "recording_blocked", "recording_pending", "recreation_required", "rejected",
    "reloaded", "returned", "running", "success", "uncertain", "unknown", "unchanged",
    "unavailable",
})
_WORKFLOW_OUTCOMES = _TOOL_OUTCOMES | {"unknown"}
_WORKFLOW_DISPOSITIONS = frozenset({
    "blocked", "canceled", "cancelled", "completed", "failed", "interrupted", "pending",
    "preview", "queued", "recording_pending", "started", "terminal", "unknown",
})
_SCHEDULER_STATUSES = frozenset({
    "CANCELLED", "ERROR", "ENQUEUED", "PENDING", "RUNNING", "SUCCESS", "UNKNOWN",
})


def _timestamp(value: Any = None) -> str:
    if isinstance(value, datetime):
        return value.astimezone(timezone.utc).isoformat(timespec="milliseconds")
    if isinstance(value, str) and value and len(value) <= 64 and all(
            char.isdigit() or char in "-:.+TZ " for char in value):
        return value
    return datetime.now(timezone.utc).isoformat(timespec="microseconds")


def _safe_tool_name(value: Any) -> str:
    return value if isinstance(value, str) and _TOOL_NAME.fullmatch(value) else "unknown"


def _safe_run_id(value: Any) -> str:
    return value if isinstance(value, str) and _RUN_ID.fullmatch(value) else "unknown"


def _known(value: Any, allowed: frozenset[str], default: str = "unknown") -> str:
    return value if isinstance(value, str) and value in allowed else default


def _payload(response: Any) -> tuple[Mapping[str, Any], bool]:
    if isinstance(response, Mapping):
        return response, bool(response.get("is_error", False))
    value = getattr(response, "structured_content", None)
    returned_error = bool(getattr(response, "is_error", False))
    return (value, returned_error) if isinstance(value, Mapping) else ({}, returned_error)


def _error_category(
    error: BaseException | str | None, returned_error: bool, uncertain_outcome: bool = False,
) -> str | None:
    if isinstance(error, TimeoutError):
        return "timeout"
    if isinstance(error, (ConnectionError, BrokenPipeError, ConnectionResetError)):
        return "connection"
    if error is not None:
        return "uncertain"
    if uncertain_outcome:
        return "uncertain"
    return "returned-error" if returned_error else None


def _workflow_row(
    observed_at: str, payload: Mapping[str, Any], workflow_id: str, category: str | None,
) -> dict[str, str]:
    row = {
        "observed_at": observed_at,
        "run_id": _safe_run_id(workflow_id),
        "scheduler_status": _known(payload.get("scheduler_status"), _SCHEDULER_STATUSES),
        "outcome": _known(payload.get("outcome"), _WORKFLOW_OUTCOMES),
        "disposition": _known(payload.get("disposition"), _WORKFLOW_DISPOSITIONS),
    }
    if category is not None:
        row["error_category"] = category
    return row


def _tool_row(
    observed_at: str, name: Any, payload: Mapping[str, Any], category: str | None,
    has_error: bool,
) -> dict[str, str]:
    returned = _known(payload.get("outcome"), _TOOL_OUTCOMES)
    row = {
        "observed_at": observed_at,
        "name": _safe_tool_name(name),
        "outcome": returned if returned != "unknown" else ("uncertain" if has_error else "returned"),
        "returned_outcome": returned,
    }
    if category is not None:
        row["error_category"] = category
    return row


def _workflow_id(payload: Mapping[str, Any]) -> str | None:
    if any(field in payload for field in ("action_run_id", "step_run_id", "coordinator_id")):
        return None
    if payload.get("identity_kind") == "technical_coordinator":
        return None
    actual = payload.get("actual_run_id")
    if payload.get("kind") == "workflow":
        if "actual_run_id" in payload:
            return actual if isinstance(actual, str) and _RUN_ID.fullmatch(actual) else None
    workflow = payload.get("workflow_run_id")
    return workflow if isinstance(workflow, str) and _RUN_ID.fullmatch(workflow) else None


class HealthObservations:
    """Retain only the latest 32 safe Tool and Workflow observations."""

    def __init__(self) -> None:
        self.started_at = _timestamp()
        self._calls: list[dict[str, str]] = []
        self._workflows: list[dict[str, str]] = []
        self._lock = threading.Lock()

    def record(
        self,
        name: Any,
        arguments: Any,
        response: Any,
        error: BaseException | str | None = None,
        started_at: Any = None,
    ) -> None:
        del arguments
        payload, returned_error = _payload(response)
        observed_at = _timestamp(started_at)
        returned_outcome = payload.get("outcome")
        category = _error_category(error, returned_error, returned_outcome == "uncertain")
        workflow_id = _workflow_id(payload)
        if isinstance(workflow_id, str) and workflow_id:
            self._append(self._workflows, _workflow_row(observed_at, payload, workflow_id, category))
        self._append(self._calls, _tool_row(observed_at, name, payload, category, error is not None))

    def _append(self, target: list[dict[str, str]], row: dict[str, str]) -> None:
        with self._lock:
            target.append(row)
            del target[:-MAX_OBSERVATIONS]

    def snapshot(self) -> dict[str, Any]:
        with self._lock:
            return {
                "started_at": self.started_at,
                "calls": [dict(row) for row in self._calls],
                "workflows": [dict(row) for row in self._workflows],
            }


__all__ = ["HealthObservations", "MAX_OBSERVATIONS"]
