# CA-E-780@5
from __future__ import annotations

import datetime as dt
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch


APP_ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(APP_ROOT), str(Path(__file__).parent)]

from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.query_store import QueryStore  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.watcher_change_log import WatcherChangeLog  # noqa: E402
from smalltest_support import extension_directory  # noqa: E402


class WatcherChangeLogTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.log = WatcherChangeLog(self.root)
        self.now = dt.datetime(2026, 11, 5, 12, tzinfo=dt.UTC)

    def _row(self, operation: str, old_path: str | None, new_path: str | None, observed_at: dt.datetime | None = None) -> dict[str, str | None]:
        return {"observed_at": (observed_at or self.now).isoformat(), "operation": operation, "old_path": old_path, "new_path": new_path}

    def test_ndjson_ttl_cap_and_required_paths(self) -> None:
        self.log._write([
            self._row("create", None, "control/expired.md", self.now - dt.timedelta(hours=49)),
            self._row("remove", "control/live.md", None, self.now - dt.timedelta(hours=1)),
        ])
        with patch.object(WatcherChangeLog, "_now", return_value=self.now):
            rows, changed = self.log.prune()
        self.assertTrue(changed)
        self.assertEqual([self._row("remove", "control/live.md", None, self.now - dt.timedelta(hours=1))], rows)

        with patch.object(WatcherChangeLog, "MAX_ROWS", 3), patch.object(WatcherChangeLog, "_now", return_value=self.now):
            rows, additions, replace_required = self.log.append_delta([
                {"operation": "create", "new_path": "control/a.md"},
                {"operation": "update", "new_path": "control/b.md"},
                {"operation": "rename", "old_path": "control/a.md", "new_path": "control/c.md"},
            ])
        self.assertTrue(replace_required)
        self.assertEqual(3, len(additions))
        self.assertEqual(["create", "update", "rename"], [row["operation"] for row in rows])
        self.assertEqual(rows, self.log._read())
        with self.assertRaisesRegex(ValueError, "old_path"):
            self.log.append([{"operation": "remove", "new_path": "control/invalid.md"}])
        with self.assertRaisesRegex(ValueError, "repository-relative"):
            self.log.append([{"operation": "create", "new_path": "/outside.md"}])

    def test_idle_prune_uses_cached_rows_until_expiry(self) -> None:
        with patch.object(WatcherChangeLog, "_now", return_value=self.now), patch.object(self.log, "_read", wraps=self.log._read) as read:
            self.log.append([{"operation": "create", "new_path": "control/new.md"}])
            rows, changed = self.log.prune()
        self.assertEqual(1, read.call_count)
        self.assertFalse(changed)
        self.assertEqual("create", rows[0]["operation"])

    def test_real_duckdb_mirror_survives_projection_replace_and_is_read_only(self) -> None:
        store = QueryStore(extension_directory=extension_directory(APP_ROOT.parents[2]))
        self.addCleanup(store.close)
        with patch.object(WatcherChangeLog, "_now", return_value=self.now):
            store.sync_change_log(self.log, [
                {"operation": "create", "new_path": "control/new.md"},
                {"operation": "move", "old_path": "control/new.md", "new_path": "control/nested/new.md"},
                {"operation": "remove", "old_path": "control/nested/new.md"},
            ])
        store.replace([], [])
        mirrored = store.run("SELECT operation, old_path, new_path FROM change_log ORDER BY operation")
        self.assertEqual(
            [["create", None, "control/new.md"], ["move", "control/new.md", "control/nested/new.md"], ["remove", "control/nested/new.md", None]],
            mirrored["rows"],
        )
        self.assertEqual(
            ["observed_at", "operation", "old_path", "new_path"],
            [column["name"] for column in store.schema()["tables"]["change_log"]],
        )
        with self.assertRaisesRegex(ValueError, "SELECT"):
            store.run("DELETE FROM change_log")

    def test_normal_append_preserves_prefix_mirrors_duplicates_and_avoids_delete(self) -> None:
        store = QueryStore(extension_directory=extension_directory(APP_ROOT.parents[2]))
        self.addCleanup(store.close)
        event = {"operation": "create", "new_path": "control/new.md"}
        with patch.object(WatcherChangeLog, "_now", return_value=self.now), patch.object(
            store, "_connection", Mock(wraps=store._connection),
        ) as connection:
            store.sync_change_log(self.log, [event])
            first_file = self.log._path.read_bytes()
            store.sync_change_log(self.log, [event])
        self.assertTrue(self.log._path.read_bytes().startswith(first_file))
        statements = [call.args[0] for call in connection.execute.call_args_list]
        self.assertFalse(any(sql.startswith("DELETE") for sql in statements))
        self.assertEqual(2, sum(sql.startswith("INSERT INTO main.change_log") for sql in statements))
        self.assertEqual(2, store.run("SELECT count(*) FROM change_log")["rows"][0][0])
        self.assertEqual(2, len(WatcherChangeLog(self.root)._read()))


if __name__ == "__main__":
    unittest.main()
