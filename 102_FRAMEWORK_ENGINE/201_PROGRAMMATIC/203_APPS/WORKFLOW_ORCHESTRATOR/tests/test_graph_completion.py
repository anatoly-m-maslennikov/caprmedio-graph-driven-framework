"""Fixture-only D539 completion/recovery boundary checks.

These tests exercise retained graph observations and executor receipts only.
They do not construct a graph, append a Journal event, or prove a live Run.
"""

from __future__ import annotations

from copy import deepcopy
import hashlib
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import MagicMock, patch


APP = Path(__file__).resolve().parents[1]
if str(APP) not in sys.path:
    sys.path.insert(0, str(APP))

from graph_completion import (  # noqa: E402
    GraphCompletionError,
    construction_outcome,
    finalize_graph_result,
)
from selected_execution import SelectedExecution, SelectedExecutionError, canonical_json  # noqa: E402
import backend  # noqa: E402


class GraphCompletionTests(unittest.TestCase):
    """Use one complete retained construction; terminal facts remain external."""

    action_run_id = "fixture-workflow:step:1:action:1"
    result_ref = "runs/fixture-workflow/graph-action.json"
    output_path = "_projection/entities-graph.json"
    digest = "a" * 64

    def receipt(self, event_id: str = "fixture-terminal-event") -> dict[str, object]:
        return {
            "event_id": event_id,
            "action_id": "CA-O-134",
            "event_digest": self.digest,
            "carrier": "_journal/events.ndjson",
            "line": 9,
            "previous_carrier_digest": "b" * 64,
            "appended_carrier_digest": "c" * 64,
        }

    def observation(self, *, effect_state: str = "created") -> dict[str, object]:
        after = {"carrier_path": self.output_path, "carrier_sha256": self.digest}
        if effect_state == "unchanged":
            effects = {"state": "unchanged", "paths": [], "before": after, "after": after}
        else:
            effects = {"state": effect_state, "paths": [self.output_path], "before": None, "after": after}
        return {
            "outcome": "incomplete",
            "entities_graph": {"entities": []},
            "source_frontier_evidence": {"source_frontier_sha256": "d" * 64},
            "selection_evidence": {"selection": {"atom_ids": []}},
            "source_fact_context_evidence": {"context_sha256": "e" * 64},
            "lineage": {"sources": []},
            "quality_dispositions": {
                "coverage": "pass", "fidelity": "pass", "validity": "pass",
                "currentness": "pass", "permission": "pass", "persistence": "pass",
                "recording": "unresolved",
            },
            "diagnostics": [],
            "non_authoritative": True,
            "output_effects": effects,
            "completion": {"state": "awaiting_terminal_recording"},
            "run_receipt_refs": ["fixture-start-event"],
            "projection_revision": self.digest,
        }

    def terminal(self, *, outcome: str, receipt: dict[str, object] | None = None,
                 disposition: str = "terminal", effect_refs: list[str] | None = None) -> dict[str, object]:
        value: dict[str, object] = {
            "disposition": disposition,
            "outcome": outcome,
            "run_id": self.action_run_id,
            "result_ref": self.result_ref,
            "effect_refs": [self.output_path] if effect_refs is None else effect_refs,
            "event_id": "fixture-terminal-event",
        }
        if receipt is not None:
            value["event_receipt"] = receipt
        return value

    def finalize(self, observation: dict[str, object], terminal: dict[str, object] | None,
                 *, receipts: list[dict[str, object]], pending_event_id: str | None = None) -> dict[str, object]:
        return finalize_graph_result(
            observation, terminal, action_run_id=self.action_run_id,
            result_ref=self.result_ref, effect_refs=observation["output_effects"]["paths"],
            receipts=receipts, pending_event_id=pending_event_id,
        )

    def test_completed_construction_needs_bound_terminal_and_preserves_pure_observation(self) -> None:
        observation = self.observation()
        before = deepcopy(observation)
        start = self.receipt("fixture-start-event")
        receipt = self.receipt()

        self.assertEqual("completed", construction_outcome(observation))
        result = self.finalize(observation, self.terminal(outcome="completed", receipt=receipt), receipts=[start, receipt])

        self.assertEqual(before, observation)
        self.assertEqual("built", result["outcome"])
        self.assertEqual("pass", result["quality_dispositions"]["recording"])
        self.assertEqual(
            {"state": "recorded", "terminal_receipt_ref": "fixture-terminal-event"},
            result["completion"],
        )
        self.assertEqual(["fixture-start-event", "fixture-terminal-event"], result["run_receipt_refs"])
        self.assertEqual(before["output_effects"], result["output_effects"])

    def test_unchanged_projection_can_only_become_recorded_no_op(self) -> None:
        observation = self.observation(effect_state="unchanged")
        start = self.receipt("fixture-start-event")
        receipt = self.receipt()
        terminal = self.terminal(outcome="no_op", receipt=receipt, effect_refs=[])

        self.assertEqual("no_op", construction_outcome(observation))
        result = self.finalize(observation, terminal, receipts=[start, receipt])

        self.assertEqual("no_op", result["outcome"])
        self.assertEqual("recorded", result["completion"]["state"])
        self.assertEqual([], result["output_effects"]["paths"])

    def test_recording_failure_retains_actual_effect_and_pending_identity(self) -> None:
        observation = self.observation()
        start = self.receipt("fixture-start-event")
        terminal = self.terminal(outcome="completed", disposition="recording_pending")

        result = self.finalize(
            observation, terminal, receipts=[start], pending_event_id="fixture-pending-terminal-event",
        )

        self.assertEqual("incomplete", result["outcome"])
        self.assertEqual("unresolved", result["quality_dispositions"]["recording"])
        self.assertEqual(
            {"state": "recording_pending", "pending_receipt_ref": "fixture-pending-terminal-event"},
            result["completion"],
        )
        self.assertEqual(observation["output_effects"], result["output_effects"])
        self.assertEqual(["fixture-start-event"], result["run_receipt_refs"])

    def test_missing_terminal_blocks_without_converting_construction_to_built(self) -> None:
        observation = self.observation()
        start = self.receipt("fixture-start-event")

        result = self.finalize(observation, None, receipts=[start])

        self.assertEqual("incomplete", result["outcome"])
        self.assertEqual({"state": "blocked"}, result["completion"])
        self.assertEqual("unresolved", result["quality_dispositions"]["recording"])

    def test_forged_or_mismatched_terminal_fails_closed(self) -> None:
        observation = self.observation()
        start = self.receipt("fixture-start-event")
        receipt = self.receipt()
        cases = (
            self.terminal(outcome="completed", receipt=receipt, effect_refs=[]),
            self.terminal(outcome="completed", receipt=self.receipt("forged-event")),
            self.terminal(outcome="no_op", receipt=receipt),
        )

        for terminal in cases:
            with self.subTest(terminal=terminal):
                with self.assertRaises(GraphCompletionError):
                    self.finalize(observation, terminal, receipts=[start, receipt])


