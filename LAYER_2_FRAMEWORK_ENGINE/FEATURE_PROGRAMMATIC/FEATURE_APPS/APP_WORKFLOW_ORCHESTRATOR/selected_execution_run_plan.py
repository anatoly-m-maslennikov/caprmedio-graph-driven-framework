"""Build and validate the finite Run plan for one frozen selected graph."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from selected_execution_contracts import RUN_ID, SelectedExecutionError


def build_requested_runs(
    graph: Mapping[str, Any],
    run_id: str,
    run_visit_limits: Mapping[str, int] | None = None,
) -> list[dict[str, Any]]:
    """Build every caller-authorized selected Run before an execution starts."""
    if not isinstance(run_id, str) or not RUN_ID.fullmatch(run_id):
        raise SelectedExecutionError("invalid selected Run ID")
    steps = graph.get("steps")
    workflow = graph.get("workflow")
    if not isinstance(steps, list) or not isinstance(workflow, Mapping):
        raise SelectedExecutionError("selected Workflow graph is invalid")
    limits = run_visit_limits_for(graph, run_visit_limits)
    expected: list[dict[str, Any]] = [
        {
            "requested_run_id": run_id,
            "kind": "workflow",
            "definition": support_definition(workflow),
        }
    ]
    for manifest_ordinal, step in enumerate(steps, start=1):
        step_id = step.get("atom_id")
        actions = step.get("actions")
        if not isinstance(step_id, str) or not isinstance(actions, list):
            raise SelectedExecutionError("selected Workflow graph is invalid")
        for visit in range(1, limits[step_id] + 1):
            requested_step = requested_step_id(run_id, manifest_ordinal, visit)
            expected.append(
                {
                    "requested_run_id": requested_step,
                    "kind": "step",
                    "definition": support_definition(step),
                    "parent_requested_run_id": run_id,
                }
            )
            for action_ordinal, action in enumerate(actions, start=1):
                requested_action = f"{requested_step}:action:{action_ordinal}"
                expected.append(
                    {
                        "requested_run_id": requested_action,
                        "kind": "action",
                        "definition": support_definition(action),
                        "parent_requested_run_id": requested_step,
                    }
                )
                expected.extend(nested_action_runs(graph, action, requested_action))
    return expected


def requested_step_id(run_id: str, manifest_ordinal: int, visit: int) -> str:
    """Keep first-visit IDs compatible while making later visits explicit."""
    first_visit = f"{run_id}:step:{manifest_ordinal}"
    return first_visit if visit == 1 else f"{first_visit}:visit:{visit}"


def declared_run_visit_limits(execution: Mapping[str, Any]) -> Mapping[str, int] | None:
    """Read optional finite revisit authority from admitted parameters."""
    parameters = execution.get("parameters")
    if not isinstance(parameters, Mapping):
        return None
    limits = parameters.get("run_visit_limits")
    if limits is None:
        return None
    if not isinstance(limits, Mapping):
        raise SelectedExecutionError("run_visit_limits must be a Step-to-positive-integer mapping")
    return limits


def run_visit_limits_for(
    graph: Mapping[str, Any],
    run_visit_limits: Mapping[str, int] | None,
) -> dict[str, int]:
    """Accept only explicit, finite revisit authority for bound Steps."""
    steps = graph.get("steps")
    if not isinstance(steps, list):
        raise SelectedExecutionError("selected Workflow graph is invalid")
    step_ids: list[str] = []
    for step in steps:
        if not isinstance(step, Mapping):
            raise SelectedExecutionError("selected Workflow graph is invalid")
        step_id = step.get("atom_id")
        if not isinstance(step_id, str):
            raise SelectedExecutionError("selected Workflow graph is invalid")
        step_ids.append(step_id)
    declared = dict(run_visit_limits or {})
    if set(declared) - set(step_ids):
        raise SelectedExecutionError("run_visit_limits includes an unbound Step")
    limits: dict[str, int] = {}
    for step_id in step_ids:
        limit = declared.get(step_id, 1)
        if type(limit) is not int or limit < 1 or limit > 100:
            raise SelectedExecutionError(
                "run_visit_limits must contain positive bounded visit limits"
            )
        limits[step_id] = limit
    return limits


def support_definition(binding: Mapping[str, Any]) -> dict[str, Any]:
    """Translate a manifest pin into the shared service's source pin shape."""
    return {
        "atom_id": binding["atom_id"],
        "version": binding["version"],
        "path": binding["path"],
        "digest": binding["sha256"],
    }


def nested_action_runs(
    graph: Mapping[str, Any],
    action: Mapping[str, Any],
    requested_action_id: str,
) -> list[dict[str, Any]]:
    """Declare the fixed source-bound child effects below supported O128 Actions."""
    if action.get("atom_id") != "CA-O-128":
        return []
    route = graph.get("route")
    if route == "replace_atom":
        return [_nested_row(requested_action_id, "CA-O-051", replacement_native_binding(graph))]
    if route == "create_atom" and has_native_action(graph, "CA-O-032"):
        return [_nested_row(requested_action_id, "CA-O-032", creation_native_binding(graph))]
    if route == "update_atom" and has_native_action(graph, "CA-O-030"):
        return [
            _nested_row(
                requested_action_id, "CA-O-030", lifecycle_native_binding(graph, "CA-O-030")
            )
        ]
    return []


def replacement_native_binding(graph: Mapping[str, Any]) -> dict[str, Any]:
    return sole_native_binding(graph, "CA-O-051", "replacement")


def creation_native_binding(graph: Mapping[str, Any]) -> dict[str, Any]:
    return sole_native_binding(graph, "CA-O-032", "creation")


def lifecycle_native_binding(graph: Mapping[str, Any], action_id: str) -> dict[str, Any]:
    if action_id != "CA-O-030":
        raise SelectedExecutionError("lifecycle native Action is not admitted")
    return sole_native_binding(graph, action_id, "lifecycle")


def sole_native_binding(graph: Mapping[str, Any], action_id: str, owner: str) -> dict[str, Any]:
    native_calls = graph.get("native_action_calls")
    if not isinstance(native_calls, list):
        raise SelectedExecutionError(f"{owner} graph has no native Action bindings")
    matches = [
        binding
        for binding in native_calls
        if isinstance(binding, Mapping) and binding.get("atom_id") == action_id
    ]
    if len(matches) != 1:
        raise SelectedExecutionError(f"{owner} graph must bind exactly one {action_id} Action")
    binding = matches[0]
    required = {"atom_id", "kind", "version", "path", "sha256"}
    if set(binding) != required or binding.get("kind") != "action":
        raise SelectedExecutionError(f"{owner} {action_id} Action binding is invalid")
    return dict(binding)


def has_native_action(graph: Mapping[str, Any], action_id: str) -> bool:
    native_calls = graph.get("native_action_calls")
    return isinstance(native_calls, list) and any(
        isinstance(binding, Mapping) and binding.get("atom_id") == action_id
        for binding in native_calls
    )


def _nested_row(
    requested_action_id: str, action_id: str, binding: Mapping[str, Any]
) -> dict[str, Any]:
    return {
        "requested_run_id": f"{requested_action_id}:nested:{action_id}",
        "kind": "action",
        "definition": support_definition(binding),
        "parent_requested_run_id": requested_action_id,
    }
