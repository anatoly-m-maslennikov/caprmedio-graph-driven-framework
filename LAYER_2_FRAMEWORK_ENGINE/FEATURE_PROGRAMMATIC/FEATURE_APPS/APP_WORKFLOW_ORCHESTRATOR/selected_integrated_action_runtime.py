"""Small runtime boundaries for the current Integrated Action bridge."""

from __future__ import annotations

from collections.abc import Callable, Mapping
import copy
from pathlib import Path
from typing import Any

from shared_context_validation import (
    SharedContextValidation,
    validate_current_shared_packet,
)


Agent = Callable[[str, Mapping[str, Any]], Mapping[str, Any]]
ActionProvider = Callable[..., object]


class IntegratedActionPending(RuntimeError):
    """The current Step needs the controlling session to submit a response."""

    def __init__(self, capture: Mapping[str, Any]) -> None:
        self.capture = copy.deepcopy(dict(capture))
        super().__init__("Integrated Action is pending interactive submission")


class IntegratedActionInputError(ValueError):
    """The packet or source-bound definition is invalid for this Action."""

    def __init__(self, validation: object) -> None:
        self.validation = validation
        super().__init__("current Integrated Action packet is invalid")


def validate_action_binding(packet: Mapping[str, Any], step_id: str, action_id: str) -> None:
    """Keep packet markers bound to the source-selected Step and Action."""
    binding = packet.get("action_binding")
    if packet.get("step_marker") != step_id or not isinstance(binding, Mapping):
        raise ValueError("Integrated Action packet binding does not match the current Step")
    if binding.get("atom_id") != action_id:
        raise ValueError("Integrated Action packet binding does not match the current Action")


def validate_bound_packet(
    packet: Mapping[str, Any],
    *,
    root: Path,
    workflow: object | None,
    step: object | None,
    action: object | None,
    profile: object | None,
    methods: object | None,
    trusted_methods: object | None,
    authorization: Mapping[str, Any] | None,
    expected_step_id: str | None = None,
    expected_action_id: str | None = None,
) -> object | None:
    """Return the validator result when a complete source binding is invalid."""
    if any(value is None for value in (workflow, step, action, profile)):
        return SharedContextValidation(
            False,
            (
                {
                    "code": "binding",
                    "message": "complete source-bound definitions are required",
                },
            ),
        )
    validation = validate_current_shared_packet(
        packet,
        workflow_definition=workflow,
        step_definition=step,
        action_definition=action,
        trusted_workflow_binding=profile,
        selected_project_root=root,
        trusted_method_projection=methods,
        trusted_methods=trusted_methods,
        trusted_execution_authorization=authorization,
    )
    if not validation.accepted:
        return validation
    if (
        expected_step_id is not None
        and validation.step_id != expected_step_id
        or expected_action_id is not None
        and validation.action_id != expected_action_id
    ):
        return SharedContextValidation(
            False,
            (
                {
                    "code": "binding",
                    "message": "validated definitions do not match the requested Step and Action",
                },
            ),
        )
    return None


def call_action(
    action: ActionProvider,
    packet: Mapping[str, Any],
    callback: Agent,
    root: Path,
    authorization: Mapping[str, Any] | None,
) -> Mapping[str, Any]:
    """Call a provider and retain the native mapping contract."""
    result = action(
        packet,
        agent=callback,
        selected_project_root=root,
        trusted_execution_authorization=authorization,
    )
    if not isinstance(result, Mapping):
        raise ValueError("Integrated Action provider returned a non-mapping")
    return dict(result)
