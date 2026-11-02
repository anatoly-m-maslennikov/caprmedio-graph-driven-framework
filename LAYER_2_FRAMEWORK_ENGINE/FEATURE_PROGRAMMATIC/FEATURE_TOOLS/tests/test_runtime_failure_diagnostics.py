"""Focused checks for the shared runtime failure diagnostic facade."""

from __future__ import annotations

from concurrent.futures import CancelledError as FutureCancelledError
from contextlib import redirect_stderr
import io
import json
from pathlib import Path
from types import SimpleNamespace
import sys
import tempfile
import unittest
from unittest.mock import patch


TOOLS = Path(__file__).resolve().parents[1]
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import runtime_failure_diagnostics as facade  # noqa: E402
from operation_error_boundary import (  # noqa: E402
    ExplicitBlockingRuntimeFailure,
    FailureRecord,
)
from technical_diagnostics import TechnicalDiagnosticLogger  # noqa: E402


class _FailingStream:
    def write(self, _value: str) -> int:
        raise OSError("password=secret")

    def flush(self) -> None:
        raise OSError("password=secret")


class RuntimeFailureDiagnosticsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path("/bound/project")
        self.selection = SimpleNamespace(settings={"actual": "settings"})

    def _logger(self, stream: io.TextIOBase) -> TechnicalDiagnosticLogger:
        return TechnicalDiagnosticLogger("ACTUAL", self.root, "test", stream, "host")

    def test_bound_root_uses_selected_settings_and_actual_component(self) -> None:
        stream = io.StringIO()
        logger = self._logger(stream)
        with (
            patch.object(facade, "active_selection", return_value=self.selection) as selected,
            patch.object(facade, "make_technical_logger", return_value=(logger, None)) as made,
        ):
            failure, secondary = facade.report_failure(
                self.root,
                RuntimeError("password=secret"),
                component="ACTUAL_COMPONENT",
                operation="lookup",
                correlation_id="corr-1",
            )
        selected.assert_called_once_with(self.root)
        made.assert_called_once_with(self.selection.settings, self.root)
        self.assertIsNone(secondary)
        self.assertEqual("RuntimeError", failure.exception_class)
        record = json.loads(stream.getvalue())
        self.assertEqual("ACTUAL_COMPONENT", record["component"])
        self.assertEqual("ACTUAL", record["project_prefix"])
        self.assertEqual("corr-1", record["correlation_id"])
        self.assertNotIn("password=secret", stream.getvalue())

    def test_unbound_or_invalid_selection_is_visible_without_guessed_prefix(self) -> None:
        stream = io.StringIO()
        logger = TechnicalDiagnosticLogger(None, None, "test", stream, "host")
        with patch.object(facade, "make_unbound_technical_logger", return_value=(logger, None)):
            with redirect_stderr(io.StringIO()):
                failure, secondary = facade.report_failure(
                    None, RuntimeError("password=secret"), component="COMP", operation="op"
                )
        self.assertEqual("internal_failure", failure.code)
        self.assertIsNone(secondary)
        record = json.loads(stream.getvalue())
        self.assertEqual("unbound", record["project_binding"])
        self.assertNotIn("project_prefix", record)

        stream = io.StringIO()
        logger = TechnicalDiagnosticLogger(None, None, "test", stream, "host")
        with (
            patch.object(facade, "active_selection", side_effect=ValueError("secret")),
            patch.object(facade, "make_unbound_technical_logger", return_value=(logger, None)),
        ):
            _failure, secondary = facade.report_failure(
                self.root, RuntimeError("password=secret"), component="COMP", operation="op"
            )
        self.assertEqual("project binding unavailable", secondary)
        self.assertEqual("unbound", json.loads(stream.getvalue())["project_binding"])

    def test_sink_failure_is_secondary_and_sanitized(self) -> None:
        logger = self._logger(_FailingStream())
        with (
            patch.object(facade, "active_selection", return_value=self.selection),
            patch.object(facade, "make_technical_logger", return_value=(logger, None)),
        ):
            _failure, secondary = facade.report_failure(
                self.root, RuntimeError("password=secret"), component="COMP", operation="op"
            )
        self.assertEqual("technical diagnostic emission failed", secondary)

    def test_structured_warning_is_not_given_a_fake_exception_class(self) -> None:
        stream = io.StringIO()
        logger = self._logger(stream)
        warning = FailureRecord("WARNING", "project_invalid", "safe warning")
        with (
            patch.object(facade, "active_selection", return_value=self.selection),
            patch.object(facade, "make_technical_logger", return_value=(logger, None)),
        ):
            failure, secondary = facade.report_failure(
                self.root, warning, component="COMP", operation="op"
            )
        self.assertIs(warning, failure)
        self.assertIsNone(secondary)
        self.assertNotIn("exception_class", json.loads(stream.getvalue()))

    def test_structured_errors_are_downgraded_without_an_actual_exception(self) -> None:
        stream = io.StringIO()
        logger = self._logger(stream)
        cases = (None, "RuntimeError", "ExplicitBlockingRuntimeFailure")
        with (
            patch.object(facade, "active_selection", return_value=self.selection),
            patch.object(facade, "make_technical_logger", return_value=(logger, None)),
        ):
            for exception_class in cases:
                with self.subTest(exception_class=exception_class):
                    stream.seek(0)
                    stream.truncate(0)
                    synthetic = FailureRecord(
                        "ERROR",
                        "synthetic_error",
                        "safe synthetic",
                        exception_class=exception_class,
                    )
                    failure, secondary = facade.report_failure(
                        self.root, synthetic, component="COMP", operation="op"
                    )
                    self.assertEqual("WARNING", failure.severity)
                    self.assertEqual(exception_class, failure.exception_class)
                    self.assertIsNone(secondary)
                    self.assertEqual("WARNING", json.loads(stream.getvalue())["severity"])

    def test_explicit_blocking_failure_remains_error(self) -> None:
        stream = io.StringIO()
        logger = self._logger(stream)
        error = ExplicitBlockingRuntimeFailure("runtime_blocked", "worker unavailable")
        with (
            patch.object(facade, "active_selection", return_value=self.selection),
            patch.object(facade, "make_technical_logger", return_value=(logger, None)),
        ):
            failure, secondary = facade.report_failure(
                self.root, error, component="COMP", operation="op"
            )
        self.assertEqual(("ERROR", "runtime_blocked"), (failure.severity, failure.code))
        self.assertIsNone(secondary)
        self.assertEqual("ERROR", json.loads(stream.getvalue())["severity"])

    def test_report_does_not_write_journal_or_source_files(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            journal = root / "journal.ndjson"
            source = root / "source.md"
            journal.write_text("old journal\n", encoding="utf-8")
            source.write_text("old source\n", encoding="utf-8")
            before = {path: path.read_bytes() for path in (journal, source)}
            logger = TechnicalDiagnosticLogger(None, None, "test", io.StringIO(), "host")
            with (
                patch.object(facade, "active_selection", side_effect=ValueError("invalid")),
                patch.object(facade, "make_unbound_technical_logger", return_value=(logger, None)),
            ):
                facade.report_failure(
                    root, RuntimeError("secret"), component="COMP", operation="op"
                )
            self.assertEqual(before, {path: path.read_bytes() for path in before})

    def test_cancellation_and_base_exceptions_are_not_swallowed(self) -> None:
        with patch.object(facade, "active_selection", side_effect=FutureCancelledError):
            with self.assertRaises(FutureCancelledError):
                facade.report_failure(
                    self.root, RuntimeError("x"), component="COMP", operation="op"
                )
        with patch.object(facade, "active_selection", side_effect=KeyboardInterrupt):
            with self.assertRaises(KeyboardInterrupt):
                facade.report_failure(
                    self.root, RuntimeError("x"), component="COMP", operation="op"
                )


if __name__ == "__main__":
    unittest.main()
