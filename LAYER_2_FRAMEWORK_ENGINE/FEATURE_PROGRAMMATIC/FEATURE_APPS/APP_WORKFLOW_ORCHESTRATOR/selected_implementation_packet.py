"""Step-local O016 packet construction from frozen inputs and observed results."""

# implementation of:
# Method: CA-M-405

from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
from typing import Any, cast

from selected_execution_contracts import SelectedExecutionError
from selected_integrated_action_outcome import binding_digest


_PRELIMINARY_REVIEW = ("CA-O-230", "CA-O-225", "preliminary_clear")
_FINAL_REVIEW = ("CA-O-230", "CA-O-225", "passed")
_FINAL_CHECKS = ("CA-O-094", "CA-O-020", "passed")


def _observation_record(prior: Mapping[str, Any]) -> dict[str, Any]:
    """Keep the action's original binding with its observed output."""
    return {
        "result": prior["result"],
        "candidate": deepcopy(prior["candidate"]),
        "binding_digest": prior["binding_digest"],
        "outputs": deepcopy(prior.get("outputs", {})),
        "evidence": deepcopy(prior.get("evidence", [])),
    }


def _row(
    prior: Mapping[str, Any], packet: Mapping[str, Any]
) -> tuple[str, str, str, Mapping[str, Any] | None] | None:
    step = prior.get("step_definition_id")
    action = prior.get("action_definition_id")
    result = prior.get("result")
    if not all(isinstance(value, str) for value in (step, action, result)):
        return None
    if "candidate" not in prior or prior.get("binding_digest") != binding_digest(packet):
        return None
    outputs = prior.get("outputs")
    return (
        cast(str, step),
        cast(str, action),
        cast(str, result),
        cast(Mapping[str, Any], outputs) if isinstance(outputs, Mapping) else None,
    )


def _preparation_phase(
    packet: dict[str, Any], row: tuple[str, str, str, Mapping[str, Any] | None]
) -> str | None:
    step, action, result, outputs = row
    if (step, action) != ("CA-O-231", "CA-O-017") or result == "blocked":
        return None
    if outputs is None:
        return None
    plan = outputs.get("plan_item")
    if isinstance(plan, Mapping):
        packet["plan_item"] = deepcopy(dict(plan))
    phase = outputs.get("review_phase")
    return phase if phase in {"preliminary", "final"} else None


def _observation_name(
    row: tuple[str, str, str, Mapping[str, Any] | None], review_phase: object
) -> str | None:
    step, action, result, _outputs = row
    if (step, action, result) == _PRELIMINARY_REVIEW and review_phase == "preliminary":
        return "preliminary_review"
    if (step, action, result) == _FINAL_CHECKS and review_phase == "final":
        return "final_checks"
    if (step, action, result) == _FINAL_REVIEW and review_phase == "final":
        return "final_review"
    return None


def _actual_observations(
    packet: dict[str, Any], prior_results: list[dict[str, Any]]
) -> dict[str, Any]:
    """Carry only declared O016 observations into the next Step packet."""
    retained: dict[str, Any] = {}
    review_phase = packet.get("review_phase")
    if review_phase not in {None, "preliminary", "final"}:
        raise SelectedExecutionError("implementation Workflow review phase is invalid")
    for prior in prior_results:
        row = _row(prior, packet)
        if row is None:
            continue
        review_phase = _preparation_phase(packet, row) or review_phase
        name = _observation_name(row, review_phase)
        if name is not None:
            retained[name] = _observation_record(prior)
    if review_phase is not None:
        packet["review_phase"] = review_phase
    return retained


def implementation_packet(
    parameters: object,
    step_id: str,
    prior_results: list[dict[str, Any]],
) -> dict[str, Any]:
    """Select one manifest-bound packet and derive retry consumption once."""
    if not isinstance(parameters, Mapping):
        raise SelectedExecutionError("implementation Workflow requires a packet mapping")
    base = parameters.get("base_packet")
    packets = parameters.get("step_packets")
    if not isinstance(base, Mapping) or not isinstance(packets, Mapping):
        raise SelectedExecutionError(
            "implementation Workflow requires base_packet and step_packets"
        )
    packet = packets.get(step_id)
    if not isinstance(packet, Mapping):
        raise SelectedExecutionError(f"implementation Workflow has no packet for Step {step_id}")
    merged = {**base, **packet}
    if merged.get("context") not in {"Integrated", "Isolated"}:
        raise SelectedExecutionError(f"implementation packet context is missing for Step {step_id}")
    retained = base.get("retained_state", {})
    if not isinstance(retained, Mapping):
        raise SelectedExecutionError("implementation base retained_state is invalid")
    step_retained = packet.get("retained_state", {})
    if not isinstance(step_retained, Mapping):
        raise SelectedExecutionError(
            f"implementation packet retained_state is invalid for Step {step_id}"
        )
    observed = list(prior_results)
    observed_state = _actual_observations(merged, observed)
    merged["retained_state"] = {
        **retained,
        **step_retained,
        **observed_state,
        "prior_results": observed,
    }
    merged["prior_results"] = observed
    retry = merged.get("retry")
    if isinstance(retry, Mapping):
        consumed = retry.get("consumed")
        if isinstance(consumed, int) and not isinstance(consumed, bool) and consumed >= 0:
            merged["retry"] = {
                **retry,
                "consumed": consumed + _started_rounds(step_id, prior_results),
            }
    return merged


def _started_rounds(step_id: str, prior_results: list[dict[str, Any]]) -> int:
    """Count only actual repair starts, never repeated retry-gate checks."""
    completed = sum(
        1
        for prior in prior_results
        if prior.get("step_definition_id") == "CA-O-099"
        and prior.get("action_definition_id") == "CA-O-021"
        and prior.get("result") == "repaired"
    )
    admitted = sum(
        1
        for prior in prior_results
        if prior.get("step_definition_id") == "CA-O-096"
        and prior.get("action_definition_id") == "CA-O-024"
        and prior.get("result") == "retry_permitted"
    )
    return completed + int(step_id == "CA-O-099" and admitted > completed)