class GraphCompletionRecoveryTests(unittest.TestCase):
    """Reconciliation reads retained evidence; it never reinvokes construction."""

    run_id = "fixture-workflow"
    requested_step = "fixture-workflow:step:1"
    requested_action = "fixture-workflow:step:1:action:1"
    actual_workflow = "actual-workflow"
    actual_step = "actual-step"
    actual_action = "actual-action"
    output_path = "_projection/entities-graph.json"

    def setUp(self) -> None:
        temp_root = Path.cwd() / ".caprmedio_tmp" / "tests"
        temp_root.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=temp_root, ignore_cleanup_errors=True)
        self.root = Path(self.temporary.name)
        self.folder = self.root / "runs" / self.run_id
        self.folder.mkdir(parents=True)
        self.runner = SelectedExecution(self.root)
        self.completion = GraphCompletionTests("runTest")
        self.completion.output_path = self.output_path
        self.observation = self.completion.observation()
        self.progress_ref = f"runs/{self.run_id}/{self.requested_action}.json"
        self.aggregate_ref = f"runs/{self.run_id}/graph_result.json"
        self.progress_path = self.root / self.progress_ref
        self.aggregate_path = self.root / self.aggregate_ref
        self.accepted_path = self.folder / "accepted.json"
        self.accepted_path.write_text("{}", encoding="utf-8")

    def tearDown(self) -> None:
        self.temporary.cleanup()

    @staticmethod
    def receipt(event_id: str) -> dict[str, object]:
        return {
            "event_id": event_id,
            "action_id": "CA-O-134",
            "event_digest": "a" * 64,
            "carrier": "_journal/events.ndjson",
            "line": 3,
            "previous_carrier_digest": "b" * 64,
            "appended_carrier_digest": "c" * 64,
        }

    def terminal(self, run_id: str, result_ref: str, receipt: dict[str, object]) -> dict[str, object]:
        return {
            "disposition": "terminal", "outcome": "completed", "run_id": run_id,
            "result_ref": result_ref, "effect_refs": [self.output_path],
            "event_id": receipt["event_id"], "event_receipt": receipt,
        }

    def fixture(self, *, confirmed_parents: bool = True,
                action_effects: list[str] | None = None) -> tuple[dict[str, object], SimpleNamespace, dict[str, object], dict[str, object]]:
        action_receipt = self.receipt("action-terminal")
        start_receipt = self.receipt("fixture-start-event")
        step_receipt = self.receipt("step-terminal")
        workflow_receipt = self.receipt("workflow-terminal")
        action = self.terminal(self.actual_action, self.progress_ref, action_receipt)
        if action_effects is not None:
            action["effect_refs"] = action_effects
        actual = {
            self.run_id: {"run_id": self.actual_workflow},
            self.requested_step: {"run_id": self.actual_step},
            self.requested_action: {"run_id": self.actual_action},
        }
        terminal = {self.requested_action: action}
        if confirmed_parents:
            terminal.update({
                self.requested_step: self.terminal(self.actual_step, self.aggregate_ref, step_receipt),
                self.run_id: self.terminal(self.actual_workflow, self.aggregate_ref, workflow_receipt),
            })
        session = SimpleNamespace(
            actual=actual, terminal=terminal, interrupted={},
            receipts=[start_receipt, action_receipt, step_receipt, workflow_receipt], pending=[],
        )
        graph = {
            "route": "build_entities_graph", "workflow": {"atom_id": "CA-O-133"},
            "steps": [{"atom_id": "CA-O-134", "actions": [{
                "atom_id": "CA-O-134", "result_map": {"built": "completed", "no_op": "no_op"},
            }]}],
        }
        execution = {"request_id": "fixture-request"}
        frozen = {"request": {"run_id": self.run_id, "execution": execution}, "graph": graph}
        return frozen, session, graph, execution

    def persisted(self) -> tuple[dict[str, object], dict[str, object], dict[str, object]]:
        progress = {
            "result": "recording_pending", "action_run_id": self.actual_action,
            "effect_refs": [self.output_path], "graph_construction_observation": deepcopy(self.observation),
            "graph_construction_digest": hashlib.sha256(canonical_json(self.observation)).hexdigest(),
            "native_result": {
                "completion": {"state": "recording_pending", "pending_receipt_ref": "action-terminal"},
            },
        }
        aggregate = {
            "outcome": "interrupted_pending", "workflow_run_id": self.actual_workflow,
            "workflow_definition_id": "CA-O-133", "step_results": [{
                "step_run_id": self.actual_step, "action_run_id": self.actual_action,
                "step_definition_id": "CA-O-134", "action_definition_id": "CA-O-134",
                "result": "recording_pending", "effect_refs": [self.output_path],
            }],
        }
        accepted = {"result": {"disposition": "recording_pending", "pending_event_ids": []}}
        return progress, aggregate, accepted

    def reconcile(self, *, confirmed_parents: bool = True,
                  action_effects: list[str] | None = None,
                  construction_digest: str | None = None) -> tuple[dict[str, object], dict[str, object], dict[str, object], MagicMock]:
        frozen, session, graph, execution = self.fixture(
            confirmed_parents=confirmed_parents, action_effects=action_effects,
        )
        progress, aggregate, accepted = self.persisted()
        if construction_digest is not None:
            progress["graph_construction_digest"] = construction_digest
        values = {
            self.progress_path: progress,
            self.aggregate_path: aggregate,
            self.accepted_path: accepted,
        }
        writes: dict[Path, object] = {}
        tracker = SimpleNamespace(
            _observe=lambda _execution: {"selected": True, "current": True},
            _session_result=lambda *_args: {"disposition": "terminal", "outcome": "completed"},
        )
        execute = MagicMock(side_effect=AssertionError("reconciliation must not rerun the graph builder"))
        pending_reader = MagicMock(side_effect=AssertionError("recovered evidence must not read a pending carrier"))
        with patch.object(self.runner, "_revalidate", return_value=graph), \
             patch.object(self.runner, "_shared_tracker", return_value=tracker), \
             patch.object(self.runner, "run_directory", return_value=self.folder), \
             patch.object(self.runner, "load", return_value=deepcopy(frozen)), \
             patch.object(self.runner, "_safe_path", side_effect=lambda ref: self.root / ref), \
             patch.object(self.runner, "_read", side_effect=lambda path: values[path]), \
             patch.object(self.runner, "_write", side_effect=lambda path, value: writes.__setitem__(path, value)), \
             patch.object(self.runner, "_execute_graph", execute), \
             patch("selected_run_recovery.read_selected_run_evidence", return_value={"events": [{"event": {"event_id": "action-terminal"}}]}), \
             patch("selected_run_recovery.validate_selected_run_events"), \
             patch("workflow_run_support._validate_common", return_value=execution), \
             patch("workflow_run_support._proposal", return_value={"fixture": "proposal"}), \
             patch("workflow_run_support.RunExecutionSession.restore", return_value=session), \
             patch("work_journal._read_pending_event", pending_reader):
            result = self.runner.reconcile_graph_recording(frozen)
        execute.assert_not_called()
        pending_reader.assert_not_called()
        return result, writes, values, execute

    def test_recovery_uses_sealed_evidence_without_replaying_builder(self) -> None:
        result, writes, _values, _execute = self.reconcile()

        progress = writes[self.progress_path]
        aggregate = writes[self.aggregate_path]
        self.assertEqual(("terminal", "completed"), (result["disposition"], result["outcome"]))
        self.assertEqual("completed", progress["result"])
        self.assertEqual("built", progress["native_result"]["outcome"])
        self.assertEqual("recorded", progress["native_result"]["completion"]["state"])
        self.assertEqual("completed", aggregate["outcome"])
        self.assertEqual("completed", aggregate["step_results"][0]["result"])

    def test_tampered_persisted_construction_digest_fails_closed(self) -> None:
        with self.assertRaises(SelectedExecutionError):
            self.reconcile(construction_digest="0" * 64)

    def test_mismatched_terminal_and_unconfirmed_parents_fail_closed(self) -> None:
        with self.assertRaises((GraphCompletionError, SelectedExecutionError)):
            self.reconcile(action_effects=[])

        result, writes, _values, _execute = self.reconcile(confirmed_parents=False)
        self.assertEqual("started", result["disposition"])
        self.assertEqual("interrupted_pending", writes[self.aggregate_path]["outcome"])
        self.assertEqual("completed", writes[self.progress_path]["result"])
        self.assertEqual("built", writes[self.progress_path]["native_result"]["outcome"])

    def test_dispatch_reconciles_only_the_same_frozen_pending_graph(self) -> None:
        frozen, _session, _graph, _execution = self.fixture()
        retained = {"result": {"disposition": "recording_pending", "outcome": "interrupted_pending"}}
        recovered = {"disposition": "terminal", "outcome": "completed"}
        no_redispatch = MagicMock(side_effect=AssertionError("dispatch must not replay graph construction"))
        no_builder = MagicMock(side_effect=AssertionError("dispatch must not invoke the graph builder"))
        no_write = MagicMock(side_effect=AssertionError("reconciliation dispatch must not add a file write"))
        with patch.object(self.runner, "run_directory", return_value=self.folder), \
             patch.object(self.runner, "_read", return_value=retained), \
             patch.object(self.runner, "load", return_value=deepcopy(frozen)), \
             patch.object(self.runner, "reconcile_graph_recording", return_value=recovered) as reconcile, \
             patch.object(self.runner, "_shared_dispatch", no_redispatch), \
             patch.object(self.runner, "_execute_graph", no_builder), \
             patch.object(self.runner, "_write", no_write):
            self.assertIs(recovered, self.runner.dispatch(frozen))
            changed = deepcopy(frozen)
            changed["request"]["execution"]["request_id"] = "changed-fixture-request"
            with self.assertRaises(SelectedExecutionError):
                self.runner.dispatch(changed)

        reconcile.assert_called_once_with(frozen)
        no_redispatch.assert_not_called()
        no_builder.assert_not_called()
        no_write.assert_not_called()


