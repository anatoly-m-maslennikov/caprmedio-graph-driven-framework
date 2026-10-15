"""Trusted form receipt and exact per-target admission for one selected batch."""

from __future__ import annotations

from contextlib import contextmanager
from contextvars import ContextVar
from collections.abc import Iterator
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Mapping

import atom_operations as operations
from connector_bindings import FileSource, capture_source
from subject_batch import load_subject_batch, require_git_checkpoint
from subject_batch_frontier import require_subject_batch_frontier
from workflow_run_support import _canonical_digest

_ACTIVE: ContextVar[Any] = ContextVar("subject_batch_admission", default=None)
CONFIRMATION = "subject_batch_confirmation.json"


@dataclass
class BatchAdmission:
    root: Path
    packet: dict[str, Any]
    session: Any
    authorities: dict[str, str]
    ordinal: int = -1
    completed: dict[str, str] = field(default_factory=dict)
    validation_scope: Any = None


def capture_batch_review(runner: Any, frozen: Mapping[str, Any]) -> dict[str, Any]:
    """Capture the whole reviewed frontier once, before any selected dispatch."""
    from subject_notation import get_profile
    from ATOM_UPDATE.atom_update import SOURCE_PINS
    from VALIDATE_ATOMS.validate_atoms_workers.proposed_carrier import source_context_from_project

    execution = frozen["request"]["execution"]
    packet = load_subject_batch(runner.root, execution["parameters"])
    require_subject_batch_frontier(packet, execution)
    require_git_checkpoint(runner.root, packet)
    from atom_subject_patch import _assert_original_identity_unique, _capture_identity_layout

    _assert_original_identity_unique(
        operations,
        runner.root,
        {item["target"]["atom_id"] for item in packet["atoms"]},
        _capture_identity_layout(operations, runner.root),
    )
    context = source_context_from_project(runner.root)
    control = operations.control_root(runner.root)
    paths = {str(Path(pin["path"]).relative_to(runner.root)) for pin in context.authority.bindings}
    paths.update(
        (control / name).relative_to(runner.root).as_posix()
        for name in (
            "operators_registry.toml",
            "project_structure.toml",
            "caprmedio_project_settings.toml",
        )
    )
    paths.update(item["definition"]["path"] for item in execution["requested_runs"])
    paths.update(pin["path"] for pin in SOURCE_PINS)
    paths.update(pin.path for pin in get_profile("approved").grammar_pins)
    paths.add(execution["definition_manifest"]["manifest_ref"])
    paths.add(execution["parameters"]["subject_batch"]["path"])
    pins = {path: capture_source(runner.root, path).sha256 for path in sorted(paths)}
    if any(value is None for value in pins.values()):
        raise ValueError("Subject batch authority frontier is incomplete")
    return {"request_digest": _canonical_digest(execution), "packet": packet, "authorities": pins}


def revalidate_batch_review(root: Path, review: Mapping[str, Any]) -> None:
    for path, digest in review["authorities"].items():
        FileSource(root, Path(path), digest).revalidate()
    for item in review["packet"]["atoms"]:
        target = item["target"]
        FileSource(root, Path(target["path"]), target["digest"]).revalidate()


def persist_subject_batch_confirmation(
    runner: Any, frozen: Mapping[str, Any], review: Mapping[str, Any], *, operator_name: str
) -> None:
    """Internal host act, called only after accepting the actual MCP form."""
    execution = frozen["request"]["execution"]
    if review["request_digest"] != _canonical_digest(execution) or not operator_name:
        raise ValueError("Subject batch review differs from this selected request")
    revalidate_batch_review(runner.root, review)
    path = runner.run_directory(frozen["request"]["run_id"]) / CONFIRMATION
    if path.exists():
        raise ValueError("Subject batch confirmation already exists; inspect its retained Run")
    runner._write(
        path,
        {
            "schema_version": 1,
            "operator_name": operator_name,
            "form": {"review": True, "pause": True},
            **review,
        },
    )


def load_subject_batch_confirmation(runner: Any, frozen: Mapping[str, Any]) -> dict[str, Any]:
    folder = runner.run_directory(frozen["request"]["run_id"])
    receipt: dict[str, Any] = runner._read(folder / CONFIRMATION)
    if (
        receipt.get("schema_version") != 1
        or receipt.get("form") != {"review": True, "pause": True}
        or not receipt.get("operator_name")
        or receipt.get("request_digest") != _canonical_digest(frozen["request"]["execution"])
    ):
        raise ValueError("Actual exact Subject batch confirmation is unavailable")
    revalidate_batch_review(runner.root, receipt)
    require_subject_batch_frontier(receipt["packet"], frozen["request"]["execution"])
    if (
        load_subject_batch(runner.root, frozen["request"]["execution"]["parameters"])
        != receipt["packet"]
    ):
        raise ValueError("Retained confirmation differs from the exact reviewed Subject packet")
    return receipt


@contextmanager
def bind_subject_batch(
    runner: Any, frozen: Mapping[str, Any], session: Any
) -> Iterator[BatchAdmission]:
    receipt = load_subject_batch_confirmation(runner, frozen)
    state = BatchAdmission(runner.root, receipt["packet"], session, receipt["authorities"])
    token = _ACTIVE.set(state)
    try:
        yield state
    finally:
        _ACTIVE.reset(token)


def active_batch_target(root: Path, target: Mapping[str, Any]) -> bool:
    state = _ACTIVE.get()
    return (
        state is not None
        and state.root == Path(root).resolve()
        and state.ordinal >= 0
        and state.packet["atoms"][state.ordinal]["target"] == target
    )


def batch_validation_scope(root: Path) -> Any:
    state = _ACTIVE.get()
    if state is None or state.root != Path(root).resolve() or state.ordinal < 0:
        return None
    if state.validation_scope is None:
        from VALIDATE_ATOMS.validate_atoms_workers.proposed_carrier import CarrierValidationScope

        state.validation_scope = CarrierValidationScope(state.root)
    return state.validation_scope


def validate_batch_action(
    root: Path, request: Mapping[str, Any], *, session: Any = None, action_run_id: str | None = None
) -> bool:
    state = _ACTIVE.get()
    if state is None:
        return False
    item = state.packet["atoms"][state.ordinal]
    if (
        state.root != Path(root).resolve()
        or request.get("target") != item["target"]
        or request.get("subject_patches") != item["subject_patches"]
        or request.get("subject_profile") != "approved"
    ):
        raise ValueError("Subject effect differs from the exact confirmed batch mapping")
    if session is not None:
        if session is not state.session or session.recording_errors:
            raise ValueError("Subject batch requires its admitted, durably recorded Session")
        key, actual = session._actual_by_id(action_run_id)
        if (
            actual["definition"]["atom_id"] != "CA-O-030"
            or key in session.terminal
            or key in session.interrupted
            or key in session.observed_effects
        ):
            raise ValueError("Subject batch requires a fresh actual O030 Action Run")
    revalidate_batch_authority(root, request)
    return True


def revalidate_batch_authority(root: Path, request: Mapping[str, Any]) -> None:
    state = _ACTIVE.get()
    if state is None:
        raise ValueError("Subject batch is not active")
    for path, digest in state.authorities.items():
        if path != request["target"]["path"]:
            FileSource(root, Path(path), state.completed.get(path, digest)).revalidate()


def batch_definition_binding(binding: Mapping[str, Any]) -> dict[str, Any]:
    state = _ACTIVE.get()
    if state is None:
        raise ValueError("Subject batch is not active")
    path = binding["path"]
    return {**binding, "sha256": state.completed.get(path, binding["digest"])}
