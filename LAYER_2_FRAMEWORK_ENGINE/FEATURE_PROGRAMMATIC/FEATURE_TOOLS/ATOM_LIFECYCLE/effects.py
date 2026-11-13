# CA-M-405@14
# CA-M-409@14
# CA-M-422@13
# CA-D-625@14

"""Private mechanical effects for already admitted lifecycle operations.

Callers must exclude concurrent writers to pinned source files: portable file APIs
cannot conditionally replace or unlink by digest. Lifecycle choices belong to the
caller; this module accepts explicit, project-contained paths and bytes only.
"""
from __future__ import annotations

from .timing import trace

import hashlib
import os
import re
import stat
from contextlib import nullcontext
from dataclasses import dataclass, field
from pathlib import Path

from project_runtime import atomic_tempfile


@dataclass
class Result:
    effects: list[dict] = field(default_factory=list)
    errors: list[dict] = field(default_factory=list)


def _error(result: Result, code: str, message: str) -> None:
    result.errors.append({"code": code, "message": message, "field": None})


def _effect(result: Result, operation: str, target: str, state: str, evidence: str) -> None:
    result.effects.append({"operation": operation, "target": target, "state": state, "evidence": evidence})


def _parent(root: Path, path: Path) -> tuple[int, str, str]:
    """Open each directory without following symlinks and retain the parent fd."""
    root = Path(os.path.abspath(root))
    path = Path(path)
    if not path.is_absolute():
        path = root / path
    # Do not normalize away traversal: reject it even if it would remain inside.
    try:
        relative = path.relative_to(root)
    except ValueError as exc:
        raise ValueError("carrier outside project") from exc
    if not relative.parts or any(part in (".", "..") for part in relative.parts):
        raise ValueError("invalid project-relative carrier path")
    flags = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW
    fd = os.open(root, flags)
    try:
        for part in relative.parts[:-1]:
            child = os.open(part, flags, dir_fd=fd)
            os.close(fd)
            fd = child
        return fd, relative.name, relative.as_posix()
    except BaseException:
        os.close(fd)
        raise


def _read(parent: int, name: str) -> bytes:
    fd = os.open(name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=parent)
    with os.fdopen(fd, "rb") as stream:
        if not stat.S_ISREG(os.fstat(stream.fileno()).st_mode):
            raise ValueError("carrier is not a regular file")
        return stream.read()


def _pinned(parent: int, name: str, digest: str) -> bytes:
    data = _read(parent, name)
    if hashlib.sha256(data).hexdigest() != digest:
        raise ValueError("stale source")
    return data


def _reader(path: Path):
    from project_selection import bound_selection
    from . import source
    get_reader = getattr(source, "query_reader", None)
    reader = get_reader() if get_reader is not None else None
    if reader is None:
        return None
    selection = bound_selection()
    prefix = re.escape(selection.settings["artifacts"]["identity"]["project_prefix"]) if selection else ".+"
    return reader if re.fullmatch(rf"(?:[0-9]+-)?{prefix}-[A-Z]-.*\.md", path.name) else None



def publication_guard():
    """Keep paired lifecycle effects invisible to the Workbench watcher until complete."""
    from .source import query_reader
    reader = query_reader()
    publication = getattr(reader, 'lifecycle_publication', None)
    if callable(publication):
        return publication()
    lock = getattr(reader, 'lifecycle_file_effect', None)
    return lock() if callable(lock) else nullcontext()


def _query_read(reader, root: Path, path: Path, parent: int, name: str) -> bytes:
    """Keep the descriptor-pinned carrier stable across the Workbench read."""
    checked_parent, checked_name, _ = _parent(root, path)
    try:
        actual = os.fstat(checked_parent)
        expected = os.fstat(parent)
        if checked_name != name or (actual.st_dev, actual.st_ino) != (expected.st_dev, expected.st_ino):
            raise ValueError("carrier parent changed")
    finally:
        os.close(checked_parent)
    descriptor = os.open(name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=parent)
    try:
        before = os.fstat(descriptor)
        if not stat.S_ISREG(before.st_mode):
            raise ValueError("carrier is not a regular file")
        try:
            data = reader.lifecycle_read(Path(root).absolute() / path, descriptor=descriptor)
        except Exception as exc:
            raise RuntimeError("Workbench carrier read failed") from exc
        actual = os.fstat(descriptor)
        after = os.stat(name, dir_fd=parent, follow_symlinks=False)
        if ((after.st_dev, after.st_ino) != (actual.st_dev, actual.st_ino)
                or (before.st_size, before.st_mtime_ns) != (actual.st_size, actual.st_mtime_ns)):
            raise ValueError("carrier changed during Workbench read")
    finally:
        os.close(descriptor)
    if not isinstance(data, bytes):
        raise RuntimeError("Workbench carrier read returned invalid bytes")
    checked_parent, _, _ = _parent(root, path)
    try:
        actual = os.fstat(checked_parent)
        expected = os.fstat(parent)
        if (actual.st_dev, actual.st_ino) != (expected.st_dev, expected.st_ino):
            raise ValueError("carrier parent changed")
    finally:
        os.close(checked_parent)
    return data


def _read_pinned(reader, root: Path, path: Path, parent: int, name: str, digest: str) -> bytes:
    if reader is None:
        return _pinned(parent, name, digest)
    data = _query_read(reader, root, path, parent, name)
    if hashlib.sha256(data).hexdigest() != digest:
        raise ValueError("stale source")
    return data