class GraphCompletionStatusTests(unittest.TestCase):
    """DBOS status observes recovered graph evidence without admitting an Action."""

    run_id = "fixture-status-workflow"

    def setUp(self) -> None:
        temp_root = Path.cwd() / ".caprmedio_tmp" / "tests"
        temp_root.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=temp_root, ignore_cleanup_errors=True)
        self.root = Path(self.temporary.name)
        self.selected_directory = self.root / "selected"
        self.selected_directory.mkdir()
        self.selected_request = self.selected_directory / "selected_request.json"
        self.accepted = self.selected_directory / "accepted.json"
        self.selected_request.touch()
        self.accepted.touch()
        self.frozen = {
            "request": {"run_id": self.run_id, "execution": {"request_id": "fixture-status-request"}},
            "graph": {"workflow": {"atom_id": "CA-O-133"}, "route": "build_entities_graph"},
        }
        self.pending = {"disposition": "recording_pending", "outcome": "interrupted_pending"}

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def status(self, recovered: object) -> tuple[dict[str, object], MagicMock, MagicMock]:
        files = {
            self.selected_request: self.frozen,
            self.accepted: {"result": self.pending},
        }
        selected = MagicMock()
        selected.run_directory.return_value = self.selected_directory
        selected._read.side_effect = lambda path: files[Path(path)]
        selected.load.return_value = deepcopy(self.frozen)
        selected.reconcile_graph_recording.side_effect = recovered if isinstance(recovered, Exception) else None
        if not isinstance(recovered, Exception):
            selected.reconcile_graph_recording.return_value = recovered
        selected.dispatch.side_effect = AssertionError("status must not dispatch an Action")
        selected._shared_dispatch.side_effect = AssertionError("status must not reach a provider")
        selected._write.side_effect = AssertionError("status observation must not write files")
        scheduler = SimpleNamespace(status="SUCCESS")
        handle = MagicMock()
        handle.get_status.return_value = scheduler
        handle.get_result.return_value = {"cached_dbos_result": True}
        transport = MagicMock()
        transport.retrieve_workflow.return_value = handle
        with patch.object(backend, "release_host_runtime", return_value=False), \
             patch.object(backend, "SelectedExecution", return_value=selected), \
             patch.object(backend, "client", return_value=transport):
            observed = backend.status(self.root, {"operation": "status", "run_id": self.run_id})
        transport.destroy.assert_called_once()
        return observed, selected, handle

    def test_cached_success_status_uses_recovered_recording_without_action_or_writes(self) -> None:
        recovered = {"disposition": "terminal", "outcome": "completed"}

        observed, selected, handle = self.status(recovered)

        self.assertEqual({"cached_dbos_result": True}, observed["result"])
        self.assertIs(recovered, observed["selected_result"])
        self.assertEqual(("terminal", "completed"), (observed["disposition"], observed["outcome"]))
        selected.load.assert_called_once_with(self.run_id)
        selected.reconcile_graph_recording.assert_called_once_with(self.frozen, persist=False)
        selected.dispatch.assert_not_called()
        selected._shared_dispatch.assert_not_called()
        selected._write.assert_not_called()
        handle.get_result.assert_called_once()

    def test_unavailable_reconciliation_retains_pending_without_raw_failure_or_completion(self) -> None:
        observed, selected, _handle = self.status(RuntimeError("fixture secret must not be disclosed"))

        self.assertIs(self.pending, observed["selected_result"])
        self.assertEqual(("recording_pending", "interrupted_pending"),
                         (observed["disposition"], observed["outcome"]))
        self.assertEqual(
            "graph-recording-reconciliation-unavailable: saved evidence or current admission gate is unresolved",
            observed["reason"],
        )
        self.assertNotIn("secret", observed["reason"])
        selected.reconcile_graph_recording.assert_called_once_with(self.frozen, persist=False)
        selected.dispatch.assert_not_called()
        selected._write.assert_not_called()

    def test_recovered_interrupted_parent_remains_incomplete_in_status(self) -> None:
        recovered = {"disposition": "started", "outcome": "interrupted_pending"}

        observed, selected, _handle = self.status(recovered)

        self.assertIs(recovered, observed["selected_result"])
        self.assertEqual(("started", "interrupted_pending"),
                         (observed["disposition"], observed["outcome"]))
        selected.reconcile_graph_recording.assert_called_once_with(self.frozen, persist=False)
        selected.dispatch.assert_not_called()
        selected._write.assert_not_called()


if __name__ == "__main__":
    unittest.main()
