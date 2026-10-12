"""Bridge one retained O164 delivery frontier into an explicit O199 command.

This is deliberately not a selected-workflow executor or an MCP route.  It
opens the already-recorded selected Release Run, proves its completed O172
frontier, and derives fresh typed candidate/export/compilation/snapshot inputs
before delegating the only catalog-writing operation to
``source_admission_command``.  Caller supplied objects and hashes are never
accepted as evidence.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
import os
from pathlib import Path
import stat
import sys
from typing import Any


_RELEASE_ROOT = Path(__file__).resolve().parent
_TOOLS_ROOT = _RELEASE_ROOT.parent
_WORKFLOW_APP_ROOT = _TOOLS_ROOT.parent / "203_APPS" / "WORKFLOW_ORCHESTRATOR"
for _path in (_TOOLS_ROOT, _WORKFLOW_APP_ROOT):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))

from release_actions import PHASES, ReleaseActionRun
from release_checkpoint import load_release_checkpoint
from release_compilation import SealedPrivateMethodologyCompilation, read_sealed_private_methodology_compilation
from release_contract import ReleaseContractError, ValidatedCandidate, canonical_json
from release_handoff import SealedMethodologyExport
from release_portable_contract import SealedPortableSourceSnapshot, collect_portable_source_snapshot, revalidate_portable_source_snapshot
from selected_execution import SelectedExecution, SelectedExecutionError
from selected_run_recovery import read_selected_run_evidence
from source_admission_command import SourceAdmissionCommandResult, run_source_admission_command
from workflow_run_support import RecordedActionStartProvenance, RunExecutionSession, SelectedRunError, _validate_common
import work_journal


_RELEASE_WORKFLOW_ID = "CA-O-164"
_RELEASE_WORKFLOW_VERSION = 9
_DELIVERY_INDEX = 2
_DELIVERY_STEP_ID, _DELIVERY_ACTION_ID, _DELIVERY_PHASE = PHASES[_DELIVERY_INDEX]


class SourceAdmissionHostCommandError(RuntimeError):
    """Stable pre-effect refusal from the retained-release/O199 bridge."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(f"{code}: {message}")


@dataclass(frozen=True)
class SourceAdmissionHostCommandRequest:
    """Only command and retained-Run selectors for one O199 invocation.

    ``release_run_id`` is the selected request identity used to locate the
    frozen selected request/checkpoint.  ``requested_action_run_id`` is the
    frozen requested O172 occurrence, not an actual generated Run UUID.
    ``release_authorization_ref`` is compared with the closed selected
    authorization carrier; it is not an approval flag and is never passed to
    O199 as a replacement authorization.
    """

    project_root: str | Path
    release_run_id: str
    requested_action_run_id: str
    operator: str
    command_id: str
    operators_registry_ref: str
    release_authorization_ref: str


@dataclass(frozen=True)
class ReopenedSourceAdmissionFrontier:
    """Read-only physical O164/O172 frontier usable by the O199 command."""

    release_run_id: str
    requested_action_run_id: str
    action_provenance: RecordedActionStartProvenance
    candidate: ValidatedCandidate
    methodology_export: SealedMethodologyExport
    private_compilation: SealedPrivateMethodologyCompilation
    source_snapshot: SealedPortableSourceSnapshot


@dataclass(frozen=True)
class SourceAdmissionHostCommandResult:
    """One reopened O164 frontier and the resulting explicit O199 command."""

    frontier: ReopenedSourceAdmissionFrontier
    admission_command: SourceAdmissionCommandResult


@dataclass(frozen=True)
class SourceAdmissionCommandPreview:
    """Read-only O164/O172 facts for one explicit O199 command proposal.

    ``snapshot_sha256`` is the D602 descriptor-array digest, calculated from
    the reopened snapshot with the admission module's one canonical descriptor
    projection.  It is returned for a later explicit execute request, not
    accepted as source evidence.
    """

    frontier: ReopenedSourceAdmissionFrontier
    snapshot_sha256: str


def _refuse(code: str, message: str) -> None:
    raise SourceAdmissionHostCommandError(code, message)


