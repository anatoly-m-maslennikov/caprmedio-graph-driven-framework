# CA-M-502@1
# CA-D-698@2
# CA-E-787@6
from __future__ import annotations

import datetime as dt
from contextlib import redirect_stderr
from io import StringIO
import json
from pathlib import Path
import sys
import tempfile
import threading
import time
import unittest
from unittest.mock import patch


APP_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(APP_ROOT))

from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.query_log import QueryLog  # noqa: E402


class QueryLogTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.log = QueryLog(Path(self.temporary.name))
        self.addCleanup(self.log.close)
        self.result = {"status": "success", "error": None, "row_count": 1, "column_count": 1}

    def test_append_uses_utc_hour_files_and_the_exact_record_shape(self) -> None:
        first = dt.datetime(2026, 11, 5, 10, 59, tzinfo=dt.UTC)
        second = dt.datetime(2026, 11, 5, 11, tzinfo=dt.UTC)
        with patch.object(QueryLog, "_now", side_effect=[first, second, second]):
            older = self.log.append("SELECT 1", self.result)
            newer = self.log.append("SELECT 2", self.result)
            records = self.log.list()["items"]

        self.assertEqual([newer, older], records)
        self.assertEqual(
            {"log_id", "at", "sql", "outcome", "error", "row_count", "column_count"},
            set(newer),
        )
        self.assertTrue(self.log._hour_path(first).is_file())
        self.assertTrue(self.log._hour_path(second).is_file())
        self.assertEqual(newer, json.loads(self.log._hour_path(second).read_text(encoding="utf-8")))

    def test_retention_keeps_legacy_bytes_unchanged(self) -> None:
        now = dt.datetime(2026, 11, 5, 12, tzinfo=dt.UTC)
        current = {"log_id": "current", "at": (now - dt.timedelta(hours=47)).isoformat(), "sql": "SELECT current", "outcome": "success", "error": None, "row_count": 1, "column_count": 1}
        expired = {"log_id": "expired", "at": (now - dt.timedelta(hours=48)).isoformat(), "sql": "SELECT expired", "outcome": "success", "error": None, "row_count": 1, "column_count": 1}
        self.log._legacy_path.parent.mkdir(parents=True)
        legacy = json.dumps([current, expired], indent=2)
        self.log._legacy_path.write_text(legacy, encoding="utf-8")
        hourly = self.log._hour_path(now - dt.timedelta(hours=49))
        hourly.parent.mkdir(parents=True, exist_ok=True)
        hourly.write_text(json.dumps(expired) + "\n", encoding="utf-8")

        with patch.object(QueryLog, "_now", return_value=now):
            self.assertEqual([current], self.log.list()["items"])
            self.assertEqual(current, self.log.get("current"))
            with self.assertRaisesRegex(ValueError, "unknown log_id"):
                self.log.get("expired")

        self.assertEqual(legacy, self.log._legacy_path.read_text(encoding="utf-8"))
        self.assertFalse(hourly.exists())

    def test_background_append_returns_before_a_blocked_writer_then_drains_on_close(self) -> None:
        entered = threading.Event()
        release = threading.Event()
        original = self.log._append_record

        def blocked(record, now):
            with self.log._lock:
                entered.set()
                release.wait(timeout=1)
                original(record, now)

        with patch.object(self.log, "_append_record", side_effect=blocked):
            started = time.monotonic()
            record = self.log.append_async("SELECT 1", self.result)
            self.assertLess(time.monotonic() - started, 0.1)
            self.assertTrue(entered.wait(timeout=1))
            started = time.monotonic()
            second = self.log.append_async("SELECT 2", self.result)
            self.assertLess(time.monotonic() - started, 0.1)
            release.set()
            self.log.close()

        self.assertEqual([second, record], self.log.list()["items"])

    def test_background_appends_stay_ordered_and_keep_submission_timestamp(self) -> None:
        first = dt.datetime(2026, 11, 5, 10, 59, tzinfo=dt.UTC)
        second = dt.datetime(2026, 11, 5, 11, tzinfo=dt.UTC)
        with patch.object(QueryLog, "_now", side_effect=[first, second, second]):
            older = self.log.append_async("SELECT 1", self.result)
            newer = self.log.append_async("SELECT 2", self.result)
            self.log.close()
            records = self.log.list()["items"]

        self.assertEqual(first.isoformat(), older["at"])
        self.assertEqual([newer, older], records)
        self.assertTrue(self.log._hour_path(first).is_file())
        self.assertTrue(self.log._hour_path(second).is_file())

    def test_background_write_failure_only_reports_to_stderr(self) -> None:
        errors = StringIO()
        with patch.object(self.log, "_append_record", side_effect=ValueError("unavailable")), redirect_stderr(errors):
            self.log.append_async("SELECT 1", self.result)
            self.log.close()
        self.assertIn("query log failed: unavailable", errors.getvalue())

    def test_bind_reads_retained_history_without_writing_and_receives_committed_appends(self) -> None:
        now = dt.datetime(2026, 11, 5, 12, tzinfo=dt.UTC)
        with patch.object(QueryLog, "_now", return_value=now - dt.timedelta(hours=1)):
            retained = self.log.append("SELECT retained", self.result)
        expired = dict(retained, log_id="expired", at=(now - dt.timedelta(hours=49)).isoformat())
        path = self.log._hour_path(QueryLog._at(expired))
        path.write_text(json.dumps(expired) + "\n", encoding="utf-8")
        before = path.read_bytes()
        received = []
        with patch.object(QueryLog, "_now", return_value=now):
            self.assertEqual([retained], self.log.bind(received.append))
            self.assertEqual(before, path.read_bytes())
            appended = self.log.append_async("SELECT new", self.result)
            self.log.close()
        self.assertEqual([appended], received)

    def test_bind_does_not_report_failed_writes(self) -> None:
        received = []
        self.log.bind(received.append)
        with patch.object(self.log, "_hourly_records", side_effect=ValueError("unavailable")), redirect_stderr(StringIO()):
            self.log.append_async("SELECT 1", self.result)
            self.log.close()
        self.assertEqual([], received)


if __name__ == "__main__":
    unittest.main()
