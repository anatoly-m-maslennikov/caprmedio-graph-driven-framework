"""Real selected Session admission reaches the deferred Subject effect boundary."""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest.mock import patch


APP = Path(__file__).resolve().parents[1]
TOOLS = APP.parent.parent / "201_TOOLS"
for location in (TOOLS / "ATOM_UPDATE/tests", TOOLS, APP):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

import atom_subject_apply as native  # noqa: E402
import atom_subject_patch as subject_patch  # noqa: E402
import work_journal  # noqa: E402
from lifecycle_intents import LifecycleError  # noqa: E402
from test_subject_apply_portfolio import REPOSITORY, SubjectApplyProject  # noqa: E402
from workflow_run_support import RunExecutionSession, SelectedRunError  # noqa: E402


TEST_TEMP_ROOT = REPOSITORY / ".caprmedio_tmp/tests/test_selected_subject_apply"
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)


class SelectedSubjectApplyTests(unittest.TestCase):
    def setUp(self) -> None:
        self.directory = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.addCleanup(self.directory.cleanup)
        self.fixture = SubjectApplyProject(Path(self.directory.name))

    def dispatch_observed(self, run_id: str, *, mutate=None, request_transform=None):
        runner, frozen = self.fixture.execution(run_id, request_transform=request_transform)
        original = native.subject_update_action
        calls = []
        codes = []

        def observed(root, parameters, **kwargs):
            if kwargs.get("execute") is True:
                calls.append(kwargs)
                if mutate is not None:
                    mutate(kwargs)
            try:
                return original(root, parameters, **kwargs)
            except LifecycleError as error:
                codes.append(error.code)
                raise

        with patch.object(native, "subject_update_action", side_effect=observed), patch.object(
            native.operations, "write_raw_atom_revision", wraps=native.operations.write_raw_atom_revision,
        ) as writer:
            result = runner.dispatch(frozen)
        writer.assert_not_called()
        self.fixture.assert_unchanged(self)
        return result, runner, frozen, calls, codes

    def test_sealed_subject_frontier_and_ordered_effect_variants_are_refused(self) -> None:
        duplicate = "target_frontier must not contain duplicate references"
        nonempty = "target_frontier must be a non-empty ordered list"
        variants = (
            ("frontier-missing-current", lambda request: request["target_frontier"].pop(0), None),
            ("frontier-missing-history", lambda request: request["target_frontier"].pop(), None),
            ("frontier-extra", lambda request: request["target_frontier"].append("fixture/unrequested.md"), None),
            ("frontier-duplicate-current", lambda request: request["target_frontier"].append(request["target_frontier"][0]), duplicate),
            ("frontier-duplicate-history", lambda request: request["target_frontier"].append(request["target_frontier"][1]), duplicate),
            ("frontier-reordered", lambda request: request["target_frontier"].reverse(), None),
            ("frontier-empty", lambda request: request["target_frontier"].clear(), nonempty),
            ("effects-missing-current", lambda request: request["effects"].pop(0), None),
            ("effects-missing-history", lambda request: request["effects"].pop(), None),
            ("effects-empty", lambda request: request["effects"].clear(), None),
            ("effects-extra", lambda request: request["effects"].append({"type": "unrequested", "path": "fixture/unrequested.md"}), None),
            ("effects-duplicate-current", lambda request: request["effects"].append(copy.deepcopy(request["effects"][0])), None),
            ("effects-duplicate-history", lambda request: request["effects"].append(copy.deepcopy(request["effects"][1])), None),
            ("effects-reordered", lambda request: request["effects"].reverse(), None),
            ("effect-current-target", lambda request: request["effects"][0].update(path="fixture/unrequested.md"), None),
            ("effect-history-target", lambda request: request["effects"][1].update(path="fixture/unrequested.md"), None),
            ("effect-current-identity", lambda request: request["effects"][0].update(atom_id="CA-R-9999"), None),
            ("effect-history-identity", lambda request: request["effects"][1].update(atom_id="CA-R-9999"), None),
            ("effect-intent-hash", lambda request: request["effects"][0].update(subject_intent_sha256="0" * 64), None),
            ("effect-current-extra-field", lambda request: request["effects"][0].update(unrequested=True), None),
            ("effect-history-missing-hash", lambda request: request["effects"][1].pop("sha256"), None),
        )
        for name, transform, earlier_message in variants:
            with self.subTest(case=name), patch.object(
                native.operations, "write_raw_atom_revision", wraps=native.operations.write_raw_atom_revision,
            ) as writer:
                if earlier_message is not None:
                    with self.assertRaises(SelectedRunError) as refused:
                        self.fixture.execution(f"subject-{name}", request_transform=transform)
                    self.assertEqual("invalid-request", refused.exception.code)
                    self.assertEqual(f"invalid-request: {earlier_message}", str(refused.exception))
                else:
                    result, _, frozen, calls, codes = self.dispatch_observed(
                        f"subject-{name}", request_transform=transform,
                    )
                    sealed = frozen["request"]["execution"]
                    self.assertEqual(sealed["target_frontier_digest"], sealed["operator_authorization"]["target_frontier_digest"])
                    self.assertEqual(sealed["effects_digest"], sealed["operator_authorization"]["effects_digest"])
                    self.assertEqual(["subject-frontier-mismatch"], codes)
                    self.assertEqual(1, len(calls))
                    self.assertFalse(any(row["run_id"] == calls[0]["action_run_id"] and row["outcome"] == "completed"
                                         for row in result["terminal_runs"]))
                writer.assert_not_called()
                self.fixture.assert_unchanged(self)

    def test_frontier_guard_mutant_produces_a_detectable_wrong_diagnostic(self) -> None:
        source = Path(native.__file__).read_text(encoding="utf-8")
        guard = (
            '        if sealed["target_frontier"] != frontier or sealed["effects"] != effects:\n'
            '            _fail("subject-frontier-mismatch", "Subject frontier and effects differ from the exact intent")\n'
        )
        self.assertEqual(1, source.count(guard))
        mutant = types.ModuleType("subject_frontier_guard_mutant")
        exec(compile(source.replace(guard, "", 1), "<disposable Subject frontier mutant>", "exec"), mutant.__dict__)
        probe = SelectedSubjectApplyTests("test_sealed_subject_frontier_and_ordered_effect_variants_are_refused")
        probe.fixture = self.fixture
        with patch.object(native, "subject_update_action", mutant.subject_update_action):
            with self.assertRaises(AssertionError) as wrong_output:
                probe.test_sealed_subject_frontier_and_ordered_effect_variants_are_refused()
        self.assertIn("subject-frontier-mismatch", str(wrong_output.exception))
        self.assertIn("subject-publication-deferred", str(wrong_output.exception))
        self.fixture.assert_unchanged(self)

    def test_real_completed_assessment_and_actual_o030_start_reach_deferred_boundary(self) -> None:
        original_start = RunExecutionSession.start_run

        def actual_ids(session, requested, *, run_id=None):
            kind = session.requested[requested]["kind"]
            return original_start(session, requested, run_id=requested if kind == "workflow" else f"actual::{requested}")

        with patch.object(RunExecutionSession, "start_run", actual_ids):
            result, runner, frozen, calls, codes = self.dispatch_observed("subject-valid-session")
        self.assertEqual(["subject-publication-deferred"], codes)
        self.assertEqual(1, len(calls))
        supplied = calls[0]
        session = supplied["session"]
        self.assertIsInstance(session, RunExecutionSession)
        self.assertTrue(supplied["action_run_id"].startswith("actual::"))
        self.assertEqual("CA-O-030", session._actual_by_id(supplied["action_run_id"])[1]["definition"]["atom_id"])
        provenance = session.read_recorded_action_start(supplied["action_run_id"])
        self.assertTrue(all(value.startswith("actual::") for value in provenance.parent_lineage[:-1]))
        assessment_id = next(key for key, row in session.actual.items() if row["definition"]["atom_id"] == "CA-O-067")
        terminal = session.terminal[assessment_id]
        self.assertEqual("completed", terminal["outcome"])
        reopened = session._reopen_started_event(terminal["event_receipt"])
        self.assertEqual("completed", reopened["event"])
        self.assertEqual(session.actual[assessment_id], reopened["run"])
        retained = json.loads((self.fixture.root / terminal["result_ref"]).read_bytes())
        self.assertEqual(supplied["assessment"], retained["native_result"]["assessment"])
        self.assertEqual(self.fixture.target["digest"], supplied["prior"]["event"]["result"]["sha256"])
        self.assertNotEqual("completed", result.get("outcome"))
        with patch.object(native, "subject_update_action", side_effect=AssertionError("retained execution replayed")):
            self.assertEqual(result, runner.dispatch(frozen))
        self.fixture.assert_unchanged(self)

    def test_missing_same_session_assessment_completion_refuses_before_deferred_boundary(self) -> None:
        def remove_completion(kwargs):
            session = kwargs["session"]
            key = next(key for key, row in session.actual.items() if row["definition"]["atom_id"] == "CA-O-067")
            session.terminal.pop(key)

        _, _, _, calls, codes = self.dispatch_observed("subject-assessment-missing", mutate=remove_completion)
        self.assertEqual(1, len(calls))
        self.assertEqual(["subject-assessment-unrecorded"], codes)

    def test_tampered_retained_assessment_content_cannot_authorize_subject_effect(self) -> None:
        def change_result(kwargs):
            session = kwargs["session"]
            key = next(key for key, row in session.actual.items() if row["definition"]["atom_id"] == "CA-O-067")
            path = self.fixture.root / session.terminal[key]["result_ref"]
            result = json.loads(path.read_bytes())
            result["native_result"]["assessment"]["request_digest"] = "0" * 64
            path.write_text(json.dumps(result), encoding="utf-8")

        _, _, _, calls, codes = self.dispatch_observed("subject-assessment-forged", mutate=change_result)
        self.assertEqual(1, len(calls))
        self.assertEqual(["subject-assessment-unrecorded"], codes)

    def test_forged_actual_start_receipt_refuses_without_replay_or_effect(self) -> None:
        def change_receipt(kwargs):
            session = kwargs["session"]
            requested, _ = session._actual_by_id(kwargs["action_run_id"])
            session._started_receipts[requested]["event_digest"] = "0" * 64

        _, _, _, calls, codes = self.dispatch_observed("subject-start-forged", mutate=change_receipt)
        self.assertEqual(1, len(calls))
        self.assertEqual(["subject-execution-unadmitted"], codes)

    def test_failed_assessment_terminal_recording_never_enters_native_effect(self) -> None:
        runner, frozen = self.fixture.execution("subject-assessment-recording-pending")
        original = work_journal.append_sealed_events

        def fail_assessment_completion(root, events, *args, **kwargs):
            event = events[0]
            if event["event"] == "completed" and event.get("run", {}).get("definition", {}).get("atom_id") == "CA-O-067":
                raise OSError("fixture assessment terminal recording failure")
            return original(root, events, *args, **kwargs)

        with patch.object(work_journal, "append_sealed_events", side_effect=fail_assessment_completion), patch.object(
            native.operations, "write_raw_atom_revision", wraps=native.operations.write_raw_atom_revision,
        ) as writer:
            result = runner.dispatch(frozen)
        self.assertEqual("recording_pending", result["disposition"])
        writer.assert_not_called()
        self.fixture.assert_unchanged(self)
        with patch.object(native, "subject_update_action", side_effect=AssertionError("recording failure replayed native")):
            self.assertEqual(result, runner.dispatch(frozen))

    def test_real_selected_noop_has_no_native_o030_or_history_effect(self) -> None:
        prepared = subject_patch.prepare_subject_intent(
            self.fixture.root, self.fixture.target, [], subject_profile="approved",
        )
        self.fixture.parameters = {"target": self.fixture.target, "subject_patches": [],
                                   "subject_profile": "approved", "subject_intent_sha256": prepared["subject_intent_sha256"]}
        self.fixture.prepared = prepared
        self.fixture.golden._semantic_update_parameters = self.fixture.parameters
        runner, frozen = self.fixture.execution("subject-noop")
        with patch.object(native.operations, "write_raw_atom_revision", wraps=native.operations.write_raw_atom_revision) as writer:
            result = runner.dispatch(frozen)
        writer.assert_not_called()
        self.assertEqual("terminal", result["disposition"])
        requested = frozen["request"]["execution"]["requested_runs"]
        outer = next(row["requested_run_id"] for row in requested if row["definition"]["atom_id"] == "CA-O-128")
        terminal = next(row for row in result["terminal_runs"] if row["run_id"] == outer)
        self.assertEqual("no_op", terminal["outcome"])
        self.assertTrue(all(row["effect_refs"] == [] for row in result["terminal_runs"]))
        child = next(row["requested_run_id"] for row in requested if row["definition"]["atom_id"] == "CA-O-030")
        self.assertNotIn(child, result["run_ids"])
        self.fixture.assert_unchanged(self)


if __name__ == "__main__":
    unittest.main()
