# CA-E-676@7

"""Immutable local saved-query carriers survive a Workbench restart."""

from contextlib import redirect_stderr
from io import StringIO
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch


APP_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(APP_ROOT))

from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.saved_queries import SavedQueryStore  # noqa: E402


class _Uuid:
    hex = "1" * 32


class SavedQueryTests(unittest.TestCase):
    def setUp(self) -> None:
        self._temporary = tempfile.TemporaryDirectory()
        self.root = Path(self._temporary.name)
        self.store = SavedQueryStore(self.root)

    def tearDown(self) -> None:
        self._temporary.cleanup()

    def test_query_and_worksheet_are_exact_immutable_utf8_files(self):
        query = self.store.save_query("SELECT 'λ'")
        worksheet = self.store.save_worksheet("SELECT 1; SELECT 2")
        directory = self.root / ".caprmedio_runtime" / "workbench" / "saved_queries"

        self.assertEqual("query", query["kind"])
        self.assertEqual("SELECT 'λ'", (directory / f"{query['saved_query_id']}.sql").read_text())
        self.assertEqual({"sql": "SELECT 1; SELECT 2"}, json.loads(
            (directory / f"{worksheet['saved_query_id']}.json").read_text()
        ))
        self.assertEqual(query, self.store.load(query["saved_query_id"]))
        self.assertEqual(worksheet, self.store.load(f"http://127.0.0.1/workbench?query={worksheet['saved_query_id']}"))

        with patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.saved_queries.uuid.uuid4", return_value=_Uuid()):
            first = self.store.save_query("SELECT 3")
            with self.assertRaisesRegex(ValueError, "saved query failed"):
                self.store.save_query("SELECT 4")
        self.assertEqual("SELECT 3", self.store.load(first["saved_query_id"])["sql"])

    def test_restart_list_and_bad_file_do_not_change_valid_saved_queries(self):
        first = self.store.save_query("SELECT 1")
        second = self.store.save_worksheet("SELECT 2; SELECT 3")
        directory = self.root / ".caprmedio_runtime" / "workbench" / "saved_queries"
        (directory / "w_bad.json").write_text("not json")
        restarted = SavedQueryStore(self.root)

        with redirect_stderr(StringIO()) as errors:
            listed = restarted.list()

        self.assertEqual({first["saved_query_id"], second["saved_query_id"]}, {
            row["saved_query_id"] for row in listed["items"]
        })
        self.assertIn("saved query skipped", errors.getvalue())
        self.assertEqual(first, restarted.load(first["saved_query_id"]))
        self.assertEqual(second, restarted.load(second["saved_query_id"]))
        with redirect_stderr(StringIO()):
            self.assertEqual(1, len(restarted.list(1)["items"]))
        with self.assertRaisesRegex(ValueError, "limit"):
            restarted.list(0)
        with self.assertRaisesRegex(ValueError, "reference"):
            restarted.load("https://elsewhere.invalid/?query=bad")
