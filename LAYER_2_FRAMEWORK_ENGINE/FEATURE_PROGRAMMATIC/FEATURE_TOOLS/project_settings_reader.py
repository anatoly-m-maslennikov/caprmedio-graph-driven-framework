"""Read complete Project Settings v2.0 without effects or legacy fallback."""

from __future__ import annotations

from collections.abc import Collection
import hashlib
from pathlib import Path

from artifact_metadata import split_frontmatter
from connector_bindings import ConnectorBindingError, FileSource
from connector_toml_parse import parse_source
from FIND_AND_FETCH_ARTIFACTS.find_and_fetch_artifacts import _load_frontmatter
from project_settings_schema import (
    SCHEMA_IDS, Diagnostic, SourcePin, SchemaPin, ProjectSettingsSnapshot,
    ProjectSettingsReadResult, _SchemaError, _parse_settings,
)


def _schema_metadata(payload: bytes, path: Path) -> tuple[str, int]:
    try:
        _, frontmatter, _ = split_frontmatter(payload.decode("utf-8"), path)
        metadata = _load_frontmatter(frontmatter)
        identity, version = metadata.get("atom_id"), metadata.get("version")
        role = {"D": "Delivery", "E": "Evaluation", "M": "Method"}.get(identity[3:4] if isinstance(identity, str) else "")
        if (not isinstance(identity, str) or identity not in SCHEMA_IDS or type(version) is not int or version < 1
                or metadata.get("status") != "Active" or metadata.get("content_role") != role):
            raise _SchemaError("schema_sources", "Current active schema authority with a valid identity and Version is required.")
        return identity, version
    except (RuntimeError, ValueError) as error:
        raise _SchemaError("schema_sources", str(error)) from error


def _schema_bindings(source: FileSource, schemas: tuple[FileSource, ...]) -> tuple[SchemaPin, ...]:
    pins = []
    for authority in schemas:
        if not isinstance(authority, FileSource) or authority.root != source.root or authority.sha256 is None:
            raise _SchemaError("schema_sources", "Exact selected Project schema sources are required.")
        identity, version = _schema_metadata(authority.read_bytes(), authority.root / authority.relative_path)
        pins.append(SchemaPin(identity, version, authority.relative_path.as_posix(), authority.sha256))
    if ({pin.atom_id for pin in pins} != SCHEMA_IDS or len(pins) != len(SCHEMA_IDS)):
        raise _SchemaError("schema_sources", "The complete distinct current schema closure is required.")
    return tuple(sorted(pins, key=lambda pin: pin.atom_id))


def read_project_settings(source: FileSource, *, schema_sources: Collection[FileSource]) -> ProjectSettingsReadResult:
    """Return the validated file values and retained physical/schema provenance."""
    try:
        if not isinstance(source, FileSource):
            raise _SchemaError("source", "An exact selected Settings source pin is required.")
        schemas = tuple(schema_sources)
        schema_pins = _schema_bindings(source, schemas)
        payload = source.read_bytes()
        _, document = parse_source(payload)
        name, prefix, control, obsolete, port, blacklist = _parse_settings(document)
        if source.relative_path != Path(control) / "caprmedio_project_settings.toml":
            raise _SchemaError("source", "Settings must occupy their selected canonical authoritative Carrier.")
        source.revalidate()
        for authority in schemas:
            authority.revalidate()
        snapshot = ProjectSettingsSnapshot("2.0", name, prefix, control, obsolete,
                                           SourcePin(source.relative_path.as_posix(), hashlib.sha256(payload).hexdigest()),
                                           schema_pins, port, blacklist)
        return ProjectSettingsReadResult(snapshot)
    except ConnectorBindingError as error:
        return ProjectSettingsReadResult(None, (Diagnostic(error.code, str(error), error.field),))
    except (UnicodeError, ValueError, TypeError, OSError, RuntimeError) as error:
        return ProjectSettingsReadResult(None, (Diagnostic("schema_invalid", str(error), getattr(error, "field", "settings")),))
