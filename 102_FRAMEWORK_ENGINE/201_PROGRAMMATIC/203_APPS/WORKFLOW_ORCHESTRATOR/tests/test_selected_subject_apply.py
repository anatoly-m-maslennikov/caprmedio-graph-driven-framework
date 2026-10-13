"""Isolated current W02 proof, not release-manifest or live-migration acceptance."""

from __future__ import annotations

import copy
import hashlib
import json
import pickle
import subprocess
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest.mock import patch


APP = Path(__file__).resolve().parents[1]
TOOLS = APP.parent.parent / "201_TOOLS"
for location in (TOOLS / "ATOM_UPDATE/tests", TOOLS / "tests", TOOLS, APP):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

import atom_subject_apply as native  # noqa: E402
import atom_subject_patch as subject_patch  # noqa: E402
import work_journal  # noqa: E402
import atom_operations as operations  # noqa: E402
from lifecycle_intents import LifecycleError  # noqa: E402
from test_subject_apply_portfolio import REPOSITORY, SubjectApplyProject, PUBLICATION_PINS  # noqa: E402
from test_engine_publication_lock import CONTENDER, BUSY, start_child, read_event, send_command  # noqa: E402
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
        self.assertIn("subject-publication-window-unconfirmed", str(wrong_output.exception))
        self.fixture.assert_unchanged(self)

    def test_public_dispatch_with_real_session_cannot_self_confirm_publication(self) -> None:
        original_start = RunExecutionSession.start_run

        def actual_ids(session, requested, *, run_id=None):
            kind = session.requested[requested]["kind"]
            return original_start(session, requested, run_id=requested if kind == "workflow" else f"actual::{requested}")

        with patch.object(RunExecutionSession, "start_run", actual_ids):
            result, runner, frozen, calls, codes = self.dispatch_observed("subject-valid-session")
        self.assertEqual(["subject-publication-window-unconfirmed"], codes)
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

    def confirmed_execution(self, run_id):
        runner, frozen = self.fixture.execution(run_id)
        return runner, frozen, self.fixture.confirmation(frozen)

    def observe_confirmed(self, runner, frozen, confirmation):
        original = native.subject_update_action
        results = []

        def observed(root, parameters, **kwargs):
            result = original(root, parameters, **kwargs)
            if kwargs.get("execute") is True:
                results.append(result)
            return result

        with patch.object(native, "subject_update_action", side_effect=observed):
            result = runner._dispatch_confirmed_subject(frozen, confirmation)
        self.assertEqual(1, len(results))
        return result, results[0]

    def assert_no_replay(self, runner, frozen, result):
        with patch.object(native, "subject_update_action", side_effect=AssertionError("retained effect replayed")):
            self.assertEqual(result, runner.dispatch(frozen))

    def assert_confirmed_refusal(self, runner, frozen, confirmation, code):
        original = native.subject_update_action
        codes = []

        def observed(root, parameters, **kwargs):
            try:
                return original(root, parameters, **kwargs)
            except LifecycleError as error:
                if kwargs.get("execute") is True:
                    codes.append(error.code)
                raise

        with patch.object(native, "subject_update_action", side_effect=observed), patch.object(
            operations, "write_raw_atom_revision", wraps=operations.write_raw_atom_revision,
        ) as writer:
            result = runner._dispatch_confirmed_subject(frozen, confirmation)
        writer.assert_not_called()
        self.assertEqual([code], codes)
        self.fixture.assert_unchanged(self)
        self.assert_no_replay(runner, frozen, result)

    def test_stale_governing_source_refuses_exact_host_record_before_effects(self):
        runner, frozen, confirmation = self.confirmed_execution("subject-private-authority-stale")
        path = self.fixture.root / PUBLICATION_PINS["CA-R-866"][0]
        changed = path.read_bytes() + b"\n<!-- fixture governing source changed -->\n"
        path.write_bytes(changed)
        self.assert_confirmed_refusal(runner, frozen, confirmation, "subject-publication-window-unconfirmed")
        self.assertEqual(changed, path.read_bytes())

    def test_confirmation_for_another_exact_request_cannot_authorize_this_session(self):
        _, _, confirmation = self.confirmed_execution("subject-private-other-request")
        runner, frozen = self.fixture.execution("subject-private-request-mismatch")
        self.assert_confirmed_refusal(runner, frozen, confirmation, "subject-publication-window-unconfirmed")

    def test_host_record_for_another_root_cannot_authorize_this_project(self):
        original = self.fixture
        _, _, confirmation = self.confirmed_execution("subject-private-original-root")
        directory = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.addCleanup(directory.cleanup)
        self.fixture = SubjectApplyProject(Path(directory.name))
        runner, frozen = self.fixture.execution("subject-private-wrong-root")
        self.assert_confirmed_refusal(runner, frozen, confirmation, "subject-publication-window-unconfirmed")
        original.assert_unchanged(self)

    def test_reviewed_candidate_changed_after_confirmation_refuses_before_effects(self):
        runner, frozen, confirmation = self.confirmed_execution("subject-private-candidate-stale")
        manifest = json.loads((self.fixture.root / self.fixture.staged["manifest_path"]).read_bytes())
        path = self.fixture.root / manifest["atoms"][0]["candidate"]["path"]
        changed = path.read_bytes() + b"\nreviewed candidate was altered\n"
        path.write_bytes(changed)
        self.assert_confirmed_refusal(runner, frozen, confirmation, "subject-publication-window-unconfirmed")
        self.assertEqual(changed, path.read_bytes())

    def test_current_mode_changed_after_confirmation_refuses_before_effects(self):
        runner, frozen, confirmation = self.confirmed_execution("subject-private-mode-stale")
        self.fixture.path.chmod(0o600)
        self.fixture.before_mode = 0o600
        self.assert_confirmed_refusal(runner, frozen, confirmation, "subject-publication-window-unconfirmed")

    def test_identical_bytes_at_new_current_inode_do_not_preserve_confirmation(self):
        runner, frozen, confirmation = self.confirmed_execution("subject-private-inode-stale")
        saved = self.fixture.path.with_name("reviewed-original.md")
        self.fixture.path.rename(saved)
        self.fixture.path.write_bytes(self.fixture.before)
        self.fixture.path.chmod(self.fixture.before_mode)
        saved.rename(saved.with_suffix(".saved"))
        self.assert_confirmed_refusal(runner, frozen, confirmation, "subject-publication-window-unconfirmed")

    def test_json_boolean_constructor_and_unissued_objects_cannot_mint_confirmation(self):
        from subject_publication_authorization import SubjectPublicationConfirmation, SubjectPublicationAuthorizationError
        runner, frozen = self.fixture.execution("subject-private-self-mint")
        issued = self.fixture.confirmation(frozen)
        with self.assertRaises(TypeError):
            json.dumps(issued)
        with self.assertRaises(TypeError):
            pickle.dumps(issued)
        with self.assertRaises(AttributeError):
            issued._record = {}
        with self.assertRaises(TypeError):
            SubjectPublicationConfirmation()
        forged = object.__new__(SubjectPublicationConfirmation)
        object.__setattr__(forged, "_record", issued._record)
        for value in (True, {"confirmed": True, "operator": "golden-operator"}, forged):
            with self.subTest(value=type(value).__name__), self.assertRaises(SubjectPublicationAuthorizationError), patch.object(
                operations, "write_raw_atom_revision", wraps=operations.write_raw_atom_revision,
            ) as writer:
                runner._dispatch_confirmed_subject(frozen, value)
            writer.assert_not_called()
            self.fixture.assert_unchanged(self)
        object.__setattr__(issued._record, "intent_digest", "0" * 64)
        with self.assertRaises(SubjectPublicationAuthorizationError), patch.object(
            operations, "write_raw_atom_revision", wraps=operations.write_raw_atom_revision,
        ) as writer:
            runner._dispatch_confirmed_subject(frozen, issued)
        writer.assert_not_called()
        self.fixture.assert_unchanged(self)

    def test_native_history_collision_preserves_foreign_exact_bytes_and_mode(self):
        runner, frozen, confirmation = self.confirmed_execution("subject-private-history-collision")
        real_write = operations.write_raw_atom_revision
        foreign = b"history that is not owned by this attempt\n"

        def collide(root, path, raw, **kwargs):
            if Path(path) == self.fixture.archive and raw is not None:
                self.fixture.archive.parent.mkdir(parents=True, exist_ok=True)
                self.fixture.archive.write_bytes(foreign)
                self.fixture.archive.chmod(0o600)
            return real_write(root, path, raw, **kwargs)

        with patch.object(operations, "write_raw_atom_revision", side_effect=collide):
            result, failed = self.observe_confirmed(runner, frozen, confirmation)
        self.assertEqual("failed", failed["outcome"])
        self.assertEqual(self.fixture.before, self.fixture.path.read_bytes())
        self.assertEqual(self.fixture.before_mode, self.fixture.path.stat().st_mode & 0o777)
        self.assertEqual(foreign, self.fixture.archive.read_bytes())
        self.assertEqual(0o600, self.fixture.archive.stat().st_mode & 0o777)
        self.assert_no_replay(runner, frozen, result)

    def test_trusted_private_dispatch_publishes_and_records_exact_current_history(self):
        runner, frozen, confirmation = self.confirmed_execution("subject-private-success")
        result, applied = self.observe_confirmed(runner, frozen, confirmation)
        self.assertEqual("applied", applied["outcome"])
        self.assertEqual(self.fixture.before, self.fixture.archive.read_bytes())
        self.assertEqual(self.fixture.before_mode, self.fixture.archive.stat().st_mode & 0o777)
        self.assertEqual(self.fixture.before_mode, self.fixture.path.stat().st_mode & 0o777)
        current = self.fixture.path.read_bytes()
        self.assertEqual(applied["observed"]["digest"], hashlib.sha256(current).hexdigest())
        self.assertEqual(self.fixture.target["version"] + 1, applied["observed"]["version"])
        self.assertNotEqual(self.fixture.target["updated_at"], applied["observed"]["updated_at"])
        self.assertEqual(self.fixture.prepared["proposed"]["content"], operations.split_frontmatter(current.decode())[1])
        self.assertEqual("terminal", result["disposition"])
        child = next(row["requested_run_id"] for row in frozen["request"]["execution"]["requested_runs"]
                     if row["definition"]["atom_id"] == "CA-O-030")
        terminal = next(row for row in result["terminal_runs"] if row["run_id"] == child)
        self.assertEqual("completed", terminal["outcome"])
        self.assertEqual(sorted([self.fixture.target["path"], self.fixture.archive.relative_to(self.fixture.root).as_posix()]),
                         terminal["effect_refs"])
        retained = json.loads((self.fixture.root / terminal["result_ref"]).read_bytes())
        self.assertEqual(applied, retained["native_result"])
        self.assertEqual("admitted", retained["lifecycle_recording"]["state"])
        self.assert_no_replay(runner, frozen, result)
        from subject_publication_authorization import SubjectPublicationAuthorizationError
        with self.assertRaises(SubjectPublicationAuthorizationError), patch.object(
            operations, "write_raw_atom_revision", wraps=operations.write_raw_atom_revision,
        ) as writer:
            runner._dispatch_confirmed_subject(frozen, confirmation)
        writer.assert_not_called()

    def test_success_preserves_crlf_source_body_and_exact_predecessor(self):
        directory = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.addCleanup(directory.cleanup)
        self.fixture = SubjectApplyProject(Path(directory.name), newline="\r\n")
        runner, frozen, confirmation = self.confirmed_execution("subject-private-crlf")
        result, applied = self.observe_confirmed(runner, frozen, confirmation)
        self.assertEqual("applied", applied["outcome"])
        current = self.fixture.path.read_bytes()
        self.assertEqual(self.fixture.before, self.fixture.archive.read_bytes())
        self.assertEqual(self.fixture.before.split(b"\r\n---\r\n", 1)[1], current.split(b"\r\n---\r\n", 1)[1])
        self.assertEqual(current.count(b"\n"), current.count(b"\r\n"))
        self.assertEqual(self.fixture.before_mode, self.fixture.path.stat().st_mode & 0o777)
        self.assert_no_replay(runner, frozen, result)

    def test_real_host_issuer_and_selected_apply_use_omitted_legacy_profile_default(self):
        directory = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.addCleanup(directory.cleanup)
        self.fixture = SubjectApplyProject(Path(directory.name), subject_profile="legacy")
        self.fixture.parameters.pop("subject_profile")
        self.assertEqual("legacy", self.fixture.prepared["subject_intent"]["subject_profile"])
        runner, frozen, confirmation = self.confirmed_execution("subject-private-legacy-default")
        self.assertNotIn("subject_profile", frozen["request"]["execution"]["parameters"])
        result, applied = self.observe_confirmed(runner, frozen, confirmation)
        self.assertEqual("applied", applied["outcome"])
        self.assertEqual(self.fixture.before, self.fixture.archive.read_bytes())
        self.assertEqual(self.fixture.target["version"] + 1, applied["observed"]["version"])
        self.assert_no_replay(runner, frozen, result)

    def test_caught_post_current_failure_restores_exact_bytes_mode_and_owned_history(self):
        runner, frozen, confirmation = self.confirmed_execution("subject-private-restored")
        real_write = operations.write_raw_atom_revision
        failed = False

        def fail_current(root, path, raw, **kwargs):
            nonlocal failed
            owner = real_write(root, path, raw, **kwargs)
            if Path(path) == self.fixture.path and raw != self.fixture.before and not failed:
                failed = True
                raise operations.ToolError("fixture-post-current", "caught publication failure",
                                           {"publication_fingerprint": owner})
            return owner

        with patch.object(operations, "write_raw_atom_revision", side_effect=fail_current):
            result, failed_result = self.observe_confirmed(runner, frozen, confirmation)
        self.assertTrue(failed)
        self.assertEqual("failed", failed_result["outcome"])
        self.assertEqual("current", failed_result["failure"]["original"]["phase"])
        self.assertTrue(all(effect["state"] == "unchanged" for effect in failed_result["effects"]))
        self.fixture.assert_unchanged(self)
        self.assert_no_replay(runner, frozen, result)

    def test_failed_post_effect_authority_check_restores_owned_current_and_history(self):
        runner, frozen, confirmation = self.confirmed_execution("subject-private-postcondition")
        real_write = operations.write_raw_atom_revision
        governing = self.fixture.root / PUBLICATION_PINS["CA-R-866"][0]
        changed = governing.read_bytes() + b"\n<!-- fixture post-effect source conflict -->\n"

        def change_authority(root, path, raw, **kwargs):
            owner = real_write(root, path, raw, **kwargs)
            if Path(path) == self.fixture.path and raw != self.fixture.before:
                governing.write_bytes(changed)
            return owner

        with patch.object(operations, "write_raw_atom_revision", side_effect=change_authority):
            result, failed = self.observe_confirmed(runner, frozen, confirmation)
        self.assertEqual("failed", failed["outcome"])
        self.assertEqual("readback", failed["failure"]["original"]["phase"])
        self.fixture.assert_unchanged(self)
        self.assertEqual(changed, governing.read_bytes())
        self.assert_no_replay(runner, frozen, result)

    def test_unknown_foreign_current_is_retained_with_no_success_or_automatic_retry(self):
        runner, frozen, confirmation = self.confirmed_execution("subject-private-unknown")
        real_write = operations.write_raw_atom_revision
        foreign = b"foreign current; manual inspection required\n"
        saved = self.fixture.path.with_name("attempt-owned-current.md")

        def replace_current(root, path, raw, **kwargs):
            owner = real_write(root, path, raw, **kwargs)
            if Path(path) == self.fixture.path and raw != self.fixture.before:
                self.fixture.path.rename(saved)
                self.fixture.path.write_bytes(foreign)
                raise operations.ToolError("fixture-outsider", "writer outside exclusive-window contract",
                                           {"publication_fingerprint": owner})
            return owner

        with patch.object(operations, "write_raw_atom_revision", side_effect=replace_current):
            result, partial = self.observe_confirmed(runner, frozen, confirmation)
        self.assertEqual("partial", partial["outcome"])
        self.assertFalse(partial["recovery"]["automatic_retry"])
        self.assertTrue(all(effect["state"] == "unknown" for effect in partial["effects"]))
        self.assertEqual(foreign, self.fixture.path.read_bytes())
        self.assertTrue(saved.exists())
        self.assertEqual(self.fixture.before, self.fixture.archive.read_bytes())
        self.assert_no_replay(runner, frozen, result)

    def test_contender_cannot_enter_validation_effects_readback_or_restoration(self):
        runner, frozen, confirmation = self.confirmed_execution("subject-private-lock")
        child = start_child(self, CONTENDER, self.fixture.root)
        self.assertEqual("ready", read_event(self, child))
        real_write = operations.write_raw_atom_revision
        real_gate = native._gate
        real_read = operations.read_raw_atom_revision
        phases = []
        failed = False
        effect_started = False

        def assert_busy():
            send_command(child)
            self.assertEqual(BUSY, read_event(self, child))

        def locked_gate(*args, **kwargs):
            assert_busy()
            return real_gate(*args, **kwargs)

        def locked_read(root, path):
            if effect_started and Path(path) in (self.fixture.path, self.fixture.archive):
                assert_busy()
            return real_read(root, path)

        def locked_write(root, path, raw, **kwargs):
            nonlocal failed, effect_started
            assert_busy()
            effect_started = True
            owner = real_write(root, path, raw, **kwargs)
            phases.append((Path(path), raw is None))
            assert_busy()
            if Path(path) == self.fixture.path and raw != self.fixture.before and not failed:
                failed = True
                raise operations.ToolError("fixture-held-failure", "restore under same owner",
                                           {"publication_fingerprint": owner})
            return owner

        with patch.object(native, "_gate", side_effect=locked_gate), patch.object(
            operations, "read_raw_atom_revision", side_effect=locked_read,
        ), patch.object(operations, "write_raw_atom_revision", side_effect=locked_write):
            result, restored = self.observe_confirmed(runner, frozen, confirmation)
        self.assertEqual("failed", restored["outcome"])
        self.assertEqual([(self.fixture.archive, False), (self.fixture.path, False),
                         (self.fixture.path, False), (self.fixture.archive, True)], phases)
        send_command(child)
        self.assertEqual("acquired", read_event(self, child))
        self.fixture.assert_unchanged(self)
        self.assert_no_replay(runner, frozen, result)

    def test_process_exit_after_history_or_current_retains_started_facts_without_replay(self):
        program = r'''
import json, os, sys
from pathlib import Path
sys.path[:0] = [sys.argv[1], sys.argv[2]]
import atom_operations as operations
from selected_execution import SelectedExecution
from subject_publication_authorization import authorize_subject_publication
root, run_id, boundary = Path(sys.argv[3]), sys.argv[4], sys.argv[5]
runner = SelectedExecution(root)
frozen = runner.load(run_id)
execution = frozen["request"]["execution"]
confirmation = authorize_subject_publication(root, execution, operator_name="golden-operator",
    llm_session={"app": "run-support", "uuid": execution["request_id"]},
    staged_manifest=json.loads(sys.argv[6]))
target = root / execution["parameters"]["target"]["path"]
real_write = operations.write_raw_atom_revision
def interrupt(root, path, raw, **kwargs):
    owner = real_write(root, path, raw, **kwargs)
    if (boundary == "current" and Path(path) == target) or (boundary == "history" and Path(path) != target):
        os._exit(73)
    return owner
operations.write_raw_atom_revision = interrupt
runner._dispatch_confirmed_subject(frozen, confirmation)
raise AssertionError("Requested publication boundary was not reached")
'''
        for boundary in ("history", "current"):
            with self.subTest(boundary=boundary):
                directory = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
                self.addCleanup(directory.cleanup)
                self.fixture = SubjectApplyProject(Path(directory.name))
                run_id = f"subject-private-process-exit-{boundary}"
                runner, frozen, _ = self.confirmed_execution(run_id)
                staged_pin = {"path": self.fixture.staged["manifest_path"], "digest": self.fixture.staged["manifest_sha256"]}
                child = subprocess.run([sys.executable, "-B", "-c", program, str(TOOLS), str(APP),
                    str(self.fixture.root), run_id, boundary, json.dumps(staged_pin)], capture_output=True, timeout=30)
                self.assertEqual(73, child.returncode, child.stderr.decode())
                current = self.fixture.path.read_bytes()
                metadata, _ = operations.split_frontmatter(current.decode())
                expected_version = self.fixture.target["version"] + (boundary == "current")
                self.assertEqual(str(expected_version), operations.frontmatter_scalar(metadata, "version"))
                if boundary == "history":
                    self.assertEqual(self.fixture.before, current)
                self.assertEqual(self.fixture.before, self.fixture.archive.read_bytes())
                events = [work_journal.validate_sealed_event(json.loads(line))
                    for path in (self.fixture.root / ".caprmedio_caprmedio/_journal").glob("*.ndjson")
                    for line in path.read_bytes().splitlines()]
                native_events = [event for event in events if event.get("run", {}).get("definition", {}).get("atom_id") == "CA-O-030"]
                self.assertEqual(["started"], [event["event"] for event in native_events])
                self.assertEqual(15, native_events[0]["run"]["definition"]["version"])
                self.assertTrue((runner.run_directory(run_id) / "dispatch-intent.json").is_file())
                self.assertFalse((runner.run_directory(run_id) / "accepted.json").exists())
                with patch.object(native, "subject_update_action", side_effect=AssertionError("interrupted effect replayed")):
                    retained = runner.dispatch(frozen)
                self.assertEqual("recording_pending", retained["disposition"])
                self.assertEqual("interrupted_pending", retained["outcome"])
                self.assertIn("no replay", retained["reason"])
                self.assertEqual(current, self.fixture.path.read_bytes())
                self.assertEqual(self.fixture.before, self.fixture.archive.read_bytes())

    def test_post_effect_recording_failure_retains_actual_effects_and_never_replays(self):
        runner, frozen, confirmation = self.confirmed_execution("subject-private-recording-pending")
        original = work_journal.append_sealed_events

        def fail_child_terminal(root, events, *args, **kwargs):
            event = events[0]
            if event["event"] == "completed" and event.get("run", {}).get("definition", {}).get("atom_id") == "CA-O-030":
                raise OSError("fixture post-effect terminal recording failure")
            return original(root, events, *args, **kwargs)

        with patch.object(work_journal, "append_sealed_events", side_effect=fail_child_terminal):
            result, applied = self.observe_confirmed(runner, frozen, confirmation)
        self.assertEqual("applied", applied["outcome"])
        self.assertEqual("recording_pending", result["disposition"])
        self.assertEqual(self.fixture.before, self.fixture.archive.read_bytes())
        self.assertEqual(self.fixture.target["version"] + 1, applied["observed"]["version"])
        self.assert_no_replay(runner, frozen, result)


if __name__ == "__main__":
    unittest.main()
