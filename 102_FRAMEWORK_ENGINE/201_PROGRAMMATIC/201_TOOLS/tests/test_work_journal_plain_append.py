"""Plain Journal append/read behavior, without first-change or receipt policy."""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
PROJECT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(TOOLS))

import work_journal as journal  # noqa: E402


class PlainJournalTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary_root = PROJECT / ".caprmedio_tmp/tests/work_journal_plain_append"
        temporary_root.mkdir(parents=True, exist_ok=True)
        temporary = tempfile.TemporaryDirectory(dir=temporary_root)
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        control = self.root / ".caprmedio_caprmedio"
        control.mkdir()
        (control / "caprmedio_project_settings.toml").write_text(
            '[paths]\ncontrol_root = ".caprmedio_caprmedio"\n'
            'journal_root = ".caprmedio_caprmedio/_journal"\n',
            encoding="utf-8",
        )
        self.partition = {"author": "observer", "local_date": "2026-10-14", "timezone": "UTC"}
        self.directory = control / "_journal"

    def append(self, rows: list[object]) -> list[dict]:
        return journal.append_sealed_events(self.root, rows, **self.partition)

    def test_append_and_read_preserve_input_order_and_content(self) -> None:
        rows = [{"custom": "first\nline", "nested": ["Ω", {"value": 7}]}, {"custom": "second"}]
        original = copy.deepcopy(rows)
        locations = self.append(rows)
        self.assertEqual(rows, journal.read_records(self.root))
        self.assertEqual(original, rows)
        self.assertEqual([1, 2], [row["line"] for row in locations])
        self.assertEqual([None, None], [row["event_id"] for row in locations])

    def test_later_append_extends_stored_rows_in_order(self) -> None:
        first, second = [{"value": 1}], [{"value": 2}, {"value": 3}]
        self.append(first)
        self.append(second)
        self.assertEqual(first + second, journal.read_records(self.root))

    def test_duplicate_rows_and_reused_ids_are_not_filtered(self) -> None:
        row = {"event_id": "same-id", "value": "original", "event_digest": "supplied-value"}
        changed = {**row, "value": "different"}
        self.append([row, row])
        self.append([changed])
        self.assertEqual([row, row, changed], journal.read_records(self.root))

    def test_missing_prior_history_does_not_block_append(self) -> None:
        rows = [{"action_type": "UPDATE"}, {"action_type": "MOVE+UPDATE"}]
        self.append(rows)
        self.assertEqual(rows, journal.read_records(self.root))
        self.assertFalse((self.root / ".caprmedio_runtime").exists())

    def test_read_returns_stored_json_values_without_shape_filtering(self) -> None:
        rows = [5, "stored string", ["stored", "list"], {"unknown": True}]
        self.directory.mkdir()
        (self.directory / "observer-2026-10-14-part-1.ndjson").write_text(
            "".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8"
        )
        self.assertEqual(rows, journal.read_records(self.root))

    def test_scalar_and_list_rows_append_without_shape_gate(self) -> None:
        rows = [5, "stored string", ["stored", "list"]]
        locations = self.append(rows)
        self.assertEqual(rows, journal.read_records(self.root))
        self.assertEqual([None] * len(rows), [row["event_id"] for row in locations])

    def test_partition_components_stay_inside_selected_journal_directory(self) -> None:
        row = {"author": "team/operator", "value": "unchanged"}
        locations = journal.append_sealed_events(
            self.root, [row], author=row["author"], local_date="2026/10/14", timezone="UTC"
        )
        path = self.root / locations[0]["carrier"]
        self.assertEqual(self.directory, path.parent)
        self.assertIn("team%2Foperator-2026%2F10%2F14", path.name)
        self.assertEqual([row], journal.read_records(self.root))

    def test_empty_read_creates_no_journal_files(self) -> None:
        self.assertEqual([], journal.read_records(self.root))
        self.assertFalse(self.directory.exists())

    def test_declared_row_rotation_preserves_append_order(self) -> None:
        rows = [{"row": number} for number in range(1001)]
        locations = self.append(rows)
        self.assertEqual(rows, journal.read_records(self.root))
        self.assertEqual((1000, 1), (locations[999]["line"], locations[1000]["line"]))
        self.assertNotEqual(locations[999]["carrier"], locations[1000]["carrier"])

    def test_numeric_parts_read_in_numeric_order(self) -> None:
        self.directory.mkdir()
        for number in range(1, 13):
            (self.directory / f"observer-2026-10-14-part-{number}.ndjson").write_text(
                json.dumps({"part": number}) + "\n", encoding="utf-8"
            )
        self.assertEqual(
            [{"part": number} for number in range(1, 13)], journal.read_records(self.root)
        )

    def test_leaf_symlink_cannot_read_or_append_outside_journal(self) -> None:
        self.directory.mkdir()
        outside = self.root / "outside.ndjson"
        original = b'{"outside": "unchanged"}\n'
        outside.write_bytes(original)
        (self.directory / "observer-2026-10-14-part-1.ndjson").symlink_to(outside)
        for operation in (
            lambda: journal.read_records(self.root),
            lambda: self.append([{"new": True}]),
        ):
            with self.subTest(operation=operation), self.assertRaises(OSError):
                operation()
            self.assertEqual(original, outside.read_bytes())

    def test_actual_filesystem_failure_is_reported(self) -> None:
        self.directory.write_text("occupied by a file", encoding="utf-8")
        with self.assertRaises(OSError):
            self.append([{"value": "not appended"}])
        self.assertEqual("occupied by a file", self.directory.read_text(encoding="utf-8"))

    def test_actual_dispatch_does_not_require_available_journal(self) -> None:
        self.directory.write_text("not a Journal directory", encoding="utf-8")
        arguments = {"request_id": "actual-request", "canonical_request_bytes": b'{"input":"exact"}'}
        observed, accepted = journal.register_selected_run_dispatch(self.root, **arguments)
        self.assertTrue(accepted)
        self.assertEqual("accepted", observed["state"])
        repeated, accepted = journal.register_selected_run_dispatch(self.root, **arguments)
        self.assertFalse(accepted)
        self.assertEqual(observed, repeated)
        with self.assertRaises(journal.WorkJournalError):
            journal.register_selected_run_dispatch(self.root, **{**arguments, "canonical_request_bytes": b'{"input":"other"}'})
        self.assertTrue(list((self.root / ".caprmedio_runtime/state/work_journal/selected_runs/requests").glob("*.json")))
        self.assertEqual("not a Journal directory", self.directory.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
