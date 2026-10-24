"""Small compare-and-swap file primitives for host installation."""

from __future__ import annotations

import os
from pathlib import Path
import stat
import tempfile


_MAX_FILE_BYTES = 4 * 1024 * 1024


class HostInstallationError(ValueError):
    """A bounded, actionable host-installation failure."""

    def __init__(
        self, code_or_message: str, message: str | None = None, *, code: str | None = None
    ) -> None:
        if code is not None:
            if message is not None:
                raise TypeError("HostInstallationError accepts one message and one code")
            self.code, self.message = code, code_or_message
        else:
            self.code = code_or_message if message is not None else "installation-failed"
            self.message = code_or_message if message is None else message
        super().__init__(self.message)


def _canonical(path: Path) -> Path:
    path = Path(path).expanduser()
    try:
        resolved = path.resolve(strict=False)
    except (OSError, RuntimeError) as error:
        raise HostInstallationError(
            "invalid-path", "Host installation path is not canonical"
        ) from error
    if not path.is_absolute() or path != resolved:
        raise HostInstallationError(
            "invalid-path", "Host installation paths must be absolute and canonical"
        )
    current = path.parent
    while True:
        try:
            info = current.lstat()
        except FileNotFoundError:
            pass
        except OSError as error:
            raise HostInstallationError(
                "invalid-path", "Host installation parent is unavailable"
            ) from error
        else:
            if stat.S_ISLNK(info.st_mode) or not stat.S_ISDIR(info.st_mode):
                raise HostInstallationError(
                    "invalid-path", "Host installation ancestors must be real directories"
                )
        if current.parent == current:
            break
        current = current.parent
    return path


def _state(path: Path) -> tuple[bytes | None, int | None]:
    _canonical(path)
    try:
        info = path.lstat()
    except FileNotFoundError:
        return None, None
    except OSError as error:
        raise HostInstallationError("read-failed", f"Cannot inspect host file: {path}") from error
    if stat.S_ISLNK(info.st_mode) or not stat.S_ISREG(info.st_mode):
        raise HostInstallationError("invalid-target", f"Host target is not a regular file: {path}")
    if info.st_size > _MAX_FILE_BYTES:
        raise HostInstallationError(
            "file-too-large", f"Host target exceeds {_MAX_FILE_BYTES} bytes: {path}"
        )
    try:
        return path.read_bytes(), stat.S_IMODE(info.st_mode)
    except OSError as error:
        raise HostInstallationError("read-failed", f"Cannot read host file: {path}") from error


def _fsync_directory(path: Path) -> None:
    try:
        descriptor = os.open(path, os.O_RDONLY)
    except OSError:
        return
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def _atomic_write(path: Path, content: bytes, mode: int) -> None:
    descriptor = -1
    temporary: str | None = None
    try:
        _canonical(path).parent.mkdir(parents=True, exist_ok=True)
        descriptor, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
        with os.fdopen(descriptor, "wb") as stream:
            descriptor = -1
            stream.write(content)
            stream.flush()
            if hasattr(os, "fchmod"):
                os.fchmod(stream.fileno(), mode)
            else:  # pragma: no cover - Windows lacks fchmod.
                os.chmod(temporary, mode)
            os.fsync(stream.fileno())
        os.replace(temporary, path)
        temporary = None
        _fsync_directory(path.parent)
    except OSError as error:
        raise HostInstallationError(
            "write-failed", f"Cannot atomically write host file: {path}"
        ) from error
    finally:
        if descriptor >= 0:
            os.close(descriptor)
        if temporary is not None:
            try:
                os.unlink(temporary)
            except FileNotFoundError:
                pass


class FileUpdate:
    """Snapshot one canonical file and apply it with byte-level CAS rollback."""

    def __init__(self, path: Path, content: bytes, mode: int = 0o600) -> None:
        self.path = _canonical(path)
        if not isinstance(content, bytes):
            raise TypeError("FileUpdate content must be bytes")
        if not isinstance(mode, int) or mode < 0 or mode > 0o777:
            raise ValueError("FileUpdate mode must be an integer file mode")
        self.content = content
        self.mode = stat.S_IMODE(mode)
        self._prior_bytes, self._prior_mode = _state(self.path)
        self._write_mode = self._prior_mode if self._prior_mode is not None else self.mode
        self.changed = self._prior_bytes != self.content
        self._applied = False

    @property
    def previous_content(self) -> bytes | None:
        return self._prior_bytes

    def apply(self) -> None:
        current = _state(self.path)
        if self._applied:
            if current != (self.content, self._write_mode):
                raise HostInstallationError(
                    "concurrent-change", f"Host file changed after apply: {self.path}"
                )
            return
        if current != (self._prior_bytes, self._prior_mode):
            raise HostInstallationError(
                "concurrent-change", f"Host file changed since preflight: {self.path}"
            )
        if self.changed:
            _atomic_write(self.path, self.content, self._write_mode)
            self._applied = True

    def restore(self) -> None:
        if not self._applied:
            return
        try:
            current = _state(self.path)
        except HostInstallationError as error:
            raise HostInstallationError(
                "restore-conflict", f"Cannot verify own host-file write: {self.path}"
            ) from error
        if current != (self.content, self._write_mode):
            raise HostInstallationError(
                "restore-conflict", f"Refusing concurrent host-file overwrite: {self.path}"
            )
        if self._prior_bytes is None:
            try:
                self.path.unlink()
                _fsync_directory(self.path.parent)
            except OSError as error:
                raise HostInstallationError(
                    "restore-failed", f"Cannot remove host file: {self.path}"
                ) from error
        else:
            _atomic_write(
                self.path,
                self._prior_bytes,
                self._prior_mode if self._prior_mode is not None else 0o600,
            )
        self._applied = False


__all__ = ["FileUpdate", "HostInstallationError"]
