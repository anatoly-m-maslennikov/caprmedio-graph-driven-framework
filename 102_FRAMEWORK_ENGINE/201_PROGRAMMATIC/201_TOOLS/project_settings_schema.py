"""Pure complete Project Settings v2.0 schema and immutable result types."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from types import MappingProxyType


# Reviewed byte closure; carried named authority must also be admitted.
SCHEMA_PINS = MappingProxyType({
    "CA-D-364": (10, "4f7513eb67fe6075f58c29d06accc4fd16c9dca7e823d794c7a4dc90cd9668c9"),
    "CA-D-366": (9, "c784150f0606565346419b44ba38e2333870de6bcbd3bf90e16dae76dbdc8e33"),
    "CA-D-375": (10, "d32280d1b04a033a9398745c8471e731bbca293ffcfe4260d9136c06951c950b"),
    "CA-D-376": (9, "f03248c4d66a550d2c2ad6018b1a42a5cf2ac6aba0488e1d3c38c388ecedb321"),
    "CA-D-378": (10, "9435f3abb5a56f46c37c43c3e758afa1e288a0af259f39a34237495d8fcf255f"),
    "CA-D-392": (8, "dfc6540a2654237153dbf7a660589ea4fa69e08124fc65ece65cf39df4d21150"),
    "CA-D-520": (1, "0241f547edfb5c20ffc9cbae2981eb40cd2dbaf1e49f0fa00e823afcf643f271"),
    "CA-E-459": (19, "c20f5a68f2d2299e44651f68348605447cad6095b06b898c3cb135994dfc2c38"),
    "CA-M-284": (14, "511958b7bb1701039215209b3be552a4b25485c48d56d19fab10c5a95564ed98"),
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

    def to_document(self) -> dict:
        """Return a fresh complete value copy, retaining optional-field absence."""
        project = {"name": self.name}
        if self.obsolete_names is not None:
            project["obsolete_names"] = list(self.obsolete_names)
        return {"schema_version": self.schema_version, "project": project,
                "artifacts": {"identity": {"project_prefix": self.project_prefix}},
                "paths": {"control_root": self.control_root}}


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


def _parse_settings(document: dict) -> tuple[str, str, str, tuple[str, ...] | None]:
    """Pure complete-schema validation; no identity-only subset or normalization."""
    _table(document, {"schema_version", "project", "artifacts", "paths"}, set(), "settings")
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
    return name, prefix, control, obsolete
