"""Shared technical diagnostic facade for public runtime failures."""

from __future__ import annotations

from concurrent.futures import CancelledError as FutureCancelledError
from contextvars import ContextVar
from dataclasses import replace
from pathlib import Path

from operation_error_boundary import (
    FailureRecord,
    classify_failure,
    emit_failure_diagnostic,
)
from project_selection import active_selection
from technical_diagnostics import make_technical_logger, make_unbound_technical_logger


_DIAGNOSTIC_SEQUENCE: ContextVar[int] = ContextVar("caprmedio_diagnostic_sequence", default=0)
_LOGGER_UNAVAILABLE = "diagnostic logger unavailable"
_BINDING_UNAVAILABLE = "project binding unavailable"


def diagnostic_sequence() -> int:
    """Return the successful diagnostic count for the current execution context."""
    return _DIAGNOSTIC_SEQUENCE.get()


def _mark_diagnostic_success() -> None:
    _DIAGNOSTIC_SEQUENCE.set(diagnostic_sequence() + 1)


def _classify(error: Exception | FailureRecord) -> FailureRecord:
    if isinstance(error, FailureRecord):
        if error.severity == "ERROR":
            return replace(error, severity="WARNING")
        return error
    if isinstance(error, FutureCancelledError):
        raise error
    if not isinstance(error, Exception):
        raise error
    return classify_failure(error)


def _logger(root: Path, component: str):
    try:
        selection = active_selection(root)
        logger, _error = make_technical_logger(selection.settings, root)
        return replace(logger, component=component) if logger is not None else None
    except FutureCancelledError:
        raise
    except Exception:
        return None


def _unbound_logger(component: str):
    try:
        logger, _error = make_unbound_technical_logger(component=component)
        return logger
    except FutureCancelledError:
        raise
    except Exception:
        return None


def _emit(logger, failure: FailureRecord, operation: str, correlation_id: str | None) -> str | None:
    try:
        secondary = emit_failure_diagnostic(
            logger, failure, operation=operation, correlation_id=correlation_id
        )
    except FutureCancelledError:
        raise
    except Exception:
        return "technical diagnostic emission failed"
    if secondary is None:
        _mark_diagnostic_success()
    return secondary


def report_failure(
    root: Path | None,
    error: Exception | FailureRecord,
    *,
    component: str,
    operation: str,
    correlation_id: str | None = None,
) -> tuple[FailureRecord, str | None]:
    """Classify a failure and emit one sanitized diagnostic when bound."""
    failure = _classify(error)
    if root is None:
        logger = _unbound_logger(component)
        if logger is None:
            return failure, _LOGGER_UNAVAILABLE
        return failure, _emit(logger, failure, operation, correlation_id)
    logger = _logger(root, component)
    if logger is None:
        logger = _unbound_logger(component)
        if logger is None:
            return failure, _LOGGER_UNAVAILABLE
        secondary = _emit(logger, failure, operation, correlation_id)
        return failure, secondary or _BINDING_UNAVAILABLE
    return failure, _emit(logger, failure, operation, correlation_id)


__all__ = ["diagnostic_sequence", "report_failure"]
