"""Focused RMED executor/worker failure-boundary checks."""

from concurrent.futures import CancelledError as FutureCancelledError
from contextlib import redirect_stderr
import io
from pathlib import Path
import sys
import tempfile
import types
import unittest
from unittest.mock import Mock, patch

APP = Path(__file__).resolve().parents[1]
TOOLS = APP.parents[1] / "201_TOOLS"
sys.path[:0] = [str(APP), str(TOOLS)]

import backend  # noqa: E402
from backend import execute_plan  # noqa: E402
from engine import Coordinator  # noqa: E402
from operation_error_boundary import ExplicitBlockingRuntimeFailure, FailureRecord  # noqa: E402


class _Engine:
    def __init__(self, root: Path):
        self.root = root
        self.finished = []

    def request(self, _run_id):
        return type("Request", (), {"selection": []})(), {}

    def finish(self, run_id, outcome, reason):
        self.finished.append((run_id, outcome, reason))
        return {"workflow_run_id": run_id, "outcome": outcome, "reason": reason}


class RmedWorkflowErrorBoundaryTests(unittest.TestCase):
    def test_execute_plan_reports_warning_without_raw_exception_or_retry(self):
        with tempfile.TemporaryDirectory() as directory:
            engine = _Engine(Path(directory))
            gather = Mock(side_effect=RuntimeError("password=private-value"))
            failure = FailureRecord("WARNING", "internal_failure", "operation failure")
            with patch("backend.report_failure", return_value=(failure, None)) as report:
                result = execute_plan(
                    engine, "run-1", gather, Mock(), Mock(), engine.finish, Mock()
                )

        report.assert_called_once()
        self.assertEqual(Path(directory), report.call_args.args[0])
        self.assertEqual(1, gather.call_count)
        self.assertEqual("interrupted", result["outcome"])
        self.assertEqual("operation failure", result["reason"])
        self.assertNotIn("private-value", repr(result))
    def test_execute_plan_keeps_explicit_runtime_failure_as_error_but_interrupted(self):
        with tempfile.TemporaryDirectory() as directory:
            engine = _Engine(Path(directory))
            error = ExplicitBlockingRuntimeFailure("worker_unavailable", "worker unavailable")
            failure = FailureRecord("ERROR", "worker_unavailable", "worker unavailable")
            with patch("backend.report_failure", return_value=(failure, None)) as report:
                result = execute_plan(
                    engine,
                    "run-2",
                    Mock(side_effect=error),
                    Mock(),
                    Mock(),
                    engine.finish,
                    Mock(),
                )

        self.assertIsInstance(report.call_args.args[1], ExplicitBlockingRuntimeFailure)
        self.assertEqual("worker_unavailable", report.call_args.args[1].code)
        self.assertEqual("ERROR", failure.severity)
        self.assertEqual(("run-2", "interrupted", "worker unavailable"), engine.finished[0])
        self.assertEqual("interrupted", result["outcome"])
    def test_cancellation_propagates_without_diagnostic_or_finish(self):
        with tempfile.TemporaryDirectory() as directory:
            engine = _Engine(Path(directory))
            with patch("backend.report_failure") as report:
                with self.assertRaises(FutureCancelledError):
                    execute_plan(
                        engine, "run-3", Mock(side_effect=FutureCancelledError()),
                        Mock(), Mock(), engine.finish, Mock()
                    )
        report.assert_not_called()
        self.assertEqual([], engine.finished)
    def test_coordinator_unknown_failure_is_warning_and_does_not_replay(self):
        with tempfile.TemporaryDirectory() as directory:
            engine = Coordinator.__new__(Coordinator)
            engine.root = Path(directory)
            engine.gather = Mock(side_effect=RuntimeError("credential=private-value"))
            engine.finish = Mock(return_value={"outcome": "interrupted"})
            failure = FailureRecord("WARNING", "internal_failure", "operation failure")
            with patch("engine.report_failure", return_value=(failure, None)) as report:
                result = engine.execute("run-4")

        report.assert_called_once()
        engine.gather.assert_called_once_with("run-4")
        engine.finish.assert_called_once_with("run-4", "interrupted", "operation failure")
        self.assertEqual({"outcome": "interrupted"}, result)
        self.assertNotIn("private-value", repr(result))
    def test_finish_failure_returns_error_without_replaying_finish(self):
        with tempfile.TemporaryDirectory() as directory:
            engine = _Engine(Path(directory))
            gather = Mock(side_effect=RuntimeError("input=private-value"))
            finish = Mock(side_effect=OSError("journal unavailable"))
            failure = FailureRecord("WARNING", "internal_failure", "operation failure")
            with patch("backend.report_failure", return_value=(failure, None)):
                result = execute_plan(
                    engine, "run-finish", gather, Mock(), Mock(), finish, Mock()
                )

        finish.assert_called_once_with("run-finish", "interrupted", "operation failure")
        self.assertEqual("interrupted", result["outcome"])
        self.assertNotIn("private-value", repr(result))
    def test_completed_finish_failure_does_not_retry_or_claim_completion(self):
        with tempfile.TemporaryDirectory() as directory:
            engine = _Engine(Path(directory))
            finish = Mock(side_effect=OSError("journal write uncertain"))
            failure = FailureRecord("WARNING", "internal_failure", "operation failure")
            with patch("backend.report_failure", return_value=(failure, None)) as report:
                result = execute_plan(
                    engine,
                    "run-complete-uncertain",
                    Mock(return_value={"outcome": "running"}),
                    Mock(),
                    Mock(),
                    finish,
                    Mock(),
                )

        report.assert_called_once()
        finish.assert_called_once_with("run-complete-uncertain", "completed", None)
        self.assertEqual("interrupted", result["outcome"])
    def test_worker_startup_failure_is_reported_without_raw_exception(self):
        with tempfile.TemporaryDirectory() as directory:
            dbos = Mock()
            dbos.launch.side_effect = RuntimeError("token=private-value")
            module = types.ModuleType("dbos")
            module.DBOS = dbos
            engine = Mock()
            engine.root = Path(directory)
            failure = FailureRecord("WARNING", "internal_failure", "operation failure")
            stream = io.StringIO()
            with (
                patch.dict(sys.modules, {"dbos": module}),
                patch.object(backend, "Coordinator", return_value=engine),
                patch.object(
                    backend,
                    "database",
                    return_value=(Path(directory) / "db.sqlite", "sqlite:///fixture"),
                ),
                patch.object(backend, "implementation_mock_runtime", return_value=False),
                patch.object(backend, "docker_runtime", return_value=False),
                patch.object(backend, "CodexAgent"),
                patch.object(backend, "register_execution"),
                patch.object(backend, "SelectedNativeProviders"),
                patch.object(backend, "report_failure", return_value=(failure, None)) as report,
                patch.object(backend.signal, "getsignal"),
                patch.object(backend.signal, "signal"),
                redirect_stderr(stream),
            ):
                result = backend.worker(Path(directory))

        self.assertEqual(1, result)
        report.assert_called_once()
        self.assertIn("operation failure", stream.getvalue())
        self.assertNotIn("private-value", stream.getvalue())
    def test_process_boundary_owns_worker_diagnostic_once(self):
        with tempfile.TemporaryDirectory() as directory:
            dbos = Mock()
            dbos.launch.side_effect = ExplicitBlockingRuntimeFailure(
                "worker_unavailable", "worker unavailable"
            )
            module = types.ModuleType("dbos")
            module.DBOS = dbos
            with (
                patch.dict(sys.modules, {"dbos": module}),
                patch.object(backend, "Coordinator", return_value=Mock()),
                patch.object(
                    backend,
                    "database",
                    return_value=(Path(directory) / "db.sqlite", "sqlite:///fixture"),
                ),
                patch.object(backend, "implementation_mock_runtime", return_value=False),
                patch.object(backend, "docker_runtime", return_value=False),
                patch.object(backend, "CodexAgent"),
                patch.object(backend, "register_execution"),
                patch.object(backend, "SelectedNativeProviders"),
                patch.object(backend, "report_failure") as report,
                patch.object(backend.signal, "getsignal"),
                patch.object(backend.signal, "signal"),
            ):
                with self.assertRaises(ExplicitBlockingRuntimeFailure):
                    backend.worker(Path(directory), _process_boundary=True)

        report.assert_not_called()


if __name__ == "__main__":
    unittest.main()
