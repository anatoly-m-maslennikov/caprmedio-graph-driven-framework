# CA-E-676@8

"""Project-Journal saved-query records retain legacy-file access."""

from contextlib import redirect_stderr
from io import StringIO
import json
from pathlib import Path
import sys
import tempfile
import unittest
import uuid
from unittest.mock import patch


APP_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(APP_ROOT))

from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.saved_queries import SavedQueryStore  # noqa: E402


_UUID7 = uuid.UUID("01940000-0000-7000-8000-000000000001")


def _settings(root: Path) -> Path:
    control = root / ".caprmedio_demo"
    control.mkdir()
    (control / "caprmedio_project_settings.toml").write_text(
        '[project]\nname = "demo"\n[paths]\ncontrol_root = ".caprmedio_demo"\n'
        'journal_root = ".caprmedio_demo/_journal"\nruntime_root = ".caprmedio_runtime"\n',
        encoding="utf-8",
    )
    return control


class SavedQueryTests(unittest.TestCase):
    def setUp(self) -> None:
        self._temporary = tempfile.TemporaryDirectory(dir=Path.cwd())
        self.root = Path(self._temporary.name)
        self.control = _settings(self.root)
        self.store = SavedQueryStore(self.root)

    def tearDown(self) -> None:
        self._temporary.cleanup()

    def test_query_and_worksheet_append_uuid7_records_with_optional_names(self):
        with patch(
            "APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.saved_queries.uuid.uuid7",
            side_effect=[_UUID7, uuid.UUID("01940000-0001-7000-8000-000000000002")],
        ):
            query = self.store.save_query("SELECT 'λ'", "Saved query")
            worksheet = self.store.save_worksheet("SELECT 1; SELECT 2", "   ")

        self.assertEqual(str(_UUID7), query["saved_query_id"])
        self.assertEqual("Saved query", query["name"])
        self.assertNotIn("name", worksheet)
        journal = next((self.control / "_journal").glob("workbench-saved-items-*-part-1.ndjson"))
        rows = [json.loads(line) for line in journal.read_text(encoding="utf-8").splitlines()]
        self.assertEqual([query, worksheet], rows)
        self.assertEqual(query, self.store.load(query["saved_query_id"]))
        self.assertEqual(worksheet, self.store.load(
            f"http://127.0.0.1/workbench?query={worksheet['saved_query_id']}"
        ))

    def test_legacy_files_remain_read_only_load_and_list_fallback(self):
        directory = self.root / ".caprmedio_runtime" / "workbench" / "saved_queries"
        directory.mkdir(parents=True)
        query_id, worksheet_id = "q_" + "1" * 32, "w_" + "2" * 32
        (directory / f"{query_id}.sql").write_text("SELECT 1", encoding="utf-8")
        (directory / f"{worksheet_id}.json").write_text('{"sql":"SELECT 2"}', encoding="utf-8")

        self.assertEqual(
            {"saved_query_id": query_id, "kind": "query", "sql": "SELECT 1"},
            self.store.load(query_id),
        )
        listed = self.store.list()
        self.assertEqual({query_id, worksheet_id}, {item["saved_query_id"] for item in listed["items"]})
        self.assertTrue(all("name" not in item for item in listed["items"]))

    def test_invalid_journal_row_does_not_hide_valid_saved_items(self):
        with patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.saved_queries.uuid.uuid7", return_value=_UUID7):
            query = self.store.save_query("SELECT 1")
        journal = next((self.control / "_journal").glob("workbench-saved-items-*-part-1.ndjson"))
        with journal.open("a", encoding="utf-8") as target:
            target.write(
                '{"saved_query_id":"01940000-0002-7000-8000-000000000003",'
                '"kind":[],"sql":"SELECT 2","saved_at":"2026-11-05T00:00:00+00:00"}\n'
            )

        with redirect_stderr(StringIO()) as errors:
            listed = self.store.list()

        self.assertEqual([query["saved_query_id"]], [item["saved_query_id"] for item in listed["items"]])
        self.assertIn("saved query skipped", errors.getvalue())
        with self.assertRaisesRegex(ValueError, "name"):
            self.store.save_query("SELECT 1", 1)
        with self.assertRaisesRegex(ValueError, "limit"):
            self.store.list(0)
