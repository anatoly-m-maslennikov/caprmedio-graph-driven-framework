"""Source-bound bridge for the current Integrated implementation Actions."""

from __future__ import annotations

from collections.abc import Callable, Mapping, Sequence
import hashlib
from pathlib import Path
from typing import Any

from selected_integrated_action_contract import (
    build_capture,
    normalise_result,
    prompt_spec,
    validate_capture_contract,
    validate_response,
)
from selected_integrated_action_provider import (
    current_integrated_action_provider,
    invoke_integrated_action_from_context,
)
from selected_integrated_action_runtime import (
    IntegratedActionInputError,
    IntegratedActionPending,
    call_action,
    validate_action_binding,
    validate_bound_packet,
)
from selected_integrated_action_outcome import validate_outcome


__all__ = [
    "IntegratedActionInputError",
    "IntegratedActionPending",
    "current_integrated_action_provider",
    "invoke_integrated_action",
    "invoke_integrated_action_from_context",
    "submit_integrated_action",
]

ActionProvider = Callable[..., Mapping[str, Any]]


def invoke_integrated_action(
    action: ActionProvider,
    packet: Mapping[str, Any],
    *,
    step_id: str,
    action_id: str,
    context: str,
    selected_project_root: Path,
    allowed_results: Sequence[str] | None = None,
    output_schema: Mapping[str, Any] | None = None,
    workflow_definition: object | None = None,
    step_definition: object | None = None,
    action_definition: object | None = None,
    trusted_workflow_binding: object | None = None,
    trusted_method_projection: object | None = None,
    trusted_methods: object | None = None,
    trusted_execution_authorization: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    if context != "Integrated":
        raise ValueError("current bridge accepts Integrated context only")
    if not isinstance(packet, Mapping):
        raise ValueError("Integrated Action packet must be a mapping")
    if any(
        value is None
        for value in (
            workflow_definition,
            step_definition,
            action_definition,
            trusted_workflow_binding,
        )
    ):
        raise IntegratedActionInputError(
            {"code": "binding", "message": "source-bound Integrated definitions are required"}
        )
    validate_action_binding(packet, step_id, action_id)
    spec = prompt_spec(step_id, action_id)
    results = tuple(allowed_results or spec["allowed_results"])
    schema = dict(output_schema or spec["output_schema"])
    validation = validate_bound_packet(
        packet,
        root=selected_project_root,
        workflow=workflow_definition,
        step=step_definition,
        action=action_definition,
        profile=trusted_workflow_binding,
        methods=trusted_method_projection,
        trusted_methods=trusted_methods,
        authorization=trusted_execution_authorization,
        expected_step_id=step_id,
        expected_action_id=action_id,
    )
    if validation is not None:
        raise IntegratedActionInputError(validation)
    definitions = {
        "workflow_definition": workflow_definition,
        "step_definition": step_definition,
        "action_definition": action_definition,
        "trusted_workflow_binding": trusted_workflow_binding,
        "trusted_method_projection": trusted_method_projection,
        "trusted_methods": trusted_methods,
        "trusted_execution_authorization": trusted_execution_authorization,
    }

    def capture_agent(prompt: str, callback_packet: Mapping[str, Any]) -> Mapping[str, Any]:
        if dict(callback_packet) != dict(packet):
            raise ValueError("Integrated Action provider changed the bound packet")
        if (
            prompt != spec["prompt"]
            or hashlib.sha256(prompt.encode("utf-8")).hexdigest() != spec["prompt_sha256"]
        ):
            raise ValueError("Integrated Action provider supplied a stale prompt")
        raise IntegratedActionPending(
            build_capture(
                prompt,
                packet,
                step_id=step_id,
                action_id=action_id,
                context=context,
                allowed_results=results,
                output_schema=schema,
                prompt_path=spec["prompt_path"],
                prompt_sha256=spec["prompt_sha256"],
                selected_project_root=selected_project_root,
                definitions=definitions,
            )
        )

    call_action(
        action, packet, capture_agent, selected_project_root, trusted_execution_authorization
    )
    raise ValueError("Integrated Action provider completed without interactive capture")


# implementation of:
# Method: CA-M-405
def submit_integrated_action(
    action: ActionProvider,
    capture: Mapping[str, Any],
    submitted_response: Mapping[str, Any],
    *,
    selected_project_root: Path | None = None,
) -> dict[str, Any]:
    packet = capture.get("packet")
    if not isinstance(packet, Mapping) or capture.get("context") != "Integrated":
        raise ValueError("Integrated Action capture is invalid")
    try:
        current_spec = prompt_spec(str(capture["step_id"]), str(capture["action_id"]))
    except (KeyError, TypeError, ValueError) as error:
        raise ValueError("Integrated Action capture prompt is invalid") from error
    if (
        capture.get("prompt") != current_spec["prompt"]
        or capture.get("prompt_sha256") != current_spec["prompt_sha256"]
    ):
        raise ValueError("Integrated Action capture prompt is stale")
    validate_capture_contract(capture, current_spec)
    root = Path(selected_project_root or str(capture.get("selected_project_root", "")))
    try:
        validate_response(
            submitted_response,
            current_spec["allowed_results"],
            current_spec["output_schema"],
        )
        validate_outcome(packet, submitted_response)
    except (KeyError, TypeError, ValueError) as error:
        pending = dict(capture)
        pending.update(reason="invalid_submitted_response", validation_error=str(error))
        raise IntegratedActionPending(pending) from error
    definitions = capture.get("definitions", {})
    if not isinstance(definitions, Mapping):
        raise ValueError("Integrated Action capture definitions are invalid")
    authorization = definitions.get("trusted_execution_authorization")
    if not isinstance(authorization, Mapping):
        authorization = None
    validation = validate_bound_packet(
        packet,
        root=root,
        workflow=definitions.get("workflow_definition"),
        step=definitions.get("step_definition"),
        action=definitions.get("action_definition"),
        profile=definitions.get("trusted_workflow_binding"),
        methods=definitions.get("trusted_method_projection"),
        trusted_methods=definitions.get("trusted_methods"),
        authorization=authorization,
        expected_step_id=str(capture["step_id"]),
        expected_action_id=str(capture["action_id"]),
    )
    if validation is not None:
        raise IntegratedActionInputError(validation)

    def submit_agent(prompt: str, callback_packet: Mapping[str, Any]) -> Mapping[str, Any]:
        if prompt != capture.get("prompt") or dict(callback_packet) != dict(packet):
            raise ValueError("Integrated Action provider changed the captured binding")
        return dict(submitted_response)

    result = call_action(action, packet, submit_agent, root, authorization)
    return normalise_result(result, capture)
