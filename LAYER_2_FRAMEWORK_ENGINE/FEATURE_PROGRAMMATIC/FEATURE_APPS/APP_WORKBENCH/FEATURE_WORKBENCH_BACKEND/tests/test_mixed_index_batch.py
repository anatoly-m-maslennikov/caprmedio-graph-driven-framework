# CA-E-677@14
"""Exercise the mixed edit/removal batch reported in C712."""

from pathlib import Path
import sys
import threading
import time
import unittest
from unittest.mock import patch

from watchdog.observers.polling import PollingObserver

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tests"))

from smalltest_support import source_path, write_atom
from test_incremental_indexing import IncrementalIndexingTests


class MixedIndexBatchTests(IncrementalIndexingTests):
    def test_updates_and_deleted_current_and_drafts_share_one_delta(self):
        paths = [
            source_path(self.declarations, "ENGINE", "04_requirement", f"CA-R-{i}.md")
            for i in range(100, 112)
        ]
        drafts = [
            path.parent / "draft" / f"CA-R-{i}@2-draft.md"
            for i, path in zip(range(110, 112), paths[-2:])
        ]
        for i, path in enumerate(paths, 100):
            write_atom(path, f"CA-R-{i}")
        for i, path in enumerate(drafts, 110):
            write_atom(path, f"CA-R-{i}", status="Draft", version=2)
        self.service._refresh([self.event(path, operation="create") for path in paths + drafts])

        for i, path in enumerate(paths[:10], 100):
            write_atom(path, f"CA-R-{i}", version=2)
        for path in paths[-2:] + drafts:
            path.unlink()
        changes = [self.event(path) for path in paths[:10]] + [
            self.event(None, old=path, operation="remove") for path in paths[-2:] + drafts
        ]
        with self.no_full_work():
            self.service._refresh(changes)

        rows = self.store.run(
            'SELECT "header.atom_id", "header.version" FROM atoms '
            'WHERE "header.atom_id" LIKE \'CA-R-1%\' ORDER BY "header.atom_id"'
        )["rows"]
        self.assertEqual([[f"CA-R-{i}", 2] for i in range(100, 110)], rows)
        self.assertEqual(False, self.service.sync_status()["syncing"])

    def test_real_watcher_applies_mixed_updates_and_deletes(self):
        paths = [
            source_path(self.declarations, "ENGINE", "04_requirement", f"CA-R-{i}.md")
            for i in range(200, 212)
        ]
        drafts = [
            path.parent / "draft" / f"CA-R-{i}@2-draft.md"
            for i, path in zip(range(210, 212), paths[-2:])
        ]
        for i, path in enumerate(paths, 200):
            write_atom(path, f"CA-R-{i}")
        for i, path in enumerate(drafts, 210):
            write_atom(path, f"CA-R-{i}", status="Draft", version=2)
        self.service._refresh([self.event(path, operation="create") for path in paths + drafts])
        with patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.source_watcher.NativeObserver", PollingObserver):
            self.service._thread = threading.Thread(target=self.service._index, daemon=True)
            self.service._thread.start()
            self.assertTrue(self.service._watch_ready.wait(5))

            for i, path in enumerate(paths[:10], 200):
                write_atom(path, f"CA-R-{i}", version=2)
            for path in paths[-2:] + drafts:
                path.unlink()
            expected = [[f"CA-R-{i}", 2] for i in range(200, 210)]
            deadline = time.monotonic() + 10
            actual = []
            while time.monotonic() < deadline:
                actual = self.store.run(
                    'SELECT "header.atom_id", "header.version" FROM atoms '
                    'WHERE "header.atom_id" LIKE \'CA-R-2%\' ORDER BY "header.atom_id"'
                )["rows"]
                if actual == expected and self.service.sync_status()["syncing"] is False:
                    break
                time.sleep(0.05)
        self.assertEqual(expected, actual)
        self.assertIsNone(self.service._failure)


if __name__ == "__main__":
    unittest.main()
