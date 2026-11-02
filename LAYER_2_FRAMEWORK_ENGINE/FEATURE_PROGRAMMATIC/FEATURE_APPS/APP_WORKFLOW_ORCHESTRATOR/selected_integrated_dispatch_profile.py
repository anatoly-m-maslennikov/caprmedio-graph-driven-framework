"""Trusted current O016 profile derived from a normalized frozen graph."""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path
from typing import Any

from selected_execution_contracts import SelectedExecutionError
from selected_graph_sources import validate_definition
from shared_context_validation_sources import CURRENT_ACTIONS, workflow_version_profile


_PIN_FIELDS = ("atom_id", "kind", "version", "path", "sha256")
def _pin(root: Path, value: object, kind: str) -> dict[str, Any]:
    if not isinstance(value, Mapping):
        raise SelectedExecutionError("current Integrated graph binding is invalid")
    checked = validate_definition(root, value, expected_kind=kind)
    return {field: checked[field] for field in _PIN_FIELDS}


def profile_from_frozen(root: Path, frozen: Mapping[str, Any]) -> dict[str, Any]:
    """Build the reviewed O016@17, O016@18, or O016@20 profile from pins."""
    graph = frozen.get("graph")
    if not isinstance(graph, Mapping) or graph.get("route") != "run_implementation_workflow":
        raise SelectedExecutionError("current Integrated dispatch requires the O016 route")
    workflow = _pin(root, graph.get("workflow"), "workflow")
    rows = graph.get("steps")
    if (
        workflow["atom_id"] != "CA-O-016"
        or workflow_version_profile(workflow["version"]) is None
        or graph.get("entry_step") != "CA-O-231"
        or not isinstance(rows, list)
        or [row.get("atom_id") if isinstance(row, Mapping) else None for row in rows]
        != list(CURRENT_ACTIONS)
    ):
        raise SelectedExecutionError("current Integrated graph profile is incomplete")
    steps: dict[str, dict[str, dict[str, Any]]] = {}
    for step_id, action_id in CURRENT_ACTIONS.items():
        row = rows[len(steps)]
        if not isinstance(row, Mapping) or not isinstance(row.get("actions"), list):
            raise SelectedExecutionError("current Integrated Step binding is invalid")
        actions = row["actions"]
        if len(actions) != 1:
            raise SelectedExecutionError("current Integrated Step must bind one Action")
        step = _pin(root, row, "step")
        action = _pin(root, actions[0], "action")
        if step["atom_id"] != step_id or action["atom_id"] != action_id:
            raise SelectedExecutionError("current Integrated Step/Action pair is stale")
        steps[step_id] = {"step": step, "action": action}
    return {"workflow": workflow, "entry_step": "CA-O-231", "steps": steps}
