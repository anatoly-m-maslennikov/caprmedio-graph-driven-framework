"""Validation of one selected Workflow route binding."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping

from selected_route_manifest import _validate_pin
from selected_route_spec import ADMITTED_SELECTED_ROUTE_NAMES, SelectedRouteError


def _validate_route_shape(entry: Any) -> None:
    required = {
        "route",
        "workflow",
        "ordered_steps",
        "ordered_actions",
        "native_action_calls",
        "entry_step",
        "on_result",
        "mutation_capable",
    }
    if not isinstance(entry, Mapping) or set(entry) != required:
        raise SelectedRouteError("route binding has an incomplete or unknown schema")
    if entry["route"] not in ADMITTED_SELECTED_ROUTE_NAMES or not isinstance(
        entry["entry_step"], str
    ):
        raise SelectedRouteError("route binding has an unsupported route or entry step")
    if (
        not isinstance(entry["mutation_capable"], bool)
        or not isinstance(entry["ordered_steps"], list)
        or not entry["ordered_steps"]
    ):
        raise SelectedRouteError("route binding has no ordered step graph")
    if not isinstance(entry["ordered_actions"], list) or not isinstance(
        entry["native_action_calls"], list
    ):
        raise SelectedRouteError("route binding has an invalid ordered Action list")


def _validate_route_steps(
    root: Path, entries: list[Any], sources: Any
) -> tuple[list[dict[str, Any]], set[str]]:
    steps: list[dict[str, Any]] = []
    for item in entries:
        if not isinstance(item, Mapping) or set(item) != {"step", "action"}:
            raise SelectedRouteError("ordered step binding must have one Step and one Action")
        steps.append(
            {
                "step": _validate_pin(root, item["step"], sources, "Step"),
                "action": _validate_pin(root, item["action"], sources, "Action"),
            }
        )
    return steps, {item["step"]["atom_id"] for item in steps}


def _validate_route_edges(edges: Any, step_ids: set[str]) -> None:
    if not isinstance(edges, list):
        raise SelectedRouteError("route on_result must be an ordered list")
    for edge in edges:
        if (
            not isinstance(edge, Mapping)
            or set(edge) != {"from", "condition", "to"}
            or not all(
                isinstance(edge[key], str) and edge[key] for key in ("from", "condition", "to")
            )
        ):
            raise SelectedRouteError("route on_result edge is malformed")
        if edge["from"] not in step_ids:
            raise SelectedRouteError("route on_result source is not in its ordered Step list")
        if edge["to"] != "complete" and edge["to"] not in step_ids:
            raise SelectedRouteError(
                "route on_result target is not in its ordered Step list or complete"
            )


def validate_route(root: Path, entry: Any, sources: Any = None) -> dict[str, Any]:
    _validate_route_shape(entry)
    result = dict(entry)
    result["workflow"] = _validate_pin(root, entry["workflow"], sources, "Workflow")
    steps, step_ids = _validate_route_steps(root, entry["ordered_steps"], sources)
    if entry["entry_step"] not in step_ids:
        raise SelectedRouteError("route entry step is not in its ordered Step list")
    actions = [_validate_pin(root, item, sources, "Action") for item in entry["ordered_actions"]]
    if [item["action"]["atom_id"] for item in steps] != [item["atom_id"] for item in actions]:
        raise SelectedRouteError("ordered Action list differs from Step Action bindings")
    _validate_route_edges(entry["on_result"], step_ids)
    result.update(
        ordered_steps=steps,
        ordered_actions=actions,
        native_action_calls=[
            _validate_pin(root, item, sources, "Action") for item in entry["native_action_calls"]
        ],
    )
    return result
