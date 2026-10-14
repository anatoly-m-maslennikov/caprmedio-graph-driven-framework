"""Plain append transport; no Journal validation or deduplication."""

from pathlib import Path
import unittest
from unittest.mock import patch

from pydantic import ValidationError

from append_mcp_test_support import AppendMcpFixture, appender


class AppendChangeRecordsMcpTest(AppendMcpFixture, unittest.TestCase):
    def test_default_dry_run_creates_no_recording_state(self):
        context = self._context()
        with patch.object(appender, "append_sealed_events", side_effect=AssertionError("append")):
            result = self.adapter.invoke({"context": context})
        self.assertEqual("dry-run", result["mode"])
        self.assertEqual(
            context["predictions"]["journal_records"],
            result["result"]["planned_effects"]["journal_records"],
        )
        self.assertEqual([], result["result"]["receipts"])
        self.assertFalse((self.root / ".caprmedio_runtime").exists())
        self.assertEqual([], self._events())

    def test_every_call_appends_even_identical_or_conflicting_ids(self):
        context = self._context()
        first = self._apply(context)
        second = self._apply(context)
        self._apply(self._context([{"event_id": "event-one", "different": True}]))
        self.assertEqual(3, len(self._events()))
        self.assertEqual(1, first["result"]["receipts"][0]["line"])
        self.assertEqual(2, second["result"]["receipts"][0]["line"])
        self.assertFalse((self.root / ".caprmedio_runtime").exists())

    def test_rows_are_caller_data_without_required_fields_or_checks(self):
        records = [
            {},
            {"event_id": False, "event_digest": "wrong", "previous_result_event": "unknown"},
            None,
            5,
        ]
        result = self._apply(self._context(records))
        self.assertEqual(records, self._events())
        self.assertEqual(False, result["result"]["receipts"][1]["event_id"])
        self.assertEqual("wrong", result["result"]["receipts"][1]["event_digest"])
        self.assertIsNone(result["result"]["receipts"][2]["event_id"])

    def test_context_root_is_data_not_an_append_destination(self):
        context = self._context()
        context["trigger"] = {"repository": {"root": "../somewhere"}}
        self._apply(context)
        self.assertEqual(context["predictions"]["journal_records"], self._events())

    def test_constructor_has_no_io_and_factory_binds_native_module(self):
        with patch.object(Path, "resolve", side_effect=AssertionError("constructor I/O")):
            adapter = appender.AppendChangeRecordsAdapter(Path("unopened"), appender)
        self.assertEqual(Path("unopened"), adapter.root)
        self.assertIs(appender, self.adapter.native)

    def test_closed_transport_and_literal_apply_preserve_existing_api(self):
        requests = [{}] + [
            {"context": self._context(), "apply": value} for value in (1, "true", None)
        ]
        requests += [{"context": self._context(), "root": str(self.root)}]
        for request in requests:
            with self.subTest(request=request):
                with self.assertRaises(ValidationError):
                    appender.AppendChangeRecordsRequest.model_validate(request)
        self.assertEqual([], self._events())

    def test_descriptor_does_not_claim_idempotent_appends(self):
        descriptor = appender.describe_tool()
        self.assertFalse(descriptor["effect_hints"]["idempotent_hint"])

    def test_partial_io_failure_does_not_create_recovery_or_retry(self):
        context = self._context([{"first": True}, {"second": True}])
        append = appender.append_sealed_events
        calls = []

        def fail_after_first(root, rows, **partition):
            calls.append(rows)
            append(root, rows[:1], **partition)
            raise OSError("ordinary write failure")

        with patch.object(appender, "append_sealed_events", side_effect=fail_after_first):
            with self.assertRaisesRegex(OSError, "ordinary write failure"):
                self._apply(context)
        self.assertEqual(1, len(calls))
        self.assertEqual([{"first": True}], self._events())
        self.assertFalse((self.root / ".caprmedio_runtime").exists())


if __name__ == "__main__":
    unittest.main()
