"""One private admitted location/absence contribution, with no lifecycle policy."""

from __future__ import annotations

import ctypes
import errno
import hashlib
import json
import os
import sys
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

from connector_bindings import ConnectorBindingError
from connector_carrier_reading import CarrierError, Location, _fingerprint, observe, open_parent, preserved


@dataclass(frozen=True)
class CarrierPlan:
    variant: str
    project_root: Path
    source_binding: Location
    expected_source: dict
    destination_binding: Location | None
    expected_destination: dict | None
    entry_inventory: dict | None
    preservation_frontier: tuple[tuple[Location, dict], ...]
    storage_owner: object
    classification: str
    admission_evidence: Callable[["CarrierPlan"], None]


def _validate(plan: CarrierPlan) -> None:
    if not isinstance(plan, CarrierPlan) or plan.variant not in {"rename", "move", "remove"}:
        raise CarrierError("input_invalid", "Unsupported private carrier plan.")
    if plan.storage_owner is None or not callable(plan.admission_evidence):
        raise CarrierError("permission_denied", "Resolved storage ownership and current admission are required.")
    if not isinstance(plan.project_root, Path) or not plan.project_root.is_absolute():
        raise CarrierError("input_invalid", "A resolved Project root is required.")
    for location in (plan.source_binding, plan.destination_binding):
        if location is None:
            continue
        if (not isinstance(location, Location) or location.root == plan.project_root
                or location.root in plan.project_root.parents
                or not location.root.is_relative_to(plan.project_root)):
            raise CarrierError("input_invalid", "Approved carrier root must be a strict Project subtree.")
        target = location.root / location.relative
        if target == location.root or target == plan.project_root or target in plan.project_root.parents:
            raise CarrierError("input_invalid", "Root and ancestor carrier effects are forbidden.")
    if plan.variant == "remove":
        if plan.destination_binding is not None or plan.expected_destination is not None:
            raise CarrierError("input_invalid", "Removal has no destination binding.")
        if plan.classification != "approved_non_atom_cleanup":
            raise CarrierError("permission_denied", "Removal requires positive non-Atom cleanup eligibility.")
        if plan.entry_inventory not in (None, {}):
            raise CarrierError("input_invalid", "Removal cannot select descendants.")
    else:
        if plan.destination_binding is None or plan.expected_destination is None:
            raise CarrierError("input_invalid", "Explicit destination and expected state are required.")
        if plan.classification not in {"owned_non_atom", "admitted_atom_lifecycle"}:
            raise CarrierError("permission_denied", "Carrier classification and lifecycle admission are required.")
        source = plan.source_binding.root / plan.source_binding.relative
        destination = plan.destination_binding.root / plan.destination_binding.relative
        if plan.variant == "rename" and source.parent != destination.parent:
            raise CarrierError("input_invalid", "Rename must retain the exact same parent.")
        if source != destination and (source.is_relative_to(destination) or destination.is_relative_to(source)):
            raise CarrierError("input_invalid", "Source and destination overlap.")
        if source != destination and plan.expected_destination.get("present") is not False:
            raise CarrierError("input_invalid", "Distinct destination must be explicitly expected absent.")
        if plan.expected_source.get("present") is not True:
            raise CarrierError("target_not_found", "Rename and move require an expected-present source.")


def _move(source_parent: int, source_name: str, destination_parent: int, destination_name: str) -> None:
    """Use the native no-overwrite primitive; unsupported platforms fail closed."""
    library = ctypes.CDLL(None, use_errno=True)
    symbol, flag = ("renameatx_np", 4) if sys.platform == "darwin" else ("renameat2", 1)
    operation = getattr(library, symbol, None)
    if operation is None:
        raise CarrierError("backend_failure", "A safe native no-overwrite move is unavailable.")
    operation.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p, ctypes.c_uint]
    operation.restype = ctypes.c_int
    if operation(source_parent, os.fsencode(source_name), destination_parent,
                 os.fsencode(destination_name), flag) != 0:
        failure = ctypes.get_errno()
        raise OSError(failure, os.strerror(failure))


def _check(plan: CarrierPlan) -> tuple[dict, dict | None]:
    if plan.admission_evidence(plan) is not None:
        raise CarrierError("permission_denied", "Admission must revalidate evidence, not return an approval flag.")
    source = observe(plan.source_binding, plan.entry_inventory)
    if source != plan.expected_source:
        code = "target_not_found" if not source["present"] and plan.expected_source.get("present") else "stale_state"
        raise CarrierError(code, "Source or ancestor differs from the admitted state.")
    if plan.variant == "remove" and source["present"] and source["entry"].get("removal_guard") in {
            "uncertain", "atom_or_governed_carrier"}:
        raise CarrierError("permission_denied", "Atom or uncertain carrier cannot be removed.")
    destination = None
    if plan.destination_binding is not None:
        same = plan.source_binding == plan.destination_binding
        destination = observe(plan.destination_binding, plan.entry_inventory if same else None)
        if destination != plan.expected_destination:
            raise CarrierError("stale_state", "Destination or ancestor differs from the admitted state.")
    for location, expected in plan.preservation_frontier:
        if observe(location) != expected:
            raise CarrierError("stale_state", "An explicitly protected preservation entry changed.")
    return source, destination


