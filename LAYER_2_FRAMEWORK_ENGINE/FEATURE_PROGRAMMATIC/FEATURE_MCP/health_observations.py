from __future__ import annotations

from collections.abc import Mapping
from datetime import datetime, timezone
import re
import threading
from typing import Any


MAX_OBSERVATIONS = 32
_TOOL_NAME = re.compile(r"^[A-Za-z0-9_.-]{1,128}$")
_RUN_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}$")
_PROJECT_PREFIX = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]{0,127}$")
_PROJECT_INSTANCE = re.compile(r"^[0-9a-f]{64}$")
_TOOL_OUTCOMES = frozenset(
    """accepted applied assessed blocked canceled cancelled completed duplicate failed
    implementation_gap input_required interrupted interrupted_pending no-op no_op partial
    pending pending_recording prepared preview published publication_recovery_required queued
    recorded recording_blocked recording_pending recreation_required rejected reloaded returned
    running success uncertain unknown unchanged unavailable""".split()
)
_WORKFLOW_OUTCOMES = _TOOL_OUTCOMES | {"unknown"}
_WORKFLOW_DISPOSITIONS = frozenset(
    """blocked canceled cancelled completed failed interrupted pending preview queued
    recording_pending started terminal unknown""".split()
)
_SCHEDULER_STATUSES = frozenset("CANCELLED ERROR ENQUEUED PENDING RUNNING SUCCESS UNKNOWN".split())


def _timestamp(value: Any = None) -> str:
    if isinstance(value, datetime):
        return value.astimezone(timezone.utc).isoformat(timespec="milliseconds")
    if (
        isinstance(value, str)
        and value
        and len(value) <= 64
        and all(char.isdigit() or char in "-:.+TZ " for char in value)
    ):
        return value
    return datetime.now(timezone.utc).isoformat(timespec="microseconds")


def _safe(value: Any, pattern: re.Pattern[str]) -> str:
    return value if isinstance(value, str) and pattern.fullmatch(value) else "unknown"


def _project_fields(row: dict[str, str], prefix: Any, instance_id: Any) -> None:
    if isinstance(prefix, str) and _PROJECT_PREFIX.fullmatch(prefix):
        row["project_prefix"] = prefix
    if isinstance(instance_id, str) and _PROJECT_INSTANCE.fullmatch(instance_id):
        row["project_instance_id"] = instance_id


def _known(value: Any, allowed: frozenset[str]) -> str:
    return value if isinstance(value, str) and value in allowed else "unknown"


def _payload(response: Any) -> tuple[Mapping[str, Any], bool]:
    if isinstance(response, Mapping):
        return response, bool(response.get("is_error", False))
    value = getattr(response, "structured_content", None)
    returned_error = bool(getattr(response, "is_error", False))
    return (value, returned_error) if isinstance(value, Mapping) else ({}, returned_error)


def _error_category(
    error: BaseException | str | None,
    returned_error: bool,
    uncertain_outcome: bool = False,
) -> str | None:
    if error is not None:
        if isinstance(error, TimeoutError):
            return "timeout"
        if isinstance(error, (ConnectionError, BrokenPipeError, ConnectionResetError)):
            return "connection"
        return "uncertain"
    return "uncertain" if uncertain_outcome else "returned-error" if returned_error else None


def _workflow_row(
    observed_at: str,
    payload: Mapping[str, Any],
    workflow_id: str,
    category: str | None,
    project_prefix: Any,
    project_instance_id: Any,
) -> dict[str, str]:
    row = {
        "observed_at": observed_at,
        "run_id": _safe(workflow_id, _RUN_ID),
        "scheduler_status": _known(payload.get("scheduler_status"), _SCHEDULER_STATUSES),
        "outcome": _known(payload.get("outcome"), _WORKFLOW_OUTCOMES),
        "disposition": _known(payload.get("disposition"), _WORKFLOW_DISPOSITIONS),
    }
    if category is not None:
        row["error_category"] = category
    _project_fields(row, project_prefix, project_instance_id)
    return row


def _tool_row(
    observed_at: str,
    name: Any,
    payload: Mapping[str, Any],
    category: str | None,
    has_error: bool,
    project_prefix: Any,
    project_instance_id: Any,
) -> dict[str, str]:
    returned = _known(payload.get("outcome"), _TOOL_OUTCOMES)
    row = {
        "observed_at": observed_at,
        "name": _safe(name, _TOOL_NAME),
        "outcome": returned
        if returned != "unknown"
        else ("uncertain" if has_error else "returned"),
        "returned_outcome": returned,
    }
    if category is not None:
        row["error_category"] = category
    _project_fields(row, project_prefix, project_instance_id)
    return row


def _workflow_id(payload: Mapping[str, Any]) -> str | None:
    blocked = ("action_run_id", "step_run_id", "coordinator_id")
    if (
        any(field in payload for field in blocked)
        or payload.get("identity_kind") == "technical_coordinator"
    ):
        return None
    identifier = (
        payload.get("actual_run_id")
        if payload.get("kind") == "workflow"
        else payload.get("workflow_run_id")
    )
    return identifier if isinstance(identifier, str) and _RUN_ID.fullmatch(identifier) else None


class HealthObservations:
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
        project_prefix: Any = None,
        project_instance_id: Any = None,
    ) -> None:
        del arguments
        payload, returned_error = _payload(response)
        observed_at = _timestamp(started_at)
        category = _error_category(error, returned_error, payload.get("outcome") == "uncertain")
        workflow_id = _workflow_id(payload)
        if workflow_id:
            self._append(
                self._workflows,
                _workflow_row(
                    observed_at,
                    payload,
                    workflow_id,
                    category,
                    project_prefix,
                    project_instance_id,
                ),
            )
        self._append(
            self._calls,
            _tool_row(
                observed_at,
                name,
                payload,
                category,
                error is not None,
                project_prefix,
                project_instance_id,
            ),
        )

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
