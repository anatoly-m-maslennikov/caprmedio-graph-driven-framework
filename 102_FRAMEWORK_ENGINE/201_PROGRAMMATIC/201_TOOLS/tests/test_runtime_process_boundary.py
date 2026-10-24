"""Focused checks for the direct Tool process boundary."""

from __future__ import annotations

from concurrent.futures import CancelledError as FutureCancelledError
from contextlib import redirect_stderr, redirect_stdout
import io
from pathlib import Path
from types import SimpleNamespace
import sys
import unittest
from unittest.mock import patch


TOOLS = Path(__file__).resolve().parents[1]
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import runtime_process_boundary as boundary  # noqa: E402
from operation_error_boundary import (  # noqa: E402
    ExplicitBlockingRuntimeFailure,
    FailureRecord,
    classify_failure,
)


def _record_report(
    calls: list[tuple[Path | None, Exception | FailureRecord, dict[str, object]]],
    root: Path | None,
    error: Exception | FailureRecord,
    **kwargs: object,
):
    calls.append((root, error, kwargs))
    failure = error if isinstance(error, FailureRecord) else classify_failure(error)
    return failure, None


def _run_boundary(
    calls: list[tuple[Path | None, Exception | FailureRecord, dict[str, object]]],
    callback,
    *,
    operation: str = "test",
    root: Path | None = None,
):
    stdout, stderr = io.StringIO(), io.StringIO()
    with (
        patch.object(
            boundary,
            "report_failure",
            side_effect=lambda bound_root, error, **kwargs: _record_report(
                calls, bound_root, error, **kwargs
            ),
        ),
        redirect_stdout(stdout),
        redirect_stderr(stderr),
    ):
        result = boundary.run_process(callback, operation=operation, root=root)
    return result, stdout.getvalue(), stderr.getvalue()


class RuntimeProcessBoundaryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.calls: list[tuple[Path | None, Exception | FailureRecord, dict[str, object]]] = []

    def _report(self, root: Path | None, error: Exception | FailureRecord, **kwargs: object):
        return _record_report(self.calls, root, error, **kwargs)

    def _run(self, callback, *, operation: str = "test", root: Path | None = None):
        return _run_boundary(self.calls, callback, operation=operation, root=root)

    def test_success_and_native_envelope_are_unchanged(self) -> None:
        envelope = {"ok": True, "result": ["verified"]}
        result, stdout, stderr = self._run(lambda: envelope)
        self.assertIs(envelope, result)
        self.assertEqual(("", ""), (stdout, stderr))
        self.assertEqual([], self.calls)

    def test_partial_stdout_survives_unknown_failure_without_secret_text(self) -> None:
        def callback() -> None:
            print("partial result")
            raise RuntimeError("password=super-secret")

        result, stdout, stderr = self._run(callback)
        self.assertEqual(2, result)
        self.assertEqual("partial result\n", stdout)
        self.assertIn("operation failed", stderr)
        self.assertNotIn("super-secret", stderr)
        self.assertEqual("WARNING", classify_failure(self.calls[0][1]).severity)

    def test_typed_runtime_failure_is_error(self) -> None:
        def callback() -> None:
            raise ExplicitBlockingRuntimeFailure("runtime_blocked", "password=super-secret")

        result, _stdout, stderr = self._run(callback)
        self.assertEqual(2, result)
        self.assertIn("runtime failure", stderr)
        self.assertNotIn("super-secret", stderr)
        self.assertEqual("ERROR", classify_failure(self.calls[0][1]).severity)

    def test_cancellation_and_keyboard_interrupt_propagate(self) -> None:
        with patch.object(boundary, "report_failure", side_effect=self._report):
            with self.assertRaises(FutureCancelledError):
                boundary.run_process(
                    lambda: (_ for _ in ()).throw(FutureCancelledError()), operation="cancel"
                )
            with self.assertRaises(KeyboardInterrupt):
                boundary.run_process(
                    lambda: (_ for _ in ()).throw(KeyboardInterrupt()), operation="interrupt"
                )
        self.assertEqual([], self.calls)

    def test_zero_system_exit_is_unchanged(self) -> None:
        error = SystemExit(0)
        with (
            patch.object(boundary, "report_failure", side_effect=self._report),
            redirect_stderr(io.StringIO()),
        ):
            with self.assertRaises(SystemExit) as raised:
                boundary.run_process(lambda: (_ for _ in ()).throw(error), operation="help")
        self.assertIs(error, raised.exception)
        self.assertEqual([], self.calls)

    def test_nonzero_system_exit_is_logged_without_fake_exception_class(self) -> None:
        error = SystemExit(7)
        with patch.object(boundary, "report_failure", side_effect=self._report):
            with self.assertRaises(SystemExit) as raised:
                boundary.run_process(lambda: (_ for _ in ()).throw(error), operation="invalid")
        self.assertIs(error, raised.exception)
        self.assertEqual(7, raised.exception.code)
        failure = self.calls[0][1]
        self.assertIsInstance(failure, FailureRecord)
        self.assertEqual("WARNING", failure.severity)
        self.assertIsNone(failure.exception_class)

    def test_nonzero_int_is_logged_and_status_is_preserved(self) -> None:
        result, _stdout, _stderr = self._run(lambda: 9, operation="status")
        self.assertEqual(9, result)
        failure = self.calls[0][1]
        self.assertIsInstance(failure, FailureRecord)
        self.assertEqual("WARNING", failure.severity)
        self.assertIsNone(failure.exception_class)
        self.assertEqual(9, failure.details["status"])

    def test_root_binding_uses_only_explicit_flag_or_active_context(self) -> None:
        explicit = Path("/explicit/project")
        with patch.object(
            boundary, "sys", SimpleNamespace(argv=["tool", "--project-root", str(explicit)])
        ):
            self._run(lambda: (_ for _ in ()).throw(RuntimeError("x")))
        self.assertEqual(explicit, self.calls[-1][0])

        active = Path("/active/project")
        with (
            patch.object(boundary, "sys", SimpleNamespace(argv=["tool"])),
            patch.object(boundary, "bound_selection", return_value=SimpleNamespace(root=active)),
        ):
            self._run(lambda: (_ for _ in ()).throw(RuntimeError("x")))
        self.assertEqual(active, self.calls[-1][0])

        with (
            patch.object(
                boundary,
                "sys",
                SimpleNamespace(argv=["tool", "--root", "/one", "--repository", "/two"]),
            ),
            patch.object(boundary, "bound_selection", return_value=SimpleNamespace(root=active)),
        ):
            self._run(lambda: (_ for _ in ()).throw(RuntimeError("x")))
        self.assertIsNone(self.calls[-1][0])


if __name__ == "__main__":
    unittest.main()
