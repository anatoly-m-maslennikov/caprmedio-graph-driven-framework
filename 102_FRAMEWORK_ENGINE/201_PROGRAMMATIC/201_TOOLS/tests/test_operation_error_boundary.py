"""Focused tests for the shared public-operation error boundary."""

from __future__ import annotations

import asyncio
from concurrent.futures import CancelledError as FutureCancelledError
import io
import json
from pathlib import Path
import sys
import unittest


TOOLS = Path(__file__).resolve().parents[1]
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from atom_operations import ToolError  # noqa: E402
from operation_error_boundary import (  # noqa: E402
    ExplicitBlockingRuntimeFailure,
    FailureRecord,
    classify_failure,
    emit_failure_diagnostic,
    operation_error_boundary,
)
from technical_diagnostics import TechnicalDiagnosticLogger  # noqa: E402


class _FailingStream:
    def write(self, _value: str) -> int:
        raise OSError("diagnostic sink unavailable")

    def flush(self) -> None:
        raise OSError("diagnostic sink unavailable")


class OperationErrorBoundaryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path.cwd()

    def test_sync_domain_failure_is_warning_and_preserves_metadata(self) -> None:
        stream = io.StringIO()

        def on_error(error: Exception) -> dict[str, object]:
            failure = classify_failure(error)
            secondary = emit_failure_diagnostic(
                logger, failure, operation="test_lookup", relative_path="atoms/a.md"
            )
            return {"failure": failure, "secondary": secondary}

        logger = TechnicalDiagnosticLogger("TEST", self.root, "test", stream, "host")

        @operation_error_boundary(on_error=on_error)
        def lookup(value: str) -> dict[str, object]:
            """Preserved function documentation."""
            raise ToolError("bad-atom", value)

        result = lookup("bad")
        self.assertEqual("lookup", lookup.__name__)
        self.assertEqual("Preserved function documentation.", lookup.__doc__)
        self.assertEqual("WARNING", result["failure"].severity)
        self.assertEqual("internal_failure", result["failure"].code)
        record = json.loads(stream.getvalue())
        self.assertEqual("WARNING", record["severity"])
        self.assertEqual("operation_failure", record["event"])
        self.assertEqual("test_lookup", record["operation"])
        self.assertEqual("failed", record["outcome"])

    def test_unknown_runtime_error_is_warning(self) -> None:
        failure = classify_failure(RuntimeError("unexpected"))
        self.assertEqual(
            FailureRecord("WARNING", "internal_failure", "operation failure",
                          exception_class="RuntimeError"),
            failure,
        )
        self.assertEqual("RuntimeError", failure.exception_class)

        stream = io.StringIO()
        logger = TechnicalDiagnosticLogger("TEST", self.root, "test", stream, "host")
        self.assertIsNone(emit_failure_diagnostic(logger, failure, operation="test_lookup"))
        self.assertEqual("RuntimeError", json.loads(stream.getvalue())["exception_class"])
        stream.truncate(0)
        stream.seek(0)
        refusal = FailureRecord("WARNING", "input_invalid", "request refused")
        self.assertIsNone(emit_failure_diagnostic(logger, refusal, operation="test_lookup"))
        record = json.loads(stream.getvalue())
        self.assertEqual("Operation failed: input_invalid", record["reason"])
        self.assertNotIn("exception_class", record)

    def test_explicit_blocking_failure_is_error(self) -> None:
        error = ExplicitBlockingRuntimeFailure("worker-unavailable", "worker unavailable")
        self.assertNotIsInstance(error, RuntimeError)
        failure = classify_failure(error)
        self.assertEqual("ERROR", failure.severity)
        self.assertEqual("worker-unavailable", failure.code)

    def test_explicit_classifier_can_classify_domain_failure(self) -> None:
        failure = classify_failure(
            ToolError("project-invalid", "invalid project"),
            classifier=lambda _error: FailureRecord("WARNING", "project_invalid", "project artifact"),
        )
        self.assertEqual("project_invalid", failure.code)
        self.assertEqual("WARNING", failure.severity)

    def test_custom_classifier_cannot_elevate_nonblocking_failure(self) -> None:
        failure = classify_failure(
            RuntimeError("unexpected"),
            classifier=lambda _error: FailureRecord("ERROR", "claimed_blocking", "not enough"),
        )
        self.assertEqual("WARNING", failure.severity)
        self.assertEqual("claimed_blocking", failure.code)

    def test_async_boundary_preserves_success_and_propagates_cancellation(self) -> None:
        seen: list[Exception] = []

        @operation_error_boundary(on_error=seen.append)
        async def operation(value: int) -> int:
            return value + 1

        self.assertEqual(2, asyncio.run(operation(1)))
        self.assertEqual([], seen)

        @operation_error_boundary(on_error=lambda error: seen.append(error))
        async def cancelled() -> None:
            raise asyncio.CancelledError

        with self.assertRaises(asyncio.CancelledError):
            asyncio.run(cancelled())
        self.assertEqual([], seen)

    def test_sync_boundary_propagates_future_cancellation(self) -> None:
        seen: list[Exception] = []

        @operation_error_boundary(on_error=seen.append)
        def cancelled() -> None:
            raise FutureCancelledError()

        with self.assertRaises(FutureCancelledError):
            cancelled()
        self.assertEqual([], seen)

    def test_diagnostic_sink_failure_is_returned_as_secondary_failure(self) -> None:
        logger = TechnicalDiagnosticLogger("TEST", self.root, "test", _FailingStream(), "host")
        failure = classify_failure(RuntimeError("unexpected"))
        secondary = emit_failure_diagnostic(logger, failure, operation="test_lookup")
        self.assertEqual("technical diagnostic emission failed", secondary)
        self.assertEqual(
            "diagnostic logger unavailable",
            emit_failure_diagnostic(None, failure, operation="test_lookup"),
        )

    def test_diagnostic_failure_does_not_expose_sink_exception_text(self) -> None:
        class SecretStream(_FailingStream):
            def write(self, _value: str) -> int:
                raise OSError("password=super-secret")

        logger = TechnicalDiagnosticLogger("TEST", self.root, "test", SecretStream(), "host")
        failure = classify_failure(RuntimeError("unexpected"))
        secondary = emit_failure_diagnostic(logger, failure, operation="test_lookup")
        self.assertEqual("technical diagnostic emission failed", secondary)

    def test_invalid_severity_is_a_bounded_diagnostic_failure(self) -> None:
        stream = io.StringIO()
        logger = TechnicalDiagnosticLogger("TEST", self.root, "test", stream, "host")
        self.assertEqual(
            "invalid diagnostic severity",
            logger.emit(code="bad", relative_path="", reason="safe", severity="TRACE"),
        )
        self.assertEqual("", stream.getvalue())


if __name__ == "__main__":
    unittest.main()
