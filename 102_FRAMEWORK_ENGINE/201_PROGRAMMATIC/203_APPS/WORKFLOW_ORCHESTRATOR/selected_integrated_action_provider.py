"""Current prompt provider and native-context adapter for Integrated Actions."""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path
from typing import Any

from selected_integrated_action_contract import prompt_spec, validate_response
from selected_integrated_action_outcome import validate_outcome
from selected_integrated_action_runtime import validate_action_binding


def current_integrated_action_provider(
    packet: Mapping[str, Any],
    *,
    agent: Any,
    selected_project_root: Path,
    trusted_execution_authorization: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Run one current source-bound prompt through a caller-owned callback."""
    del selected_project_root, trusted_execution_authorization
    step_id = packet.get("step_marker")
    binding = packet.get("action_binding")
    action_id = binding.get("atom_id") if isinstance(binding, Mapping) else None
    if not isinstance(step_id, str) or not isinstance(action_id, str):
        raise ValueError("current Step and Action bindings are missing")
    validate_action_binding(packet, step_id, action_id)
    spec = prompt_spec(step_id, action_id)
    response = agent(spec["prompt"], packet)
    checked = validate_response(response, spec["allowed_results"], spec["output_schema"])
    validate_outcome(packet, checked)
    return {
        **checked,
        "step": step_id,
        "action": action_id,
        "context": "Integrated",
        "source_bindings": list(packet.get("source_bindings", [])),
        "retained_state": dict(packet.get("retained_state", {})),
        "prompt_sha256": spec["prompt_sha256"],
    }


def invoke_integrated_action_from_context(
    context: Mapping[str, Any],
    *,
    trusted_method_projection: object | None = None,
    trusted_methods: object | None = None,
    action: Any = None,
) -> dict[str, Any]:
    """Adapt the existing native context shape to the current bridge."""
    from selected_integrated_action import invoke_integrated_action

    packet = context.get("parameters")
    root = context.get("project_root")
    if not isinstance(packet, Mapping) or not isinstance(root, Path):
        raise ValueError("native Integrated context is incomplete")
    provider = current_integrated_action_provider if action is None else action
    authorization = context.get("trusted_execution_authorization")
    return invoke_integrated_action(
        provider,
        packet,
        step_id=str(context.get("step_definition_id")),
        action_id=str(context.get("action_definition_id")),
        context="Integrated",
        selected_project_root=root,
        workflow_definition=context.get("workflow_definition"),
        step_definition=context.get("step_definition"),
        action_definition=context.get("action_definition"),
        trusted_workflow_binding=context.get("trusted_workflow_binding"),
        trusted_method_projection=trusted_method_projection,
        trusted_methods=trusted_methods,
        trusted_execution_authorization=authorization
        if isinstance(authorization, Mapping)
        else None,
    )