def _text(value: object, field: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip() or "\n" in value or "\r" in value:
        _refuse("source-admission-host-command-invalid", f"{field} must be one bounded identifier")
    return value


def _root(value: object) -> Path:
    try:
        supplied = Path(value)  # type: ignore[arg-type]
        root = supplied.resolve(strict=True)
    except (OSError, TypeError, ValueError) as error:
        raise SourceAdmissionHostCommandError(
            "source-admission-host-command-root-invalid", "Project root is unavailable",
        ) from error
    if supplied.is_symlink() or root.is_symlink() or not root.is_dir():
        _refuse("source-admission-host-command-root-invalid", "Project root must be a regular directory")
    return root


def _request(value: object) -> SourceAdmissionHostCommandRequest:
    if type(value) is not SourceAdmissionHostCommandRequest:
        _refuse("source-admission-host-command-invalid", "bridge requires one typed host-command request")
    return value


def _as_mapping(value: object, code: str, label: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        _refuse(code, f"{label} is not a mapping")
    return value


def _definition(binding: object, *, kind: str, atom_id: str, label: str) -> dict[str, object]:
    value = _as_mapping(binding, "source-admission-host-command-release-invalid", label)
    expected = {"atom_id", "kind", "version", "path", "sha256"}
    extras = {
        "workflow": frozenset(),
        "step": frozenset({"actions", "on_result"}),
        "action": frozenset({"result_map"}),
    }[kind]
    if set(value) != expected | extras or value.get("kind") != kind or value.get("atom_id") != atom_id:
        _refuse("source-admission-host-command-release-invalid", f"{label} differs from its required selected definition")
    version = value.get("version")
    path = value.get("path")
    digest = value.get("sha256")
    if type(version) is not int or version < 1 or not isinstance(path, str) or not path or not isinstance(digest, str) or len(digest) != 64:
        _refuse("source-admission-host-command-release-invalid", f"{label} has an invalid selected definition")
    return {"atom_id": atom_id, "version": version, "path": path, "digest": digest}


def _graph(frozen: Mapping[str, Any]) -> tuple[dict[str, object], tuple[tuple[dict[str, object], dict[str, object]], ...]]:
    graph = _as_mapping(frozen.get("graph"), "source-admission-host-command-release-invalid", "frozen graph")
    if graph.get("route") != "release_version":
        _refuse("source-admission-host-command-release-invalid", "frozen Run is not the Release Version route")
    workflow = _definition(graph.get("workflow"), kind="workflow", atom_id=_RELEASE_WORKFLOW_ID, label="frozen workflow")
    if workflow["version"] != _RELEASE_WORKFLOW_VERSION:
        _refuse("source-admission-host-command-release-invalid", "frozen Release workflow is not O164@9")
    raw_steps = graph.get("steps")
    if not isinstance(raw_steps, list) or len(raw_steps) != len(PHASES):
        _refuse("source-admission-host-command-release-invalid", "frozen Release graph lacks the exact O164 phase sequence")
    pairs: list[tuple[dict[str, object], dict[str, object]]] = []
    for index, (step_id, action_id, _phase) in enumerate(PHASES):
        step = _definition(raw_steps[index], kind="step", atom_id=step_id, label=f"frozen step {index}")
        raw_actions = _as_mapping(raw_steps[index], "source-admission-host-command-release-invalid", f"frozen step {index}").get("actions")
        if not isinstance(raw_actions, list) or len(raw_actions) != 1:
            _refuse("source-admission-host-command-release-invalid", f"frozen step {index} lacks one Action")
        action = _definition(raw_actions[0], kind="action", atom_id=action_id, label=f"frozen action {index}")
        pairs.append((step, action))
    return workflow, tuple(pairs)


def _expected_action_id(release_run_id: str) -> str:
    return f"{release_run_id}:step:{_DELIVERY_INDEX + 1}:action:1"


def _same_definition(actual: object, expected: Mapping[str, object]) -> bool:
    return isinstance(actual, Mapping) and dict(actual) == dict(expected)


def _terminal_completed(session: RunExecutionSession, requested_id: str, *, label: str) -> Mapping[str, Any]:
    terminal = session.terminal.get(requested_id)
    if not isinstance(terminal, Mapping):
        _refuse("source-admission-host-command-release-incomplete", f"{label} has no durable terminal record")
    if terminal.get("disposition") != "terminal" or terminal.get("outcome") != "completed":
        _refuse("source-admission-host-command-release-uncertain", f"{label} is not durably completed")
    return terminal


def _current_graph(runner: SelectedExecution, frozen: Mapping[str, Any]) -> Mapping[str, Any]:
    try:
        current = runner._revalidate(frozen)
    except (OSError, RuntimeError, ValueError, SelectedExecutionError) as error:
        raise SourceAdmissionHostCommandError(
            "source-admission-host-command-release-stale", "current selected Release source cannot be revalidated",
        ) from error
    if canonical_json(current) != canonical_json(frozen.get("graph")):
        _refuse("source-admission-host-command-release-stale", "current selected Release graph differs from frozen graph")
    return current


def _reopen_release_source_admission_frontier(
    root: Path,
    release_run_id: str,
    requested_action_id: str,
    authorization_ref: str,
) -> ReopenedSourceAdmissionFrontier:
    """Read one completed O172 checkpoint and derive its pre-catalog snapshot.

    The function has no Journal, catalog, checkpoint, or projection effect.
    It intentionally refuses every completed/advanced frontier except the
    exact first three O164@9 occurrences: freeze, validate, and delivery.
    """

    if requested_action_id != _expected_action_id(release_run_id):
        _refuse("source-admission-host-command-action-mismatch", "requested Action is not the exact O172 occurrence")

    try:
        runner = SelectedExecution(root)
        frozen = runner.load(release_run_id)
    except (FileNotFoundError, OSError, ValueError, RuntimeError, SelectedExecutionError) as error:
        raise SourceAdmissionHostCommandError(
            "source-admission-host-command-release-missing", "frozen selected Release Run is unavailable",
        ) from error
    frozen_request = _as_mapping(frozen.get("request"), "source-admission-host-command-release-invalid", "frozen selected request")
    if frozen_request.get("run_id") != release_run_id or frozen_request.get("operation") != "enqueue_selected":
        _refuse("source-admission-host-command-release-invalid", "frozen selected request does not bind the requested Release Run")
    workflow, pairs = _graph(frozen)
    _current_graph(runner, frozen)

    try:
        execution = _validate_common(_as_mapping(frozen_request.get("execution"), "source-admission-host-command-release-invalid", "frozen execution"))
    except (SelectedRunError, ValueError, TypeError) as error:
        raise SourceAdmissionHostCommandError(
            "source-admission-host-command-release-invalid", "frozen selected execution is not closed and valid",
        ) from error
    if execution.get("operation_route") != "release_version":
        _refuse("source-admission-host-command-release-invalid", "frozen execution is not the Release Version route")
    authorization = _as_mapping(execution.get("operator_authorization"), "source-admission-host-command-release-invalid", "frozen operator authorization")
    if authorization.get("authorization_ref") != authorization_ref:
        _refuse("source-admission-host-command-authorization-mismatch", "release authorization carrier differs from the frozen Run")
    parameters = execution.get("parameters")
    if not isinstance(parameters, Mapping) or parameters.get("project_root") != str(root):
        _refuse("source-admission-host-command-project-mismatch", "frozen release parameters do not bind this Project")

    try:
        evidence = read_selected_run_evidence(root, execution)
        session = RunExecutionSession.restore(runner._shared_tracker(frozen), execution, evidence["events"])
    except (OSError, RuntimeError, ValueError, KeyError, TypeError, SelectedExecutionError, SelectedRunError) as error:
        raise SourceAdmissionHostCommandError(
            "source-admission-host-command-release-evidence-invalid", "selected Release Journal evidence cannot be reopened",
        ) from error

    requested_steps = tuple(f"{release_run_id}:step:{index + 1}" for index in range(_DELIVERY_INDEX + 1))
    requested_actions = tuple(f"{step}:action:1" for step in requested_steps)
    workflow_actual = session.actual.get(release_run_id)
    if not isinstance(workflow_actual, Mapping) or workflow_actual.get("kind") != "workflow" or not _same_definition(workflow_actual.get("definition"), workflow):
        _refuse("source-admission-host-command-release-evidence-invalid", "actual Workflow differs from frozen O164")
    workflow_run_id = workflow_actual.get("run_id")
    if not isinstance(workflow_run_id, str) or not workflow_run_id:
        _refuse("source-admission-host-command-release-evidence-invalid", "actual Workflow has no bounded Run identity")
    for index, (requested_step, requested_action) in enumerate(zip(requested_steps, requested_actions)):
        actual_step = session.actual.get(requested_step)
        actual_action = session.actual.get(requested_action)
        expected_step, expected_action = pairs[index]
        if (
            not isinstance(actual_step, Mapping)
            or not isinstance(actual_action, Mapping)
            or actual_step.get("kind") != "step"
            or actual_action.get("kind") != "action"
            or actual_step.get("parent_run_id") != workflow_run_id
            or actual_action.get("parent_run_id") != actual_step.get("run_id")
            or not _same_definition(actual_step.get("definition"), expected_step)
            or not _same_definition(actual_action.get("definition"), expected_action)
        ):
            _refuse("source-admission-host-command-release-evidence-invalid", f"O164 phase {index} actual Run differs from frozen source")
        _terminal_completed(session, requested_action, label=f"O164 phase {index} Action")
        _terminal_completed(session, requested_step, label=f"O164 phase {index} Step")

    delivery_actual = session.actual[requested_action_id]
    try:
        provenance = session.read_recorded_action_start(str(delivery_actual["run_id"]))
    except (KeyError, RuntimeError, ValueError, SelectedRunError) as error:
        raise SourceAdmissionHostCommandError(
            "source-admission-host-command-release-evidence-invalid", "O172 start receipt cannot be physically reopened",
        ) from error

    folder = runner.run_directory(release_run_id)
    try:
        checkpoint = runner._read(folder / "release_action_run.json")
        private_run, _recordings = load_release_checkpoint(
            checkpoint,
            expected_request=parameters,
            expected_workflow_run_id=workflow_run_id,
        )
    except (OSError, RuntimeError, ValueError, TypeError, KeyError, ReleaseContractError, SelectedExecutionError) as error:
        raise SourceAdmissionHostCommandError(
            "source-admission-host-command-checkpoint-invalid", "O164 private checkpoint cannot be reopened",
        ) from error
    if type(private_run) is not ReleaseActionRun:
        _refuse("source-admission-host-command-checkpoint-invalid", "checkpoint did not restore one private Release Run")
    if private_run.in_progress is not None or private_run.stopped:
        _refuse("source-admission-host-command-release-uncertain", "O164 checkpoint is in-progress or stopped")
    if private_run.next_phase != _DELIVERY_INDEX + 1:
        code = "source-admission-host-command-release-advanced" if private_run.next_phase > _DELIVERY_INDEX + 1 else "source-admission-host-command-release-incomplete"
        _refuse(code, "O164 checkpoint is not exactly at the completed O172 frontier")
    if set(private_run.contexts) != {0, 1, 2} or set(private_run.results) != {0, 1, 2}:
        _refuse("source-admission-host-command-checkpoint-invalid", "O164 checkpoint has an incomplete or advanced phase frontier")
    if private_run.portable_compilation is not None or private_run.portable_source_snapshot is not None or private_run.private_compilation is not None:
        _refuse("source-admission-host-command-release-advanced", "O164 checkpoint already contains a post-admission portable frontier")
    if not isinstance(private_run.candidate, ValidatedCandidate) or not isinstance(private_run.methodology_export, SealedMethodologyExport):
        _refuse("source-admission-host-command-checkpoint-invalid", "O164 checkpoint lacks its sealed candidate/export frontier")
    for index, (context, result) in enumerate(zip((private_run.contexts[key] for key in range(3)), (private_run.results[key] for key in range(3)))):
        expected_step, expected_action = pairs[index]
        actual_step = session.actual[requested_steps[index]]
        actual_action = session.actual[requested_actions[index]]
        if (
            context.workflow_run_id != workflow_run_id
            or context.step_run_id != actual_step["run_id"]
            or context.action_run_id != actual_action["run_id"]
            or context.parent_workflow_run_id != workflow_run_id
            or context.parent_step_run_id != actual_step["run_id"]
            or context.workflow_atom_id != _RELEASE_WORKFLOW_ID
            or context.workflow_version != _RELEASE_WORKFLOW_VERSION
            or context.step_atom_id != expected_step["atom_id"]
            or context.action_atom_id != expected_action["atom_id"]
            or result.outcome != "completed"
            or result.workflow_run_id != workflow_run_id
            or result.step_run_id != actual_step["run_id"]
            or result.action_run_id != actual_action["run_id"]
            or result.candidate_snapshot_manifest_sha256 != private_run.candidate.manifest.sha256
        ):
            _refuse("source-admission-host-command-checkpoint-invalid", f"O164 checkpoint phase {index} is not the retained Journal occurrence")

    try:
        private = read_sealed_private_methodology_compilation(private_run.methodology_export)
        snapshot = collect_portable_source_snapshot(private_run.candidate, private, candidate_run_id=workflow_run_id)
        snapshot = revalidate_portable_source_snapshot(snapshot)
    except (OSError, RuntimeError, ValueError, ReleaseContractError) as error:
        raise SourceAdmissionHostCommandError(
            "source-admission-host-command-frontier-stale", "O164 candidate/export pre-catalog frontier changed",
        ) from error
    # Recheck selected source after every expensive physical reopen and before
    # the direct command is allowed to record its own O199 start.
    _current_graph(runner, frozen)
    return ReopenedSourceAdmissionFrontier(
        release_run_id,
        requested_action_id,
        provenance,
        private_run.candidate,
        private_run.methodology_export,
        private,
        snapshot,
    )


def _frozen_authorization_ref(root: Path, release_run_id: str) -> str:
    """Read the closed O164 authorization reference without trusting a caller."""

    try:
        runner = SelectedExecution(root)
        frozen = runner.load(release_run_id)
    except (FileNotFoundError, OSError, ValueError, RuntimeError, SelectedExecutionError) as error:
        raise SourceAdmissionHostCommandError(
            "source-admission-host-command-release-missing", "frozen selected Release Run is unavailable",
        ) from error
    frozen_request = _as_mapping(frozen.get("request"), "source-admission-host-command-release-invalid", "frozen selected request")
    if frozen_request.get("run_id") != release_run_id or frozen_request.get("operation") != "enqueue_selected":
        _refuse("source-admission-host-command-release-invalid", "frozen selected request does not bind the requested Release Run")
    try:
        execution = _validate_common(
            _as_mapping(frozen_request.get("execution"), "source-admission-host-command-release-invalid", "frozen execution")
        )
    except (SelectedRunError, ValueError, TypeError) as error:
        raise SourceAdmissionHostCommandError(
            "source-admission-host-command-release-invalid", "frozen selected execution is not closed and valid",
        ) from error
    if execution.get("operation_route") != "release_version":
        _refuse("source-admission-host-command-release-invalid", "frozen execution is not the Release Version route")
    authorization = _as_mapping(
        execution.get("operator_authorization"),
        "source-admission-host-command-release-invalid",
        "frozen operator authorization",
    )
    return _text(authorization.get("authorization_ref"), "frozen release authorization_ref")


def _registry_ref(root: Path) -> str:
    """Derive the one Project-configured operator registry, never a caller path."""

    try:
        settings = work_journal.resolve_settings_path(root)
        registry = settings.parent / "operators_registry.toml"
        relative = registry.relative_to(root)
        metadata = os.lstat(registry)
        if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
            _refuse("source-admission-host-command-registry-invalid", "configured Operator registry is not a regular file")
        registry.resolve(strict=True).relative_to(root)
    except SourceAdmissionHostCommandError:
        raise
    except (OSError, RuntimeError, ValueError) as error:
        raise SourceAdmissionHostCommandError(
            "source-admission-host-command-registry-invalid", "configured Operator registry is unavailable or unsafe",
        ) from error
    return relative.as_posix()


def _snapshot_sha256(snapshot: SealedPortableSourceSnapshot) -> str:
    """Use D602's one descriptor projection for the adapter-visible checksum."""

    try:
        # D602 has the only authoritative package-row-to-descriptor mapping.
        # Keep this narrow import private to avoid a second producer or codec.
        from source_catalog_admission import _descriptors_from_snapshot, source_snapshot_sha256

        return source_snapshot_sha256(_descriptors_from_snapshot(snapshot))
    except Exception as error:
        code = getattr(error, "code", "source-admission-host-command-snapshot-invalid")
        raise SourceAdmissionHostCommandError(
            str(code), "retained O172 snapshot has no valid D602 descriptor projection",
        ) from error


def reopen_release_source_admission_frontier(
    request: SourceAdmissionHostCommandRequest,
) -> ReopenedSourceAdmissionFrontier:
    """Low-level retained-run reopener for an already command-bound request."""

    command = _request(request)
    root = _root(command.project_root)
    release_run_id = _text(command.release_run_id, "release_run_id")
    requested_action_id = _text(command.requested_action_run_id, "requested_action_run_id")
    authorization_ref = _text(command.release_authorization_ref, "release_authorization_ref")
    return _reopen_release_source_admission_frontier(root, release_run_id, requested_action_id, authorization_ref)


def preview_source_admission_command(
    project_root: str | Path,
    *,
    release_run_id: str,
) -> SourceAdmissionCommandPreview:
    """Read exactly one retained O164/O172 frontier; never select or scan Runs."""

    root = _root(project_root)
    release = _text(release_run_id, "release_run_id")
    authorization_ref = _frozen_authorization_ref(root, release)
    frontier = _reopen_release_source_admission_frontier(
        root,
        release,
        _expected_action_id(release),
        authorization_ref,
    )
    return SourceAdmissionCommandPreview(frontier, _snapshot_sha256(frontier.source_snapshot))


def run_release_source_admission_command(
    request: SourceAdmissionHostCommandRequest,
) -> SourceAdmissionHostCommandResult:
    """Explicitly admit the one pre-catalog snapshot retained at completed O172."""

    command = _request(request)
    frontier = reopen_release_source_admission_frontier(command)
    operator = _text(command.operator, "operator")
    command_id = _text(command.command_id, "command_id")
    registry_ref = _text(command.operators_registry_ref, "operators_registry_ref")
    # The direct command repeats physical snapshot observation immediately
    # before its direct O199 start; do not replace that guard with this
    # bridge's prior observation.
    admitted = run_source_admission_command(
        frontier.candidate,
        frontier.private_compilation,
        candidate_run_id=frontier.source_snapshot.candidate_run_id,
        operator=operator,
        command_id=command_id,
        operators_registry_ref=registry_ref,
    )
    if admitted.source_snapshot != frontier.source_snapshot:
        _refuse("source-admission-host-command-frontier-stale", "O199 recomputed a different pre-catalog snapshot")
    return SourceAdmissionHostCommandResult(frontier, admitted)


def execute_source_admission_command(
    project_root: str | Path,
    *,
    command_id: str,
    release_run_id: str,
    operator: str,
    authorization_ref: str,
    observed_snapshot_sha256: str,
) -> SourceAdmissionHostCommandResult:
    """Execute O199 only for one re-previewed, explicitly observed O172 snapshot."""

    root = _root(project_root)
    release = _text(release_run_id, "release_run_id")
    supplied_authorization = _text(authorization_ref, "authorization_ref")
    expected_authorization = _frozen_authorization_ref(root, release)
    if supplied_authorization != expected_authorization:
        _refuse("source-admission-host-command-authorization-mismatch", "adapter authorization carrier differs from frozen O164")
    observed = _text(observed_snapshot_sha256, "observed_snapshot_sha256")
    if len(observed) != 64 or any(character not in "0123456789abcdef" for character in observed):
        _refuse("source-admission-host-command-invalid", "observed_snapshot_sha256 must be a lowercase SHA-256")
    preview = preview_source_admission_command(root, release_run_id=release)
    if observed != preview.snapshot_sha256:
        _refuse("source-admission-host-command-snapshot-mismatch", "adapter snapshot does not match the re-opened O172 frontier")
    request = SourceAdmissionHostCommandRequest(
        project_root=root,
        release_run_id=release,
        requested_action_run_id=_expected_action_id(release),
        operator=_text(operator, "operator"),
        command_id=_text(command_id, "command_id"),
        operators_registry_ref=_registry_ref(root),
        release_authorization_ref=expected_authorization,
    )
    return run_release_source_admission_command(request)


__all__ = [
    "ReopenedSourceAdmissionFrontier",
    "SourceAdmissionCommandPreview",
    "SourceAdmissionHostCommandError",
    "SourceAdmissionHostCommandRequest",
    "SourceAdmissionHostCommandResult",
    "execute_source_admission_command",
    "preview_source_admission_command",
    "reopen_release_source_admission_frontier",
    "run_release_source_admission_command",
]
