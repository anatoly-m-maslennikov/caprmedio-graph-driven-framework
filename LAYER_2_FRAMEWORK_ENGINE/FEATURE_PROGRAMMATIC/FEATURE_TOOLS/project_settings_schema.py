"""Pure complete Project Settings v2.0 schema and immutable result types."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path


SCHEMA_IDS = frozenset({
    "CA-D-364", "CA-D-366", "CA-D-375", "CA-D-376", "CA-D-378",
    "CA-D-392", "CA-D-520", "CA-E-459", "CA-M-284",
})


@dataclass(frozen=True)
class Diagnostic:
    code: str
    message: str
    field: str | None = None


@dataclass(frozen=True)
class SourcePin:
    path: str
    sha256: str


@dataclass(frozen=True)
class SchemaPin:
    atom_id: str
    version: int
    path: str
    sha256: str


@dataclass(frozen=True)
class ProjectSettingsSnapshot:
    schema_version: str
    name: str
    project_prefix: str
    control_root: str
    obsolete_names: tuple[str, ...] | None
    source: SourcePin
    schema_sources: tuple[SchemaPin, ...]
    project_mcp_http_port: int | None
    project_mcp_tool_blacklist: tuple[str, ...] | None = None

    def to_document(self) -> dict:
        """Return a fresh complete value copy, retaining optional-field absence."""
        project = {"name": self.name}
        if self.obsolete_names is not None:
            project["obsolete_names"] = list(self.obsolete_names)
        document = {"schema_version": self.schema_version, "project": project,
                    "artifacts": {"identity": {"project_prefix": self.project_prefix}},
                    "paths": {"control_root": self.control_root}}
        if self.project_mcp_http_port is not None:
            document["project_mcp"] = {"http_port": self.project_mcp_http_port}
            if self.project_mcp_tool_blacklist is not None:
                document["project_mcp"]["tool_blacklist"] = list(self.project_mcp_tool_blacklist)
        return document


@dataclass(frozen=True)
class ProjectSettingsReadResult:
    snapshot: ProjectSettingsSnapshot | None
    errors: tuple[Diagnostic, ...] = ()


class _SchemaError(ValueError):
    def __init__(self, field: str, message: str):
        self.field = field
        super().__init__(message)


def _table(value, required: set[str], optional: set[str], field: str) -> dict:
    if type(value) is not dict or not required <= value.keys() or value.keys() - required - optional:
        raise _SchemaError(field, "Required fields are missing or unsupported fields are present.")
    return value


def _string(value, field: str) -> str:
    if type(value) is not str or not value:
        raise _SchemaError(field, "An exact nonempty string is required.")
    return value


def mcp_tool_blacklist(settings: Mapping[str, object]) -> frozenset[str]:
    """Read exact disabled MCP names from validated or frozen Settings values."""
    mcp = settings.get("project_mcp", {})
    if not isinstance(mcp, Mapping):
        raise _SchemaError("project_mcp", "A Settings table is required.")
    names = mcp.get("tool_blacklist", ())
    if type(names) not in (list, tuple):
        raise _SchemaError("project_mcp.tool_blacklist", "An array of exact nonempty strings is required.")
    return frozenset(_string(name, "project_mcp.tool_blacklist") for name in names)


def _parse_mcp_settings(document: dict) -> tuple[int | None, tuple[str, ...] | None]:
    if "project_mcp" not in document:
        return None, None
    mcp = _table(document["project_mcp"], {"http_port"}, {"tool_blacklist"}, "project_mcp")
    port = mcp["http_port"]
    if type(port) is not int or not 1 <= port <= 65535:
        raise _SchemaError("project_mcp.http_port", "An exact integer in 1..65535 is required.")
    if "tool_blacklist" not in mcp:
        return port, None
    if type(mcp["tool_blacklist"]) is not list:
        raise _SchemaError("project_mcp.tool_blacklist", "An array of exact nonempty strings is required.")
    mcp_tool_blacklist(document)
    return port, tuple(mcp["tool_blacklist"])


def _parse_settings(document: dict) -> tuple[str, str, str, tuple[str, ...] | None, int | None, tuple[str, ...] | None]:
    """Pure complete-schema validation; no identity-only subset or normalization."""
    _table(document, {"schema_version", "project", "artifacts", "paths"}, {"project_mcp"}, "settings")
    if type(document["schema_version"]) is not str or document["schema_version"] != "2.0":
        raise _SchemaError("schema_version", "The exact string schema version 2.0 is required.")
    project = _table(document["project"], {"name"}, {"obsolete_names"}, "project")
    name = _string(project["name"], "project.name")
    if name != name.lower():
        raise _SchemaError("project.name", "The selected Project name must already be lowercase.")
    artifacts = _table(document["artifacts"], {"identity"}, set(), "artifacts")
    identity = _table(artifacts["identity"], {"project_prefix"}, set(), "artifacts.identity")
    prefix = _string(identity["project_prefix"], "artifacts.identity.project_prefix")
    if prefix != prefix.upper():
        raise _SchemaError("artifacts.identity.project_prefix", "The selected Project prefix must already be uppercase.")
    paths = _table(document["paths"], {"control_root"}, set(), "paths")
    control = _string(paths["control_root"], "paths.control_root")
    if control != f".caprmedio_{name}" or len(Path(control).parts) != 1 or Path(control).as_posix() != control:
        raise _SchemaError("paths.control_root", "The control root must be the exact selected direct Project child.")
    obsolete = project.get("obsolete_names")
    if "obsolete_names" in project:
        if type(obsolete) is not list:
            raise _SchemaError("project.obsolete_names", "Obsolete names must be an array of exact nonempty strings.")
        for value in obsolete:
            _string(value, "project.obsolete_names")
        obsolete = tuple(obsolete)
    port, blacklist = _parse_mcp_settings(document)
    return name, prefix, control, obsolete, port, blacklist
