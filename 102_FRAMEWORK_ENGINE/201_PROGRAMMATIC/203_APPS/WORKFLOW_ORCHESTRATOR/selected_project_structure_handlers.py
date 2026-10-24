"""Native capability adapters for the source-bound Project Structure Actions."""

from __future__ import annotations

from collections.abc import Callable, Mapping
from pathlib import Path
from typing import Any

from selected_execution_contracts import SelectedExecutionError


ActionHandler = Callable[[dict[str, Any]], Mapping[str, Any]]
STRUCTURAL_RESULTS = {
    ("CA-O-004", "selected"): "current sources selected",
    ("CA-O-012", "prepared"): "proposal ready",
    ("CA-O-005", "accepted"): "checks complete",
    ("CA-O-013", "authorized"): "authorization valid",
    ("CA-O-014", "completed"): "cutover completed",
    ("CA-O-014", "no_op"): "cutover completed",
}


def project_structure_handlers(root: Path) -> dict[str, ActionHandler]:
    """Return only the registered source-bound Project Structure Actions."""
    import project_structure  # type: ignore[import-not-found]  # Runtime source adapter.

    handlers = project_structure.queue_action_handlers(root)
    return {action_id: _structure_handler(handlers) for action_id in handlers}


def _structure_handler(handlers: Mapping[str, Callable[..., Mapping[str, Any]]]) -> ActionHandler:
    def structure(context: dict[str, Any]) -> dict[str, Any]:
        action_id = context["action_definition_id"]
        handler = handlers.get(action_id)
        if handler is None:
            return {
                "result": "blocked",
                "terminal_outcome": "interrupted_pending",
                "effect_refs": [],
            }
        result = handler(context)
        if not isinstance(result, Mapping) or not isinstance(result.get("result"), str):
            raise SelectedExecutionError(
                "Project Structure Action returned an invalid queue envelope"
            )
        label = STRUCTURAL_RESULTS.get((action_id, result["result"]), result["result"])
        output: dict[str, Any] = {
            "result": label,
            "effect_refs": result.get("effect_refs", []),
            "native_result": result.get("native_result"),
        }
        if label in {"blocked", "stale", "conflict"}:
            output["terminal_outcome"] = "interrupted_pending"
        elif action_id == "CA-O-005" and context["step_definition_id"] == "CA-O-144":
            output["terminal_outcome"] = "completed"
        return output

    return structure
