# implementation of:
# Requirement: CA-R-1524
# Method: CA-M-405, CA-M-422

from collections.abc import Mapping
from copy import deepcopy
import json
from pathlib import Path
from typing import Any

from selected_evidence_io import atomic_write, run_directory
from selected_execution_contracts import SelectedExecutionError
from selected_integrated_frontier_records import IntegratedFrontierError, project_root
from selected_integrated_session_record import (
    CHECKPOINT_NAME,
    CheckpointRecord,
    context,
    digest,
    evidence_bytes,
)
from selected_integrated_checkpoint_read import load_bound_checkpoint


def _root(root: Path) -> Path:
    try:
        return project_root(root)
    except IntegratedFrontierError as error:
        raise SelectedExecutionError("selected checkpoint Project root is unavailable") from error


class CheckpointSession:
    def __init__(self, root: Path, frozen: Mapping[str, Any], tracker: Any) -> None:
        from workflow_run_support import RunExecutionSession

        self.root = Path(root)
        self.run_id, request, self.frozen_digest = context(frozen)
        self._session = RunExecutionSession(tracker, request)
        self.evidence_digests: dict[str, str] = {}
        self._bind()

    def _bind(self) -> None:
        for attribute in (
            "tracker request requested workflow_definition_bindings actual terminal "
            "interrupted observed_effects start_event_ids recording_errors"
        ).split():
            setattr(self, attribute, getattr(self._session, attribute))

    def __getattr__(self, name: str) -> Any:
        return getattr(self._session, name)

    def _record(self, root: Path) -> CheckpointRecord:
        for receipt in (*self.terminal.values(), *self.interrupted.values()):
            reference = receipt.get("result_ref")
            if isinstance(reference, str):
                observed = digest(evidence_bytes(root, reference))
                retained = self.evidence_digests.setdefault(reference, observed)
                if retained != observed:
                    raise SelectedExecutionError(
                        "selected checkpoint evidence changed after recording"
                    )
        return CheckpointRecord(
            schema_version=1,
            project_root_digest=digest(root.as_posix().encode()),
            run_id=self.run_id,
            frozen_digest=self.frozen_digest,
            request=deepcopy(self.request),
            actual=deepcopy(self.actual),
            terminal=deepcopy(self.terminal),
            interrupted=deepcopy(self.interrupted),
            observed_effects=deepcopy(self.observed_effects),
            start_event_ids=deepcopy(self.start_event_ids),
            recording_errors=list(self.recording_errors),
            evidence_digests=dict(self.evidence_digests),
        )

    def save(self) -> None:
        root = _root(self.root)
        atomic_write(
            run_directory(root, self.run_id) / CHECKPOINT_NAME, self._record(root).model_dump()
        )
        self.root = root

    def _after[T](self, value: T) -> T:
        self.save()
        return value

    def start_run(self, requested_run_id: str, *, run_id: str | None = None) -> dict[str, Any]:
        return self._after(self._session.start_run(requested_run_id, run_id=run_id))

    def note_effects(self, run_id: str, *, result_ref: str, effect_refs: list[str]) -> None:
        self._session.note_effects(run_id, result_ref=result_ref, effect_refs=effect_refs)
        self.save()

    def finish_run(self, run_id: str, **result: Any) -> dict[str, Any]:
        return self._after(self._session.finish_run(run_id, **result))

    def recover_run(self, run_id: str, **result: Any) -> dict[str, Any]:
        return self._after(self._session.recover_run(run_id, **result))

    def interrupt_open_runs(self) -> None:
        self._session.interrupt_open_runs()
        self.save()

    def read_recorded_action_start(self, action_run_id: str) -> Any:
        return self._session.read_recorded_action_start(action_run_id)

    def _actual_by_id(self, run_id: str) -> tuple[str, dict[str, Any]]:
        return self._session._actual_by_id(run_id)

    start, finish, record_effects = start_run, finish_run, note_effects


def create_checkpoint(root: Path, frozen: Mapping[str, Any], tracker: Any) -> CheckpointSession:
    return CheckpointSession(root, frozen, tracker)


def restore_checkpoint(root: Path, frozen: Mapping[str, Any], tracker: Any) -> CheckpointSession:
    safe_root = _root(Path(root))
    record, _evidence = load_bound_checkpoint(safe_root, frozen)
    session = CheckpointSession(safe_root, frozen, tracker)
    for name in ("actual", "terminal", "interrupted", "observed_effects", "start_event_ids"):
        getattr(session._session, name).update(deepcopy(getattr(record, name)))
    session._session.recording_errors.extend(record.recording_errors)
    session.evidence_digests = dict(record.evidence_digests)
    if session.interrupted:
        raise SelectedExecutionError("selected checkpoint interruption requires explicit recovery")
    return session


def load_completed_output(
    root: Path,
    run_id: str,
    requested_action_id: str,
    session: CheckpointSession,
) -> Mapping[str, Any] | None:
    if run_id != session.run_id:
        raise SelectedExecutionError("selected checkpoint Run binding differs")
    requested = session.requested.get(requested_action_id)
    terminal = session.terminal.get(requested_action_id)
    if requested is None or requested.get("kind") != "action" or terminal is None:
        return None
    actual = session.actual.get(requested_action_id)
    reference = terminal.get("result_ref")
    if (
        terminal.get("disposition") != "terminal"
        or terminal.get("outcome") != "completed"
        or not isinstance(actual, Mapping)
        or terminal.get("run_id") != actual.get("run_id")
        or not isinstance(reference, str)
        or session.evidence_digests.get(reference) is None
    ):
        raise SelectedExecutionError("retained selected Action terminal is invalid")
    safe_root = _root(Path(root))
    expected = (
        (run_directory(safe_root, run_id) / f"{requested_action_id}.json")
        .relative_to(safe_root)
        .as_posix()
    )
    payload = evidence_bytes(safe_root, reference)
    if reference != expected or digest(payload) != session.evidence_digests[reference]:
        raise SelectedExecutionError("retained selected Action progress changed")
    try:
        progress = json.loads(payload)
    except (UnicodeDecodeError, ValueError) as error:
        raise SelectedExecutionError("retained selected Action progress is invalid") from error
    if not isinstance(progress, dict):
        raise SelectedExecutionError("retained selected Action progress is invalid")
    if progress.get("action_run_id") != actual["run_id"] or progress.get(
        "effect_refs"
    ) != terminal.get("effect_refs"):
        raise SelectedExecutionError("retained selected Action progress is inconsistent")
    if not all(key in progress for key in ("result", "effect_refs", "native_result")):
        raise SelectedExecutionError("retained selected Action progress is incomplete")
    return {key: progress[key] for key in ("result", "effect_refs", "native_result")}
