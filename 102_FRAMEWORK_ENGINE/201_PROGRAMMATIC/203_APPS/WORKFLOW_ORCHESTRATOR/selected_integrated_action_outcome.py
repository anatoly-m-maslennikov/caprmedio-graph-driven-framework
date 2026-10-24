"""Source-defined postconditions for current Integrated Action results."""

from __future__ import annotations

from collections.abc import Mapping
import hashlib
import json
from typing import Any


FAILURE_RESULTS = frozenset(
    {
        "blocked",
        "failed",
        "findings",
        "partial",
        "unresolved",
        "authority_change_required",
        "environment_blocker",
    }
)

_BINDING_FIELDS = (
    "candidate",
    "phase",
    "source_bindings",
    "requirements",
    "delivery",
    "evaluations",
    "method_projection",
    "methods",
    "red",
    "golden_e2e",
    "baseline_command",
)


def binding_digest(packet: Mapping[str, Any]) -> str:
    """Hash only the candidate and current R/M/D/E and test-input bindings."""
    payload = {key: packet.get(key) for key in _BINDING_FIELDS}
    try:
        encoded = json.dumps(
            payload,
            ensure_ascii=False,
            separators=(",", ":"),
            sort_keys=True,
        )
    except (TypeError, ValueError) as error:
        raise ValueError("current Integrated Action bindings are not serializable") from error
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def _identity(value: object) -> object:
    if not isinstance(value, Mapping):
        return value
    for key in ("candidate_id", "id", "identity", "name", "ref"):
        if key in value:
            return value[key]
    return None


def _retained_record(packet: Mapping[str, Any], name: str) -> Mapping[str, Any] | None:
    retained = packet.get("retained_state")
    value = retained.get(name) if isinstance(retained, Mapping) else None
    return value if isinstance(value, Mapping) else None


def _same_candidate(record: Mapping[str, Any], packet: Mapping[str, Any]) -> bool:
    return (
        "candidate" in record
        and _identity(record["candidate"]) == _identity(packet.get("candidate"))
        and record.get("binding_digest") == binding_digest(packet)
    )


def _validate_result_shape(response: Mapping[str, Any]) -> None:
    result = response["result"]
    if result in FAILURE_RESULTS and not response["blockers"]:
        raise ValueError("non-successful Integrated result requires blockers")
    if result in {"complete", "passed", "preliminary_clear"} and (
        not response["outputs"] or not response["evidence"]
    ):
        raise ValueError("terminal or review result requires outputs and evidence")


def _require_current_record(packet: Mapping[str, Any], name: str, result: str) -> None:
    record = _retained_record(packet, name)
    if record is None or record.get("result") != result or not _same_candidate(record, packet):
        raise ValueError(f"{result} requires current {name} for the candidate")


def _validate_review_result(packet: Mapping[str, Any], result: str) -> None:
    phase = packet.get("review_phase")
    if result == "preliminary_clear" and phase != "preliminary":
        raise ValueError("preliminary_clear requires a preliminary review phase")
    if result == "passed":
        if phase != "final":
            raise ValueError("passed requires a final review phase")
        _require_current_record(packet, "final_checks", "passed")


def _validate_retry_budget(packet: Mapping[str, Any], result: str) -> None:
    if (packet.get("step_marker"), result) not in {
        ("CA-O-096", "retry_permitted"),
        ("CA-O-099", "repaired"),
    }:
        return
    retry = packet.get("retry")
    if not isinstance(retry, Mapping):
        raise ValueError("retry result requires the retained retry budget")
    consumed = retry.get("consumed")
    limit = retry.get("effective_limit")
    if (
        isinstance(consumed, bool)
        or not isinstance(consumed, int)
        or isinstance(limit, bool)
        or not isinstance(limit, int)
        or consumed < 0
        or limit < 0
    ):
        raise ValueError("retry result requires a valid retained retry budget")
    # O096 admits a new retry round only while one remains.  O099 is
    # evaluated after that admission has already incremented the packet's
    # consumed count, so equality is the final valid repair round.
    exhausted = consumed >= limit if packet.get("step_marker") == "CA-O-096" else consumed > limit
    if exhausted:
        raise ValueError(f"{result} exceeds the retained retry budget")


def _validate_step_postconditions(packet: Mapping[str, Any], result: str) -> None:
    step_id = packet.get("step_marker")
    if step_id == "CA-O-230":
        _validate_review_result(packet, result)
    if step_id == "CA-O-094" and result == "passed":
        _require_current_record(packet, "preliminary_review", "preliminary_clear")
    if step_id == "CA-O-231" and result == "complete":
        _require_current_record(packet, "final_review", "passed")
        _require_current_record(packet, "final_checks", "passed")
    _validate_retry_budget(packet, result)


# implementation of:
# Method: CA-M-405
def validate_outcome(packet: Mapping[str, Any], response: Mapping[str, Any]) -> None:
    _validate_result_shape(response)
    _validate_step_postconditions(packet, response["result"])
