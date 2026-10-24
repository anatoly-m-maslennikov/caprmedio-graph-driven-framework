"""Public selected-Workflow failure-boundary checks."""

from __future__ import annotations

from concurrent.futures import CancelledError as FutureCancelledError
from typing import Any, NoReturn
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[3] / "201_TOOLS"
PROJECT_ROOT = Path(__file__).resolve().parents[5]
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from operation_error_boundary import FailureRecord  # noqa: E402
from selected_workflow_error_fixtures import (  # noqa: E402
    build_request,
    execute_request,
    make_tracker,
)
from workflow_run_support import RunExecutionSession  # noqa: E402


class SelectedWorkflowErrorBoundaryTests(unittest.TestCase):
    def setUp(self) -> None:
        fixture_parent = PROJECT_ROOT / ".caprmedio_tmp/tests/selected-workflow-error-boundaries"
        fixture_parent.mkdir(parents=True, exist_ok=True)
        self.directory = tempfile.TemporaryDirectory(dir=fixture_parent)
        self.root = Path(self.directory.name)
        (self.root / ".git").mkdir()
        control = self.root / ".caprmedio_caprmedio"
        control.mkdir()
        (control / "caprmedio_project_settings.toml").write_text(
            "[paths]\ncontrol_root = '.caprmedio_caprmedio'\n"
            "journal_root = '.caprmedio_caprmedio/_journal'\n",
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.directory.cleanup()

    def test_failure_before_start_is_explicit_without_business_run(self) -> None:
        def execute(_request: dict[str, Any], _session: RunExecutionSession) -> NoReturn:
            raise RuntimeError("password=fixture-secret")

        tracker = make_tracker(self.root, execute)
        result = execute_request(tracker, build_request())
        self.assertEqual("failed", result["disposition"])
        self.assertEqual("failed", result["outcome"])
        self.assertEqual([], result["run_ids"])
        self.assertEqual("internal_failure", result["failure"]["code"])
        self.assertNotIn("fixture-secret", json.dumps(result))
        self.assertFalse(list((self.root / ".caprmedio_caprmedio/_journal").glob("*.ndjson")))

    def test_failure_after_start_is_interrupted_and_preserves_actual_run(self) -> None:
        def execute(_request: dict[str, Any], session: RunExecutionSession) -> NoReturn:
            session.start_run("workflow")
            raise RuntimeError("after-start")

        tracker = make_tracker(self.root, execute)
        result = execute_request(tracker, build_request("after-start"))
        self.assertEqual("started", result["disposition"])
        self.assertEqual("interrupted_pending", result["outcome"])
        self.assertEqual("interrupted_pending", result["terminal_runs"][0]["outcome"])
        events = [
            json.loads(line)
            for path in (self.root / ".caprmedio_caprmedio/_journal").glob("*.ndjson")
            for line in path.read_text(encoding="utf-8").splitlines()
        ]
        self.assertEqual(["started", "interrupted"], [event["event"] for event in events])

    def test_partial_effect_is_retained_and_repeat_is_inspection_only(self) -> None:
        calls = 0

        def execute(_request: dict[str, Any], session: RunExecutionSession) -> NoReturn:
            nonlocal calls
            calls += 1
            run = session.start_run("workflow")
            session.note_effects(
                run["run_id"], result_ref="results/partial.json", effect_refs=["target.md"]
            )
            raise RuntimeError("effect-before-failure")

        request = build_request("partial")
        first = execute_request(
            make_tracker(self.root, execute),
            request,
        )
        self.assertEqual("partial", first["outcome"])
        self.assertEqual(["target.md"], first["terminal_runs"][0]["effect_refs"])
        second = execute_request(
            make_tracker(self.root, execute),
            request,
        )
        self.assertEqual("inspect-or-recover-only", second["retry_disposition"])
        self.assertEqual(1, calls)

    def test_logger_failure_is_visible_without_replacing_uncertainty(self) -> None:
        def execute(_request: dict[str, Any], _session: RunExecutionSession) -> NoReturn:
            raise RuntimeError("unexpected")

        tracker = make_tracker(self.root, execute)
        with patch(
            "workflow_run_support.report_failure",
            return_value=(
                FailureRecord("WARNING", "internal_failure", "operation failure"),
                "technical diagnostic emission failed",
            ),
        ):
            result = execute_request(tracker, build_request("logger-failure"))
        self.assertEqual("internal_failure", result["failure"]["code"])
        self.assertEqual(
            "technical diagnostic emission failed", result["failure"]["diagnostic_error"]
        )

    def test_future_cancellation_is_not_converted_to_a_result(self) -> None:
        def execute(_request: dict[str, Any], _session: RunExecutionSession) -> NoReturn:
            raise FutureCancelledError()

        tracker = make_tracker(self.root, execute)
        with self.assertRaises(FutureCancelledError):
            execute_request(tracker, build_request("cancelled"))


if __name__ == "__main__":
    unittest.main()
