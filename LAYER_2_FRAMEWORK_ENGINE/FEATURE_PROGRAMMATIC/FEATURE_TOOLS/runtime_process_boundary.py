"""One thin failure boundary for directly executed Project Tools."""

from __future__ import annotations

from collections.abc import Callable
from concurrent.futures import CancelledError as FutureCancelledError
from pathlib import Path
import sys
from typing import Any

from operation_error_boundary import FailureRecord, operation_error_boundary
from project_selection import bound_selection
from runtime_failure_diagnostics import diagnostic_sequence, report_failure


_COMPONENT = "TOOL_PROCESS"
_ROOT_FLAGS = ("--project-root", "--repository", "--root")


def _explicit_cli_root() -> tuple[bool, Path | None]:
    values: list[str] = []
    seen = False
    arguments = sys.argv[1:]
    index = 0
    while index < len(arguments):
        argument = arguments[index]
        matched = next((flag for flag in _ROOT_FLAGS if argument == flag), None)
        if matched is not None:
            seen = True
            if index + 1 >= len(arguments) or arguments[index + 1].startswith("-"):
                return True, None
            values.append(arguments[index + 1])
            index += 2
            continue
        matched = next((flag for flag in _ROOT_FLAGS if argument.startswith(flag + "=")), None)
        if matched is not None:
            seen = True
            value = argument[len(matched) + 1 :]
            if not value:
                return True, None
            values.append(value)
        index += 1
    if not seen or not values or len(set(values)) != 1:
        return seen, None
    try:
        return True, Path(values[0])
    except TypeError, ValueError:
        return True, None


def _diagnostic_root(root: Path | None) -> Path | None:
    if root is not None:
        return root
    explicit, value = _explicit_cli_root()
    if explicit:
        return value
    try:
        selection = bound_selection()
    except FutureCancelledError:
        raise
    except Exception:
        return None
    return selection.root if selection is not None else None


def _report(
    root: Path | None, error: Exception | FailureRecord, operation: str
) -> tuple[FailureRecord | None, str | None]:
    try:
        return report_failure(root, error, component=_COMPONENT, operation=operation)
    except FutureCancelledError:
        raise
    except Exception:
        return None, "diagnostic logger unavailable"


def _stderr(message: str) -> None:
    try:
        sys.stderr.write(message)
        sys.stderr.flush()
    except Exception:
        pass


def _failure_text(failure: FailureRecord | None, secondary: str | None) -> str:
    if failure is not None and failure.severity == "ERROR":
        text = "caprmedio: runtime failure\n"
    else:
        text = "caprmedio: operation failed\n"
    if secondary is not None:
        text += "caprmedio: technical diagnostics unavailable\n"
    return text


def _handle_exception(root: Path | None, error: Exception, operation: str) -> int:
    failure, secondary = _report(root, error, operation)
    _stderr(_failure_text(failure, secondary))
    return 2


def _synthetic_exit(status: object) -> FailureRecord:
    details: dict[str, Any] = {}
    if isinstance(status, int) and not isinstance(status, bool):
        details["status"] = status
    return FailureRecord(
        "WARNING",
        "process_nonzero_exit",
        "process exited with a non-zero status",
        details=details,
    )


def _handle_exit(root: Path | None, status: object, operation: str) -> None:
    failure, secondary = _report(root, _synthetic_exit(status), operation)
    if secondary is not None:
        _stderr("caprmedio: technical diagnostics unavailable\n")
    elif failure is None:
        _stderr("caprmedio: process exited with a non-zero status\n")


def _nonzero_status(status: object) -> bool:
    return status is not None and (not isinstance(status, int) or status != 0)


def run_process(
    callback: Callable[[], object], *, operation: str, root: Path | None = None
) -> object:
    """Run one direct entrypoint without changing its stdout or result contract."""
    diagnostic_root = _diagnostic_root(root)
    callback_failed = False
    sequence_before = diagnostic_sequence()

    def on_error(error: Exception) -> int:
        nonlocal callback_failed
        callback_failed = True
        return _handle_exception(diagnostic_root, error, operation)

    guarded = operation_error_boundary(on_error=on_error)(callback)
    try:
        result = guarded()
    except FutureCancelledError:
        raise
    except SystemExit as error:
        if _nonzero_status(error.code) and diagnostic_sequence() == sequence_before:
            _handle_exit(diagnostic_root, error.code, operation)
        raise

    if (
        not callback_failed
        and isinstance(result, int)
        and not isinstance(result, bool)
        and result != 0
        and diagnostic_sequence() == sequence_before
    ):
        failure, secondary = _report(diagnostic_root, _synthetic_exit(result), operation)
        if secondary is not None:
            _stderr("caprmedio: technical diagnostics unavailable\n")
        elif failure is None:
            _stderr("caprmedio: process exited with a non-zero status\n")
    return result


__all__ = ["run_process"]
