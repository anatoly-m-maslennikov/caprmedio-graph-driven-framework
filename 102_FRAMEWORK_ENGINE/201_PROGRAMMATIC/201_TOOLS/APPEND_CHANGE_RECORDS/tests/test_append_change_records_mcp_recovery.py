"""Project-bound MCP append checks using the actual Journal writer."""

import hashlib
import json
import unittest
from unittest.mock import patch

from append_mcp_test_support import AppendMcpFixture, appender, work_journal


class AppendMcpRecoveryTest(AppendMcpFixture, unittest.TestCase):
    def test_actual_partial_append_is_pending_and_retry_does_not_replay_source(self) -> None:
        context = self._recovery_context()
        events = context["predictions"]["journal_records"]
        original = work_journal._append_locked
        artifact = self.fixture.artifact.read_bytes()

        def fail_second(root, event, *args, **kwargs):
            if event["event_id"] == events[1]["event_id"]:
                raise OSError("injected second-event storage failure")
            return original(root, event, *args, **kwargs)

        with patch.object(work_journal, "_append_locked", side_effect=fail_second):
            result = self._apply(context)
        self.assertFalse(result["ok"])
        self.assertEqual("recording_pending", result["result"]["state"])
        self.assertEqual([events[0]], self._events())
        self.assertEqual(events[0]["event_digest"], result["result"]["receipts"][0]["event_digest"])
        pending = list((self.root / ".caprmedio_runtime/state/work_journal/pending").glob("*.json"))
        self.assertTrue(pending)
        self.assertIn(
            events[1], [json.loads(json.loads(path.read_text())["event_bytes"]) for path in pending]
        )
        with patch.object(appender, "run", side_effect=AssertionError("source workflow replayed")):
            retried = self._apply(context)
        self.assertTrue(retried["ok"])
        self.assertEqual(events, self._events())
        self.assertEqual(artifact, self.fixture.artifact.read_bytes())
        self.assertEqual(
            [], list((self.root / ".caprmedio_runtime/state/work_journal/pending").glob("*.json"))
        )

    def test_receipt_write_failure_retains_observed_append_and_retry_clears_pending(self) -> None:
        context = self._context(replacement=True)
        event = context["predictions"]["journal_records"][0]
        receipt_path = work_journal._receipt_path(self.root, event["event_id"])
        original = work_journal._atomic_json
        artifact = self.fixture.artifact.read_bytes()

        def fail_receipt(path, value):
            if path == receipt_path:
                raise OSError("injected receipt write failure after carrier append")
            return original(path, value)

        with patch.object(work_journal, "_atomic_json", side_effect=fail_receipt):
            result = self._apply(context)
        self.assertFalse(result["ok"])
        self.assertEqual("recording_pending", result["result"]["state"])
        self.assertEqual([event], self._events())
        receipts = result["result"]["receipts"]
        self.assertEqual(1, len(receipts))
        payload = work_journal.canonical_json_bytes(event) + b"\n"
        self.assertEqual(
            {
                "event_id": event["event_id"],
                "action_id": event["action_id"],
                "event_digest": event["event_digest"],
                "carrier": ".caprmedio_caprmedio/_journal/test-user-2026-08-20-part-1.ndjson",
                "line": 1,
                "previous_carrier_digest": hashlib.sha256(b"").hexdigest(),
                "appended_carrier_digest": hashlib.sha256(payload).hexdigest(),
            },
            receipts[0],
        )
        self.assertEqual(payload, (self.root / receipts[0]["carrier"]).read_bytes())
        self.assertEqual(
            event["event_digest"], result["result"]["pending_events"][0]["event_digest"]
        )
        pending_dir = self.root / ".caprmedio_runtime/state/work_journal/pending"
        self.assertEqual(1, len(list(pending_dir.glob("*.json"))))
        with patch.object(appender, "run", side_effect=AssertionError("source workflow replayed")):
            retried = self._apply(context)
        self.assertTrue(retried["ok"])
        self.assertEqual([event], self._events())
        self.assertEqual(artifact, self.fixture.artifact.read_bytes())
        self.assertEqual([], list(pending_dir.glob("*.json")))

    def test_unsafe_settings_after_first_append_preserve_partial_receipt_and_refuse_outside_write(
        self,
    ) -> None:
        context = self._recovery_context()
        events = context["predictions"]["journal_records"]
        settings = self.root / ".caprmedio_caprmedio/caprmedio_project_settings.toml"
        original_settings = settings.read_bytes()
        original_recover = appender.recover_pending_event
        first_receipts = []
        outside = self.root.parent / "outside"
        self.assertFalse(outside.exists())
        artifact = self.fixture.artifact.read_bytes()

        def invalidate_settings_after_first(root, event_id):
            receipt = original_recover(root, event_id)
            if event_id == events[0]["event_id"]:
                first_receipts.append(receipt)
                settings.write_bytes(
                    original_settings.replace(
                        b'journal_root = ".caprmedio_caprmedio/_journal"',
                        b'journal_root = "../outside"',
                    )
                )
            return receipt

        with patch.object(
            appender, "recover_pending_event", side_effect=invalidate_settings_after_first
        ):
            result = self._apply(context)
        self.assertFalse(result["ok"])
        self.assertEqual("recording_pending", result["result"]["state"])
        self.assertEqual(first_receipts, result["result"]["receipts"])
        self.assertEqual(1, len(first_receipts))
        self.assertEqual(events[0]["event_digest"], first_receipts[0]["event_digest"])
        self.assertTrue(result["result"]["inspection_required"])
        self.assertTrue(result["result"]["pending_errors"])
        self.assertEqual([events[0]], self._events())
        self.assertFalse(outside.exists())
        settings.write_bytes(original_settings)
        with patch.object(appender, "run", side_effect=AssertionError("source workflow replayed")):
            retried = self._apply(context)
        self.assertTrue(retried["ok"])
        self.assertEqual(events, self._events())
        self.assertEqual(artifact, self.fixture.artifact.read_bytes())
        self.assertFalse(outside.exists())
        self.assertEqual(
            [], list((self.root / ".caprmedio_runtime/state/work_journal/pending").glob("*.json"))
        )


if __name__ == "__main__":
    unittest.main()
