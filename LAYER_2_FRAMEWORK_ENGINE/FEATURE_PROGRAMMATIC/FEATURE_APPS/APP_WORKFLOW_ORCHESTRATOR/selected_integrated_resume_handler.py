"""Graph handler for one already-admitted Integrated Action result."""

# implementation of:
# Requirement: CA-R-1522
# Method: CA-M-405

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from selected_execution_contracts import ActionHandler, SelectedExecutionError


def submitted_handler(
    capture: Mapping[str, Any],
    accepted: Mapping[str, Any],
    pending_handler: ActionHandler,
) -> ActionHandler:
    """Consume exactly the captured Action while leaving later visits pending."""
    binding = capture.get("run_binding")
    if not isinstance(binding, Mapping):
        raise SelectedExecutionError("Integrated capture has no Action Run binding")
    requested = binding.get("requested_action_id")
    action_run_id = binding.get("action_run_id")
    result = accepted.get("result")
    if not all(isinstance(value, str) and value for value in (requested, action_run_id, result)):
        raise SelectedExecutionError("Integrated submitted result is incomplete")

    def invoke(context: dict[str, Any]) -> Mapping[str, Any]:
        if context.get("requested_action_run_id") != requested:
            return pending_handler(context)
        if context.get("action_run_id") != action_run_id:
            raise SelectedExecutionError("Integrated submitted result Run binding is stale")
        return {"result": result, "effect_refs": [], "native_result": dict(accepted)}

    return invoke


def replace_handler(
    action_id: str,
    handlers: Mapping[str, ActionHandler],
    capture: Mapping[str, Any],
    accepted: Mapping[str, Any],
) -> dict[str, ActionHandler]:
    """Replace only the captured Action definition handler for recovery."""
    original = handlers.get(action_id)
    if original is None:
        raise SelectedExecutionError("Integrated Action handler is unavailable")
    return {**handlers, action_id: submitted_handler(capture, accepted, original)}
