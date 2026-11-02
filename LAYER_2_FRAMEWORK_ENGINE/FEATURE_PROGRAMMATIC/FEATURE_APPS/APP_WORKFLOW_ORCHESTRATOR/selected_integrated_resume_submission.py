"""Closed submission shaping for one retained Integrated continuation."""

# implementation of:
# Requirement: CA-R-1524
# Method: CA-M-405

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, cast

from selected_execution_contracts import SelectedExecutionError
from selected_integrated_action_contract import validate_response
from selected_integrated_action_outcome import validate_outcome
from selected_integrated_frontier_records import digest


def continuation_id(submission: object) -> str:
    """Read the public continuation identity without accepting extra controls."""
    if not isinstance(submission, Mapping) or set(submission) != {
        "continuation_id",
        "action_run_id",
        "result",
    }:
        raise SelectedExecutionError("Integrated result submission fields are unsupported")
    value = submission.get("continuation_id")
    if not isinstance(value, str) or not value:
        raise SelectedExecutionError("Integrated result submission has no continuation")
    return value


def sealed_submission(submission: object, capture: Mapping[str, Any]) -> dict[str, Any]:
    """Validate an outer result before sealing its canonical store carrier."""
    continuation = continuation_id(submission)
    submitted = cast(Mapping[str, Any], submission)
    binding = capture.get("run_binding")
    result = submitted.get("result")
    if not isinstance(binding, Mapping) or not isinstance(result, Mapping):
        raise SelectedExecutionError("Integrated result submission is incomplete")
    if submitted.get("action_run_id") != binding.get("action_run_id"):
        raise SelectedExecutionError("Integrated result submission Action Run is stale")
    try:
        checked = validate_response(
            result,
            cast(list[str], capture["allowed_results"]),
            cast(Mapping[str, Any], capture["output_schema"]),
        )
        validate_outcome(cast(Mapping[str, Any], capture["packet"]), checked)
    except (KeyError, TypeError, ValueError) as error:
        raise SelectedExecutionError("Integrated submitted result is invalid") from error
    return {
        "continuation_id": continuation,
        "result": checked,
        "result_digest": digest(checked),
    }
