# CA-E-676@8
# CA-M-472@1

"""Project-Journal saved-query records retain legacy-file access."""

from contextlib import redirect_stderr
from io import StringIO
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
