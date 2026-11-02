from __future__ import annotations
from typing import Any
from shared_context_packets import ACTIONS


def build_graph(fixture: Any) -> dict[str, Any]:
    actions = {pin["atom_id"]: pin for pin in fixture.source_pins() if pin.get("kind") == "action"}
    rows = []
    for step_id in fixture.manifest["workflow"]["steps"]:
        step = next(pin for pin in fixture.source_pins() if pin.get("atom_id") == step_id)
        action_id = ACTIONS[step_id]
        rows.append(
            {
                "atom_id": step_id,
                "source": dict(step),
                "actions": [{"atom_id": action_id, "source": dict(actions[action_id])}],
            }
        )
    return {
        "route": "run_implementation_workflow",
        "workflow": {"atom_id": "CA-O-016", "version": 17},
        "entry_step": fixture.manifest["workflow"]["entry_step"],
        "steps": rows,
        "transitions": fixture.manifest["workflow"]["transitions"],
    }
