"""Pure preview and mutation boundary for machine-local host settings."""

from __future__ import annotations

import json
import os
from pathlib import Path

from INSTALL_TOOLS.host_installation_io import FileUpdate
import host_runtime_config


_DEFAULT_HTTP_PORT = 8092
_DEFAULT_MAX_LOADED_PROJECTS = 2


def _absolute_path(value: Path | str) -> Path:
    try:
        path = Path(value).expanduser()
        if not path.is_absolute():
            path = Path(os.path.abspath(path))
        return path
    except (OSError, RuntimeError, TypeError, ValueError) as error:
        raise ValueError("Host settings path is invalid") from error


def _toml_literal(value: object) -> str:
    if isinstance(value, str):
        return json.dumps(value, ensure_ascii=False)
    return repr(value)


def _render(projects_root: object, http_port: object, max_loaded_projects: object) -> bytes:
    return (
        "schema_version = 1\n\n"
        "[shared_mcp]\n"
        f"projects_root = {_toml_literal(str(projects_root))}\n"
        f"http_port = {_toml_literal(http_port)}\n"
        f"max_loaded_projects = {_toml_literal(max_loaded_projects)}\n"
    ).encode("utf-8")


def _load_existing(path: Path):
    if not path.exists():
        return None, None
    config = host_runtime_config.load_host_runtime_config(path)
    raw = host_runtime_config._read_config(path)
    values = host_runtime_config._document(raw)
    if values != (config.projects_root, config.http_port, config.max_loaded_projects):
        raise host_runtime_config.HostRuntimeConfigError(
            "Host runtime configuration changed during read"
        )
    return config, raw


def _propose(existing, projects_root, http_port, max_loaded_projects):
    if projects_root is None:
        if existing is None:
            raise host_runtime_config.HostRuntimeConfigError(
                "Host runtime projects_root is required when settings are missing"
            )
        projects_root = existing.projects_root
    if http_port is None:
        http_port = existing.http_port if existing else _DEFAULT_HTTP_PORT
    if max_loaded_projects is None:
        max_loaded_projects = (
            existing.max_loaded_projects if existing else _DEFAULT_MAX_LOADED_PROJECTS
        )
    return projects_root, http_port, max_loaded_projects


def _validated_content(
    path: Path, existing, original, proposed
) -> tuple[bytes, tuple[Path, int, int]]:
    rendered = _render(*proposed)
    if len(rendered) > host_runtime_config._MAX_CONFIG_BYTES:
        raise host_runtime_config.HostRuntimeConfigError(
            "Host runtime configuration exceeds 4096 bytes"
        )
    values = host_runtime_config._document(rendered)
    content = rendered
    if existing is not None and original is not None:
        original_values = host_runtime_config._document(original)
        if values == original_values:
            content = original
            values = original_values
    if len(content) > host_runtime_config._MAX_CONFIG_BYTES:
        raise host_runtime_config.HostRuntimeConfigError(
            "Host runtime configuration exceeds 4096 bytes"
        )
    try:
        if path == values[0] or path.is_relative_to(values[0]):
            raise host_runtime_config.HostRuntimeConfigError(
                "Host runtime configuration must be outside projects_root"
            )
    except ValueError as error:
        raise host_runtime_config.HostRuntimeConfigError(
            "Host runtime configuration must be outside projects_root"
        ) from error
    return content, values


class HostRuntimeSettings:
    """Preview and apply one validated shared host configuration."""

    def __init__(
        self,
        *,
        projects_root: Path | None = None,
        host_settings: Path | None = None,
        http_port: int | None = None,
        max_loaded_projects: int | None = None,
    ) -> None:
        path = _absolute_path(
            host_runtime_config._default_path() if host_settings is None else host_settings
        )
        existing, original = _load_existing(path)
        proposed = _propose(existing, projects_root, http_port, max_loaded_projects)
        content, (canonical_root, canonical_port, canonical_maximum) = _validated_content(
            path, existing, original, proposed
        )
        self._update = FileUpdate(path, content, mode=0o600)
        if existing is not None:
            host_runtime_config._canonical_config_path(self._update.path)
        if self._update.previous_content != original:
            raise host_runtime_config.HostRuntimeConfigError(
                "Host runtime configuration changed during preflight"
            )
        self._values = {
            "host_settings": str(self._update.path),
            "projects_root": str(canonical_root),
            "http_port": canonical_port,
            "max_loaded_projects": canonical_maximum,
            "changed": self._update.changed,
        }

    @property
    def path(self) -> Path:
        return self._update.path

    @property
    def preview(self) -> dict[str, str | int | bool]:
        return dict(self._values)

    def apply(self) -> None:
        self._update.apply()

    def restore(self) -> None:
        self._update.restore()


__all__ = ["HostRuntimeSettings"]
