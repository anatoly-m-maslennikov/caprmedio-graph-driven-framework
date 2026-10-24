from collections.abc import Mapping
from pathlib import Path
from typing import Any

from selected_evidence_io import run_directory
from selected_execution_contracts import ActionHandler, SelectedExecutionError
from selected_execution_run_plan import (
    creation_native_binding,
    lifecycle_native_binding,
    replacement_native_binding,
)
from selected_implementation_packet import implementation_packet
from selected_graph_inputs import graph_parameters_with_actual_recording
from selected_graph_terminal import result_writer


def _native_binding_context(
    root: Path,
    graph: Mapping[str, Any],
    route: object,
    action: Mapping[str, Any],
    requested_action_id: str,
    run_id: str,
) -> dict[str, Any]:
    context: dict[str, Any] = {}
    action_id = action.get("atom_id")
    native_calls = graph.get("native_action_calls")
    if (
        route == "create_atom"
        and action_id == "CA-O-128"
        and isinstance(native_calls, list)
        and any(
            isinstance(binding, Mapping) and binding.get("atom_id") == "CA-O-032"
            for binding in native_calls
        )
    ):
        nested_id = f"{requested_action_id}:nested:CA-O-032"
        context.update(
            {
                "creation_action_binding": creation_native_binding(graph),
                "creation_requested_run_id": nested_id,
                "creation_result_writer": result_writer(
                    root, run_directory(root, run_id) / f"{nested_id}.json", "creation"
                ),
            }
        )
    lifecycle_action = "CA-O-030" if route == "update_atom" else None
    if (
        action_id == "CA-O-128"
        and lifecycle_action is not None
        and isinstance(native_calls, list)
        and any(
            isinstance(binding, Mapping) and binding.get("atom_id") == lifecycle_action
            for binding in native_calls
        )
    ):
        nested_id = f"{requested_action_id}:nested:{lifecycle_action}"
        context.update(
            {
                "lifecycle_action_binding": lifecycle_native_binding(graph, lifecycle_action),
                "lifecycle_requested_run_id": nested_id,
                "lifecycle_result_writer": result_writer(
                    root, run_directory(root, run_id) / f"{nested_id}.json", "lifecycle"
                ),
            }
        )
    if route == "replace_atom" and action_id == "CA-O-128":
        nested_id = f"{requested_action_id}:nested:CA-O-051"
        context.update(
            {
                "replacement_action_binding": replacement_native_binding(graph),
                "replacement_requested_run_id": nested_id,
                "replacement_result_writer": result_writer(
                    root, run_directory(root, run_id) / f"{nested_id}.json", "replacement"
                ),
            }
        )
    return context


def _parameters(
    graph: Mapping[str, Any],
    execution: Mapping[str, Any],
    step_id: str,
    prior_results: list[dict[str, Any]],
    session: Any,
    *,
    workflow_run_id: str,
    step_run_id: str,
    action_run_id: str,
) -> tuple[object, Mapping[str, Any] | None]:
    parameters: object = execution.get("parameters")
    trusted_authorization: Mapping[str, Any] | None = None
    if graph.get("workflow", {}).get("atom_id") == "CA-O-016":
        parameters = implementation_packet(parameters, step_id, prior_results)
        authorization = execution.get("operator_authorization")
        if isinstance(authorization, Mapping):
            trusted_authorization = authorization
            parameters = {**parameters, "operator_authorization": dict(authorization)}
    if graph.get("route") in {"build_entities_graph", "build_terms_graph"}:
        parameters = graph_parameters_with_actual_recording(
            parameters,
            session,
            workflow_run_id=workflow_run_id,
            step_run_id=step_run_id,
            action_run_id=action_run_id,
        )
    return parameters, trusted_authorization


def build_action_context(
    root: Path,
    handlers: Mapping[str, ActionHandler],
    frozen: Mapping[str, Any],
    session: Any,
    graph: Mapping[str, Any],
    step: Mapping[str, Any],
    action: Mapping[str, Any],
    *,
    workflow_run_id: str,
    step_run_id: str,
    action_run_id: str,
    requested_action_id: str,
    implementation_prior_results: list[dict[str, Any]],
    structural_prior_results: list[dict[str, Any]],
    lifecycle_prior_results: list[dict[str, Any]],
    journal_preparation: Any | None,
    restored_action_ids: frozenset[str],
) -> tuple[ActionHandler, dict[str, Any]]:
    request = frozen["request"]
    execution = request["execution"]
    action_id = action["atom_id"]
    handler = handlers.get(action_id)
    if handler is None:
        raise SelectedExecutionError(f"no native handler registered for Action {action_id}")
    parameters, trusted_authorization = _parameters(
        graph,
        execution,
        step["atom_id"],
        implementation_prior_results,
        session,
        workflow_run_id=workflow_run_id,
        step_run_id=step_run_id,
        action_run_id=action_run_id,
    )
    context: dict[str, Any] = {
        "project_root": root,
        "workflow_run_id": workflow_run_id,
        "step_run_id": step_run_id,
        "action_run_id": action_run_id,
        "workflow_definition": graph["workflow"],
        "step_definition": {
            key: value for key, value in step.items() if key not in {"actions", "on_result"}
        },
        "action_definition": action,
        "action_binding": action,
        "route": graph["route"],
        "workflow_definition_id": graph["workflow"]["atom_id"],
        "step_definition_id": step["atom_id"],
        "action_definition_id": action_id,
        "parameters": parameters,
        "trusted_execution_authorization": trusted_authorization,
        "target_frontier": execution.get("target_frontier"),
        "effects": execution.get("effects"),
        "initiative": execution.get("initiative"),
        "sealed_outer_admission": True,
        "session": session,
        "requested_action_run_id": requested_action_id,
    }
    context.update(
        _native_binding_context(
            root, graph, graph.get("route"), action, requested_action_id, request["run_id"]
        )
    )
    if any(
        context.get(key) is not None
        for key in (
            "creation_action_binding",
            "lifecycle_action_binding",
            "replacement_action_binding",
        )
    ):
        context["execution_request_id"] = execution.get("request_id")
    if graph.get("route") == "change_atom_status" and action_id == "CA-O-128":
        context["lifecycle_current_state"] = True
        context["execution_request_id"] = execution.get("request_id")
        context["restored_action"] = requested_action_id in restored_action_ids
    if action_id == "CA-O-162":
        context["journal_preparation"] = journal_preparation
    if graph["workflow"]["atom_id"] == "CA-O-015":
        context["structural_prior_results"] = list(structural_prior_results)
    if graph["workflow"]["atom_id"] == "CA-O-127":
        context["lifecycle_prior_results"] = list(lifecycle_prior_results)
    return handler, context
