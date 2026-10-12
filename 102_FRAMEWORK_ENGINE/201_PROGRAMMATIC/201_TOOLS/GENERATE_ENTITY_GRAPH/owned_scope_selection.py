"""Prepare a sealed, metadata-owned Atom selection for one Scope Unit.

This helper deliberately does not build a graph or infer ownership from a
folder.  It only prepares source Atom IDs that a caller may later bind
into the existing strict graph request.
"""

from __future__ import annotations

import hashlib
import importlib
import sys
import tomllib
from pathlib import Path
from typing import Any


def _generator() -> Any:
    """Load the graph implementation lazily, avoiding an import-time cycle."""

    tools_root = str(Path(__file__).resolve().parents[1])
    if tools_root not in sys.path:
        sys.path.insert(0, tools_root)
    return importlib.import_module("GENERATE_ENTITY_GRAPH.generate_entity_graph")


def _diagnostic(code: str, message: str, **details: object) -> dict[str, object]:
    record: dict[str, object] = {"severity": "error", "code": code, "message": message}
    if details:
        record["details"] = details
    return record


def _result(
    outcome: str,
    scope_unit_name: str,
    *,
    frontier: dict[str, object] | None = None,
    inventory: dict[str, object] | None = None,
    diagnostics: list[dict[str, object]] | None = None,
) -> dict[str, object]:
    return {
        "outcome": outcome,
        "selection": {"atom_ids": [], "scope_unit_names": [scope_unit_name]},
        "source_frontier": frontier or {},
        "inventory": inventory or {"support_sources": [], "external_references": []},
        "diagnostics": diagnostics or [],
    }


def prepare_owned_scope_selection(repository: Path, selected_folder: Path, scope_unit_name: str) -> dict[str, object]:
    """Return exact-Active source Atom IDs and sealed ownership evidence.

    Scope Unit names are structural evidence, not a membership query: an Atom
    is selected only when its own explicit ``current_scope_unit`` equals the
    requested name and its explicit ``status`` is exactly ``Active``. Other
    role/type lifecycle spellings need their own source-pinned evaluator; this
    helper neither normalizes them nor grants native graph membership.
    """

    diagnostics: list[dict[str, object]] = []
    if not isinstance(scope_unit_name, str) or not scope_unit_name:
        return _result("failed", str(scope_unit_name), diagnostics=[
            _diagnostic("scope-unit-name-invalid", "scope_unit_name must be a non-empty string.")
        ])

    try:
        repository = repository.resolve(strict=True)
        selected_folder = selected_folder.resolve(strict=True)
        if not repository.is_dir() or not selected_folder.is_dir():
            raise ValueError("repository and selected_folder must be directories")
        try:
            selected_folder.relative_to(repository)
        except ValueError as error:
            raise ValueError("selected_folder must be inside repository") from error
    except (OSError, ValueError) as error:
        return _result("failed", scope_unit_name, diagnostics=[
            _diagnostic("selected-folder-outside-project", "Selected folder must be an existing project path.")
        ])

    graph = _generator()
    try:
        # The existing discovery and frontier own parsing, exclusion and source
        # hashing.  Selection-specific checks below intentionally add no query
        # language and no folder-to-owner convention.
        carriers, discovery_diagnostics = graph.discover_atoms(repository, selected_folder)
        frontier = graph.source_frontier_for(repository, selected_folder)
        control_root = graph._configured_control_root(repository)
        structure_path = control_root / "project_structure.toml"
        if not structure_path.is_file():
            raise graph.EntityGraphError(
                "project-structure-unavailable", "Configured Project Structure carrier is unavailable.",
                path=graph._display_path(structure_path, repository),
            )
        structure_evidence = frontier.get("project_structure")
        expected_hash = hashlib.sha256(structure_path.read_bytes()).hexdigest()
        if not isinstance(structure_evidence, dict) or structure_evidence.get("carrier_sha256") != expected_hash:
            raise graph.EntityGraphError(
                "project-structure-unbound", "Project Structure hash is not bound into the source frontier."
            )
        structure = tomllib.loads(structure_path.read_text(encoding="utf-8"))
        rows = [
            row for row in structure.get("scope_units", [])
            if isinstance(row, dict) and row.get("scope_unit_name") == scope_unit_name
        ]
        if len(rows) != 1:
            raise graph.EntityGraphError(
                "scope-unit-structure-ambiguous",
                "Exactly one current Project Structure row is required for the selected Scope Unit.",
                scope_unit_name=scope_unit_name, matching_rows=len(rows),
            )

        seen: set[str] = set()
        native_ids: list[str] = []
        support_sources: list[dict[str, object]] = []
        for carrier in carriers:
            explicit_id = graph.top_scalar(carrier.frontmatter, "atom_id")
            owner = graph.top_scalar(carrier.frontmatter, "current_scope_unit")
            explicit_status = graph.top_scalar(carrier.frontmatter, "status")
            missing = [
                name for name, value in (("atom_id", explicit_id), ("current_scope_unit", owner), ("status", explicit_status))
                if not isinstance(value, str) or not value
            ]
            if missing:
                raise graph.EntityGraphError(
                    "owned-scope-property-missing",
                    "Selected Atom Carrier lacks required explicit ownership properties.",
                    carrier_path=carrier.carrier_path, properties=missing,
                )
            # Do this before any ID-indexing operation.  In particular, do not
            # accept discover_atoms' historical filename fallback as authority.
            if explicit_id in seen:
                raise graph.EntityGraphError(
                    "atom-id-duplicate", "Selected Atom Carriers contain a duplicate explicit atom_id.", atom_id=explicit_id
                )
            seen.add(explicit_id)
            if explicit_status == "Active" and owner == scope_unit_name:
                native_ids.append(explicit_id)
            elif explicit_status == "Active":
                support_sources.append({
                    "atom_id": explicit_id,
                    "current_scope_unit": owner,
                    "carrier_path": carrier.carrier_path,
                    "carrier_sha256": carrier.sha256,
                })

        for evidence in frontier.get("carriers", []):
            if not isinstance(evidence, dict) or not isinstance(evidence.get("carrier_path"), str):
                raise graph.EntityGraphError("source-frontier-invalid", "Source frontier has invalid carrier evidence.")
            graph._safe_repository_path(repository, evidence["carrier_path"], name="source_frontier.carrier_path")
        diagnostics.extend(discovery_diagnostics)
    except graph.EntityGraphError as error:
        if error.code == "atom-set-empty":
            return _result("incomplete", scope_unit_name, diagnostics=[*diagnostics, error.record()])
        return _result("failed", scope_unit_name, diagnostics=[*diagnostics, error.record()])
    except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError, ValueError) as error:
        return _result("failed", scope_unit_name, diagnostics=[*diagnostics, _diagnostic(
            "owned-scope-selection-invalid", "Owned Scope selection source cannot be prepared."
        )])

    inventory = {"support_sources": sorted(support_sources, key=lambda item: str(item["atom_id"])), "external_references": []}
    result = _result("prepared" if native_ids else "incomplete", scope_unit_name,
                     frontier=frontier, inventory=inventory, diagnostics=diagnostics)
    result["selection"] = {"atom_ids": sorted(native_ids), "scope_unit_names": [scope_unit_name]}
    if not native_ids:
        result["diagnostics"].append(_diagnostic(
            "owned-atom-set-empty", "No exact Active Atom Carrier is owned by the selected Scope Unit.",
            scope_unit_name=scope_unit_name,
        ))
    return result
