"""Read the machine-local shared MCP host configuration."""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import os
from pathlib import Path
import stat
import tomllib
from typing import Any


_MAX_CONFIG_BYTES = 4 * 1024
_MAX_LOADED_PROJECTS = 64
_READ_LIMITS = {
    "max_candidates": 1,
    "max_file_bytes": _MAX_CONFIG_BYTES,
    "max_total_read_bytes": 2 * _MAX_CONFIG_BYTES,
    "timeout_seconds": 5,
    "max_findings": 1,
}


class HostRuntimeConfigError(ValueError):
    """The shared host configuration cannot be trusted or resolved."""


def _error(message: str) -> HostRuntimeConfigError:
    return HostRuntimeConfigError(message)


def _path(value: Path | str, *, absolute: bool = False) -> Path:
    if not isinstance(value, (Path, str)) or not str(value) or "\x00" in str(value):
        raise _error("Host runtime path is invalid")
    try:
        raw = Path(value).expanduser()
        if ".." in raw.parts or (absolute and not raw.is_absolute()):
            raise _error("Host runtime path is unsafe")
        return Path(os.path.abspath(raw))
    except HostRuntimeConfigError:
        raise
    except (OSError, RuntimeError, TypeError, ValueError) as error:
        raise _error("Host runtime path is unavailable or unsafe") from error


def _canonical_directory(value: Path | str, *, reject_filesystem_root: bool = False) -> Path:
    path = _path(value, absolute=True)
    try:
        if path.resolve(strict=True) != path:
            raise _error("Host runtime directory must be canonical")
        info = path.stat()
        if not stat.S_ISDIR(info.st_mode) or (reject_filesystem_root and path.parent == path):
            raise _error("Host runtime directory is invalid")
        return path
    except HostRuntimeConfigError:
        raise
    except (OSError, RuntimeError, ValueError) as error:
        raise _error("Host runtime directory is unavailable or unsafe") from error


def _canonical_config_path(value: Path | str) -> Path:
    path = _path(value)
    try:
        if path.resolve(strict=True) != path:
            raise _error("Host runtime configuration file must be canonical")
        info = path.lstat()
        if (
            path.is_symlink()
            or not stat.S_ISREG(info.st_mode)
            or stat.S_IMODE(info.st_mode) & 0o022
        ):
            raise _error("Host runtime configuration file is unsafe")
        return path
    except HostRuntimeConfigError:
        raise
    except (OSError, RuntimeError, ValueError) as error:
        raise _error("Host runtime configuration file is unavailable or unsafe") from error


def _read_config(path: Path) -> bytes:
    try:
        from VALIDATE_ATOMS.validate_atoms_workers.read_io import ReadContext

        reader = ReadContext(roots=[str(path.parent)], limits=dict(_READ_LIMITS))
        raw = reader.read(path)
        if reader.currentness()["state"] != "unchanged":
            raise _error("Host runtime configuration changed during read")
        return raw
    except HostRuntimeConfigError:
        raise
    except (OSError, RuntimeError, UnicodeError, ValueError, KeyError) as error:
        raise _error("Host runtime configuration is unavailable or unsafe") from error


def _exact_int(value: Any, message: str, *, minimum: int, maximum: int) -> int:
    if type(value) is not int or not minimum <= value <= maximum:
        raise _error(message)
    return value


def _document(raw: bytes) -> tuple[Path, int, int]:
    try:
        value = tomllib.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, tomllib.TOMLDecodeError, TypeError, ValueError) as error:
        raise _error("Host runtime configuration TOML is invalid") from error
    if not isinstance(value, dict) or set(value) != {"schema_version", "shared_mcp"}:
        raise _error("Host runtime configuration keys are invalid")
    if type(value["schema_version"]) is not int or value["schema_version"] != 1:
        raise _error("Host runtime configuration schema_version must be 1")
    shared = value["shared_mcp"]
    if not isinstance(shared, dict) or not {"projects_root", "http_port"} <= set(shared):
        raise _error("Host runtime shared_mcp settings are incomplete")
    if set(shared) - {"projects_root", "http_port", "max_loaded_projects"}:
        raise _error("Host runtime shared_mcp keys are invalid")
    root_value = shared["projects_root"]
    if not isinstance(root_value, str):
        raise _error("Host runtime projects_root must be an absolute directory")
    root = _canonical_directory(root_value, reject_filesystem_root=True)
    port = _exact_int(
        shared["http_port"], "Host runtime http_port is invalid", minimum=1, maximum=65535
    )
    maximum = _exact_int(
        shared.get("max_loaded_projects", 2),
        "Host runtime max_loaded_projects is invalid",
        minimum=1,
        maximum=_MAX_LOADED_PROJECTS,
    )
    return root, port, maximum


@dataclass(frozen=True)
class HostRuntimeConfig:
    """Immutable, provenance-carrying shared host settings."""

    source_path: Path
    projects_root: Path
    http_port: int
    raw_sha256: str
    max_loaded_projects: int = 2

    @property
    def shared_runtime_id(self) -> str:
        value = f"{self.source_path}\0{self.projects_root}".encode("utf-8")
        return hashlib.sha256(value).hexdigest()

    def resolve_project(self, project_root: Path | str):
        return resolve_host_project(self, project_root)


def _default_path() -> Path:
    try:
        base = os.environ.get("XDG_CONFIG_HOME") or str(Path.home() / ".config")
        return Path(base) / "caprmedio" / "runtime.toml"
    except (OSError, RuntimeError, TypeError, ValueError) as error:
        raise _error("Host runtime configuration default path is unavailable") from error


def load_host_runtime_config(path: Path | str | None = None) -> HostRuntimeConfig:
    """Load one canonical host config without writing or using a fallback."""
    source = _canonical_config_path(_default_path() if path is None else path)
    raw = _read_config(source)
    projects_root, http_port, maximum = _document(raw)
    return HostRuntimeConfig(
        source, projects_root, http_port, hashlib.sha256(raw).hexdigest(), maximum
    )


def resolve_host_project(config: HostRuntimeConfig, project_root: Path | str):
    """Resolve one explicit Project strictly below the configured host root."""
    if not isinstance(config, HostRuntimeConfig):
        raise _error("Host runtime configuration is invalid")
    candidate = _canonical_directory(project_root)
    try:
        if candidate == config.projects_root or not candidate.is_relative_to(config.projects_root):
            raise _error("Project root is outside the shared host root")
    except ValueError as error:
        raise _error("Project root is outside the shared host root") from error
    try:
        from project_selection import resolve_project
    except (ImportError, ModuleNotFoundError) as error:
        raise _error("Project selection resolver is unavailable") from error
    from technical_diagnostics import _project_prefix

    selection = resolve_project(candidate)
    _project_prefix(selection.settings)
    return selection


__all__ = [
    "HostRuntimeConfig",
    "HostRuntimeConfigError",
    "load_host_runtime_config",
    "resolve_host_project",
]
