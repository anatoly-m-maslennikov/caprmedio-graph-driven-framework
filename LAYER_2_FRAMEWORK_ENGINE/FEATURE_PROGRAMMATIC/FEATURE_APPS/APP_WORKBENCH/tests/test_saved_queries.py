# CA-E-676@11
# CA-D-673@12
"""Project-Journal saved-query records retain legacy-file access."""

from contextlib import redirect_stderr
from io import StringIO
import json
from pathlib import Path
import sys
import tempfile
import unittest


APP_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(APP_ROOT))

from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.saved_queries import SavedQueryStore  # noqa: E402


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

    def test_invalid_journal_row_does_not_hide_valid_saved_items(self):
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

    def test_views_write_new_kind_and_historical_worksheets_read_as_views(self):
        created = self.store.save_view("SELECT 'new view'", "New view")
        self.assertEqual("view", created["kind"])
        journal = next((self.control / "_journal").glob("workbench-saved-items-*-part-1.ndjson"))
        before = journal.read_bytes()
        historical_id = "01940000-0002-7000-8000-000000000003"
        with journal.open("a", encoding="utf-8") as target:
            target.write(
                json.dumps({
                    "saved_query_id": historical_id,
                    "kind": "worksheet",
                    "sql": "SELECT 'historical worksheet'",
                    "saved_at": "2026-11-05T00:00:00+00:00",
                    "name": "Historical worksheet",
                }) + "\n"
            )
        historical_bytes = journal.read_bytes()

        loaded = self.store.load(historical_id)
        listed = {item["saved_query_id"]: item for item in self.store.list()["items"]}

        self.assertEqual("view", loaded["kind"])
        self.assertEqual("SELECT 'historical worksheet'", loaded["sql"])
        self.assertEqual("view", listed[historical_id]["kind"])
        self.assertEqual("New view", listed[created["saved_query_id"]]["name"])
        self.assertNotEqual(before, historical_bytes)
        self.assertEqual(historical_bytes, journal.read_bytes())

    def test_legacy_worksheet_file_loads_and_lists_as_a_view(self):
        legacy_id = "w_" + "a" * 32
        self.store._legacy_directory.mkdir(parents=True)
        path = self.store._legacy_directory / f"{legacy_id}.json"
        path.write_text('{"sql":"SELECT \'legacy view\'"}', encoding="utf-8")

        loaded = self.store.load(legacy_id)
        listed = {item["saved_query_id"]: item for item in self.store.list()["items"]}

        self.assertEqual({"saved_query_id": legacy_id, "kind": "view", "sql": "SELECT 'legacy view'"}, loaded)
        self.assertEqual("view", listed[legacy_id]["kind"])
