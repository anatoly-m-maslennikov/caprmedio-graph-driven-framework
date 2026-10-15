"""Logging failure preserves real selected Subject effects without replay."""

from __future__ import annotations

import copy
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

    def test_terminal_logging_failure_preserves_subject_publication_without_replay(self):
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
        self.assertEqual(result["disposition"], "terminal")
        self.assertIn("isolated post-effect terminal recording failure", result["diagnostics"])
        self.assertEqual(self.fixture.archive.read_bytes(), self.fixture.before)
        current = carrier_snapshot(self.fixture.path)
        history = carrier_snapshot(self.fixture.archive)

        event = failed_events[0]
        self.assertEqual(event["run"]["run_id"], action_run_id)
        self.assertEqual(event["outcome"], "completed")
        self.assertTrue(event["effect_refs"])
        terminal = next(row for row in result["terminal_runs"] if row["run_id"] == action_run_id)
        self.assertEqual("terminal", terminal["disposition"])
        self.assertEqual("completed", terminal["outcome"])
        self.assertEqual("isolated post-effect terminal recording failure", terminal["recording_error"])
        self.assertEqual(event["effect_refs"], terminal["effect_refs"])
        retained = json.loads((self.root / terminal["result_ref"]).read_bytes())
        self.assertEqual(applied, retained["native_result"])
        rows = work_journal.read_records(self.root)
        self.assertNotIn(event, rows)

        with patch.object(native, "subject_update_action", side_effect=AssertionError("Subject publication replayed")) as publisher, patch.object(
            operations, "write_raw_atom_revision", side_effect=AssertionError("Atom carrier rewritten on repeat dispatch"),
        ) as writer, patch.object(session.tracker, "executor", side_effect=AssertionError("Run executor replayed")) as executor, patch.object(
            work_journal, "append_sealed_events", side_effect=AssertionError("Journal append retried"),
        ) as append:
            self.assertEqual(runner.dispatch(frozen), result)
        publisher.assert_not_called()
        writer.assert_not_called()
        executor.assert_not_called()
        append.assert_not_called()
        self.assertEqual(rows, work_journal.read_records(self.root))
        self.assertEqual(carrier_snapshot(self.fixture.path), current)
        self.assertEqual(carrier_snapshot(self.fixture.archive), history)


if __name__ == "__main__":
    unittest.main()
