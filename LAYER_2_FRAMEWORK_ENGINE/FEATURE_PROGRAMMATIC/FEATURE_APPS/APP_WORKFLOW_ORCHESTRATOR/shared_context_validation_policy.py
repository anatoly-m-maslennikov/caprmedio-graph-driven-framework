"""Step-sensitive Plan, candidate, workspace, and retry checks."""

from __future__ import annotations

from collections.abc import Mapping
import math
from typing import Any

from implementation_agent_workspace import workspace, workspace_write_admitted
from shared_context_validation_sources import SharedContextPacketError


_WRITE_STEPS = frozenset({"CA-O-232", "CA-O-233", "CA-O-099"})


def _present(value: object) -> bool:
    if isinstance(value, str):
        return bool(value.strip())
    return value is not None and (not isinstance(value, Mapping) or bool(value))


def _identity(value: object) -> object:
    if not isinstance(value, Mapping):
        return value
    for key in ("id", "identity", "name", "ref", "candidate_id", "phase_id"):
        if key in value:
            return value[key]
    return None


def validate_plan_candidate(packet: Mapping[str, Any], step_id: str) -> None:
    """Require a Plan after initial preparation, but never invent one at O231."""
    plan = packet.get("plan_item")
    if step_id != "CA-O-231" or plan is not None:
        if not isinstance(plan, Mapping) or not _present(plan.get("item_id")):
            raise SharedContextPacketError("plan", "selected Plan item is missing")
        dod = plan.get("dod")
        if not isinstance(dod, list) or not dod or not all(_present(item) for item in dod):
            raise SharedContextPacketError("plan", "selected Plan Definition of Done is incomplete")
        estimate = plan.get("estimated_minutes")
        if (
            isinstance(estimate, bool)
            or not isinstance(estimate, (int, float))
            or not math.isfinite(estimate)
            or estimate <= 0
        ):
            raise SharedContextPacketError("plan", "selected Plan estimate is invalid")
    if not _present(_identity(packet.get("candidate"))) or not _present(
        _identity(packet.get("phase"))
    ):
        raise SharedContextPacketError("candidate", "candidate or phase identity is missing")
    retained = packet.get("retained_state", {})
    review = retained.get("preliminary_review") if isinstance(retained, Mapping) else None
    if isinstance(review, Mapping) and review.get("result") == "preliminary_clear":
        if _identity(review.get("candidate")) != _identity(packet.get("candidate")):
            raise SharedContextPacketError(
                "candidate", "preliminary clearance is bound to another candidate"
            )


def _write_workspace(packet: Mapping[str, Any]) -> None:
    permissions = packet.get("permissions")
    if not isinstance(permissions, Mapping) or permissions.get("allowed") is not True:
        raise SharedContextPacketError("permissions", "implementation permission is incomplete")
    try:
        admitted_workspace = workspace(packet)
        if not workspace_write_admitted(packet, admitted_workspace):
            raise ValueError("implementation workspace capability is missing")
    except (OSError, ValueError) as error:
        raise SharedContextPacketError("permissions", str(error)) from error


def validate_permissions_retry(packet: Mapping[str, Any], step_id: str) -> bool:
    """Return whether valid O096 input must yield the retry-blocked decision."""
    permissions = packet.get("permissions")
    if not isinstance(permissions, Mapping) or permissions.get("allowed") is not True:
        raise SharedContextPacketError("permissions", "implementation permission is incomplete")
    if step_id in _WRITE_STEPS:
        _write_workspace(packet)
    retry = packet.get("retry")
    if not isinstance(retry, Mapping):
        raise SharedContextPacketError("retry", "effective retry input is missing")
    consumed, limit = retry.get("consumed"), retry.get("effective_limit")
    if (
        isinstance(consumed, bool)
        or not isinstance(consumed, int)
        or consumed < 0
        or isinstance(limit, bool)
        or not isinstance(limit, int)
        or limit < 0
        or not _present(retry.get("source"))
    ):
        raise SharedContextPacketError("retry", "effective retry input is invalid")
    if step_id == "CA-O-096":
        if retry.get("remaining_failure") is not True:
            raise SharedContextPacketError("retry", "repair retry has no remaining failure")
        return consumed >= limit
    if step_id == "CA-O-099" and retry.get("admitted") is not True:
        raise SharedContextPacketError("retry", "repair retry has not been admitted")
    return False
