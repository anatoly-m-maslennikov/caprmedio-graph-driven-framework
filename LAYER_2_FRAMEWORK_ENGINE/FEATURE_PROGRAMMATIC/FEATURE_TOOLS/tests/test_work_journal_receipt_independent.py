"""Independent checks observe actual append locations, not cached proofs."""

from __future__ import annotations

import json
import unittest

import test_work_journal_schema_v5 as fixtures
import work_journal


class WorkJournalReceiptIndependentTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.WorkJournalSchemaV5Test(methodName="runTest")
        self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)
        self.root, self.event = self.fixture.root, self.fixture.event
        self.partition = {"author": "test-user", "local_date": "2026-10-04", "timezone": "UTC"}

    def test_locations_describe_new_rows_without_cache_or_digest_proofs(self):
        rows = [self.event, self.event, {**self.event, "result_ref": "changed"}]
        locations = work_journal.append_sealed_events(self.root, rows, **self.partition)
        self.assertEqual([1, 2, 3], [value["line"] for value in locations])
        self.assertEqual(
            {"event_id", "action_id", "event_digest", "carrier", "line"}, set(locations[0])
        )
        self.assertEqual(rows, work_journal.read_records(self.root))
        self.assertFalse((self.root / ".caprmedio_runtime").exists())

    def test_existing_spacing_and_key_order_remain_untouched(self):
        first = work_journal.append_sealed_events(self.root, [self.event], **self.partition)[0]
        carrier = self.root / first["carrier"]
        original = json.dumps(self.event, sort_keys=False, separators=(", ", ": ")).encode() + b"\n"
        carrier.write_bytes(original)
        work_journal.append_sealed_events(self.root, [{"unknown": True}], **self.partition)
        self.assertTrue(carrier.read_bytes().startswith(original))
        self.assertEqual([self.event, {"unknown": True}], work_journal.read_records(self.root))

    def test_actual_deleted_file_is_not_reconstructed_from_a_receipt(self):
        location = work_journal.append_sealed_events(self.root, [self.event], **self.partition)[0]
        (self.root / location["carrier"]).unlink()
        self.assertEqual([], work_journal.read_records(self.root))
        work_journal.append_sealed_events(self.root, [{"new": True}], **self.partition)
        self.assertEqual([{"new": True}], work_journal.read_records(self.root))


if __name__ == "__main__":
    unittest.main()
