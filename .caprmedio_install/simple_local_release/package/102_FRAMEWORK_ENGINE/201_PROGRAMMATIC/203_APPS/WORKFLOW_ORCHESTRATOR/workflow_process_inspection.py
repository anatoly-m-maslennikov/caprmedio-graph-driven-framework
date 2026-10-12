"""Read-only fenced coverage for the native and release-host Workflow workers.

The two workers each use a lifecycle singleton ``worker.lock``.  A release
host's shutdown admission lock is intentionally not its start lock, so a zero
worker answer needs all three physical fences: native worker, release-host
worker, and the existing release-host admission fence.  No readiness carrier
is treated as evidence of absence.
"""
from __future__ import annotations

from collections.abc import Mapping
import fcntl
import os
from pathlib import Path
import stat
import time


_NORMAL_PARTS = (".caprmedio_install", "workflow_orchestrator")
_RELEASE_PARTS = (*_NORMAL_PARTS, "release-host")


def _safe_directory(root: Path, parts: tuple[str, ...]) -> Path:
    current = root
    for part in parts:
        current = current / part
        status = os.lstat(current) if os.path.lexists(current) else None
        if status is None:
            current.mkdir(mode=0o700)
            status = os.lstat(current)
        if stat.S_ISLNK(status.st_mode) or not stat.S_ISDIR(status.st_mode):
            raise RuntimeError("workflow worker writer fence is unsafe")
    return current


def _open_worker_lock(directory: Path, name: str) -> int:
    path = directory / "worker.lock"
    descriptor = None
    try:
        descriptor = os.open(path, os.O_RDWR | os.O_CREAT | getattr(os, "O_NOFOLLOW", 0), 0o600)
        if not stat.S_ISREG(os.fstat(descriptor).st_mode):
            raise RuntimeError(f"{name} worker writer fence is unsafe")
        try:
            fcntl.flock(descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as error:
            raise RuntimeError(f"{name} worker writer fence is busy") from error
        return descriptor
    except BaseException:
        if descriptor is not None:
            os.close(descriptor)
        raise


def _close_worker_lock(descriptor: int) -> None:
    try:
        fcntl.flock(descriptor, fcntl.LOCK_UN)
    finally:
        os.close(descriptor)


def collect_legacy_processes(admission: object, deadline: float, *, fenced: bool = False) -> dict[str, object]:
    """Prove zero only while all physical worker-start locks are retained."""
    if not fenced or time.monotonic() >= deadline:
        return {"outcome": "unavailable", "records": []}
    return {"outcome": "complete", "records": []}


class _WorkflowProcessFence:
    """Hold both worker-start locks and the release admission fence."""

    def __init__(self, admission: object, deadline: float) -> None:
        root = getattr(admission, "project_root", None)
        try:
            self._root = Path(root)
            if not self._root.is_absolute() or self._root.is_symlink() or not self._root.is_dir():
                raise ValueError()
        except (TypeError, ValueError, OSError) as error:
            raise RuntimeError("workflow Project is unavailable") from error
        self._admission, self._closed = admission, False
        if time.monotonic() >= deadline:
            raise RuntimeError("workflow provider deadline expired")
        self._normal_descriptor = self._release_descriptor = None
        self._release_fence = None
        try:
            normal = _safe_directory(self._root, _NORMAL_PARTS)
            release = _safe_directory(self._root, _RELEASE_PARTS)
            self._normal_descriptor = _open_worker_lock(normal, "normal")
            self._release_descriptor = _open_worker_lock(release, "release-host")
            remaining = max(0.0, min(30.0, deadline - time.monotonic()))
            if remaining <= 0:
                raise RuntimeError("workflow provider deadline expired")
            from release_host_shutdown import admission_fence
            self._release_fence = admission_fence(self._root, timeout=remaining)
            self._release_fence.__enter__()
        except BaseException:
            if self._release_fence is not None:
                self._release_fence.__exit__(None, None, None)
            if self._release_descriptor is not None:
                _close_worker_lock(self._release_descriptor)
            if self._normal_descriptor is not None:
                _close_worker_lock(self._normal_descriptor)
            raise

    def snapshot(self, deadline: float) -> Mapping[str, object]:
        if self._closed or time.monotonic() >= deadline:
            return {"outcome": "unavailable", "records": []}
        return collect_legacy_processes(self._admission, deadline, fenced=True)

    def close(self) -> None:
        if self._closed:
            return
        self._closed = True
        try:
            if self._release_fence is not None:
                self._release_fence.__exit__(None, None, None)
        finally:
            try:
                if self._release_descriptor is not None:
                    _close_worker_lock(self._release_descriptor)
            finally:
                if self._normal_descriptor is not None:
                    _close_worker_lock(self._normal_descriptor)


def open_legacy_process_fence(admission: object, deadline: float) -> _WorkflowProcessFence:
    """Use the exact normal/start and release-host admission fences, read-only."""
    return _WorkflowProcessFence(admission, deadline)


__all__ = ["collect_legacy_processes", "open_legacy_process_fence"]