def _changed(reader, old: Path | None, new: Path | None) -> None:
    if reader is not None:
        try:
            reader.lifecycle_changed(old, new)
        except Exception as exc:
            raise RuntimeError("Workbench synchronization failed") from exc


def _message(exc: Exception) -> str:
    # Do not disclose host paths carried by filesystem exceptions.
    if isinstance(exc, RuntimeError) and str(exc) in {
        "Workbench carrier read failed", "Workbench carrier read returned invalid bytes",
        "Workbench synchronization failed",
    }:
        return str(exc)
    return str(exc) if isinstance(exc, ValueError) else f"filesystem operation failed ({type(exc).__name__})"


def _cleanup_temp(root: Path, temp: str | None, result: Result) -> None:
    if temp is None:
        return
    try:
        os.unlink(temp)
    except FileNotFoundError:
        pass
    except OSError:
        # Staging is under project temp; report its project-relative path.
        try:
            retained = Path(temp).relative_to(Path(root).absolute()).as_posix()
        except ValueError:
            retained = ".caprmedio_tmp (path unavailable)"
        _error(result, "backend_failure", f"temporary carrier retained at {retained}")


def _write(root: Path, path: Path, data: bytes, expected: str | None, result: Result) -> None:
    temp = None
    parent = None
    committed = False
    operation = "create" if expected is None else "modify"
    target = None
    try:
        parent, name, target = _parent(root, path)
        destination = Path(root).absolute() / target
        reader = _reader(destination)
        if expected is not None:
            old = _read_pinned(reader, root, destination, parent, name, expected)
            if old == data:
                return
        fd, temp = atomic_tempfile(destination, "atom_lifecycle", repository=root)
        with os.fdopen(fd, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        if expected is None:
            lock = getattr(reader, 'lifecycle_file_effect', None)
            with lock() if callable(lock) else nullcontext():
                os.link(temp, name, dst_dir_fd=parent, follow_symlinks=False)
                committed = True
                # Removing the staging link changes the published inode's ctime.
                # Keep watcher reads out until the inode is stable.
                staging, temp = temp, None
                os.unlink(staging)
        else:
            _read_pinned(reader, root, destination, parent, name, expected)
            os.replace(temp, name, dst_dir_fd=parent)
            temp = None
            committed = True
        _changed(reader, destination if expected is not None else None, destination)
        readback = _query_read(reader, root, destination, parent, name) if reader is not None else _read(parent, name)
        if readback != data:
            raise OSError("readback differs")
        _effect(result, operation, target, "known", hashlib.sha256(data).hexdigest())
    except (OSError, ValueError, RuntimeError) as exc:
        if committed:
            _effect(result, operation, target, "unknown", "publication occurred but synchronization or readback failed")
            _error(result, "effect_uncertain", _message(exc))
        else:
            _error(result, "stale_state" if isinstance(exc, (ValueError, FileExistsError)) else "backend_failure", _message(exc))
    finally:
        if parent is not None:
            os.close(parent)
        _cleanup_temp(root, temp, result)


@trace('filesystem.create')
def create(root: Path, path: Path, content: bytes) -> Result:
    result = Result()
    _write(Path(root), Path(path), content, None, result)
    return result


@trace('filesystem.replace')
def replace(root: Path, path: Path, expected_sha256: str, content: bytes) -> Result:
    result = Result()
    _write(Path(root), Path(path), content, expected_sha256, result)
    return result


@trace('filesystem.remove')
def remove(root: Path, path: Path, expected_sha256: str) -> Result:
    result = Result()
    parent = None
    committed = False
    target = None
    try:
        parent, name, target = _parent(Path(root), Path(path))
        destination = Path(root).absolute() / target
        reader = _reader(destination)
        _read_pinned(reader, Path(root), destination, parent, name, expected_sha256)
        os.unlink(name, dir_fd=parent)
        committed = True
        _changed(reader, destination, None)
        try:
            os.stat(name, dir_fd=parent, follow_symlinks=False)
        except FileNotFoundError:
            pass
        else:
            raise OSError("source remains after removal")
        _effect(result, "remove", target, "known", f"absent after removal; prior sha256 {expected_sha256}")
    except (OSError, ValueError, RuntimeError) as exc:
        if committed:
            _effect(result, "remove", target, "unknown", "removal occurred but synchronization or readback failed")
            _error(result, "effect_uncertain", _message(exc))
        else:
            _error(result, "stale_state" if isinstance(exc, ValueError) else "backend_failure", _message(exc))
    finally:
        if parent is not None:
            os.close(parent)
    return result


def relocate(root: Path, source: Path, expected_sha256: str, destination: Path) -> Result:
    result = Result()
    parent = None
    try:
        parent, name, target = _parent(Path(root), Path(source))
        source_path = Path(root).absolute() / target
        content = _read_pinned(_reader(source_path), Path(root), source_path, parent, name, expected_sha256)
    except (OSError, ValueError, RuntimeError) as exc:
        _error(result, "stale_state" if isinstance(exc, ValueError) else "backend_failure", _message(exc))
        return result
    finally:
        if parent is not None:
            os.close(parent)
    _write(Path(root), Path(destination), content, None, result)
    if not result.errors:
        removed = remove(root, source, expected_sha256)
        result.effects.extend(removed.effects)
        result.errors.extend(removed.errors)
    return result
