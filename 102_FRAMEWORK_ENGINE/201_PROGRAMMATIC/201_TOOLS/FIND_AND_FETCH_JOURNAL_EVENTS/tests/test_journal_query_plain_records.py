"""The existing query transport reads plain rows without certifying them."""

import json
import unittest

import test_find_and_fetch_journal_events as fixtures
from find_and_fetch_journal_events import JournalQueryResult, create_adapter


class PlainJournalQueryTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.JournalQueryGoldenTest(
            "test_e575_typed_pointer_filtering_missing_vs_null_and_rejections"
        )
        self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)
        self.root = self.fixture.root

    def all_values(self, snapshot, limit=2):
        values = []
        request = {"mode": "full_events", "limit": limit}
        while True:
            result = fixtures.query(snapshot, request)
            JournalQueryResult.model_validate(result)
            values.extend(item["event"] for item in result["results"])
            if result["next_cursor"] is None:
                return values, result
            request["cursor"] = result["next_cursor"]

    def test_duplicate_ids_and_unverified_metadata_remain_distinct_rows(self):
        rows = [
            {"event_id": "same", "event_digest": "wrong", "value": 1},
            {"event_id": "same", "event_digest": "different", "value": 2},
        ]
        self.fixture.write_events("plain.ndjson", *rows)
        snapshot = fixtures.capture_snapshot(self.root)
        values, result = self.all_values(snapshot, limit=1)
        self.assertEqual(rows, values)
        self.assertEqual(["same", "same"], snapshot["event_ids"])
        self.assertEqual(2, result["coverage"]["scanned"])

    def test_absent_and_nonstring_ids_preserve_arbitrary_json_values(self):
        rows = [{"value": 1}, {"event_id": 17}, [1, None], "text", None]
        self.fixture.write_events("plain.ndjson", *rows)
        snapshot = fixtures.capture_snapshot(self.root)
        values, result = self.all_values(snapshot)
        self.assertEqual(rows, values)
        self.assertEqual([], snapshot["event_ids"])
        self.assertEqual(5, result["coverage"]["scanned"])
        self.assertEqual([None, None], fixtures.query(snapshot, {})["results"])

    def test_direct_adapter_result_schema_accepts_missing_id(self):
        self.fixture.write_events("plain.ndjson", [1, 2])
        result = create_adapter(self.root).invoke({"mode": "full_events"})
        self.assertEqual([{"event_id": None, "event": [1, 2]}], result.results)

    def test_blank_lines_and_normal_duplicate_key_decoding_do_not_gate_read(self):
        path = self.fixture.journal / "plain.ndjson"
        original = b'\n{"event_id":"old","event_id":"new"}\n\n'
        path.write_bytes(original)
        result = fixtures.query(fixtures.capture_snapshot(self.root), {"mode": "full_events"})
        self.assertEqual([{"event_id": "new", "event": {"event_id": "new"}}], result["results"])
        self.assertEqual(original, path.read_bytes())

    def test_filter_and_snapshot_pagination_keep_original_duplicate_rows(self):
        rows = [{"event_id": "same", "value": value} for value in (1, 2)]
        path = self.fixture.write_events("plain.ndjson", *rows)
        snapshot = fixtures.capture_snapshot(self.root)
        result = fixtures.query(snapshot, {"filter": '"event:/value" = 2', "mode": "full_events"})
        self.assertEqual([{"event_id": "same", "event": rows[1]}], result["results"])
        with path.open("ab") as stream:
            stream.write(json.dumps({"event_id": "later"}).encode() + b"\n")
        values, _ = self.all_values(snapshot, limit=1)
        self.assertEqual(rows, values)


if __name__ == "__main__":
    unittest.main()
