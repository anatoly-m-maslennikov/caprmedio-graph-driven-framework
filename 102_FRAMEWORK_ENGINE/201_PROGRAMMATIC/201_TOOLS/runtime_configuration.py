"""Safe handling for mutable target-owned runtime configuration.

The immutable Framework package can supply one admitted TOML default, but the
target-owned ``.caprmedio_runtime/config.toml`` is created only when absent.
This module never renders, merges, or replaces an existing configuration.
"""

from __future__ import annotations

import hashlib
import os
import stat
import tomllib
import uuid
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Literal

from framework_package import FrameworkPackageError, VerifiedFrameworkPackage, verify_framework_package
from installation_transaction import InstallationPublicationLock, InstallationTransactionError


RUNTIME_CONFIGURATION_RELATIVE = Path(".caprmedio_runtime/config.toml")
RUNTIME_CONFIGURATION_DEFAULT_ROLE = "default"
_RUNTIME_DIRECTORY = RUNTIME_CONFIGURATION_RELATIVE.parent
_FORBIDDEN_MEMBER_COMPONENTS = frozenset(
    {
        ".caprmedio_runtime",
        ".caprmedio_tmp",
        ".caprmedio_project",
        ".git",
        "operator_registry",
        "run_records",
        "credentials",
        "secrets",
        "private_settings",
    }
)


