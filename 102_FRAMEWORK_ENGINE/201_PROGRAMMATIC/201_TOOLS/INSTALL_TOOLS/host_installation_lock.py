"""Nonblocking advisory locks for one host-installation scope."""

from __future__ import annotations

from contextlib import contextmanager
import errno
import os
from pathlib import Path
import stat
from typing import Iterator

from INSTALL_TOOLS.host_installation_io import HostInstallationError, _canonical

try:
    import fcntl
except ImportError:
    fcntl = None


def _prepare_directory(directory: Path) -> Path:
    directory = _canonical(directory)
    try:
        directory.mkdir(parents=True, exist_ok=True)
    except OSError as error:
        raise HostInstallationError(
            "lock-failed", "Cannot create installation lock directory"
        ) from error
    return _canonical(directory)


def _validate_name(name: str) -> str:
    if not isinstance(name, str) or not name or Path(name).name != name:
        raise HostInstallationError("invalid-lock", "Installation lock name must be a file name")
    return name


def _lock_path(root: Path, name: str) -> Path:
    path = root / _validate_name(name)
    try:
        info = path.lstat()
    except FileNotFoundError:
        return path
    except OSError as error:
        raise HostInstallationError("invalid-lock", "Installation lock is unavailable") from error
    if stat.S_ISLNK(info.st_mode) or not stat.S_ISREG(info.st_mode):
        raise HostInstallationError("invalid-lock", "Installation lock must be a regular file")
    return path


def _acquire(lock_path: Path) -> int:
    flags = os.O_CREAT | os.O_RDWR | os.O_NONBLOCK
    if hasattr(os, "O_NOFOLLOW"):
        flags |= os.O_NOFOLLOW
    try:
        descriptor = os.open(lock_path, flags, 0o600)
    except OSError as error:
        if error.errno == errno.ELOOP:
            raise HostInstallationError(
                "invalid-lock", "Installation lock must not be a symlink"
            ) from error
        raise HostInstallationError("lock-failed", "Cannot open installation lock") from error
    try:
        info = os.fstat(descriptor)
        if not stat.S_ISREG(info.st_mode):
            raise HostInstallationError("invalid-lock", "Installation lock must be a regular file")
        fcntl.flock(descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError as error:
        os.close(descriptor)
        if error.errno in (errno.EACCES, errno.EAGAIN):
            raise HostInstallationError(
                "installation-busy", "Installation lock is already held"
            ) from error
        raise HostInstallationError("lock-failed", "Cannot acquire installation lock") from error
    except BaseException:
        os.close(descriptor)
        raise
    return descriptor


@contextmanager
def installation_lock(directory: Path, name: str = ".caprmedio-install.lock") -> Iterator[None]:
    """Acquire one POSIX lock without waiting or retrying when it is busy."""

    if fcntl is None:
        raise HostInstallationError("lock-unsupported", "Installation locking requires POSIX flock")
    name = _validate_name(name)
    root = _prepare_directory(directory)
    lock_path = _lock_path(root, name)
    descriptor = _acquire(lock_path)
    try:
        yield
    finally:
        os.close(descriptor)


__all__ = ["installation_lock"]
