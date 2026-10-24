"""Validation of selected query-source admission proofs."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping

from selected_definition_sources import CurrentDefinitionSources
from selected_route_manifest import _query_admission_specs, _validate_pin
from selected_route_spec import (
    QUERY_ROUTE_NAMES,
    _QUERY_SOURCE_ADMISSION_FIELDS,
    SelectedRouteError,
)


def _validate_admission_shape(value: Any, expected: Mapping[str, Any]) -> None:
    if not isinstance(value, Mapping) or set(value) != _QUERY_SOURCE_ADMISSION_FIELDS:
        raise SelectedRouteError("query-source admission has an incomplete or unknown schema")
    if value.get("route") != expected["route"]:
        raise SelectedRouteError("query-source admission route order or identity differs")


def _validate_admission_definitions(
    root: Path, value: Mapping[str, Any], sources: Any
) -> dict[str, Any]:
    if not isinstance(value.get("ordered_steps"), list) or not isinstance(
        value.get("ordered_actions"), list
    ):
        raise SelectedRouteError("query-source admission definitions are malformed")
    admission: dict[str, Any] = {
        "route": value["route"],
        "acceptance_frontier": _validate_pin(root, value["acceptance_frontier"], sources, "Plan"),
        "workflow": _validate_pin(root, value["workflow"], sources, "Workflow"),
        "ordered_steps": [],
        "ordered_actions": [],
    }
    for item in value["ordered_steps"]:
        if not isinstance(item, Mapping) or set(item) != {"step", "action"}:
            raise SelectedRouteError("query-source admission Step binding is malformed")
        admission["ordered_steps"].append(
            {
                "step": _validate_pin(root, item["step"], sources, "Step"),
                "action": _validate_pin(root, item["action"], sources, "Action"),
            }
        )
    admission["ordered_actions"] = [
        _validate_pin(root, item, sources, "Action") for item in value["ordered_actions"]
    ]
    return admission


def validate_query_source_admissions(
    root: Path, admissions: Any, routes: list[dict[str, Any]], sources: Any = None
) -> list[dict[str, Any]]:
    owned_sources = sources is None
    sources = sources or CurrentDefinitionSources(root)
    specifications = _query_admission_specs(root, sources)
    if not isinstance(admissions, list) or len(admissions) != len(specifications):
        raise SelectedRouteError("selected query-source admissions must contain exactly two routes")
    by_route = {entry["route"]: entry for entry in routes}
    validated: list[dict[str, Any]] = []
    for value, expected in zip(admissions, specifications, strict=True):
        _validate_admission_shape(value, expected)
        route = by_route.get(value["route"])
        if route is None or route["route"] not in QUERY_ROUTE_NAMES or route["mutation_capable"]:
            raise SelectedRouteError(
                "query-source admission does not bind one read-only selected route"
            )
        admission = _validate_admission_definitions(root, value, sources)
        if admission != expected:
            raise SelectedRouteError(
                "query-source admission differs from the accepted source frontier"
            )
        if any(
            admission[key] != route[key] for key in ("workflow", "ordered_steps", "ordered_actions")
        ):
            raise SelectedRouteError(
                "query-source admission definitions differ from the selected route"
            )
        validated.append(admission)
    if owned_sources:
        sources.revalidate()
    return validated
