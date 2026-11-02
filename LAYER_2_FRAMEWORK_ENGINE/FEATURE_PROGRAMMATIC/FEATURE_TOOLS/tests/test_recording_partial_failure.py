"""Partial Journal recording remains visible at the append boundary."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


TOOLS = Path(__file__).resolve().parents[1]
APPENDER = TOOLS / "APPEND_CHANGE_RECORDS"
TEST_TEMP_ROOT = TOOLS.parents[2] / ".caprmedio_tmp" / "tests" / "recording_partial_failure"
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)
for directory in (TOOLS, APPENDER):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))

import append_change_records as appender  # noqa: E402
import work_journal as journal  # noqa: E402


class RecordingPartialFailureTests(unittest.TestCase):
    def test_append_returns_known_receipts_and_unknown_current_row(self) -> None:
        with tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT) as directory:
            root = Path(directory)
            control = root / ".caprmedio_caprmedio"
            control.mkdir()
            (control / "caprmedio_project_settings.toml").write_text(
                '[paths]\ncontrol_root = ".caprmedio_caprmedio"\n'
                'journal_root = ".caprmedio_caprmedio/_journal"\n',
                encoding="utf-8",
            )
            context = {
                "author": "test-user",
                "local_date": "2026-10-21",
                "timezone": "UTC",
                "predictions": {"journal_records": [{"row": 1}, {"row": 2}]},
            }
            original = journal._append_event
            calls = 0

            def append_then_fail(*args: object, **kwargs: object) -> dict[str, object]:
                nonlocal calls
                calls += 1
                if calls == 2:
                    raise OSError("fixture write failure")
                return original(*args, **kwargs)

            with patch.object(journal, "_append_event", side_effect=append_then_fail):
                result = appender.create_adapter(root).invoke({"context": context, "apply": True})

            self.assertFalse(result["ok"])
            self.assertEqual("incomplete", result["result"]["state"])
            self.assertTrue(result["result"]["incomplete"])
            self.assertEqual(1, len(result["result"]["receipts"]))
            self.assertEqual("journal-append-incomplete", result["result"]["error"]["code"])
            self.assertEqual(
                {"record_index": 1, "state": "unknown"},
                result["result"]["uncertain"],
            )
            self.assertEqual([{"row": 1}], journal.read_records(root))



if __name__ == "__main__":
    unittest.main()