class RuntimeConfigurationError(RuntimeError):
    """Stable refusal from the mutable runtime-configuration boundary."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(message)


ConfigurationValidator = Callable[[Mapping[str, Any]], None]


@dataclass(frozen=True)
class _ProjectRoot:
    """A validated Project pathname plus the inode it named at validation."""

    path: Path
    device: int
    inode: int


@dataclass(frozen=True)
class RuntimeConfiguration:
    """Exact bytes and parsed TOML read from the target-owned carrier."""

    path: Path
    payload: bytes
    sha256: str
    document: Mapping[str, Any]


@dataclass(frozen=True)
class RuntimeConfigurationResult:
    """A read/create result without concealing a needed migration."""

    state: Literal["absent", "created", "preserved", "blocked"]
    path: Path
    configuration: RuntimeConfiguration | None
    reason: Literal["migration-needed"] | None = None


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _project_root(value: Path | str) -> _ProjectRoot:
    try:
        supplied = Path(value).expanduser()
        if any(part == ".." for part in supplied.parts):
            raise RuntimeConfigurationError("runtime-config-project-invalid", "Project root must not traverse parents")
        root = Path(os.path.abspath(supplied))
        for candidate in (root, *root.parents):
            if candidate.is_symlink():
                raise RuntimeConfigurationError(
                    "runtime-config-project-unsafe", "Project root contains a symlink ancestor"
                )
        observed = root.lstat()
    except RuntimeConfigurationError:
        raise
    except (OSError, TypeError, ValueError) as error:
        raise RuntimeConfigurationError("runtime-config-project-invalid", "Project root is unavailable") from error
    if root.is_symlink() or not stat.S_ISDIR(observed.st_mode):
        raise RuntimeConfigurationError("runtime-config-project-unsafe", "Project root must be a real directory")
    return _ProjectRoot(path=root, device=observed.st_dev, inode=observed.st_ino)


def _flags(*, directory: bool = False, write: bool = False, create: bool = False, exclusive: bool = False) -> int:
    flags = os.O_CLOEXEC | os.O_NOFOLLOW
    flags |= os.O_WRONLY if write else os.O_RDONLY
    if directory:
        flags |= os.O_DIRECTORY
    if create:
        flags |= os.O_CREAT
    if exclusive:
        flags |= os.O_EXCL
    return flags


def _open_project_root(root: _ProjectRoot) -> int:
    """Anchor the validated Project inode without following a changed ancestor."""

    try:
        descriptor = os.open(root.path.anchor, _flags(directory=True))
    except OSError as error:
        raise RuntimeConfigurationError("runtime-config-project-unsafe", "Project root cannot be safely opened") from error
    try:
        for component in root.path.parts[1:]:
            try:
                next_descriptor = os.open(component, _flags(directory=True), dir_fd=descriptor)
            except OSError as error:
                raise RuntimeConfigurationError(
                    "runtime-config-project-unsafe", "Project root has an unsafe changed ancestor"
                ) from error
            os.close(descriptor)
            descriptor = next_descriptor
        observed = os.fstat(descriptor)
        if not stat.S_ISDIR(observed.st_mode) or (observed.st_dev, observed.st_ino) != (root.device, root.inode):
            raise RuntimeConfigurationError("runtime-config-project-unsafe", "Project root changed after validation")
        return descriptor
    except BaseException:
        os.close(descriptor)
        raise


def _open_runtime_directory(root: _ProjectRoot) -> int | None:
    project_fd = _open_project_root(root)
    try:
        try:
            return os.open(_RUNTIME_DIRECTORY.name, _flags(directory=True), dir_fd=project_fd)
        except FileNotFoundError:
            return None
        except OSError as error:
            raise RuntimeConfigurationError(
                "runtime-config-path-unsafe", "runtime configuration directory is not a real directory"
            ) from error
    finally:
        os.close(project_fd)


def _read_all(descriptor: int) -> bytes:
    chunks: list[bytes] = []
    while True:
        chunk = os.read(descriptor, 65536)
        if not chunk:
            return b"".join(chunks)
        chunks.append(chunk)


def _write_all(descriptor: int, payload: bytes) -> None:
    offset = 0
    while offset < len(payload):
        written = os.write(descriptor, payload[offset:])
        if written <= 0:  # pragma: no cover - defensive OS failure boundary.
            raise OSError("short write while staging runtime configuration")
        offset += written


def _read_config_payload(root: _ProjectRoot) -> bytes | None:
    runtime_fd = _open_runtime_directory(root)
    if runtime_fd is None:
        return None
    try:
        try:
            descriptor = os.open(RUNTIME_CONFIGURATION_RELATIVE.name, _flags(), dir_fd=runtime_fd)
        except FileNotFoundError:
            return None
        except OSError as error:
            raise RuntimeConfigurationError(
                "runtime-config-path-unsafe", "runtime configuration is not a real regular file"
            ) from error
        try:
            observed = os.fstat(descriptor)
            if not stat.S_ISREG(observed.st_mode) or observed.st_nlink != 1:
                raise RuntimeConfigurationError(
                    "runtime-config-path-unsafe", "runtime configuration must be an unaliased regular file"
                )
            return _read_all(descriptor)
        finally:
            os.close(descriptor)
    finally:
        os.close(runtime_fd)


def _configuration_from_payload(
    path: Path, payload: bytes, validator: ConfigurationValidator | None
) -> RuntimeConfiguration:
    try:
        document = tomllib.loads(payload.decode("utf-8"))
    except (UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise RuntimeConfigurationError(
            "runtime-config-migration-needed", "runtime configuration is not compatible TOML and requires migration"
        ) from error
    if not isinstance(document, dict):  # pragma: no cover - tomllib currently returns dict for valid documents.
        raise RuntimeConfigurationError(
            "runtime-config-migration-needed", "runtime configuration is not a TOML table and requires migration"
        )
    if validator is not None:
        try:
            validator(document)
        except Exception as error:
            raise RuntimeConfigurationError(
                "runtime-config-migration-needed", "runtime configuration schema requires migration"
            ) from error
    return RuntimeConfiguration(path=path, payload=payload, sha256=_sha256(payload), document=document)


def _blocked(path: Path, error: RuntimeConfigurationError) -> RuntimeConfigurationResult:
    if error.code != "runtime-config-migration-needed":
        raise error
    return RuntimeConfigurationResult(state="blocked", path=path, configuration=None, reason="migration-needed")


def read_runtime_configuration(
    project_root: Path | str, *, validator: ConfigurationValidator | None = None
) -> RuntimeConfigurationResult:
    """Read target-owned configuration without creating or changing anything.

    The generic configuration schema belongs to the admitted package/authority.
    An optional validator therefore checks that authority's schema without this
    boundary inventing configuration keys or parameter defaults.
    """

    root = _project_root(project_root)
    path = root.path / RUNTIME_CONFIGURATION_RELATIVE
    payload = _read_config_payload(root)
    if payload is None:
        return RuntimeConfigurationResult(state="absent", path=path, configuration=None)
    try:
        configuration = _configuration_from_payload(path, payload, validator)
    except RuntimeConfigurationError as error:
        return _blocked(path, error)
    return RuntimeConfigurationResult(state="preserved", path=path, configuration=configuration)


def _safe_default_member(value: str) -> Path:
    if not isinstance(value, str) or not value:
        raise RuntimeConfigurationError("runtime-config-default-invalid", "default member must be a non-empty path")
    candidate = Path(value)
    if (
        candidate.is_absolute()
        or candidate == Path(".")
        or candidate.as_posix() != value
        or any(part in {"", ".", ".."} for part in candidate.parts)
        or candidate.suffix != ".toml"
    ):
        raise RuntimeConfigurationError("runtime-config-default-invalid", "default member path is unsafe or not TOML")
    for component in candidate.parts:
        lowered = component.lower()
        if lowered in _FORBIDDEN_MEMBER_COMPONENTS or lowered.startswith(".env") or lowered.endswith(".env"):
            raise RuntimeConfigurationError("runtime-config-default-invalid", "default member path is private")
    return candidate


def _reopen_package(package: VerifiedFrameworkPackage) -> VerifiedFrameworkPackage:
    if not isinstance(package, VerifiedFrameworkPackage):
        raise RuntimeConfigurationError("runtime-config-package-invalid", "configuration requires a typed verified package")
    try:
        reopened = verify_framework_package(package.root)
    except FrameworkPackageError as error:
        raise RuntimeConfigurationError("runtime-config-package-invalid", "package could not be physically reopened") from error
    if reopened != package:
        raise RuntimeConfigurationError(
            "runtime-config-package-stale", "typed package handoff differs from physical package bytes"
        )
    return reopened


def _admitted_default(package: VerifiedFrameworkPackage, member: str, validator: ConfigurationValidator | None) -> bytes:
    relative = _safe_default_member(member)
    rows = [row for row in package.inventory if row.path == relative.as_posix()]
    if len(rows) != 1 or rows[0].role != RUNTIME_CONFIGURATION_DEFAULT_ROLE:
        raise RuntimeConfigurationError(
            "runtime-config-default-not-admitted", "requested configuration default is not an admitted default member"
        )
    carrier = package.root / relative
    try:
        directory_fd = os.open(package.root, _flags(directory=True))
    except OSError as error:
        raise RuntimeConfigurationError("runtime-config-default-invalid", "package root cannot be safely reopened") from error
    try:
        for component in relative.parts[:-1]:
            try:
                next_fd = os.open(component, _flags(directory=True), dir_fd=directory_fd)
            except OSError as error:
                raise RuntimeConfigurationError(
                    "runtime-config-default-invalid", "default member has an unsafe ancestor"
                ) from error
            os.close(directory_fd)
            directory_fd = next_fd
        try:
            descriptor = os.open(relative.name, _flags(), dir_fd=directory_fd)
        except OSError as error:
            raise RuntimeConfigurationError("runtime-config-default-invalid", "default member cannot be safely opened") from error
        try:
            observed = os.fstat(descriptor)
            if not stat.S_ISREG(observed.st_mode) or observed.st_nlink != 1:
                raise RuntimeConfigurationError("runtime-config-default-invalid", "default member is not a safe regular file")
            payload = _read_all(descriptor)
        finally:
            os.close(descriptor)
    finally:
        os.close(directory_fd)
    if _sha256(payload) != rows[0].sha256:
        raise RuntimeConfigurationError("runtime-config-default-invalid", "default member differs from admitted bytes")
    try:
        _configuration_from_payload(carrier, payload, validator)
    except RuntimeConfigurationError as error:
        if error.code == "runtime-config-migration-needed":
            raise RuntimeConfigurationError("runtime-config-default-invalid", "default member is not schema-compatible TOML") from error
        raise
    return payload


def _require_creation_lock(lock: InstallationPublicationLock, root: _ProjectRoot) -> None:
    if not isinstance(lock, InstallationPublicationLock):
        raise RuntimeConfigurationError(
            "runtime-config-lock-required", "creating configuration requires the Project installation publication lock"
        )
    if lock.project_root != root.path:
        raise RuntimeConfigurationError(
            "runtime-config-lock-project-mismatch", "installation publication lock belongs to another Project"
        )
    try:
        lock.revalidate()
    except InstallationTransactionError as error:
        raise RuntimeConfigurationError("runtime-config-lock-invalid", "installation publication lock is not active") from error


def _publish_if_absent(root: _ProjectRoot, payload: bytes, lock: InstallationPublicationLock) -> bool:
    """Link a private staged file into place without replacing a raced target."""

    _require_creation_lock(lock, root)
    runtime_fd = _open_runtime_directory(root)
    if runtime_fd is None:
        raise RuntimeConfigurationError(
            "runtime-config-lock-invalid", "active installation lock did not provide the runtime directory"
        )
    stage_name = f".config-stage-{uuid.uuid4().hex}.toml"
    stage_created = False
    try:
        try:
            stage_fd = os.open(stage_name, _flags(write=True, create=True, exclusive=True), 0o600, dir_fd=runtime_fd)
        except OSError as error:
            raise RuntimeConfigurationError("runtime-config-publish-failed", "private configuration staging failed") from error
        stage_created = True
        try:
            _write_all(stage_fd, payload)
            os.fsync(stage_fd)
        finally:
            os.close(stage_fd)
        _require_creation_lock(lock, root)
        try:
            os.link(stage_name, RUNTIME_CONFIGURATION_RELATIVE.name, src_dir_fd=runtime_fd, dst_dir_fd=runtime_fd)
        except FileExistsError:
            return False
        except OSError as error:
            raise RuntimeConfigurationError("runtime-config-publish-failed", "configuration publication failed") from error
        os.fsync(runtime_fd)
        return True
    finally:
        if stage_created:
            try:
                os.unlink(stage_name, dir_fd=runtime_fd)
                os.fsync(runtime_fd)
            except FileNotFoundError:
                pass
            except OSError as error:
                raise RuntimeConfigurationError("runtime-config-publish-failed", "configuration staging cleanup failed") from error
        os.close(runtime_fd)


def ensure_runtime_configuration(
    project_root: Path | str,
    package: VerifiedFrameworkPackage,
    *,
    default_member: str,
    lock: InstallationPublicationLock | None = None,
    validator: ConfigurationValidator | None = None,
) -> RuntimeConfigurationResult:
    """Preserve an existing config or publish exact admitted default bytes once.

    This operation is intentionally suitable for first activation, upgrade,
    rollback, and recovery: only an absent target carrier is created.  A stale
    target observed during publication wins over the staged default and is
    re-read; this helper never replaces it.
    """

    root = _project_root(project_root)
    verified = _reopen_package(package)
    initial = read_runtime_configuration(root.path, validator=validator)
    if initial.state != "absent":
        return initial
    payload = _admitted_default(verified, default_member, validator)
    if lock is None:
        raise RuntimeConfigurationError(
            "runtime-config-lock-required", "creating configuration requires the Project installation publication lock"
        )
    _require_creation_lock(lock, root)
    before_publish = read_runtime_configuration(root.path, validator=validator)
    if before_publish.state != "absent":
        return before_publish
    created = _publish_if_absent(root, payload, lock)
    final = read_runtime_configuration(root.path, validator=validator)
    if final.state == "blocked":
        return final
    if final.state == "absent":
        raise RuntimeConfigurationError("runtime-config-publish-failed", "configuration disappeared after publication")
    if created:
        if final.configuration is None or final.configuration.payload != payload:
            raise RuntimeConfigurationError("runtime-config-publish-failed", "published configuration bytes differ from staged bytes")
        return RuntimeConfigurationResult(state="created", path=final.path, configuration=final.configuration)
    return RuntimeConfigurationResult(state="preserved", path=final.path, configuration=final.configuration)


__all__ = [
    "ConfigurationValidator",
    "RUNTIME_CONFIGURATION_DEFAULT_ROLE",
    "RUNTIME_CONFIGURATION_RELATIVE",
    "RuntimeConfiguration",
    "RuntimeConfigurationError",
    "RuntimeConfigurationResult",
    "ensure_runtime_configuration",
    "read_runtime_configuration",
]
