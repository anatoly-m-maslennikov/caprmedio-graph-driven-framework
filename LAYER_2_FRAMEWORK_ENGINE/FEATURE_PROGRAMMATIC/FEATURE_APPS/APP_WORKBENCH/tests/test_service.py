# CA-E-676@8
# CA-E-677@8

"""Service failures stop this owner rather than retrying its startup."""

from contextlib import redirect_stderr
from io import StringIO
from pathlib import Path
import sys
import threading
import time
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from watchfiles import Change  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.saved_queries import SavedQueryError  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service import WorkbenchService  # noqa: E402


class ServiceTests(unittest.TestCase):
    def test_start_uses_runtime_projection_path(self):
        reader = unittest.mock.Mock()
        reader.capture.return_value = ([], [])
        reader.excluded_count = 0
        store = unittest.mock.Mock()
        extension_directory = Path("/extensions")

        with (
            patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service.SourceReader", return_value=reader),
            patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service.QueryStore", return_value=store) as connect,
        ):
            service = WorkbenchService(Path("/project"), extension_directory=extension_directory)
            service._index = lambda: service._watch_ready.set()
            service._start()
            self.addCleanup(service.close)

        connect.assert_called_once_with(
            extension_directory=extension_directory,
            database_path=Path("/project") / ".caprmedio_runtime" / "workbench" / "projection.duckdb",
        )

    def test_query_methods_forward_page_size_and_start_once(self):
        store = unittest.mock.Mock()
        store.run.return_value = {"query_id": "q"}
        store.page.return_value = {"query_id": "q", "offset": 3}
        store.check.return_value = {"valid": True}

        with patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service.SourceReader"):
            service = WorkbenchService(Path("/project"))
        saved = unittest.mock.Mock()
        saved.save_query.side_effect = lambda sql, name=None: (
            {"saved_query_id": "q_" + "1" * 32, "kind": "query", "sql": sql}
            | ({"name": name} if name else {})
        )
        saved.save_worksheet.return_value = {"saved_query_id": "w_" + "1" * 32, "kind": "worksheet", "sql": "SELECT 2", "name": "Sheet"}
        saved.load.return_value = {"saved_query_id": "q_" + "1" * 32, "kind": "query", "sql": "SELECT 1"}
        saved.list.return_value = {"items": []}
        service._saved_queries = saved
        service._store = store
        service._start = unittest.mock.Mock()

        self.assertEqual({"query_id": "q"}, service.run("SELECT 1", page_size=2))
        self.assertEqual({"query_id": "q", "offset": 3}, service.page("q", 3, page_size=4))
        self.assertEqual({"valid": True}, service.check("SELECT 1"))
        self.assertEqual(3, service._start.call_count)
        store.run.assert_called_once_with(
            "SELECT 1", page_size=2,
            saved_query={"saved_query_id": "q_" + "1" * 32, "kind": "query", "sql": "SELECT 1"},
        )
        store.page.assert_called_once_with("q", 3, page_size=4)
        store.check.assert_called_once_with(
            "SELECT 1",
            saved_query={"saved_query_id": "q_" + "1" * 32, "kind": "query", "sql": "SELECT 1"},
        )
        self.assertEqual({"saved_query_id": "q_" + "1" * 32, "kind": "query", "sql": "SELECT 1", "name": "Query"}, service.save("SELECT 1", name="Query"))
        saved.save_query.assert_called_with("SELECT 1", "Query")
        self.assertEqual({"saved_query_id": "w_" + "1" * 32, "kind": "worksheet", "sql": "SELECT 2", "name": "Sheet"}, service.save_worksheet("SELECT 2", name="Sheet"))
        saved.save_worksheet.assert_called_once_with("SELECT 2", "Sheet")
        self.assertEqual({"saved_query_id": "q_" + "1" * 32, "kind": "query", "sql": "SELECT 1"}, service.load("q_" + "1" * 32))
        self.assertEqual({"items": []}, service.saved_list())

    def test_refresh_releases_reader_rows_only_after_store_replace(self):
        reader = unittest.mock.Mock()
        reader.capture.return_value = ([], [])
        reader.excluded_count = 0
        calls: list[str] = []
        reader.release_cache.side_effect = lambda: calls.append("release")
        store = unittest.mock.Mock()
        store.replace.side_effect = lambda _atoms, _scopes: calls.append("replace")

        with patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service.SourceReader", return_value=reader):
            service = WorkbenchService(Path("/project"))
        service._store = store

        service._refresh()

        self.assertEqual(calls, ["replace", "release"])
        store.replace.assert_called_once_with([], [])
        reader.release_cache.assert_called_once_with()

    def test_failed_startup_is_reported_once_and_not_retried(self):
        with (
            patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service.SourceReader"),
            patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service.QueryStore", side_effect=RuntimeError("extension unavailable")) as connect,
            patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service.SavedQueryStore") as saved,
            redirect_stderr(StringIO()) as errors,
        ):
            saved.return_value.save_query.return_value = {
                "saved_query_id": "q_" + "1" * 32, "kind": "query", "sql": "SELECT 1",
            }
            service = WorkbenchService(Path.cwd())
            for _ in range(2):
                with self.assertRaisesRegex(RuntimeError, "restart required"):
                    service.run("SELECT 1")
            service.close()
            connect.assert_called_once()
            self.assertEqual(1, errors.getvalue().count("Workbench startup failed"))

    def test_one_grouped_watch_batch_refreshes_once_and_uses_stop_event(self):
        reader = unittest.mock.Mock()
        reader.root = Path("/project")
        reader.control_root = Path("/project/.caprmedio_caprmedio")
        reader.excluded_count = 0
        store = unittest.mock.Mock()
        store.run.return_value = {"columns": [], "rows": [], "row_count": 0, "column_count": 0}
        watch_started = threading.Event()
        generator_entered = threading.Event()
        release_batch = threading.Event()
        batch_finished = threading.Event()
        observed: dict[str, object] = {}

        def capture():
            self.assertTrue(generator_entered.is_set())
            return [], []

        reader.capture.side_effect = capture

        def fake_watch(path, *, stop_event, rust_timeout, yield_on_timeout):
            observed.update(
                path=path,
                stop_event=stop_event,
                rust_timeout=rust_timeout,
                yield_on_timeout=yield_on_timeout,
            )
            watch_started.set()

            def batches():
                generator_entered.set()
                yield set()
                release_batch.wait(2)
                yield {
                    (Change.added, "/project/.caprmedio_caprmedio/04_requirement/CA-R-1.md"),
                    (Change.modified, "/project/.caprmedio_caprmedio/04_requirement/CA-R-2.md"),
                    (Change.deleted, "/project/.caprmedio_caprmedio/04_requirement/CA-R-3.md"),
                }
                batch_finished.set()

            return batches()

        with (
            patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service.SourceReader", return_value=reader),
            patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service.QueryStore", return_value=store),
            patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service.SavedQueryStore") as saved,
            patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service.watch", side_effect=fake_watch),
            patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service.configured_journal_root", return_value=Path(".caprmedio_caprmedio/_journal")),
        ):
            saved.return_value.save_query.return_value = {
                "saved_query_id": "q_" + "1" * 32, "kind": "query", "sql": "SELECT 1",
            }
            service = WorkbenchService(Path("/project"))
            self.addCleanup(service.close)
            service.run("SELECT 1")
            self.assertTrue(watch_started.wait(2))
            self.assertEqual(1, reader.capture.call_count)
            release_batch.set()
            self.assertTrue(batch_finished.wait(3))
            deadline = time.monotonic() + 3
            while reader.capture.call_count < 2 and time.monotonic() < deadline:
                time.sleep(0.01)
            self.assertEqual(2, reader.capture.call_count)
            self.assertEqual(str(reader.control_root), observed["path"])
            self.assertIs(service._stop, observed["stop_event"])
            self.assertEqual(100, observed["rust_timeout"])
            self.assertTrue(observed["yield_on_timeout"])

    def test_journal_changes_are_not_source_refreshes(self):
        with patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service.SourceReader"):
            service = WorkbenchService(Path("/project"))

        with patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service.configured_journal_root", return_value=Path(".caprmedio_caprmedio/_journal")):
            self.assertTrue(service._journal_only({
                (Change.modified, "/project/.caprmedio_caprmedio/_journal/workbench-saved-items-2026-11-05-part-1.ndjson"),
            }))
            self.assertFalse(service._journal_only({
                (Change.modified, "/project/.caprmedio_caprmedio/_journal/workbench-saved-items-2026-11-05-part-1.ndjson"),
                (Change.modified, "/project/.caprmedio_caprmedio/04_requirement/CA-R-1.md"),
            }))

    def test_watcher_rejects_sources_outside_the_selected_repository(self):
        reader = unittest.mock.Mock()
        reader.root = Path("/mounted/current-repo")
        reader.control_root = Path("/mounted/another-repo/.caprmedio_another")
        with (
            patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service.SourceReader", return_value=reader),
            patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service.watch") as watch,
            redirect_stderr(StringIO()) as errors,
        ):
            service = WorkbenchService(reader.root)
            service._index()
            self.assertTrue(service._watch_ready.is_set())
            self.assertIn("inside the selected repository", service._failure)
            self.assertIn("inside the selected repository", errors.getvalue())
            watch.assert_not_called()
            reader.capture.assert_not_called()

    def test_saved_query_identity_survives_a_later_query_error(self):
        store = unittest.mock.Mock()
        store.run.side_effect = ValueError("bad SQL")
        with patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service.SourceReader"):
            service = WorkbenchService(Path("/project"))
        saved = {"saved_query_id": "q_" + "2" * 32, "kind": "query", "sql": "invalid"}
        service._saved_queries = unittest.mock.Mock(save_query=unittest.mock.Mock(return_value=saved))
        service._store = store
        service._start = unittest.mock.Mock()

        with self.assertRaises(SavedQueryError) as raised:
            service.run("invalid")

        self.assertEqual(saved, raised.exception.saved_query)
        self.assertIsInstance(raised.exception.original_error, ValueError)

    def test_save_failure_does_not_start_or_execute(self):
        with patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service.SourceReader"):
            service = WorkbenchService(Path("/project"))
        service._saved_queries = unittest.mock.Mock(save_query=unittest.mock.Mock(side_effect=ValueError("disk full")))
        service._start = unittest.mock.Mock()

        with self.assertRaisesRegex(ValueError, "disk full"):
            service.run("SELECT 1")

        service._start.assert_not_called()