def execute(plan: CarrierPlan, *, logical_target: dict) -> dict:
    """Private writer: receiving adapter must supply the admitted logical target.

    Admission callback rechecks permission, ownership, schema, cleanup or exact
    Atom lifecycle/history evidence. Neither classification strings nor this
    private plan are permission. No public path entrypoint is provided.
    """
    result = {"data": None, "current_state": None, "effects": [], "errors": []}
    attempted = False
    changed = False
    source = destination = None
    try:
        _validate(plan)
        source, destination = _check(plan)
        no_op = (plan.source_binding == plan.destination_binding or
                 (plan.variant == "remove" and source["present"] is False))
        if not no_op:
            parent, _ = open_parent(plan.source_binding)
            destination_parent = None
            try:
                if plan.destination_binding is not None:
                    destination_parent, _ = open_parent(plan.destination_binding)
                _check(plan)
                if (_fingerprint(os.fstat(parent)) != source["ancestors"][-1]
                        or (destination_parent is not None and
                            _fingerprint(os.fstat(destination_parent)) != destination["ancestors"][-1])):
                    raise CarrierError("stale_state", "Held parent differs from the admitted current parent.")
                attempted = True
                if plan.variant == "remove":
                    operation = os.rmdir if source["entry"]["kind"] == "folder" else os.unlink
                    operation(Path(plan.source_binding.relative).name, dir_fd=parent)
                else:
                    _move(parent, Path(plan.source_binding.relative).name,
                          destination_parent, Path(plan.destination_binding.relative).name)
                changed = True
            finally:
                os.close(parent)
                if destination_parent is not None:
                    os.close(destination_parent)
        after_source = observe(plan.source_binding, plan.entry_inventory)
        after_destination = None
        if plan.destination_binding is not None:
            # Inventory validates unchanged entries; ctime of moved root alone may change.
            after_destination = observe(plan.destination_binding, plan.entry_inventory)
        if no_op:
            if after_source != source or after_destination != destination:
                raise CarrierError("backend_failure", "No-op requested state is not verified unchanged.")
        elif after_source["present"]:
            raise CarrierError("backend_failure", "Old source absence is not verified.")
        elif plan.variant != "remove" and (
                not after_destination["present"] or
                preserved(after_destination["entry"]) != preserved(source["entry"])):
            raise CarrierError("backend_failure", "Exact destination preservation is not verified.")
        for location, expected in plan.preservation_frontier:
            after = observe(location)
            if after["present"] != expected["present"] or (after["present"] and
                    preserved(after["entry"]) != preserved(expected["entry"])):
                raise CarrierError("backend_failure", "Unrelated preservation entry changed.")
        evidence = {"variant": plan.variant, "source_present": after_source["present"],
                    "destination_present": None if after_destination is None else after_destination["present"],
                    "carrier_kind": source.get("entry", {}).get("kind"),
                    "state_token": hashlib.sha256(json.dumps(
                        after_destination or after_source, sort_keys=True).encode()).hexdigest()}
        result["data"] = {"variant": plan.variant, "no_op": no_op}
        result["current_state"] = evidence
        if changed:
            result["effects"] = [{"operation": "modify", "target": logical_target,
                                  "state": "known", "evidence": evidence}]
    except (CarrierError, OSError, ValueError, TypeError, AttributeError) as error:
        structured = isinstance(error, (CarrierError, ConnectorBindingError))
        code = error.code if structured else "backend_failure"
        if structured and not changed:
            attempted = False
        if isinstance(error, OSError) and error.errno in {errno.EEXIST, errno.ENOTEMPTY} and not changed:
            code, attempted = "stale_state", False
        if attempted:
            result["effects"] = [{"operation": "modify", "target": logical_target,
                                  "state": "known" if changed else "unknown",
                                  "evidence": {"variant": plan.variant, "native_call_returned": changed}}]
            if not changed:
                result["errors"].append({"code": "effect_uncertain", "message": "Storage effect could not be verified.", "field": None})
        result["errors"].append({"code": code, "message": "Private carrier operation failed its required binding or storage proof.",
                                 "field": getattr(error, "field", None) if structured else None})
    return result
