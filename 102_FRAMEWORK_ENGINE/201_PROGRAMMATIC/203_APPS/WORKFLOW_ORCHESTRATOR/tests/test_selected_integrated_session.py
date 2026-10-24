"""Restart and evidence-integrity checks for durable selected Run sessions."""

from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import sys
import tempfile
import unittest


APP = Path(__file__).resolve().parents[1]
TOOLS = APP.parents[1] / "201_TOOLS"
for location in (APP, TOOLS):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

from selected_evidence_io import atomic_write, run_directory  # noqa: E402
from selected_execution_contracts import SelectedExecutionError  # noqa: E402
from selected_integrated_session import (  # noqa: E402
    CHECKPOINT_NAME,
    CheckpointSession,
    create_checkpoint,
    load_completed_output,
    load_bound_checkpoint,
    restore_checkpoint,
)


class RecordingStub:
    """A Journal-free canonical-session recorder with deterministic event IDs."""

    def __init__(self, finish_error: str | None = "journal unavailable") -> None:
        self.calls = 0
        self.finish_error = finish_error

    def _record_run_event(
        self, _request: object, _run: object, event: str, *_: object
    ) -> tuple[str | None, str | None]:
        self.calls += 1
        return (f"event-{self.calls}", self.finish_error if event == "completed" else None)


class SelectedIntegratedSessionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        (self.root / ".git").mkdir()
        (self.root / ".caprmedio_tmp").mkdir()
        self.run_id = "checkpoint-run"
        self.requested = f"{self.run_id}:step:1:action:1"
        self.request = {
            "request_id": "checkpoint-request",
            "operation_route": "update_atom",
            "requested_runs": [
                {
                    "requested_run_id": self.requested,
                    "kind": "action",
                    "definition": {
                        "atom_id": "CA-O-017",
                        "version": 1,
                        "path": "definitions/action.md",
                        "digest": "a" * 64,
                    },
                }
            ],
        }
        self.frozen = {
            "request": {"run_id": self.run_id, "execution": self.request},
            "graph": {"route": "update_atom"},
        }
        self.folder = run_directory(self.root, self.run_id)
        self.folder.mkdir(parents=True)
        self.progress = self.folder / f"{self.requested}.json"
        self.ref = self.progress.relative_to(self.root).as_posix()
        self.effect_refs = ["effects/one.json"]
        self.output = {
            "result": "completed",
            "effect_refs": self.effect_refs,
            "native_result": {"state": "done"},
        }

    def _completed(self) -> CheckpointSession:
        session = create_checkpoint(self.root, self.frozen, RecordingStub())
        self.assertFalse((self.folder / CHECKPOINT_NAME).exists())
        run = session.start_run(self.requested, run_id="actual-action")
        atomic_write(self.progress, {**self.output, "action_run_id": run["run_id"]})
        session.note_effects(run["run_id"], result_ref=self.ref, effect_refs=self.effect_refs)
        session.finish_run(
            run["run_id"], outcome="completed", result_ref=self.ref, effect_refs=self.effect_refs
        )
        return session

    def _interrupted_graph(self) -> Path:
        session = create_checkpoint(self.root, self.frozen, RecordingStub())
        run = session.start_run(self.requested, run_id="actual-action")
        graph_result = self.folder / "graph_result.json"
        atomic_write(
            graph_result, {"outcome": "interrupted_pending", "workflow_run_id": self.run_id}
        )
        session.finish_run(
            run["run_id"],
            outcome="interrupted_pending",
            result_ref=graph_result.relative_to(self.root).as_posix(),
            effect_refs=[],
        )
        return graph_result

    def test_restart_retains_canonical_run_facts_without_a_journal(self) -> None:
        session = self._completed()
        restored = restore_checkpoint(self.root, self.frozen, RecordingStub())
        self.assertEqual(session.actual, restored.actual)
        self.assertEqual(session.terminal, restored.terminal)
        self.assertEqual(session.observed_effects, restored.observed_effects)
        self.assertEqual(session.start_event_ids, restored.start_event_ids)
        self.assertEqual(["journal unavailable"], restored.recording_errors)
        self.assertEqual(
            self.output, load_completed_output(self.root, self.run_id, self.requested, restored)
        )
        self.assertFalse((self.root / ".caprmedio_caprmedio" / "_journal").exists())

    def test_changed_progress_is_refused_before_a_provider_can_run(self) -> None:
        session = self._completed()
        restored = restore_checkpoint(self.root, self.frozen, RecordingStub())
        atomic_write(
            self.progress, {**self.output, "action_run_id": "actual-action", "result": "changed"}
        )
        with self.assertRaisesRegex(SelectedExecutionError, "changed"):
            session.save()
        with self.assertRaisesRegex(SelectedExecutionError, "changed"):
            load_completed_output(self.root, self.run_id, self.requested, restored)

    def test_nested_lifecycle_and_evidence_key_tampering_are_refused(self) -> None:
        self._completed()
        checkpoint = self.folder / CHECKPOINT_NAME
        record = json.loads(checkpoint.read_text(encoding="utf-8"))
        record["actual"][self.requested]["kind"] = "workflow"
        atomic_write(checkpoint, record)
        with self.assertRaisesRegex(SelectedExecutionError, "lifecycle"):
            restore_checkpoint(self.root, self.frozen, RecordingStub())
        record["actual"][self.requested]["kind"] = "action"
        record["evidence_digests"]["not-bound.json"] = "a" * 64
        atomic_write(checkpoint, record)
        with self.assertRaisesRegex(SelectedExecutionError, "evidence digests"):
            restore_checkpoint(self.root, self.frozen, RecordingStub())

    def test_frozen_mismatch_link_and_malformed_checkpoint_are_refused(self) -> None:
        self._completed()
        changed = deepcopy(self.frozen)
        changed["graph"] = {"route": "create_atom"}
        with self.assertRaisesRegex(SelectedExecutionError, "binding differs"):
            restore_checkpoint(self.root, changed, RecordingStub())
        checkpoint = self.folder / CHECKPOINT_NAME
        external = self.root / "outside.json"
        external.write_bytes(checkpoint.read_bytes())
        checkpoint.unlink()
        checkpoint.symlink_to(external)
        with self.assertRaisesRegex(SelectedExecutionError, "unsafe"):
            restore_checkpoint(self.root, self.frozen, RecordingStub())
        checkpoint.unlink()
        checkpoint.write_bytes(b"{")
        with self.assertRaisesRegex(SelectedExecutionError, "invalid"):
            restore_checkpoint(self.root, self.frozen, RecordingStub())

    def test_interrupted_checkpoint_is_not_a_normal_resume(self) -> None:
        session = create_checkpoint(self.root, self.frozen, RecordingStub())
        run = session.start_run(self.requested, run_id="actual-action")
        session.finish_run(
            run["run_id"], outcome="interrupted_pending", result_ref=None, effect_refs=[]
        )
        with self.assertRaisesRegex(SelectedExecutionError, "explicit recovery"):
            restore_checkpoint(self.root, self.frozen, RecordingStub())

    def test_bound_checkpoint_reads_a_verified_interrupted_graph_without_resuming(self) -> None:
        self._interrupted_graph()
        record, evidence = load_bound_checkpoint(self.root, self.frozen)
        self.assertIn(self.requested, record.interrupted)
        self.assertTrue(next(iter(evidence)).endswith("/graph_result.json"))
        record.interrupted.clear()
        restored, _evidence = load_bound_checkpoint(self.root, self.frozen)
        self.assertIn(self.requested, restored.interrupted)
        with self.assertRaisesRegex(SelectedExecutionError, "explicit recovery"):
            restore_checkpoint(self.root, self.frozen, RecordingStub())

    def test_bound_checkpoint_refuses_missing_or_changed_interrupted_graph_evidence(self) -> None:
        for mutation in ("missing", "changed"):
            with self.subTest(mutation=mutation):
                graph_result = self._interrupted_graph()
                if mutation == "missing":
                    graph_result.unlink()
                else:
                    atomic_write(graph_result, {"outcome": "changed"})
                with self.assertRaises(SelectedExecutionError):
                    load_bound_checkpoint(self.root, self.frozen)


if __name__ == "__main__":
    unittest.main()
