"""Typed Project-MCP settings from the one target-owned runtime TOML.

Defaults are carried by ``defaults/runtime-config.toml`` in the admitted
package, not duplicated here. Installed startup cannot build an image,
regardless of the development build setting.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
import math
from pathlib import Path
from typing import Any

from runtime_configuration import RuntimeConfigurationError, read_runtime_configuration


DEFAULT_MEMBER = "defaults/runtime-config.toml"


@dataclass(frozen=True)
class ProjectMCPSettings:
    startup_timeout_seconds: float
    build_timeout_seconds: float
    build_if_missing: bool
    port: int | None


def _refuse(message: str) -> None:
    raise RuntimeConfigurationError("runtime-config-migration-needed", message)


def _timeout(value: object, maximum: float, field: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (float, int)):
        _refuse(f"{field} must be a number")
    if not 0 < value <= maximum or not math.isfinite(value):
        _refuse(f"{field} must be positive and at most {maximum:g} seconds")
    return float(value)


def parse_project_mcp_settings(document: Mapping[str, Any]) -> ProjectMCPSettings:
    """Validate this consumer's section without modifying unrelated settings."""
    if type(document.get("schema_version")) is not int or document["schema_version"] != 1:
        _refuse("runtime configuration schema requires explicit migration")
    section = document.get("project_mcp")
    if not isinstance(section, Mapping):
        _refuse("runtime configuration needs a project_mcp table")
    required = {"startup_timeout_seconds", "build_timeout_seconds", "build_if_missing"}
    if not required <= section.keys() or set(section) - required - {"port"}:
        _refuse("project_mcp settings have missing or unsupported keys")
    startup = _timeout(section["startup_timeout_seconds"], 60.0, "startup_timeout_seconds")
    build = _timeout(section["build_timeout_seconds"], 600.0, "build_timeout_seconds")
    if type(section["build_if_missing"]) is not bool:
        _refuse("build_if_missing must be a boolean")
    port = section.get("port")
    if "port" in section and (type(port) is not int or not 1 <= port <= 65535):
        _refuse("port must be an integer from 1 to 65535 or omitted")
    return ProjectMCPSettings(startup, build, section["build_if_missing"], port)


def load_project_mcp_settings(project_root: Path | str) -> ProjectMCPSettings:
    """Read only; creation of absent configuration belongs to installation."""
    result = read_runtime_configuration(project_root, validator=parse_project_mcp_settings)
    if result.state == "absent":
        raise RuntimeConfigurationError("runtime-config-missing", "installation must create runtime config before startup")
    if result.state == "blocked" or result.configuration is None:
        _refuse("runtime configuration requires explicit migration before startup")
    return parse_project_mcp_settings(result.configuration.document)
