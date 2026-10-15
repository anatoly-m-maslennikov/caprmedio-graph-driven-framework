"""Release Journal events preserve failures without becoming release gates."""

from __future__ import annotations

from pathlib import Path
import sys
from types import ModuleType
import unittest
from unittest.mock import Mock, patch

REPOSITORY = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPOSITORY))
sys.path.insert(0, str(REPOSITORY / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS"))
from PROJECT_TOOLS import release_events  # noqa: E402
import work_journal  # noqa: E402


class ReleaseEventsTests(unittest.TestCase):
    def test_started_and_terminal_linkage(self) -> None:
        for outcome in ("completed", "failed"):
            with self.subTest(outcome=outcome):
                invoke = Mock(return_value={"outcome": outcome})
                with patch.object(
                    release_events, "record_release_event", return_value=("start", None)
                ) as record:
                    result = release_events.run_recorded_release(
                        REPOSITORY, "release_version", "run", invoke
                    )
                self.assertEqual(
                    record.call_args_list[0].args,
                    (REPOSITORY, "release_version", "run", "started", None),
                )
                self.assertEqual(
                    record.call_args_list[1].args,
                    (REPOSITORY, "release_version", "run", outcome, "start", outcome),
                )
                self.assertEqual(result["outcome"], outcome)
                invoke.assert_called_once_with()

    def test_recording_errors_do_not_change_completion(self) -> None:
        with patch.object(
            release_events,
            "record_release_event",
            side_effect=[(None, "start unavailable"), (None, "terminal unavailable")],
        ):
            result = release_events.run_recorded_release(
                REPOSITORY, "public.release", "run", lambda: {"outcome": "completed"}
            )
        self.assertEqual(result["outcome"], "completed")
        self.assertEqual(result["recording_error"], "start unavailable; terminal unavailable")

    def test_exception_gets_terminal_failure_without_retry(self) -> None:
        invoke = Mock(side_effect=OSError("unavailable"))
        with patch.object(
            release_events, "record_release_event", return_value=("start", None)
        ) as record:
            result = release_events.run_recorded_release(
                REPOSITORY, "public.release", "run", invoke
            )
        self.assertEqual(result["outcome"], "failed")
        self.assertEqual(record.call_args.args[3:], ("failed", "start", "failed"))
        invoke.assert_called_once_with()

    def test_plain_event_schema_and_nonblocking_append_failure(self) -> None:
        journal = ModuleType("work_journal")
        event_record = Mock(return_value={"event_id": "event"})
        append_record = Mock()
        setattr(journal, "event_record", event_record)
        setattr(journal, "append_record", append_record)
        with patch.dict(sys.modules, {"work_journal": journal}):
            self.assertEqual(
                release_events.record_release_event(
                    REPOSITORY, "release_version", "run", "started", None
                ),
                ("event", None),
            )
            append_record.side_effect = OSError("Journal unavailable")
            result = release_events.record_release_event(
                REPOSITORY, "release_version", "run", "failed", "event", "failed"
            )
        self.assertIn("Journal unavailable", result[1] or "")
        self.assertEqual(
            event_record.call_args.kwargs,
            {
                "root": REPOSITORY,
                "event": "failed",
                "action_id": "run",
                "kind": "workflow",
                "scope": "project",
                "operation": "release_version",
                "session_id": "run",
                "subjects": [],
                "outputs": [],
                "preceding_event": "event",
                "details": {"outcome": "failed"},
            },
        )

    def test_malformed_timestamp_settings_do_not_block_primary_execution(self) -> None:
        settings: tuple[Path, dict[str, object]] = (
            REPOSITORY / "settings.toml",
            {"artifact_timestamps": []},
        )
        invoke = Mock(return_value={"outcome": "completed"})
        with (
            patch.object(work_journal, "_read_project_settings", return_value=settings),
            patch.object(work_journal, "append_record") as append,
        ):
            result = release_events.run_recorded_release(
                REPOSITORY, "release_version", "run", invoke
            )
        self.assertEqual(result["outcome"], "completed")
        self.assertIn("Release started recording failed", str(result["recording_error"]))
        self.assertIn("Release completed recording failed", str(result["recording_error"]))
        invoke.assert_called_once_with()
        append.assert_not_called()

    def test_malformed_terminal_timestamp_settings_do_not_change_completion(self) -> None:
        valid = (REPOSITORY / "settings.toml", {"artifact_timestamps": {"timezone": "UTC"}})
        malformed: tuple[Path, dict[str, object]] = (
            REPOSITORY / "settings.toml",
            {"artifact_timestamps": []},
        )
        invoke = Mock(return_value={"outcome": "completed"})
        with (
            patch.object(work_journal, "_read_project_settings", side_effect=[valid, malformed]),
            patch.object(work_journal, "append_record") as append,
        ):
            result = release_events.run_recorded_release(
                REPOSITORY, "public.release", "run", invoke
            )
        self.assertEqual(result["outcome"], "completed")
        self.assertNotIn("Release started recording failed", str(result["recording_error"]))
        self.assertIn("Release completed recording failed", str(result["recording_error"]))
        invoke.assert_called_once_with()
        append.assert_called_once()


if __name__ == "__main__":
    unittest.main()
