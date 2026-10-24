"""Manifest parsing and source-pin validation for selected routes."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping

from connector_bindings import capture_source
from selected_definition_sources import CurrentDefinitionSources
from selected_route_manifest import (
    _current_pin,
    _selected_authority_ref,
    canonical_digest,
    selected_manifest_ref,
)
from selected_route_query import validate_query_source_admissions
from selected_route_request_support import find_shadow_manifest_fields, require_digest
from selected_route_route import validate_route
from selected_route_spec import (
    ADMITTED_SELECTED_ROUTE_NAMES,
    SELECTED_ROUTE_NAMES,
    _DIGEST,
    _FRESHNESS_FIELDS,
    _ORIGINAL_SELECTED_SOURCE_REGISTRY_REF,
    SelectedRouteError,
)

_validate_route = validate_route
_validate_query_source_admissions = validate_query_source_admissions
_find_shadow_manifest_fields = find_shadow_manifest_fields
_require_digest = require_digest


def _definition_sequence(route: Mapping[str, Any]) -> list[dict[str, Any]]:
    return [
        route["workflow"],
        *[item["step"] for item in route["ordered_steps"]],
        *route["ordered_actions"],
    ]


def _unique_manifest_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise SelectedRouteError(
                f"selected workflow binding manifest has duplicate JSON member: {key}"
            )
        result[key] = value
    return result


def _validate_manifest_freshness(
    project_root: Path, manifest: Mapping[str, Any], manifest_ref: str
) -> Mapping[str, Any]:
    required = {
        "schema_version",
        "source_freshness",
        "query_source_admissions",
        "routes",
        "canonical_manifest_sha256",
    }
    if (
        not isinstance(manifest, Mapping)
        or set(manifest) != required
        or manifest["schema_version"] != 1
    ):
        raise SelectedRouteError("selected workflow binding manifest schema is invalid")
    digest = manifest["canonical_manifest_sha256"]
    if not isinstance(digest, str) or not _DIGEST.fullmatch(digest):
        raise SelectedRouteError("selected workflow binding manifest digest is invalid")
    if (
        canonical_digest(
            {key: value for key, value in manifest.items() if key != "canonical_manifest_sha256"}
        )
        != digest
    ):
        raise SelectedRouteError("selected workflow binding manifest canonical digest differs")
    freshness = manifest["source_freshness"]
    if not isinstance(freshness, Mapping) or set(freshness) != _FRESHNESS_FIELDS:
        raise SelectedRouteError("selected workflow binding manifest source freshness is invalid")
    if (
        not all(
            isinstance(freshness[key], str) and freshness[key]
            for key in _FRESHNESS_FIELDS - {"selected_source_registry_version"}
        )
        or type(freshness["selected_source_registry_version"]) is not int
        or freshness["selected_source_registry_version"] < 1
    ):
        raise SelectedRouteError(
            "selected workflow binding manifest source freshness is incomplete"
        )
    if not _DIGEST.fullmatch(freshness["selected_source_registry_digest"]) or not _DIGEST.fullmatch(
        freshness["selected_binding_digest"]
    ):
        raise SelectedRouteError("selected workflow binding manifest freshness digest is invalid")
    if freshness["selected_source_registry_ref"] != _selected_authority_ref(
        project_root, _ORIGINAL_SELECTED_SOURCE_REGISTRY_REF
    ):
        raise SelectedRouteError(
            "selected workflow binding manifest does not retain the CA-A-1142 registry authority"
        )
    if freshness["selected_binding_ref"] != f"{manifest_ref}#/routes":
        raise SelectedRouteError(
            "selected workflow binding manifest does not retain its binding reference"
        )
    return freshness


def _validate_manifest_routes(
    project_root: Path,
    manifest: Mapping[str, Any],
    freshness: Mapping[str, Any],
    sources: CurrentDefinitionSources,
) -> tuple[Mapping[str, Any], list[dict[str, Any]], list[dict[str, Any]]]:
    registry = _current_pin(
        project_root,
        {"atom_id": "CA-A-1142", "source_path": freshness["selected_source_registry_ref"]},
        sources,
        "Analysis Report",
    )
    routes = manifest["routes"]
    if not isinstance(routes, list) or len(routes) not in {
        len(SELECTED_ROUTE_NAMES),
        len(ADMITTED_SELECTED_ROUTE_NAMES),
    }:
        raise SelectedRouteError(
            "selected workflow binding manifest must contain fifteen routes or sixteen with move_atom"
        )
    expected_names = (
        ADMITTED_SELECTED_ROUTE_NAMES
        if len(routes) == len(ADMITTED_SELECTED_ROUTE_NAMES)
        else SELECTED_ROUTE_NAMES
    )
    if canonical_digest(routes) != freshness["selected_binding_digest"]:
        raise SelectedRouteError("selected workflow route binding digest differs")
    validated = [_validate_route(project_root, entry, sources) for entry in routes]
    if tuple(entry["route"] for entry in validated) != expected_names or len(
        {entry["route"] for entry in validated}
    ) != len(expected_names):
        raise SelectedRouteError("selected workflow route registry is incomplete or duplicate")
    admissions = _validate_query_source_admissions(
        project_root, manifest["query_source_admissions"], validated, sources
    )
    return registry, validated, admissions


def validate_selected_manifest_document(root: str | Path, manifest: Any) -> dict[str, Any]:
    project_root = Path(root).resolve(strict=True)
    manifest_ref = selected_manifest_ref(project_root)
    freshness = _validate_manifest_freshness(project_root, manifest, manifest_ref)
    sources = CurrentDefinitionSources(project_root)
    registry, validated, admissions = _validate_manifest_routes(
        project_root, manifest, freshness, sources
    )
    freshness = {
        **freshness,
        "selected_source_registry_version": registry["version"],
        "selected_source_registry_digest": registry["digest"],
        "selected_binding_digest": canonical_digest(validated),
    }
    resolved = {
        "schema_version": 1,
        "source_freshness": freshness,
        "query_source_admissions": admissions,
        "routes": validated,
    }
    sources.revalidate()
    return {
        "manifest_ref": manifest_ref,
        **resolved,
        "canonical_manifest_sha256": canonical_digest(resolved),
    }


def load_selected_manifest(root: str | Path) -> dict[str, Any]:
    project_root = Path(root).resolve(strict=True)
    try:
        source = capture_source(project_root, selected_manifest_ref(project_root))
        manifest = json.loads(
            source.read_bytes().decode("utf-8"), object_pairs_hook=_unique_manifest_object
        )
    except (OSError, json.JSONDecodeError) as error:
        raise SelectedRouteError("selected workflow binding manifest is unreadable") from error
    result = validate_selected_manifest_document(project_root, manifest)
    source.revalidate()
    return result
