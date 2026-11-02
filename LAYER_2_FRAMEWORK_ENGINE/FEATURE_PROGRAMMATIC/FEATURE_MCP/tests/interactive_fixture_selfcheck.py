"""Manual, non-discovered self-check for the disposable Interactive fixture."""

from __future__ import annotations

from pathlib import Path
import tempfile
from typing import Any

from interactive_mcp_fixture import build_interactive_mcp_fixture
from shared_context_current_fixture import CurrentSharedContextFixture  # type: ignore[import-not-found]
from shared_context_packets import ACTIONS  # type: ignore[import-not-found]
from shared_context_validation import (
    validate_current_shared_packet,
)
from selected_route_validation import load_selected_manifest


def main() -> None:
    current = CurrentSharedContextFixture.load()
    pins = {pin["atom_id"]: dict(pin) for pin in current.source_pins()}
    trusted_profile: dict[str, Any] = {
        "workflow": pins["CA-O-016"],
        "entry_step": "CA-O-231",
        "steps": {
            step: {"step": pins[step], "action": pins[action]} for step, action in ACTIONS.items()
        },
    }
    trusted_methods = current.support_inventory["method_projection"]
    with tempfile.TemporaryDirectory(prefix="interactive-mcp-") as temporary:
        fixture = build_interactive_mcp_fixture(Path(temporary))
        loaded = load_selected_manifest(fixture.root)
        assert loaded["canonical_manifest_sha256"] == fixture.manifest["canonical_manifest_sha256"]
        assert fixture.manifest["manifest_ref"].endswith("selected_workflow_bindings.json")
        route = next(
            row
            for row in fixture.manifest["routes"]
            if row["route"] == "run_implementation_workflow"
        )
        assert route["workflow"]["atom_id"] == "CA-O-016"
        assert route["entry_step"] == "CA-O-231"
        assert [row["step"]["atom_id"] for row in route["ordered_steps"]] == [
            "CA-O-231",
            "CA-O-232",
            "CA-O-233",
            "CA-O-094",
            "CA-O-234",
            "CA-O-096",
            "CA-O-099",
            "CA-O-230",
        ]
        packet = fixture.current_context_packet["base_packet"]
        workspace = Path(packet["workspace"])
        assert workspace.is_dir() and workspace.is_absolute()
        assert packet["permissions"]["implementation_workspace"]["path"] == str(workspace)
        assert fixture.current_context_packet["run_visit_limits"]["CA-O-230"] >= 2
        assert any(edge["to"] == "blocked" for edge in fixture.current_graph["transitions"])
        assert fixture.method_projection_path.read_text(encoding="utf-8")
        packet = {
            **fixture.current_context_packet["base_packet"],
            **fixture.current_context_packet["step_packets"]["CA-O-231"],
        }
        row = trusted_profile["steps"]["CA-O-231"]
        validation = validate_current_shared_packet(
            packet,
            workflow_definition=trusted_profile["workflow"],
            step_definition=row["step"],
            action_definition=row["action"],
            trusted_workflow_binding=trusted_profile,
            selected_project_root=fixture.root,
            trusted_method_projection=trusted_methods,
        )
        assert validation.accepted, validation.as_result()
        print(f"interactive fixture OK: {fixture.root}")


if __name__ == "__main__":
    main()
