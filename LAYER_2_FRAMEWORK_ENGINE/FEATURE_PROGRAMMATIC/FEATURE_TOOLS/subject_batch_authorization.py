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
_OPERATIVE_CLAUSE = "The instructed Subjects-only batch admits `source_subject_profile: \"legacy\"` with target `subject_profile: \"approved\"` only for the exact active packet member and its bound request."
_INTENT_DELIVERY_CLAUSE = "The transition intent is exactly `{schema_version: 2, target, subject_profile: \"approved\", subject_profile_evidence, source_subject_profile: \"legacy\", source_subject_profile_evidence, subject_patches, proposal, execution_metadata, predecessorArchive, noop}`."
_PACKET_DELIVERY_CLAUSE = "The existing closed schema1 packet and ordinary singleton request above remain unchanged and reject `source_subject_profile`. A separately instructed legacy-to-approved batch uses exactly `{schema_version: 2, subject_profile: \"approved\", source_subject_profile: \"legacy\", git_checkpoint, atoms}`."
_TRANSITION_AUTHORITY = (
    (".caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-18_FEATURE_TOOL_WORKFLOWS/05_method/CA-M-371-TOOL_WORKFLOWS-ENG_DECISION--preview-exact-subject-patches-for-valid-atom-carriers.md", _OPERATIVE_CLAUSE),
    (".caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-18_FEATURE_TOOL_WORKFLOWS/04_requirement/CA-R-866-TOOL_WORKFLOWS-RULE--update-caprmedio-markdown-atoms.md", _OPERATIVE_CLAUSE),
    (".caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-18_FEATURE_TOOL_WORKFLOWS/09_operations/CA-O-030-TOOL_WORKFLOWS-ACTION--update-sealed-caprmedio-atom-carriers.md", _OPERATIVE_CLAUSE),
    (".caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-18_FEATURE_TOOL_WORKFLOWS/07_delivery/CA-D-659-TOOL_WORKFLOWS-DECISION--deliver-atom-update-tool.md", _INTENT_DELIVERY_CLAUSE),
    (".caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/07_delivery/CA-D-660-TOOLS-DECISION--deliver-sealed-lifecycle-dispatch-interface.md", _PACKET_DELIVERY_CLAUSE),
)


@dataclass
class BatchAdmission:
    root: Path
    packet: dict[str, Any]
    session: Any
    authorities: dict[str, str]
    ordinal: int = -1
    completed: dict[str, str] = field(default_factory=dict)


def require_subject_profile_transition_authority(root: Path) -> None:
    """Admit mixed-profile packets only after all live contracts say so."""
    for path, clause in _TRANSITION_AUTHORITY:
        if path is None:
            raise ValueError("Subject profile transition delivery authority is unbound")
        source = capture_source(root, path)
        try:
            raw = source.read_bytes().decode("utf-8")
        except Exception:
            raise ValueError("Subject profile transition authority is unavailable")
        if clause not in raw:
            raise ValueError("Subject profile transition authority is not active")


def capture_batch_admission(root: Path, frozen: Mapping[str, Any]) -> dict[str, Any]:
    """Bind the selected packet and finite governing sources without a review round."""
    root = Path(root).resolve(strict=True)
    from subject_notation import get_profile
    from ATOM_UPDATE.atom_update import SOURCE_PINS
    from project_selection import active_selection

    execution = frozen["request"]["execution"]
    packet = load_subject_batch(root, execution["parameters"])
    if packet.get("source_subject_profile") == "legacy":
        require_subject_profile_transition_authority(root)
    require_subject_batch_frontier(packet, execution, root=root)
    require_git_checkpoint(root, packet)
    control = operations.control_root(root)
    selection = active_selection(root)
    if selection.control_root != control:
        raise ValueError("Selected Scope Unit Declaration frontier disagrees with the batch Project")
    paths = set(
        (control / name).relative_to(root).as_posix()
        for name in ("operators_registry.toml", "caprmedio_project_settings.toml")
    )
    paths.update(
        (Path(path).relative_to(root) if Path(path).is_absolute() else Path(path)).as_posix()
        for path in selection.declaration_paths
    )
    paths.update(item["definition"]["path"] for item in execution["requested_runs"])
    paths.update(pin["path"] for pin in SOURCE_PINS)
    paths.update(pin.path for pin in get_profile("approved").grammar_pins)
    if packet.get("source_subject_profile") == "legacy":
        paths.update(pin.path for pin in get_profile("legacy").grammar_pins)
        paths.update(path for path, _ in _TRANSITION_AUTHORITY if path is not None)
    paths.add(execution["definition_manifest"]["manifest_ref"])
    paths.add(execution["parameters"]["subject_batch"]["path"])
    pins = {path: capture_source(root, path).sha256 for path in sorted(paths)}
    if any(value is None for value in pins.values()):
        raise ValueError("Subject batch authority frontier is incomplete")
    return {"packet": packet, "authorities": pins}


@contextmanager
def bind_subject_batch(
    root: Path, frozen: Mapping[str, Any], session: Any
) -> Iterator[BatchAdmission]:
    root = Path(root).resolve(strict=True)
    execution = frozen["request"]["execution"]
    if (
        not isinstance(session, RunExecutionSession)
        or Path(session.tracker.root).resolve() != root
        or execution.get("mode") != "execute"
        or execution.get("operation_route") != "update_atom"
        or _canonical_digest(session.request) != _canonical_digest(execution)
    ):
        raise ValueError("Subject batch requires the actual authorized selected Session")
    admitted = capture_batch_admission(root, frozen)
    state = BatchAdmission(root, admitted["packet"], session, admitted["authorities"])
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


def active_batch_transition(
    root: Path, target: Mapping[str, Any], source_profile: str, subject_profile: str
) -> bool:
    """Only the admitted packet may change Subject notation profiles."""
    state = _ACTIVE.get()
    return (
        active_batch_target(root, target)
        and state.packet.get("source_subject_profile") == source_profile
        and state.packet.get("subject_profile") == subject_profile
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
        or request.get("source_subject_profile") != state.packet.get("source_subject_profile")
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
