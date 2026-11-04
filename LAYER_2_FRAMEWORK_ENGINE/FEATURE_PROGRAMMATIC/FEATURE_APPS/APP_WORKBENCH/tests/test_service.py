# CA-E-677@6

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
from APP_WORKBENCH.service import WorkbenchService  # noqa: E402


class ServiceTests(unittest.TestCase):
    def test_failed_startup_is_reported_once_and_not_retried(self):
        with (
            patch("APP_WORKBENCH.service.SourceReader"),
            patch("APP_WORKBENCH.service.QueryStore", side_effect=RuntimeError("extension unavailable")) as connect,
            redirect_stderr(StringIO()) as errors,
        ):
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
            patch("APP_WORKBENCH.service.SourceReader", return_value=reader),
            patch("APP_WORKBENCH.service.QueryStore", return_value=store),
            patch("APP_WORKBENCH.service.watch", side_effect=fake_watch),
        ):
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

    def test_watcher_rejects_sources_outside_the_selected_repository(self):
        reader = unittest.mock.Mock()
        reader.root = Path("/mounted/current-repo")
        reader.control_root = Path("/mounted/another-repo/.caprmedio_another")
        with (
            patch("APP_WORKBENCH.service.SourceReader", return_value=reader),
            patch("APP_WORKBENCH.service.watch") as watch,
            redirect_stderr(StringIO()) as errors,
        ):
            service = WorkbenchService(reader.root)
            service._index()
            self.assertTrue(service._watch_ready.is_set())
            self.assertIn("inside the selected repository", service._failure)
            self.assertIn("inside the selected repository", errors.getvalue())
            watch.assert_not_called()
            reader.capture.assert_not_called()
