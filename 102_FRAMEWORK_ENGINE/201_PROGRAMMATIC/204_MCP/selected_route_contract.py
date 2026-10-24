"""Public contract metadata for the selected-route manifest."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from selected_route_spec import SELECTED_ROUTE_NAMES, _FRESHNESS_FIELDS


def selected_manifest_contract(root: str | Path | None = None) -> dict[str, Any]:
    from selected_route_manifest import selected_manifest_ref

    return {
        "manifest_ref": selected_manifest_ref(root),
        "schema_version": 1,
        "canonical_digest": {
            "algorithm": "sha256",
            "serialization": "RFC8785",
            "self_field": "canonical_manifest_sha256",
            "self_field_omitted_from_digest": True,
        },
        "outer_fields": [
            "schema_version",
            "source_freshness",
            "query_source_admissions",
            "routes",
            "canonical_manifest_sha256",
        ],
        "source_freshness_fields": sorted(_FRESHNESS_FIELDS),
        "query_source_admission_fields": [
            "route",
            "acceptance_frontier",
            "workflow",
            "ordered_steps",
            "ordered_actions",
        ],
        "route_fields": [
            "route",
            "workflow",
            "ordered_steps",
            "ordered_actions",
            "native_action_calls",
            "entry_step",
            "on_result",
            "mutation_capable",
        ],
        "definition_pin_fields": ["atom_id", "version", "source_path", "digest"],
        "on_result_fields": ["from", "condition", "to"],
        "on_result_terminal_target": "complete",
        "route_names": list(SELECTED_ROUTE_NAMES),
        "optional_route_names": ["move_atom"],
    }
