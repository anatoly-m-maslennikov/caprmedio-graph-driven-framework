"""Read complete Project Settings v2.0 without effects or legacy fallback."""

from __future__ import annotations

from collections.abc import Collection
import hashlib
from pathlib import Path

from artifact_metadata import one_value, split_frontmatter
from connector_bindings import ConnectorBindingError, FileSource
from connector_toml_parse import parse_source
from project_settings_schema import (
    SCHEMA_PINS, Diagnostic, SourcePin, SchemaPin, ProjectSettingsSnapshot,
    ProjectSettingsReadResult, _SchemaError, _parse_settings,
)


def _schema_bindings(source: FileSource, schemas: tuple[FileSource, ...]) -> tuple[SchemaPin, ...]:
    pins = []
    for authority in schemas:
        if not isinstance(authority, FileSource) or authority.root != source.root or authority.sha256 is None:
            raise _SchemaError("schema_sources", "Exact selected Project schema sources are required.")
        if authority.sha256 not in {digest for _, digest in SCHEMA_PINS.values()}:
            raise _SchemaError("schema_sources", "Schema bytes are not an independently accepted revision.")
        text = authority.read_bytes().decode("utf-8")
        delimiter, frontmatter, _ = split_frontmatter(text, authority.root / authority.relative_path)
        identity = one_value(frontmatter, delimiter, "atom_id")
        expected = SCHEMA_PINS.get(identity)
        if (expected is None or authority.sha256 != expected[1]
                or one_value(frontmatter, delimiter, "version") != str(expected[0])):
            raise _SchemaError("schema_sources", "Schema authority differs from the independently accepted source revision.")
        pins.append(SchemaPin(identity, expected[0], authority.relative_path.as_posix(), authority.sha256))
    if (not SCHEMA_PINS or {pin.atom_id for pin in pins} != SCHEMA_PINS.keys()
            or len(pins) != len(SCHEMA_PINS)):
        raise _SchemaError("schema_sources", "The complete distinct accepted schema closure is required.")
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
        name, prefix, control, obsolete, port = _parse_settings(document)
        if source.relative_path != Path(control) / "caprmedio_project_settings.toml":
            raise _SchemaError("source", "Settings must occupy their selected canonical authoritative Carrier.")
        source.revalidate()
        for authority in schemas:
            authority.revalidate()
        snapshot = ProjectSettingsSnapshot("2.0", name, prefix, control, obsolete,
                                           SourcePin(source.relative_path.as_posix(), hashlib.sha256(payload).hexdigest()),
                                           schema_pins, port)
        return ProjectSettingsReadResult(snapshot)
    except ConnectorBindingError as error:
        return ProjectSettingsReadResult(None, (Diagnostic(error.code, str(error), error.field),))
    except (UnicodeError, ValueError, TypeError, OSError, RuntimeError) as error:
        return ProjectSettingsReadResult(None, (Diagnostic("schema_invalid", str(error), getattr(error, "field", "settings")),))
