"""Caller-safe validation for one current O016 shared-context Action packet."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from pydantic import ValidationError

from shared_context_validation_boundary import SharedContextPacketBoundary
from shared_context_validation_policy import validate_permissions_retry, validate_plan_candidate
from shared_context_validation_rmed import validate_rmed_inputs
from shared_context_validation_sources import (
    SharedContextPacketError,
    is_current_shared_workflow_profile,
    project_source_scope,
    validate_source_bindings,
    validated_context,
    workflow_version_profile,
)


@dataclass(frozen=True)
class SharedContextValidation:
    """An explicit validation outcome; invalid caller input is not a runtime fault."""

    accepted: bool
    warnings: tuple[dict[str, str], ...]
    step_id: str | None = None
    action_id: str | None = None
    outcome: str = "accepted"

    def as_result(self) -> dict[str, object]:
        return {
            "status": self.outcome if self.accepted else "invalid_packet",
            "warnings": list(self.warnings),
            "step_id": self.step_id,
            "action_id": self.action_id,
        }


def _invalid(error: SharedContextPacketError) -> SharedContextValidation:
    return SharedContextValidation(False, ({"code": error.code, "message": str(error)},))


def _packet_context(
    packet: Mapping[str, Any], source_ids: set[str], step_id: str, source_root: str
) -> None:
    if packet.get("context") != "Integrated":
        raise SharedContextPacketError(
            "context", "current shared Workflow requires Integrated context"
        )
    selected = packet.get("selected_project")
    references = selected.get("source_references") if isinstance(selected, Mapping) else None
    if (
        not isinstance(selected, Mapping)
        or selected.get("kind") != "selected_project"
        or selected.get("source_root") != source_root
        or references != packet.get("source_bindings")
    ):
        raise SharedContextPacketError("selected_project", "selected Project binding is stale")
    phase = packet.get("review_phase")
    if step_id == "CA-O-230" and phase not in {"preliminary", "final"}:
        raise SharedContextPacketError(
            "review_phase", "review Step needs an explicit preliminary or final phase"
        )
    obligations = packet.get("required_obligation_map")
    if obligations is not None and (
        not isinstance(obligations, Mapping)
        or not obligations
        or any(
            not isinstance(key, str)
            or not key
            or not isinstance(value, list)
            or not value
            or any(not isinstance(item, str) or item not in source_ids for item in value)
            for key, value in obligations.items()
        )
    ):
        raise SharedContextPacketError("obligations", "required obligation map is invalid")


def _authorization(packet: Mapping[str, Any], trusted: Mapping[str, Any] | None) -> None:
    if trusted is None:
        return
    if not isinstance(packet.get("operator_authorization"), Mapping):
        raise SharedContextPacketError("authorization", "retained authorization is missing")
    if dict(packet["operator_authorization"]) != dict(trusted):
        raise SharedContextPacketError(
            "authorization", "retained authorization differs from admission"
        )


def _validate_method_version(packet: Mapping[str, Any], profile: Mapping[str, Any]) -> None:
    workflow = profile.get("workflow")
    version = workflow.get("version") if isinstance(workflow, Mapping) else None
    has_direct = packet.get("methods") is not None
    profile_name = workflow_version_profile(version)
    if profile_name == "legacy_projection" and has_direct:
        raise SharedContextPacketError(
            "methods", "O016@17 admits only the legacy Method projection"
        )
    if profile_name == "direct_methods" and not has_direct:
        raise SharedContextPacketError(
            "methods", f"O016@{version} requires direct Methods"
        )


def validate_current_shared_packet(
    packet: object,
    *,
    workflow_definition: object,
    step_definition: object,
    action_definition: object,
    trusted_workflow_binding: object,
    selected_project_root: Path,
    trusted_execution_authorization: Mapping[str, Any] | None = None,
    trusted_method_projection: object | None = None,
    trusted_methods: object | None = None,
) -> SharedContextValidation:
    """Validate current packet data without treating malformed input as a runtime error."""
    if not isinstance(packet, Mapping):
        return SharedContextValidation(
            False, ({"code": "packet", "message": "packet must be a mapping"},)
        )
    if not is_current_shared_workflow_profile(trusted_workflow_binding):
        return SharedContextValidation(
            False, ({"code": "profile", "message": "trusted current Workflow profile is invalid"},)
        )
    try:
        typed_packet = SharedContextPacketBoundary.model_validate(dict(packet)).model_dump(
            exclude_unset=True
        )
        assert isinstance(trusted_workflow_binding, Mapping)
        _validate_method_version(typed_packet, trusted_workflow_binding)
        step_id, action_id, pins = validated_context(
            selected_project_root,
            trusted_workflow_binding,
            workflow_definition,
            step_definition,
            action_definition,
        )
        validate_source_bindings(selected_project_root, typed_packet.get("source_bindings"), pins)
        source_ids = validate_rmed_inputs(
            selected_project_root,
            typed_packet,
            trusted_method_projection,
            trusted_methods=trusted_methods,
        )
        _packet_context(
            typed_packet, source_ids, step_id, project_source_scope(selected_project_root).root
        )
        validate_plan_candidate(typed_packet, step_id)
        retry_blocked = validate_permissions_retry(typed_packet, step_id)
        _authorization(typed_packet, trusted_execution_authorization)
    except ValidationError:
        return SharedContextValidation(
            False, ({"code": "packet", "message": "packet envelope is invalid"},)
        )
    except SharedContextPacketError as error:
        return _invalid(error)
    outcome = "retry_blocked" if retry_blocked else "accepted"
    return SharedContextValidation(True, (), step_id, action_id, outcome)
