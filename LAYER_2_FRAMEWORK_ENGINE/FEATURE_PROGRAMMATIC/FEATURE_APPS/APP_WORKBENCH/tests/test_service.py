# CA-E-676@11
# CA-E-677@8
# CA-R-2950@1
# CA-R-2952@1
# CA-M-465@13
# CA-M-490@1
# CA-M-491@1
# CA-D-695@1
# CA-D-696@1
# CA-E-780@1
# CA-E-781@1
# CA-M-472@1

"""Service failures stop this owner rather than retrying its startup."""

from contextlib import redirect_stderr
from io import StringIO
from pathlib import Path
import sys
import tempfile
import threading
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service import WorkbenchService  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.errors import WorkbenchUnavailableError  # noqa: E402


class ServiceTests(unittest.TestCase):

    def test_failed_startup_is_reported_once_and_not_retried(self):
        with (
            patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service.SourceReader"),
            patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service.QueryStore", side_effect=RuntimeError("extension unavailable")) as connect,
            redirect_stderr(StringIO()) as errors,
        ):
            service = WorkbenchService(Path.cwd())
            for _ in range(2):
                with self.assertRaisesRegex(WorkbenchUnavailableError, "restart required"):
                    service.run("SELECT 1")
            service.close()
            connect.assert_called_once()
            self.assertEqual(1, errors.getvalue().count("Workbench startup failed"))

    def test_journal_changes_are_not_source_refreshes(self):
        with patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service.SourceReader"):
            service = WorkbenchService(Path("/project"))

        with patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service.configured_journal_root", return_value=Path(".caprmedio_caprmedio/_journal")):
            self.assertTrue(service._journal_only([
                {"operation": "update", "old_path": None, "new_path": ".caprmedio_caprmedio/_journal/workbench-saved-items.ndjson"},
            ]))
            self.assertFalse(service._journal_only([
                {"operation": "update", "old_path": None, "new_path": ".caprmedio_caprmedio/_journal/workbench-saved-items.ndjson"},
                {"operation": "update", "old_path": None, "new_path": ".caprmedio_caprmedio/04_requirement/CA-R-1.md"},
            ]))
            self.assertFalse(service._journal_only([
                {
                    "operation": "move",
                    "old_path": ".caprmedio_caprmedio/_journal/workbench-saved-items.ndjson",
                    "new_path": ".caprmedio_caprmedio/04_requirement/CA-R-1.md",
                },
            ]))

    def test_watcher_rejects_sources_outside_the_selected_repository(self):
        reader = unittest.mock.Mock()
        reader.root = Path("/mounted/current-repo")
        reader.control_root = Path("/mounted/another-repo/.caprmedio_another")
        with (
            patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service.SourceReader", return_value=reader),
            redirect_stderr(StringIO()) as errors,
        ):
            service = WorkbenchService(reader.root)
            service._index()
            self.assertTrue(service._watch_ready.is_set())
            self.assertIn("inside the selected repository", str(service._failure))
            self.assertIn("inside the selected repository", errors.getvalue())
            reader.capture.assert_not_called()

    def test_watcher_batch_logs_then_refreshes_on_the_owner_thread(self):
        reader = unittest.mock.Mock()
        reader.root = Path("/project")
        reader.control_root = Path("/project/.caprmedio_project")
        event = {"operation": "update", "old_path": None, "new_path": ".caprmedio_project/04_requirement/CA-R-1.md"}
        watcher = unittest.mock.Mock()
        change_log = unittest.mock.Mock()

        with (
            patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service.SourceReader", return_value=reader),
            patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service.SourceWatcher", return_value=watcher),
            patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service.configured_journal_root", return_value=Path(".caprmedio_project/_journal")),
        ):
            service = WorkbenchService(reader.root)
            service._store = unittest.mock.Mock()
            service._watcher_change_log = change_log
            service._refresh = unittest.mock.Mock()
            watcher.changes.side_effect = lambda timeout: (service._stop.set() or [event])
            service._index()

        watcher.start.assert_called_once()
        watcher.close.assert_called_once()
        service._store.sync_change_log.assert_has_calls([
            unittest.mock.call(change_log, [event]),
            unittest.mock.call(change_log),
        ])
        service._refresh.assert_called_once()

    def test_start_rehydrates_the_log_before_serving(self):
        with patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service.SourceReader"):
            service = WorkbenchService(Path("/project"))
        service._store = unittest.mock.Mock()
        service._watcher_change_log = unittest.mock.Mock()

        service._rehydrate_watcher_changes()

        service._store.sync_change_log.assert_called_once_with(
            service._watcher_change_log, initialize=True,
        )

    def test_sync_status_is_available_while_capture_is_running(self):
        reader = unittest.mock.Mock()
        reader.excluded_count = 0
        started, release = threading.Event(), threading.Event()

        def capture():
            started.set()
            self.assertTrue(release.wait(timeout=1))
            return [], []

        reader.capture.side_effect = capture
        with patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service.SourceReader", return_value=reader):
            service = WorkbenchService(Path("/project"))
        service._store = unittest.mock.Mock()
        self.assertEqual({"syncing": False, "last_synced_at": None}, service.sync_status())
        reader.capture.assert_not_called()
        worker = threading.Thread(target=service._refresh)
        worker.start()
        self.assertTrue(started.wait(timeout=1))
        self.assertEqual({"syncing": True, "last_synced_at": None}, service.sync_status())

        release.set()
        worker.join(timeout=1)
        self.assertFalse(worker.is_alive())
        status = service.sync_status()
        self.assertFalse(status["syncing"])
        self.assertIsInstance(status["last_synced_at"], str)

    def test_sync_status_keeps_the_last_success_after_capture_failure(self):
        reader = unittest.mock.Mock(capture=unittest.mock.Mock(return_value=([], [])), excluded_count=0)
        with patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service.SourceReader", return_value=reader):
            service = WorkbenchService(Path("/project"))
        service._store = unittest.mock.Mock()
        service._refresh()
        successful = service.sync_status()
        reader.capture.side_effect = RuntimeError("broken source")

        with self.assertRaisesRegex(RuntimeError, "broken source"):
            service._refresh()

        self.assertEqual(successful["last_synced_at"], service.sync_status()["last_synced_at"])
        self.assertEqual(False, service.sync_status()["syncing"])

    def test_run_keeps_completed_result_when_late_save_fails(self):
        with patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service.SourceReader"):
            service = WorkbenchService(Path("/project"))
        service._saved_queries = unittest.mock.Mock(save_query=unittest.mock.Mock(side_effect=ValueError("disk full")))
        service._start = unittest.mock.Mock()
        service._store = unittest.mock.Mock(run=unittest.mock.Mock(return_value={
            "query_id": "done", "rows": [[1]], "row_count": 1, "column_count": 1,
        }))
        service._query_log = unittest.mock.Mock()

        with redirect_stderr(StringIO()) as errors:
            result = service.run("SELECT 1", save=True, name="important")

        self.assertEqual({"query_id": "done", "rows": [[1]], "row_count": 1, "column_count": 1, "outcome": "partial", "save_error": "disk full"}, result)
        service._start.assert_called_once()
        service._store.run.assert_called_once_with("SELECT 1", page_size=100, preview=None, include_rows=True)
        service._saved_queries.save_query.assert_called_once_with("SELECT 1", "important")
        service._query_log.append.assert_called_once()
        self.assertIn("saved query failed: disk full", errors.getvalue())

    def test_run_saves_only_after_a_completed_result(self):
        with patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service.SourceReader"):
            service = WorkbenchService(Path("/project"))
        service._start = unittest.mock.Mock()
        service._store = unittest.mock.Mock(run=unittest.mock.Mock(return_value={
            "query_id": "done", "rows": [[1]], "row_count": 1, "column_count": 1,
        }))
        service._query_log = unittest.mock.Mock()
        service._saved_queries = unittest.mock.Mock(
            save_query=unittest.mock.Mock(return_value={"saved_query_id": "saved", "kind": "query"}),
        )

        result = service.run("SELECT 1", save=True, name="important")

        self.assertEqual(
            {"query_id": "done", "rows": [[1]], "row_count": 1, "column_count": 1, "saved_query_id": "saved", "kind": "query"},
            result,
        )
        service._store.run.assert_called_once_with("SELECT 1", page_size=100, preview=None, include_rows=True)
        service._saved_queries.save_query.assert_called_once_with("SELECT 1", "important")
        service._query_log.append.assert_called_once()

    def test_invalid_preview_does_not_start_the_service(self):
        with patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service.SourceReader"):
            service = WorkbenchService(Path("/project"))
        service._start = unittest.mock.Mock()

        with self.assertRaisesRegex(ValueError, "preview"):
            service.run("SELECT 1", preview=True)

        service._start.assert_not_called()

    def test_existing_invalid_runtime_ttl_stops_startup(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            settings = root / ".caprmedio_runtime" / "caprmedio_runtime_settings.toml"
            settings.parent.mkdir()
            settings.write_text("[workbench]\nresult_ttl_seconds = 0\n", encoding="utf-8")
            with (
                patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service.SourceReader"),
                patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service.QueryStore") as store,
                redirect_stderr(StringIO()) as errors,
            ):
                service = WorkbenchService(root)
                with self.assertRaisesRegex(WorkbenchUnavailableError, "positive integer"):
                    service.run("SELECT 1")
                service.close()

        store.assert_not_called()
        self.assertIn("Workbench startup failed", errors.getvalue())
