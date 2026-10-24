"""Structural and freshness checks for one selected route request."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Mapping, cast

from selected_route_spec import _REQUEST_ID, SelectedRouteError
from selected_route_validation import _find_shadow_manifest_fields, _require_digest


def _public_digest(value: Any) -> str:
    public = sys.modules.get("selected_routes")
    if public is None:
        raise RuntimeError("selected_routes public module is unavailable")
    return cast(str, public.canonical_digest(value))


def _validate_request_shape(adapter: Any, route: str, request: Any) -> dict[str, Any]:
    if not isinstance(request, Mapping):
        raise SelectedRouteError("request must be an object")
    allowed = {
        "operation_route",
        "mode",
        "request_id",
        "parameters",
        "parameters_digest",
        "target_frontier",
        "target_frontier_digest",
        "effects",
        "effects_digest",
        "definition_manifest",
        "source_freshness",
        "expected_definition_revisions",
        "initiative",
        "lineage",
        "proposal_receipt",
        "proposal_receipt_digest",
        "assigned_action_id",
        "requested_runs",
        "operator_authorization",
    }
    if set(request) - allowed or _find_shadow_manifest_fields(
        request, allowed_definition_manifest=True
    ):
        raise SelectedRouteError("request contains unknown or shadow manifest fields")
    normalized = dict(request)
    normalized.setdefault("mode", "preview")
    if normalized.get("operation_route") != route or route not in adapter.routes:
        raise SelectedRouteError("request route is not the selected MCP route")
    if normalized["mode"] not in {"preview", "execute"}:
        raise SelectedRouteError("mode must be preview or execute")
    if not isinstance(normalized.get("request_id"), str) or not _REQUEST_ID.fullmatch(
        normalized["request_id"]
    ):
        raise SelectedRouteError("request_id must be a stable safe identity")
    return normalized


def _validate_payloads(normalized: Mapping[str, Any]) -> None:
    if not isinstance(normalized.get("parameters"), Mapping) or _public_digest(
        normalized["parameters"]
    ) != _require_digest(normalized.get("parameters_digest"), "parameters_digest differs"):
        raise SelectedRouteError("parameters or parameters_digest differs")
    frontier = normalized.get("target_frontier")
    if (
        not isinstance(frontier, list)
        or not frontier
        or not all(
            isinstance(ref, str) and ref and not ref.startswith("/") and ".." not in Path(ref).parts
            for ref in frontier
        )
    ):
        raise SelectedRouteError("target_frontier is invalid")
    if len(set(frontier)) != len(frontier) or _public_digest(frontier) != _require_digest(
        normalized.get("target_frontier_digest"), "target_frontier_digest differs"
    ):
        raise SelectedRouteError("target_frontier_digest differs")
    effects = normalized.get("effects")
    if not isinstance(effects, list) or any(
        not isinstance(effect, Mapping)
        or not isinstance(effect.get("type"), str)
        or not effect["type"]
        for effect in effects
    ):
        raise SelectedRouteError("effects are invalid")
    if _public_digest(effects) != _require_digest(
        normalized.get("effects_digest"), "effects_digest differs"
    ):
        raise SelectedRouteError("effects_digest differs")


def _validate_binding(adapter: Any, normalized: Mapping[str, Any]) -> None:
    manifest = normalized.get("definition_manifest")
    if not isinstance(manifest, Mapping) or set(manifest) != {"manifest_ref", "manifest_digest"}:
        raise SelectedRouteError("definition_manifest is invalid")
    if manifest != {
        "manifest_ref": adapter.manifest["manifest_ref"],
        "manifest_digest": adapter.manifest["canonical_manifest_sha256"],
    }:
        raise SelectedRouteError(
            "definition_manifest is stale or does not identify the canonical binding"
        )
    freshness = normalized.get("source_freshness")
    if (
        not isinstance(freshness, Mapping)
        or dict(freshness) != adapter.manifest["source_freshness"]
    ):
        raise SelectedRouteError("source_freshness is stale or incomplete")


def _validate_initiative_lineage(normalized: Mapping[str, Any]) -> None:
    initiative = normalized.get("initiative")
    if (
        not isinstance(initiative, Mapping)
        or not set(initiative) <= {"initiative_id", "instruction_summary", "initiative_ref"}
        or not all(
            isinstance(initiative.get(key), str) and initiative[key]
            for key in ("initiative_id", "instruction_summary")
        )
        or (
            "initiative_ref" in initiative
            and (
                not isinstance(initiative["initiative_ref"], str)
                or not initiative["initiative_ref"]
                or initiative["initiative_ref"].startswith("/")
                or ".." in Path(initiative["initiative_ref"]).parts
            )
        )
    ):
        raise SelectedRouteError("initiative must be an explicit sealed authorization boundary")
    lineage = normalized.get("lineage")
    if "lineage" in normalized and (
        not isinstance(lineage, list)
        or any(not isinstance(value, str) or not value for value in lineage)
    ):
        raise SelectedRouteError("lineage must contain only actual parent Run references")


def validate_request(adapter: Any, route: str, request: Any) -> dict[str, Any]:
    normalized = _validate_request_shape(adapter, route, request)
    _validate_payloads(normalized)
    _validate_binding(adapter, normalized)
    _validate_initiative_lineage(normalized)
    if "expected_definition_revisions" in normalized and normalized[
        "expected_definition_revisions"
    ] != adapter._expected_revisions(route):
        raise SelectedRouteError(
            "expected definition revisions differ from the selected route binding"
        )
    return normalized
