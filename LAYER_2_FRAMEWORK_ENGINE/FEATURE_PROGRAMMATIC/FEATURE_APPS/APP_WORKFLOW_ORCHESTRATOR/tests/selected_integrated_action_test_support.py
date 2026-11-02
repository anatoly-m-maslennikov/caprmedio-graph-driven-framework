"""Shared frozen-project setup for Integrated Action functional tests."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from shared_context_packets import ACTIONS


def materialize_bound_inputs(
    fixture: Any, parent: Path
) -> tuple[Path, dict[str, Any], dict[str, Any]]:
    """Materialize the fixture and its explicit source-bound support inventory."""
    root = fixture.materialize(parent / "project")
    for row in fixture._support_rows():
        target = root / str(row["path"])
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(fixture.support_source_bytes(str(row["atom_id"])))
    pins = {pin["atom_id"]: dict(pin) for pin in fixture.source_pins()}
    profile: dict[str, Any] = {
        "workflow": pins["CA-O-016"],
        "entry_step": "CA-O-231",
        "steps": {
            step: {"step": pins[step], "action": pins[action]} for step, action in ACTIONS.items()
        },
    }
    return root, profile, fixture.support_inventory["method_projection"]
