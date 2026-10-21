"""Selected-request authorization and exact per-target batch admission."""

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
from VALIDATE_ATOMS.validate_atoms_workers.parsing import parse_carrier
from workflow_run_support import RunExecutionSession, _canonical_digest

_ACTIVE: ContextVar[Any] = ContextVar("subject_batch_admission", default=None)


@dataclass
class BatchAdmission:
    root: Path
    packet: dict[str, Any]
    session: Any
    authorities: dict[str, str]
    ordinal: int = -1
    completed: dict[str, str] = field(default_factory=dict)


def capture_batch_admission(runner: Any, frozen: Mapping[str, Any]) -> dict[str, Any]:
    """Bind the selected packet and finite governing sources without a review round."""
    from subject_notation import get_profile
    from ATOM_UPDATE.atom_update import SOURCE_PINS

    execution = frozen["request"]["execution"]
    packet = load_subject_batch(runner.root, execution["parameters"])
    require_subject_batch_frontier(packet, execution, root=runner.root)
    require_git_checkpoint(runner.root, packet)
    control = operations.control_root(runner.root)
    paths = set(
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
    return {"packet": packet, "authorities": pins}


@contextmanager
def bind_subject_batch(
    runner: Any, frozen: Mapping[str, Any], session: Any
) -> Iterator[BatchAdmission]:
    execution = frozen["request"]["execution"]
    if (
        not isinstance(session, RunExecutionSession)
        or Path(session.tracker.root).resolve() != runner.root
        or execution.get("mode") != "execute"
        or execution.get("operation_route") != "update_atom"
        or _canonical_digest(session.request) != _canonical_digest(execution)
    ):
        raise ValueError("Subject batch requires the actual authorized selected Session")
    admitted = capture_batch_admission(runner, frozen)
    state = BatchAdmission(runner.root, admitted["packet"], session, admitted["authorities"])
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


def validate_batch_carrier(root: Path, path: Path, frontmatter: str, body: str) -> bool:
    state = _ACTIVE.get()
    if state is None:
        return False
    if (
        state.root != Path(root).resolve()
        or state.ordinal < 0
        or path != root / state.packet["atoms"][state.ordinal]["target"]["path"]
    ):
        raise ValueError("Subject batch carrier validation differs from its exact target")
    # Exact byte patches preserve the body; the caller rebuilds its graph after promotion.
    parse_carrier(("---\n" + frontmatter + "\n---\n" + body).encode("utf-8"), path)
    return True


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
        raise ValueError("Subject effect differs from the exact admitted batch mapping")
    if session is not None:
        if session is not state.session:
            raise ValueError("Subject batch requires its admitted Session")
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
