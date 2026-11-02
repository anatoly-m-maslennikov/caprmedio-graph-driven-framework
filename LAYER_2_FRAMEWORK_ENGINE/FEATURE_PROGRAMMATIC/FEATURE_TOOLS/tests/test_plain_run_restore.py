"""Raw Journal rows restore Run state without receipts or deduplication."""

from __future__ import annotations

from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock


TOOLS = Path(__file__).resolve().parents[1]
for location in (TOOLS, TOOLS / "tests"):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

import test_selected_run_recovery as fixture_module  # noqa: E402
import selected_run_recovery  # noqa: E402
from workflow_run_support import RunExecutionSession  # noqa: E402


class PlainRunRestoreTests(unittest.TestCase):
    def test_raw_started_and_completed_rows_restore_terminal_run(self) -> None:
        fixture = fixture_module.SelectedRunRecoveryTest()
        request = fixture._request()
        events = fixture._events(request)

        session = RunExecutionSession.restore(object(), request, events + [events[-1]])

        self.assertEqual({"workflow-1660", "action-1660"}, set(session.actual))
        self.assertEqual({"workflow-1660", "action-1660"}, set(session.terminal))
        self.assertEqual("completed", session.terminal["workflow-1660"]["outcome"])

    def test_missing_raw_event_id_remains_unknown(self) -> None:
        fixture = fixture_module.SelectedRunRecoveryTest()
        request = fixture._request()
        events = [
            {key: value for key, value in event.items() if key != "event_id"}
            for event in fixture._events(request)
        ]

        session = RunExecutionSession.restore(
            type("Tracker", (), {"journal_context": {"author": "fixture"}})(), request, events
        )

        self.assertIsNone(session.read_recorded_action_start("actual-action-1660").event_id)

    def test_foreign_request_with_same_action_and_definitions_does_not_restore_terminal(
        self,
    ) -> None:
        fixture = fixture_module.SelectedRunRecoveryTest()
        request = fixture._request()
        foreign = [
            {**event, "llm_session": {"uuid": "another-request"}}
            for event in fixture._events(request)
        ]
        wrong_action = [
            {**event, "action_id": "another-action"} for event in fixture._events(request)
        ]
        with (
            tempfile.TemporaryDirectory() as temporary,
            mock.patch.object(
                selected_run_recovery,
                "inspect_selected_run_dispatch",
                return_value={"state": "accepted"},
            ),
            mock.patch.object(
                selected_run_recovery.work_journal,
                "read_records",
                return_value=foreign + wrong_action,
            ),
        ):
            evidence = selected_run_recovery.read_selected_run_evidence(temporary, request)
        self.assertEqual([], evidence["events"])
        session = RunExecutionSession.restore(object(), request, evidence["events"])
        self.assertEqual({}, session.actual)
        self.assertEqual({}, session.terminal)

    def test_exact_request_rows_remain_ordinary_duplicate_observations(self) -> None:
        fixture = fixture_module.SelectedRunRecoveryTest()
        request = fixture._request()
        events = fixture._events(request)
        with (
            tempfile.TemporaryDirectory() as temporary,
            mock.patch.object(
                selected_run_recovery,
                "inspect_selected_run_dispatch",
                return_value={"state": "accepted"},
            ),
            mock.patch.object(
                selected_run_recovery.work_journal,
                "read_records",
                return_value=events + [events[-1]],
            ),
        ):
            evidence = selected_run_recovery.read_selected_run_evidence(temporary, request)
        self.assertEqual(events + [events[-1]], evidence["events"])


if __name__ == "__main__":
    unittest.main()
