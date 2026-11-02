from __future__ import annotations
import copy
from typing import Any, Mapping

ACTIONS = {
    "CA-O-231": "CA-O-017",
    "CA-O-232": "CA-O-018",
    "CA-O-233": "CA-O-019",
    "CA-O-094": "CA-O-020",
    "CA-O-234": "CA-O-089",
    "CA-O-096": "CA-O-024",
    "CA-O-099": "CA-O-021",
    "CA-O-230": "CA-O-225",
}


def _input_binding(fixture: Any, atom_id: str) -> dict[str, Any]:
    row = next(row for row in fixture._support_rows() if row["atom_id"] == atom_id)
    binding = dict(row)
    binding["content"] = fixture.support_source_bytes(atom_id).decode("utf-8")
    return binding


def _selection_fields(
    fixture: Any, source_bindings: list[dict[str, Any]], methods: Mapping[str, Any]
) -> dict[str, Any]:
    return {
        "context": "Integrated",
        "selected_project": {
            "kind": "selected_project",
            "source_root": ".caprmedio_caprmedio",
            "source_references": source_bindings,
        },
        "source_bindings": source_bindings,
        "method_projection": {
            "content": fixture.method_projection_content(),
            "sources": methods["sources"],
        },
    }


def _rde_fields(fixture: Any, applicable: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "requirements": [
            _input_binding(fixture, row["atom_id"]) for row in applicable["requirements"]
        ],
        "delivery": [_input_binding(fixture, row["atom_id"]) for row in applicable["deliveries"]],
        "evaluations": [
            _input_binding(fixture, row["atom_id"]) for row in applicable["evaluations"]
        ],
    }


def _permission_fields() -> dict[str, Any]:
    return {
        "permissions": {
            "allowed": True,
            "implementation_workspace": {
                "kind": "disposable_workspace",
                "path": "fixture/disposable-workspace",
                "allow_write": True,
            },
        },
        "workspace": "fixture/disposable-workspace",
        "candidate": "fixture-candidate-v1",
        "phase": "implementation",
        "owned_paths": ["."],
    }


def _plan_fields() -> dict[str, Any]:
    return {
        "plan_item": {
            "plan_id": "current-shared-context-plan",
            "item_id": "current-implementation",
            "dod": ["candidate and bound checks are retained"],
            "owned_paths": ["."],
            "estimated_minutes": 1,
        },
        "red": {
            "expectation": "the current fixture journey returns declared outcomes",
            "fixtures": ["fixture/disposable-workspace/current_candidate.py"],
            "commands": ["python -I -B fixture/disposable-workspace/current_candidate.py"],
        },
        "golden_e2e": ["current fixture candidate assertion"],
        "baseline_command": "python -I -B fixture/disposable-workspace/current_candidate.py",
    }


def _state_fields(applicable: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "confidence": {"observed": 1.0, "effective": 0.9, "source": "fixture-settings"},
        "retry": {
            "consumed": 0,
            "effective_limit": 1,
            "source": "fixture-settings",
            "remaining_failure": True,
            "admitted": True,
        },
        "coverage": {
            "required": [row["atom_id"] for row in applicable["evaluations"]],
            "checked": [],
            "complete": False,
            "candidate": "fixture-candidate-v1",
            "phase": "implementation",
        },
        "retained_state": {"transport": "external-agent-test-double", "prior_results": []},
    }


def _base_packet(
    fixture: Any,
    source_bindings: list[dict[str, Any]],
    methods: Mapping[str, Any],
    applicable: Mapping[str, Any],
) -> dict[str, Any]:
    base: dict[str, Any] = {}
    for fields in (
        _selection_fields(fixture, source_bindings, methods),
        _rde_fields(fixture, applicable),
        _permission_fields(),
        _plan_fields(),
        _state_fields(applicable),
    ):
        base.update(fields)
    return base


def _step_packets(source_bindings: list[dict[str, Any]]) -> dict[str, Any]:
    packets = {}
    for step_id, action_id in ACTIONS.items():
        step = next(pin for pin in source_bindings if pin["atom_id"] == step_id)
        action = next(pin for pin in source_bindings if pin["atom_id"] == action_id)
        packets[step_id] = {
            "context": "Integrated",
            "step_marker": step_id,
            "step_binding": step,
            "action_binding": action,
        }
    return packets


def build_native_parameters(fixture: Any) -> dict[str, Any]:
    fixture.verify()
    support = fixture.support_inventory
    source_bindings = [dict(pin) for pin in fixture.source_pins()]
    base = _base_packet(
        fixture,
        source_bindings,
        support["method_projection"],
        support["applicable_rde"],
    )
    return {
        "base_packet": base,
        "run_visit_limits": {"CA-O-231": 4, "CA-O-094": 2},
        "step_packets": _step_packets(source_bindings),
    }


def packet_variant(fixture: Any, **changes: object) -> dict[str, Any]:
    packet = copy.deepcopy(build_native_parameters(fixture))
    base = packet["base_packet"]
    if isinstance(changes.get("stale_atom"), str):
        binding = next(
            row for row in base["source_bindings"] if row["atom_id"] == changes["stale_atom"]
        )
        binding["sha256"] = "0" * 64
    if isinstance(changes.get("review_phase"), str):
        base["review_phase"] = changes["review_phase"]
    if isinstance(changes.get("candidate"), str):
        base["candidate"] = changes["candidate"]
    if isinstance(changes.get("retry_limit"), int):
        base["retry"]["effective_limit"] = changes["retry_limit"]
    if isinstance(changes.get("retry_consumed"), int):
        base["retry"]["consumed"] = changes["retry_consumed"]
    return packet


def packet_bindings_are_current(fixture: Any, packet: Mapping[str, Any]) -> bool:
    expected = {row["atom_id"]: row["sha256"] for row in fixture.source_pins()}
    actual = packet.get("base_packet", {}).get("source_bindings", [])
    return (
        isinstance(actual, list)
        and all(
            isinstance(row, Mapping) and expected.get(row.get("atom_id")) == row.get("sha256")
            for row in actual
        )
        and {row.get("atom_id") for row in actual if isinstance(row, Mapping)} == set(expected)
    )
