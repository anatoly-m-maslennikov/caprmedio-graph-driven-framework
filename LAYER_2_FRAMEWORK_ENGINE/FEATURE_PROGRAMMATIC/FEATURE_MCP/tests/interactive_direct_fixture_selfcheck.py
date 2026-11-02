# implementation of:
# Requirement: CA-R-2117
# Method: CA-M-431
"""Executable self-check for the frozen direct-RMED MCP fixture."""

from __future__ import annotations

import hashlib
from pathlib import Path
import tempfile
from typing import Any

from interactive_direct_fixture import InteractiveDirectFixture, build_interactive_direct_fixture
from selected_graph_validation import validate_graph
from selected_route_validation import load_selected_manifest
from shared_context_direct_fixture import DirectSharedContextFixture
from shared_context_packets import ACTIONS
from shared_context_validation import validate_current_shared_packet


STEP_IDS = (
    "CA-O-231",
    "CA-O-232",
    "CA-O-233",
    "CA-O-094",
    "CA-O-234",
    "CA-O-096",
    "CA-O-099",
    "CA-O-230",
)


def _profile(fixture: DirectSharedContextFixture) -> dict[str, Any]:
    pins = {str(pin["atom_id"]): dict(pin) for pin in fixture.source_pins()}
    return {
        "workflow": pins["CA-O-016"],
        "entry_step": "CA-O-231",
        "steps": {
            step: {"step": pins[step], "action": pins[action]}
            for step, action in ACTIONS.items()
        },
    }


def _check_manifest(interactive: InteractiveDirectFixture) -> None:
    loaded = load_selected_manifest(interactive.root)
    assert loaded["canonical_manifest_sha256"] == interactive.manifest["canonical_manifest_sha256"]
    route = next(row for row in interactive.manifest["routes"] if row["route"] == "run_implementation_workflow")
    assert route["workflow"]["version"] == 18
    assert [row["step"]["atom_id"] for row in route["ordered_steps"]] == list(STEP_IDS)


def _direct_packet(interactive: InteractiveDirectFixture) -> dict[str, Any]:
    return {
        **interactive.current_context_packet["base_packet"],
        **interactive.current_context_packet["step_packets"]["CA-O-231"],
    }


# implementation of:
# Requirement: CA-R-2117
# Method: CA-M-431
def _check_direct_source_rows(packet: dict[str, Any]) -> None:
    expected = {"atom_id", "version", "path", "sha256", "content"}
    for key in ("methods", "requirements", "delivery", "evaluations"):
        rows = packet[key]
        assert isinstance(rows, list) and all(set(row) == expected for row in rows)


# implementation of:
# Requirement: CA-R-2117
# Method: CA-M-431
def _check_packet(
    interactive: InteractiveDirectFixture,
    profile: dict[str, Any],
    packet: dict[str, Any],
) -> None:
    assert "methods" in packet and "method_projection" not in packet
    _check_direct_source_rows(packet)
    row = profile["steps"]["CA-O-231"]
    accepted = validate_current_shared_packet(
        packet,
        workflow_definition=profile["workflow"],
        step_definition=row["step"],
        action_definition=row["action"],
        trusted_workflow_binding=profile,
        selected_project_root=interactive.root,
        trusted_methods=interactive.trusted_methods,
    )
    assert accepted.accepted, accepted.as_result()
    stale = {**packet, "methods": [dict(packet["methods"][0], sha256="0" * 64), *packet["methods"][1:]]}
    rejected = validate_current_shared_packet(
        stale,
        workflow_definition=profile["workflow"],
        step_definition=row["step"],
        action_definition=row["action"],
        trusted_workflow_binding=profile,
        selected_project_root=interactive.root,
        trusted_methods=interactive.trusted_methods,
    )
    assert not rejected.accepted and rejected.warnings[0]["code"] in {"rmed", "method_authority"}


# implementation of:
# Requirement: CA-R-2117
# Method: CA-M-431
def _check_graph_roundtrip(fixture: Any) -> None:
    execution = {
        **fixture.execution_request,
        "mode": "execute",
        "definition_manifest": {
            "manifest_ref": fixture.manifest["manifest_ref"],
            "manifest_digest": fixture.manifest["canonical_manifest_sha256"],
        },
        "source_freshness": fixture.manifest["source_freshness"],
    }
    graph = validate_graph(fixture.root, execution)
    assert graph["entry_step"] == "CA-O-231"
    assert [row["atom_id"] for row in graph["steps"]] == list(STEP_IDS)
    assert [row["actions"][0]["atom_id"] for row in graph["steps"]] == [
        ACTIONS[step] for step in STEP_IDS
    ]
    expected = {
        (edge["from"], edge["result"]): edge["to"]
        for edge in fixture.current_graph["transitions"]
    }
    actual: dict[tuple[str, str], str] = {}
    for step in graph["steps"]:
        for edge in step["on_result"]:
            target = edge.get("next") or {"completed": "completed", "interrupted_pending": "blocked"}.get(
                edge.get("terminal", "")
            )
            assert isinstance(target, str)
            actual[(step["atom_id"], edge["result"])] = target
    assert actual == expected


def _fixture_hashes(fixture: DirectSharedContextFixture, interactive: InteractiveDirectFixture) -> tuple[str, str, str]:
    manifest_hash = hashlib.sha256((fixture.root / "manifest.json").read_bytes()).hexdigest()
    inventory_hash = hashlib.sha256((fixture.root / "support_inventory.json").read_bytes()).hexdigest()
    return manifest_hash, inventory_hash, interactive.manifest["canonical_manifest_sha256"]


def main() -> None:
    fixture = DirectSharedContextFixture.load()
    fixture.verify()
    profile = _profile(fixture)
    with tempfile.TemporaryDirectory(prefix="interactive-direct-") as temporary:
        interactive = build_interactive_direct_fixture(Path(temporary))
        _check_manifest(interactive)
        packet = _direct_packet(interactive)
        _check_packet(interactive, profile, packet)
        _check_graph_roundtrip(interactive)
        manifest_hash, inventory_hash, selected_manifest_hash = _fixture_hashes(fixture, interactive)
        print(
            "direct interactive fixture OK: "
            f"source_pins={len(fixture.source_pins())} "
            f"support_rows={len(fixture._support_rows())} "
            f"methods={len(fixture.trusted_methods)} "
            f"manifest_sha256={manifest_hash} "
            f"inventory_sha256={inventory_hash} "
            f"selected_manifest_sha256={selected_manifest_hash}"
        )


if __name__ == "__main__":
    main()

