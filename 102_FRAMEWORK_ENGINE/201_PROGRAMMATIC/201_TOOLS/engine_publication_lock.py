"""Reentrant Engine ownership of the existing Project-root publication lock."""

from __future__ import annotations

from contextlib import contextmanager
from contextvars import ContextVar
import math
import os
from pathlib import Path
import threading

from RELEASE_VERSION.selector_publication_lock import (
    SelectorPublicationLockError as EnginePublicationLockError,
    selector_publication_lock,
)


_HELD: ContextVar[tuple] = ContextVar("engine_publication_locks", default=())
_LIVE: dict[object, tuple] = {}


@contextmanager
def engine_publication_lock(root: Path | str, *, timeout_seconds: float = 30):
    """Nest only within the same process/thread's actual acquired boundary."""
    if (isinstance(timeout_seconds, bool) or not isinstance(timeout_seconds, (int, float))
            or not math.isfinite(timeout_seconds) or not 0 <= timeout_seconds <= 30):
        raise EnginePublicationLockError("selector-publication-lock-invalid", "timeout must be within [0, 30]")
    identity = (Path(root).absolute(), os.getpid(), threading.get_ident())
    if any(owner == identity and _LIVE.get(acquisition) == identity
           for owner, acquisition in _HELD.get()):
        yield
        return
    with selector_publication_lock(root, timeout_seconds=timeout_seconds):
        acquisition = object()
        _LIVE[acquisition] = identity
        token = _HELD.set((*_HELD.get(), (identity, acquisition)))
        try:
            yield
        finally:
            _LIVE.pop(acquisition, None)
            _HELD.reset(token)
