"""Pure source-bound admission for recursively contained lifecycle changes.

The selected route admits one parent Atom.  This module only seals the
additional source-derived descendants; it does not select a route, dispatch an
effect, authorize a request, or perform a lifecycle mutation.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import asdict
import json
from pathlib import Path
import re
from typing import Any

import lifecycle_intents
from contained_atom_targets import (
    ContainedAtomInventory,
    ContainedAtomTarget,
    discover_contained_atom_targets,
)
from container_lifecycle import plan_contained_status_changes
from VALIDATE_ATOMS.validate_atoms_workers.proposed_carrier import (
    _current,
    source_context_from_project,
)


_ADMISSION_FIELDS = (
    "operation",
    "prior",
    "requested_status",
    "current_status",
    "status_model",
    "archive",
)
_IDENTITY_FIELDS = ("atom_id", "path", "version")


class ContainerLifecycleAdmissionError(RuntimeError):
    """A contained lifecycle seal cannot be proved from current source bytes."""


def _mapping(value: object, name: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise ContainerLifecycleAdmissionError(f"{name} must be a mapping")
    return value


def _prior_digest(prior: Mapping[str, Any]) -> str:
    digest = prior.get("digest")
    if digest is None:
        # The inventory calls this source pin sha256. Native lifecycle
        # descriptors call the same carrier-byte digest ``digest``.
        digest = prior.get("sha256")
    if not isinstance(digest, str) or re.fullmatch(r"[0-9a-f]{64}", digest) is None:
        raise ContainerLifecycleAdmissionError("parent prior lacks an exact carrier SHA-256")
    return digest


def _admission(value: object, name: str) -> dict[str, Any]:
    admission = _mapping(value, name)
    missing = [field for field in _ADMISSION_FIELDS if field not in admission]
    if missing:
        raise ContainerLifecycleAdmissionError(
            f"{name} lacks native admission fields: {', '.join(missing)}"
        )
    if admission["operation"] != "change_status":
        raise ContainerLifecycleAdmissionError(f"{name} is not a change_status admission")
    prior = _mapping(admission["prior"], f"{name}.prior")
    for field in (*_IDENTITY_FIELDS, "content_role", "type"):
        if field not in prior:
            raise ContainerLifecycleAdmissionError(f"{name}.prior lacks {field}")
    _prior_digest(prior)
    if not isinstance(admission["requested_status"], str) or not admission["requested_status"]:
        raise ContainerLifecycleAdmissionError(f"{name}.requested_status is invalid")
    if not isinstance(admission["current_status"], str) or not admission["current_status"]:
        raise ContainerLifecycleAdmissionError(f"{name}.current_status is invalid")
    if not isinstance(admission["status_model"], Mapping):
        raise ContainerLifecycleAdmissionError(f"{name}.status_model is invalid")
    if type(admission["archive"]) is not bool:
        raise ContainerLifecycleAdmissionError(f"{name}.archive is invalid")
    result = {field: admission[field] for field in _ADMISSION_FIELDS}
    result["prior"] = dict(prior)
    result["status_model"] = dict(_mapping(admission["status_model"], f"{name}.status_model"))
    return result


def _same_identity(left: Mapping[str, Any], right: Mapping[str, Any]) -> bool:
    return all(left.get(field) == right.get(field) for field in _IDENTITY_FIELDS)


def _same_snapshot(left: Mapping[str, Any], right: Mapping[str, Any]) -> bool:
    left_digest = left.get("digest", left.get("sha256"))
    right_digest = right.get("digest", right.get("sha256"))
    return _same_identity(left, right) and left_digest == right_digest


def _verify_parent(inventory: ContainedAtomInventory, prior: Mapping[str, Any]) -> None:
    parent = inventory.parent
    expected = _prior_digest(prior)
    if (
        parent.atom_id != prior["atom_id"]
        or parent.path != prior["path"]
        or parent.version != prior["version"]
        or parent.sha256 != expected
    ):
        raise ContainerLifecycleAdmissionError(
            "parent source snapshot drifted during containment discovery"
        )
    if parent.status != prior.get("status", prior.get("current_status")):
        raise ContainerLifecycleAdmissionError(
            "parent current status drifted during containment discovery"
        )
    if parent.metadata.get("content_role") != prior["content_role"]:
        raise ContainerLifecycleAdmissionError(
            "parent Content Role drifted during containment discovery"
        )
    if parent.metadata.get("type") != prior["type"]:
        raise ContainerLifecycleAdmissionError("parent Type drifted during containment discovery")


def _request_parts(
    parameters: Mapping[str, Any], parent_admission: Mapping[str, Any],
) -> tuple[dict[str, Any], Mapping[str, Any], str]:
    request = _mapping(parameters, "parameters")
    parent = _admission(parent_admission, "parent_admission")
    prior = _mapping(parent["prior"], "parent_admission.prior")
    requested = request.get("status")
    if not isinstance(requested, str) or not requested:
        raise ContainerLifecycleAdmissionError("parameters.status is required")
    if requested != parent["requested_status"]:
        raise ContainerLifecycleAdmissionError("requested status differs from parent admission")
    supplied_target = request.get("target")
    if supplied_target is not None:
        supplied = _mapping(supplied_target, "parameters.target")
        if not _same_snapshot(supplied, prior):
            raise ContainerLifecycleAdmissionError(
                "parameters.target differs from parent admission"
            )
    return parent, prior, requested


def _is_container(prior: Mapping[str, Any]) -> bool:
    content_role = prior["content_role"]
    atom_type = prior["type"]
    return (
        content_role == "Plan" and atom_type == "Plan"
    ) or (
        content_role == "Operations" and atom_type in {"Workflow", "Step"}
    )


def _discover_plan(
    root: Path, prior: Mapping[str, Any], requested: str,
) -> tuple[Any, ContainedAtomInventory, tuple[tuple[ContainedAtomTarget, str], ...]]:
    try:
        context = source_context_from_project(root)
        inventory = discover_contained_atom_targets(
            context,
            prior["atom_id"],
            expected_version=prior["version"],
            expected_sha256=_prior_digest(prior),
        )
        if not isinstance(inventory, ContainedAtomInventory):
            raise ContainerLifecycleAdmissionError("contained target inventory is invalid")
        _verify_parent(inventory, prior)
        return context, inventory, plan_contained_status_changes(inventory, requested)
    except ContainerLifecycleAdmissionError:
        raise
    except Exception as error:  # source context/frontier/planner errors refuse closed
        raise ContainerLifecycleAdmissionError(
            "contained target source or plan is unavailable"
        ) from error


def _revalidate_plan(
    root: Path, context: Any, initial: ContainedAtomInventory, prior: Mapping[str, Any],
) -> None:
    try:
        _current(context._reader, context._selection)
        refreshed = discover_contained_atom_targets(
            context,
            prior["atom_id"],
            expected_version=prior["version"],
            expected_sha256=_prior_digest(prior),
        )
        if not isinstance(refreshed, ContainedAtomInventory) or refreshed != initial:
            raise ContainerLifecycleAdmissionError(
                "contained source frontier changed during child admission"
            )
    except ContainerLifecycleAdmissionError:
        raise
    except Exception as error:  # final source currentness failures refuse closed
        raise ContainerLifecycleAdmissionError(
            "contained source currentness is unavailable"
        ) from error


def _child_descriptor(root: Path, target: ContainedAtomTarget) -> dict[str, Any]:
    try:
        descriptor = lifecycle_intents.carrier_descriptor(root, target.path)
    except Exception as error:  # source/read failures must refuse closed
        raise ContainerLifecycleAdmissionError(
            f"contained target source is unavailable: {target.atom_id}"
        ) from error
    if not isinstance(descriptor, Mapping):
        raise ContainerLifecycleAdmissionError("contained target descriptor is invalid")
    if (
        descriptor.get("atom_id") != target.atom_id
        or descriptor.get("path") != target.path
        or descriptor.get("version") != target.version
        or descriptor.get("digest") != target.sha256
        or descriptor.get("status") != target.status
        or descriptor.get("content_role") != target.content_role
        or descriptor.get("type") != target.atom_type
    ):
        raise ContainerLifecycleAdmissionError(
            f"contained target source snapshot drifted: {target.atom_id}"
        )
    return dict(descriptor)


def _admit_child(
    root: Path, target: ContainedAtomTarget, derived_status: str,
) -> dict[str, Any]:
    descriptor = _child_descriptor(root, target)
    try:
        child_admission = lifecycle_intents.preflight_atom_lifecycle(
            root,
            "change_status",
            {"target": descriptor, "status": derived_status},
        )
        child = _admission(child_admission, f"child {target.atom_id}")
    except ContainerLifecycleAdmissionError:
        raise
    except Exception as error:  # native model/source errors refuse closed
        raise ContainerLifecycleAdmissionError(
            f"contained target lifecycle admission failed: {target.atom_id}"
        ) from error
    child_prior = _mapping(child["prior"], f"child {target.atom_id}.prior")
    if not _same_snapshot(child_prior, descriptor):
        raise ContainerLifecycleAdmissionError(
            f"contained target admission no longer matches source: {target.atom_id}"
        )
    if child["requested_status"] != derived_status or child["current_status"] != target.status:
        raise ContainerLifecycleAdmissionError(
            f"contained target admission status drifted: {target.atom_id}"
        )
    return {"target": asdict(target), "status": derived_status, "admission": child}


def _json_safe(value: object) -> None:
    try:
        json.dumps(value, ensure_ascii=False, allow_nan=False)
    except (TypeError, ValueError) as error:
        raise ContainerLifecycleAdmissionError(
            "contained lifecycle seal is not serializable"
        ) from error


def seal_contained_status_changes(
    root: Path, parameters: Mapping[str, Any], parent_admission: Mapping[str, Any],
) -> dict[str, Any] | None:
    """Return a pure source-derived seal for one admitted container parent.

    The parent admission is supplied by the current single-Atom route.  A
    valid Plan/Plan or Operations/Workflow|Step parent is expanded only after
    its exact prior identity/version/digest is used to bind discovery. Every
    planned child is then independently re-preflighted by the native lifecycle
    intent before its serializable admission is retained.
    """
    root = Path(root).resolve()
    parent, prior, requested = _request_parts(parameters, parent_admission)
    if not _is_container(prior):
        return None

    context, inventory, planned = _discover_plan(root, prior, requested)

    if not planned:
        return None

    descendants = [
        _admit_child(root, target, derived_status)
        for target, derived_status in planned
        if isinstance(target, ContainedAtomTarget) and isinstance(derived_status, str)
    ]
    if len(descendants) != len(planned):
        raise ContainerLifecycleAdmissionError("contained lifecycle plan is malformed")
    _revalidate_plan(root, context, inventory, prior)

    seal = {"parent": parent, "descendants": descendants}
    _json_safe(seal)
    return seal

