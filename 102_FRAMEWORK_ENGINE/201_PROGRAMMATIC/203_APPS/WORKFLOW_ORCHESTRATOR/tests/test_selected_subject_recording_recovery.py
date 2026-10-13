"""Actual recording-only repair after a real selected Subject publication."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

APP = Path(__file__).resolve().parents[1]
TOOLS = APP.parent.parent / "201_TOOLS"
for location in (TOOLS / "ATOM_UPDATE/tests", TOOLS, APP):
    sys.path.insert(0, str(location))

import atom_subject_apply as native
import atom_operations as operations
import work_journal
from test_subject_apply_portfolio import SubjectApplyProject
from workflow_run_support import RunExecutionSession


def canonical_bytes(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"),
                      allow_nan=False).encode("utf-8")


def carrier_snapshot(path):
    observed = path.lstat()
    return (path.read_bytes(), observed.st_dev, observed.st_ino, observed.st_mode,
            observed.st_mtime_ns, observed.st_ctime_ns)


class SelectedSubjectRecordingRecoveryTests(unittest.TestCase):
    def setUp(self):
        scratch = TOOLS.parents[2] / ".caprmedio_tmp/tests/test_selected_subject_recording_recovery"
        scratch.mkdir(parents=True, exist_ok=True)
        self.directory = tempfile.TemporaryDirectory(prefix="recording-repair-", dir=scratch,
                                                     ignore_cleanup_errors=True)
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.fixture = SubjectApplyProject(self.root)

    def test_real_pending_terminal_event_is_recovered_without_subject_republication(self):
        runner, frozen = self.fixture.execution("subject-recording-only-repair")
        confirmation = self.fixture.confirmation(frozen)
        real_publish = native.subject_update_action
        real_append = work_journal.append_sealed_events
        publications, failed_events = [], []

        def observe_publication(root, parameters, **kwargs):
            result = real_publish(root, parameters, **kwargs)
            if kwargs.get("execute") is True:
                publications.append((kwargs["session"], kwargs["action_run_id"], result))
            return result

        def fail_terminal(root, events, *args, **kwargs):
            event = events[0]
            if event["event"] == "completed" and event.get("run", {}).get("definition", {}).get("atom_id") == "CA-O-030":
                failed_events.append(copy.deepcopy(event))
                raise OSError("isolated post-effect terminal recording failure")
            return real_append(root, events, *args, **kwargs)

        with patch.object(native, "subject_update_action", side_effect=observe_publication), patch.object(
            work_journal, "append_sealed_events", side_effect=fail_terminal,
        ):
            result = runner._dispatch_confirmed_subject(frozen, confirmation)

        self.assertEqual(len(publications), 1)
        self.assertEqual(len(failed_events), 1)
        session, action_run_id, applied = publications[0]
        self.assertIsInstance(session, RunExecutionSession)
        self.assertEqual(applied["outcome"], "applied")
        self.assertEqual(applied["observed"]["version"], self.fixture.target["version"] + 1)
        self.assertEqual(result["disposition"], "recording_pending")
        self.assertEqual(self.fixture.archive.read_bytes(), self.fixture.before)
        current = carrier_snapshot(self.fixture.path)
        history = carrier_snapshot(self.fixture.archive)

        event = failed_events[0]
        event_id = event["event_id"]
        expected_bytes = canonical_bytes(event)
        self.assertEqual(event["run"]["run_id"], action_run_id)
        self.assertEqual(event["outcome"], "completed")
        self.assertTrue(event["effect_refs"])
        self.assertIn(event_id, result["pending_event_ids"])
        pending_path = work_journal._pending_path(self.root, event_id)
        pending = json.loads(pending_path.read_bytes())
        self.assertEqual(pending["event_bytes"].encode(), expected_bytes)
        self.assertEqual(pending["event_bytes_digest"], hashlib.sha256(expected_bytes).hexdigest())
        context = json.loads(pending["append_context_bytes"])
        journal = self.root / context["partition_ref"]
        before_journal = journal.read_bytes()
        self.assertNotIn(expected_bytes, before_journal.splitlines())
        receipt_path = work_journal._receipt_path(self.root, event_id)
        self.assertFalse(receipt_path.exists())

        with patch.object(native, "subject_update_action", side_effect=AssertionError("Subject publication replayed")) as publisher, patch.object(
            operations, "write_raw_atom_revision", side_effect=AssertionError("Atom carrier rewritten during recording repair"),
        ) as writer, patch.object(session.tracker, "executor", side_effect=AssertionError("Run executor replayed")) as executor, patch.object(
            session.tracker, "recover_recording", wraps=session.tracker.recover_recording,
        ) as tracker_recovery, patch.object(work_journal, "recover_pending_event", wraps=work_journal.recover_pending_event) as journal_recovery:
            receipt = session.recover(event_id)
            self.assertEqual(runner.dispatch(frozen), result)
        publisher.assert_not_called()
        writer.assert_not_called()
        executor.assert_not_called()
        tracker_recovery.assert_called_once_with(event_id)
        journal_recovery.assert_called_once_with(self.root, event_id)

        after_journal = journal.read_bytes()
        self.assertEqual(after_journal, before_journal + expected_bytes + b"\n")
        self.assertEqual(json.loads(after_journal.splitlines()[-1]), event)
        self.assertEqual(after_journal.splitlines().count(expected_bytes), 1)
        self.assertEqual(receipt["event_id"], event_id)
        self.assertEqual(receipt["event_digest"], event["event_digest"])
        self.assertEqual(receipt["carrier"], context["partition_ref"])
        self.assertEqual(receipt["line"], len(before_journal.splitlines()) + 1)
        self.assertEqual(receipt["previous_carrier_digest"], hashlib.sha256(before_journal).hexdigest())
        self.assertEqual(receipt["appended_carrier_digest"], hashlib.sha256(after_journal).hexdigest())
        self.assertEqual(json.loads(receipt_path.read_bytes()), receipt)
        self.assertFalse(pending_path.exists())
        self.assertEqual(carrier_snapshot(self.fixture.path), current)
        self.assertEqual(carrier_snapshot(self.fixture.archive), history)


if __name__ == "__main__":
    unittest.main()
