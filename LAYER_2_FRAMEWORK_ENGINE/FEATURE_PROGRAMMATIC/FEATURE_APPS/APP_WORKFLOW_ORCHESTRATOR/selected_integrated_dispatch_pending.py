"""Currentness checks for a retained Integrated pending capture."""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path
from typing import Any

from selected_execution_contracts import SelectedExecutionError
from selected_integrated_action_contract import prompt_spec, validate_capture_contract
from selected_integrated_frontier_records import digest
from shared_context_validation import validate_current_shared_packet


# implementation of:
# Method: CA-M-405
def revalidate_pending(
    root: Path,
    frozen: Mapping[str, Any],
    profile: Mapping[str, Any],
    method_projection: object | None,
    methods: object | None,
    frontier: Mapping[str, Any],
    capture: Mapping[str, Any],
) -> None:
    """Refuse a retained prompt after any sealed source or authority drift."""
    definitions = capture.get("definitions")
    packet = capture.get("packet")
    request = frozen.get("request")
    execution = request.get("execution") if isinstance(request, Mapping) else None
    if (
        not isinstance(definitions, Mapping)
        or not isinstance(packet, Mapping)
        or not isinstance(execution, Mapping)
    ):
        raise SelectedExecutionError("retained Integrated frontier is incomplete")
    authorization = execution.get("operator_authorization")
    authorization = authorization if isinstance(authorization, Mapping) else None
    sources = {
        "profile": profile,
        "method_projection": method_projection,
        "methods": methods,
    }
    if (
        digest(sources) != frontier.get("source_digest")
        or digest(packet) != frontier.get("packet_digest")
        or digest(authorization) != frontier.get("authorization_digest")
        or definitions.get("trusted_workflow_binding") != profile
        or definitions.get("trusted_method_projection") != method_projection
        or definitions.get("trusted_methods") != methods
        or definitions.get("trusted_execution_authorization") != authorization
    ):
        raise SelectedExecutionError("retained Integrated frontier differs from current authority")
    step_id, action_id = capture.get("step_id"), capture.get("action_id")
    if not isinstance(step_id, str) or not isinstance(action_id, str):
        raise SelectedExecutionError("retained Integrated frontier Step/Action is stale")
    steps = profile.get("steps")
    row = steps.get(step_id) if isinstance(steps, Mapping) else None
    if not isinstance(row, Mapping) or row.get("action", {}).get("atom_id") != action_id:
        raise SelectedExecutionError("retained Integrated frontier Step/Action is stale")
    try:
        spec = prompt_spec(step_id, action_id)
        if (
            capture.get("prompt") != spec["prompt"]
            or capture.get("prompt_sha256") != spec["prompt_sha256"]
        ):
            raise ValueError("Integrated Action capture prompt is stale")
        validate_capture_contract(capture, spec)
    except (OSError, TypeError, ValueError) as error:
        raise SelectedExecutionError("retained Integrated Action prompt is stale") from error
    validation = validate_current_shared_packet(
        packet,
        workflow_definition=profile.get("workflow"),
        step_definition=row.get("step"),
        action_definition=row.get("action"),
        trusted_workflow_binding=profile,
        selected_project_root=root,
        trusted_method_projection=method_projection,
        trusted_methods=methods,
        trusted_execution_authorization=authorization,
    )
    if not validation.accepted:
        raise SelectedExecutionError("retained Integrated packet is no longer admitted")
