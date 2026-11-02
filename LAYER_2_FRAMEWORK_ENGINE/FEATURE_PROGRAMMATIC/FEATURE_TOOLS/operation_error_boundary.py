"""Small shared boundary for observable public-operation failures."""

from __future__ import annotations

from collections.abc import Callable, Mapping
from concurrent.futures import CancelledError as FutureCancelledError
from dataclasses import dataclass, field, replace
from functools import wraps
import inspect
from typing import Any, Literal, ParamSpec, TypeVar, cast

from technical_diagnostics import TechnicalDiagnosticLogger


P = ParamSpec("P")
R = TypeVar("R")
Severity = Literal["WARNING", "ERROR"]
FailureClassifier = Callable[[Exception], "FailureRecord | None"]


class ExplicitBlockingRuntimeFailure(Exception):
    """A caller-declared runtime failure that prevents safe operation."""

    def __init__(self, code: str, message: str, details: Mapping[str, object] | None = None) -> None:
        self.code = code
        self.message = message
        self.details = dict(details or {})
        super().__init__(message)


@dataclass(frozen=True, slots=True)
class FailureRecord:
    """A caller-neutral classification; the caller still owns its response shape."""

    severity: Severity
    code: str
    message: str
    details: Mapping[str, object] = field(default_factory=dict)
    diagnostic_error: str | None = None
    exception_class: str | None = None


def classify_failure(error: Exception, *, classifier: FailureClassifier | None = None) -> FailureRecord:
    """Classify without treating Python exception ancestry as impact.

    Only ``ExplicitBlockingRuntimeFailure`` can produce an ``ERROR`` record;
    caller classifiers may refine every other failure, but cannot elevate it.
    """

    if isinstance(error, ExplicitBlockingRuntimeFailure):
        return FailureRecord("ERROR", error.code, error.message, error.details,
                             exception_class=type(error).__name__)
    if classifier is not None:
        classified = classifier(error)
        if classified is not None:
            classified = replace(classified, exception_class=type(error).__name__)
            return (classified if classified.severity == "WARNING"
                    else replace(classified, severity="WARNING"))
    return FailureRecord("WARNING", "internal_failure", "operation failure",
                         exception_class=type(error).__name__)


def emit_failure_diagnostic(
    logger: TechnicalDiagnosticLogger | None,
    failure: FailureRecord,
    *,
    operation: str,
    relative_path: str = "",
    correlation_id: str | None = None,
) -> str | None:
    """Emit a safe technical record and return a secondary sink failure, if any."""

    if logger is None:
        return "diagnostic logger unavailable"
    try:
        sink_failure = logger.emit(
            code=failure.code,
            relative_path=relative_path,
            reason=(f"Operation failed: {failure.code}"
                    + (f" ({failure.exception_class})" if failure.exception_class else "")),
            severity=failure.severity,
            event="operation_failure",
            operation=operation,
            outcome="blocked" if failure.severity == "ERROR" else "failed",
            exception_class=failure.exception_class,
            correlation_id=correlation_id,
        )
        return "technical diagnostic emission failed" if sink_failure else None
    except Exception:
        return "technical diagnostic emission failed"


def operation_error_boundary(
    *,
    on_error: Callable[[Exception], R],
) -> Callable[[Callable[P, Any]], Callable[P, R]]:
    """Return a sync/async boundary that delegates response construction to its caller."""

    def decorate(function: Callable[P, Any]) -> Callable[P, R]:
        if inspect.iscoroutinefunction(function):

            @wraps(function)
            async def async_wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
                try:
                    return await function(*args, **kwargs)
                except FutureCancelledError:
                    raise
                except Exception as error:
                    return on_error(error)

            return cast(Callable[P, R], async_wrapper)

        @wraps(function)
        def sync_wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            try:
                return function(*args, **kwargs)
            except FutureCancelledError:
                raise
            except Exception as error:
                return on_error(error)

        return sync_wrapper

    return decorate


__all__ = [
    "ExplicitBlockingRuntimeFailure",
    "FailureClassifier",
    "FailureRecord",
    "classify_failure",
    "emit_failure_diagnostic",
    "operation_error_boundary",
]
