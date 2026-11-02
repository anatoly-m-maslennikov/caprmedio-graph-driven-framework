from __future__ import annotations
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any
from selected_execution_contracts import (
    SelectedExecutionError,
    _contains_execution_secret,
)
from selected_graph_sources import load_manifest, select_route, validate_definition
from selected_source_graph_edges import source_bound_d547_edges


def contains_execution_secret(execution: Mapping[str, Any]) -> bool:
    return _contains_execution_secret(execution)


def _ordered_definitions(
    root: Path, ordered: list[object]
) -> tuple[list[dict[str, Any]], set[str]]:
    steps: list[dict[str, Any]] = []
    seen: set[str] = set()
    for raw in ordered:
        if not isinstance(raw, Mapping) or set(raw) != {"step", "action"}:
            raise SelectedExecutionError("D547 selected ordered Step/Action binding is invalid")
        step = validate_definition(root, raw["step"], expected_kind="step")
        action = validate_definition(root, raw["action"], expected_kind="action")
        if step["atom_id"] in seen:
            raise SelectedExecutionError("D547 selected Workflow has duplicate Step bindings")
        seen.add(step["atom_id"])
        step["actions"] = [action]
        steps.append(step)
    return steps, seen


def _transition(source_edges: bool, target: str, seen: set[str]) -> dict[str, str]:
    transition: dict[str, str] = {}
    if source_edges:
        terminal = {"completed": "completed", "blocked": "interrupted_pending"}.get(target)
        if terminal is not None:
            transition["terminal"] = terminal
        elif target in seen:
            transition["next"] = target
        else:
            raise SelectedExecutionError("D547 source Workflow has an undeclared terminal result")
    elif target == "complete":
        transition["terminal"] = "completed"
    else:
        transition["next"] = target
    return transition


def _graph_transitions(
    raw_edges: Sequence[object], source_edges: bool, seen: set[str]
) -> dict[str, list[dict[str, str]]]:
    transitions: dict[str, list[dict[str, str]]] = {}
    pairs: set[tuple[str, str]] = set()
    for raw in raw_edges:
        if not isinstance(raw, Mapping) or set(raw) != {"from", "condition", "to"}:
            raise SelectedExecutionError("D547 selected On Result binding is invalid")
        source, condition, target = raw["from"], raw["condition"], raw["to"]
        if not all(isinstance(value, str) and value for value in (source, condition, target)):
            raise SelectedExecutionError("D547 selected On Result binding has an invalid endpoint")
        if (source, condition) in pairs:
            raise SelectedExecutionError(
                "D547 selected Workflow has duplicate On Result conditions"
            )
        pairs.add((source, condition))
        item = _transition(source_edges, target, seen)
        item["result"] = condition
        transitions.setdefault(source, []).append(item)
    return transitions


def assemble_d547_graph(root: Path, route: Mapping[str, Any]) -> tuple[list[dict[str, Any]], str]:
    ordered, entry = route.get("ordered_steps"), route.get("entry_step")
    if not isinstance(ordered, list) or not ordered or not isinstance(entry, str):
        raise SelectedExecutionError(
            "D547 selected Workflow must bind ordered Steps and entry_step"
        )
    steps, seen = _ordered_definitions(root, ordered)
    source_edges = source_bound_d547_edges(root, route, seen)
    raw_edges = source_edges if source_edges is not None else route.get("on_result")
    if not isinstance(raw_edges, list):
        raise SelectedExecutionError("D547 selected Workflow On Result bindings are invalid")
    transitions = _graph_transitions(raw_edges, source_edges is not None, seen)
    for step in steps:
        step["on_result"] = transitions.get(step["atom_id"], [])
    if entry not in seen:
        raise SelectedExecutionError("D547 selected Workflow entry_step is not bound")
    for source, values in transitions.items():
        if source not in seen:
            raise SelectedExecutionError("D547 On Result source is not a bound Step")
        if any(item.get("next") not in seen for item in values if item.get("next") is not None):
            raise SelectedExecutionError("D547 On Result target is not a bound Step")
    return steps, entry


def _plain_graph_steps(root: Path, raw_steps: object) -> tuple[list[dict[str, Any]], str]:
    if not isinstance(raw_steps, list) or not raw_steps:
        raise SelectedExecutionError("selected Workflow must bind ordered Steps")
    steps: list[dict[str, Any]] = []
    ids: set[str] = set()
    for raw in raw_steps:
        if not isinstance(raw, Mapping):
            raise SelectedExecutionError("selected Step binding is invalid")
        step = validate_definition(root, raw, expected_kind="step")
        if step["atom_id"] in ids:
            raise SelectedExecutionError("selected Workflow has duplicate Step bindings")
        ids.add(step["atom_id"])
        actions, transitions = raw.get("actions"), raw.get("on_result")
        if not isinstance(actions, list) or not actions:
            raise SelectedExecutionError("selected Step must bind ordered Actions")
        if not isinstance(transitions, list) or not transitions:
            raise SelectedExecutionError("selected Step must bind On Result transitions")
        if any(not isinstance(item, Mapping) for item in transitions):
            raise SelectedExecutionError("selected On Result transition is invalid")
        step["actions"] = [
            validate_definition(root, action, expected_kind="action")
            for action in actions
            if isinstance(action, Mapping)
        ]
        if len(step["actions"]) != len(actions):
            raise SelectedExecutionError("selected Action binding is invalid")
        step["on_result"] = [dict(item) for item in transitions]
        steps.append(step)
    return steps, steps[0]["atom_id"]


def validate_graph(root: Path, execution: Mapping[str, Any]) -> dict[str, Any]:
    if contains_execution_secret(execution):
        raise SelectedExecutionError("selected execution carries a secret field")
    if execution.get("mode") != "execute":
        raise SelectedExecutionError("enqueue_selected accepts only an execute request")
    route_name = execution.get("operation_route")
    if not isinstance(route_name, str) or not route_name:
        raise SelectedExecutionError("selected operation route is required")
    manifest, manifest_ref, manifest_digest = load_manifest(root, execution)
    route = select_route(manifest, route_name)
    freshness = manifest.get("source_freshness")
    if freshness is not None and (
        not isinstance(freshness, Mapping) or execution.get("source_freshness") != freshness
    ):
        raise SelectedExecutionError(
            "selected request source freshness does not match definition manifest"
        )
    workflow = route.get("workflow")
    if not isinstance(workflow, Mapping):
        raise SelectedExecutionError("selected Workflow binding is required")
    validated_workflow = validate_definition(root, workflow, expected_kind="workflow")
    native = route.get("native_action_calls", [])
    if not isinstance(native, list):
        raise SelectedExecutionError("selected native Action bindings are invalid")
    validated_native = [
        validate_definition(root, binding, expected_kind="action")
        for binding in native
        if isinstance(binding, Mapping)
    ]
    if len(validated_native) != len(native):
        raise SelectedExecutionError("selected native Action binding is invalid")
    steps, entry = (
        assemble_d547_graph(root, route)
        if "ordered_steps" in route
        else _plain_graph_steps(root, route.get("steps"))
    )
    return {
        "route": route_name,
        "workflow": validated_workflow,
        "steps": steps,
        "entry_step": entry,
        "native_action_calls": validated_native,
        "manifest_ref": manifest_ref,
        "manifest_digest": manifest_digest,
    }
