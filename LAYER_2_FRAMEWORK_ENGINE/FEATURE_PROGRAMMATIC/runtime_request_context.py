# CA-M-517@1
"""Bind generic request context for the duration of one runtime call."""

from collections.abc import Iterator
from contextlib import contextmanager
from contextvars import ContextVar
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class RuntimeRequestContext:
    session_id: str | None = None

    def __post_init__(self) -> None:
        if self.session_id is not None and (
            not isinstance(self.session_id, str) or not self.session_id.strip()
        ):
            raise ValueError("session_id must be a non-empty string or None")


_REQUEST_CONTEXT: ContextVar[RuntimeRequestContext | None] = ContextVar(
    "caprmedio_runtime_request_context", default=None
)


@contextmanager
def bind_request_context(context: RuntimeRequestContext) -> Iterator[RuntimeRequestContext]:
    if not isinstance(context, RuntimeRequestContext):
        raise TypeError("context must be a RuntimeRequestContext")
    token = _REQUEST_CONTEXT.set(context)
    try:
        yield context
    finally:
        _REQUEST_CONTEXT.reset(token)


def current_request_context() -> RuntimeRequestContext | None:
    return _REQUEST_CONTEXT.get()
