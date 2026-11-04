# CA-E-676@9
# CA-E-677@8
# CA-M-472@1

"""Service failures stop this owner rather than retrying its startup."""

from contextlib import redirect_stderr
from io import StringIO
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service import WorkbenchService  # noqa: E402


class ServiceTests(unittest.TestCase):

    def test_failed_startup_is_reported_once_and_not_retried(self):
        with (
            patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service.SourceReader"),
            patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service.QueryStore", side_effect=RuntimeError("extension unavailable")) as connect,
            redirect_stderr(StringIO()) as errors,
        ):
            service = WorkbenchService(Path.cwd())
            for _ in range(2):
                with self.assertRaisesRegex(RuntimeError, "restart required"):
                    service.run("SELECT 1")
            service.close()
            connect.assert_called_once()
            self.assertEqual(1, errors.getvalue().count("Workbench startup failed"))

    def test_journal_changes_are_not_source_refreshes(self):
        with patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service.SourceReader"):
            service = WorkbenchService(Path("/project"))

        with patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service.configured_journal_root", return_value=Path(".caprmedio_caprmedio/_journal")):
            self.assertTrue(service._journal_only({
                (object(), "/project/.caprmedio_caprmedio/_journal/workbench-saved-items-2026-11-05-part-1.ndjson"),
            }))
            self.assertFalse(service._journal_only({
                (object(), "/project/.caprmedio_caprmedio/_journal/workbench-saved-items-2026-11-05-part-1.ndjson"),
                (object(), "/project/.caprmedio_caprmedio/04_requirement/CA-R-1.md"),
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

    def test_explicit_save_failure_does_not_start_or_execute(self):
        with patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service.SourceReader"):
            service = WorkbenchService(Path("/project"))
        service._saved_queries = unittest.mock.Mock(save_query=unittest.mock.Mock(side_effect=ValueError("disk full")))
        service._start = unittest.mock.Mock()

        with self.assertRaisesRegex(ValueError, "disk full"):
            service.save("SELECT 1")

        service._start.assert_not_called()
