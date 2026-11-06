"""Adapt grouped Header reads without changing source carriers or provenance."""

import json
from collections.abc import Mapping

from carrier_aliases import carrier_read_view
from header_groups import TOPIC_SUBJECT_FIELDS, header_path
from header_yaml import header_scalar, parse_header


def scalar_header_fields(frontmatter: str) -> dict[str, str]:
    """Expose lexical identity/state/classification values for checked raw pins."""
    result = {}
    for key in ("atom_id", "version", "content_role", "type", "status"):
        value = header_scalar(frontmatter, key)
        if value is not None:
            result[key] = value
    return result


def nested_subject_block(frontmatter: str) -> list[str]:
    """Feed semantic Topics into the existing bounded Subject value parser."""
    metadata = parse_header(frontmatter)
    subjects = carrier_read_view(metadata).get("subjects")
    if not isinstance(subjects, Mapping):
        return []
    return [
        f"  {aliases[0]}: {json.dumps(subjects[aliases[0]], ensure_ascii=False)}"
        for aliases in TOPIC_SUBJECT_FIELDS.values() if aliases[0] in subjects
    ]


def subject_source_keys(frontmatter: str) -> dict[str, str]:
    """Keep actual Topics property paths when the Subject read view is derived."""
    metadata = parse_header(frontmatter)
    result = {}
    for aliases in TOPIC_SUBJECT_FIELDS.values():
        for alias in aliases:
            path = header_path(f"subjects.{alias}", metadata)
            result[alias] = ".".join(path) if path[0] != "subjects" else alias
    return result


def carrier_ownership(
    frontmatter: str, declaration: Mapping[str, object], scope_unit_name: str,
) -> tuple[object, object, dict[str, object]]:
    """Compare declared Container IDs separately from legacy Scope Unit names."""
    metadata = carrier_read_view(parse_header(frontmatter))
    container = metadata.get("container")
    if isinstance(container, Mapping):
        return container.get("scope_unit"), declaration.get("scope_unit_id"), {"container": dict(container)}
    if "container" in metadata:
        return None, None, {"container": container}
    owner = metadata.get("current_scope_unit")
    return owner, scope_unit_name, {"current_scope_unit": owner}
