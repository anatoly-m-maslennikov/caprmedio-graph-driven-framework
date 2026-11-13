# CA-D-657@11

"""Read compatibility for carrier field names; never mutate the source mapping."""

from typing import Any
import re

from header_groups import (GROUP_FIELDS, ROLE_FIELDS, TOPIC_SUBJECT_FIELDS, equal_values,
                           header_value, validate_header_groups)


_equal = equal_values


def carrier_status_folder(name: str) -> str:
    """Read the semantic label of an ordinary or three-digit Status folder."""
    label = re.sub(r'^[0-9]{3}_', '', name.casefold())
    return {'drafts': 'draft', 'archive': 'archived'}.get(label, label)


def named_value_token(canonical: str) -> str | None:
    if not isinstance(canonical, str) or not re.fullmatch(r'[A-Za-z0-9]+(?:[ _-]+[A-Za-z0-9]+)*', canonical):
        return None
    return re.sub(r'[ _-]+', '_', canonical).lower()


def matches_named_value(carried: Any, canonical: str) -> bool:
    token = named_value_token(canonical)
    return carried == canonical or (token is not None and carried == token)


def canonical_role_name(value: Any) -> Any:
    if value in ('Analysis & Advisory', 'analysis_and_advisory'):
        return 'Analysis and Advisory'
    return value


def _read_aliases(mapping: dict[str, Any], pairs: tuple[tuple[str, str], ...]) -> dict[str, Any]:
    view = dict(mapping)
    for old, new in pairs:
        if old in mapping and new in mapping and not _equal(mapping[old], mapping[new]):
            raise ValueError(f"Conflicting carrier aliases: {old} and {new}.")
        if old not in mapping and new in mapping:
            view[old] = mapping[new]
    return view


def carrier_read_view(metadata: dict[str, Any]) -> dict[str, Any]:
    """Expose semantic read keys for grouped and historical Headers, without rewriting."""
    view = dict(metadata)
    validate_header_groups(metadata)
    fields = tuple(field for values in GROUP_FIELDS.values() for field in values)
    fields += ("destination", "priority", *ROLE_FIELDS["plan"])
    for name in fields:
        present, value = header_value(metadata, name)
        if present:
            view[name] = value
    view = _read_aliases(view, (("content_role", "role"), ("type", "form"),
                               ("carrier_destination", "destination"),
                               ("autonomous_confidence_threshold", "ai_agent_confidence_threshold")))
    if isinstance(view.get("subjects"), dict):
        view["subjects"] = _read_aliases(view["subjects"], (("governs", "active"), ("depends_on", "passive")))
    return _read_topics(view)


def _read_topics(view: dict[str, Any]) -> dict[str, Any]:
    topics = view.get("topics")
    if isinstance(topics, dict):
        if "subjects" in view and not isinstance(view["subjects"], dict):
            raise ValueError("Header Subjects must be a mapping.")
        subjects = dict(view.get("subjects", {}))
        for topic, aliases in TOPIC_SUBJECT_FIELDS.items():
            if topic not in topics:
                continue
            for alias in aliases:
                if alias in subjects and not _equal(subjects[alias], topics[topic]):
                    raise ValueError(f"Conflicting Header Topics and Subject aliases: {topic}.")
                subjects[alias] = topics[topic]
        if subjects:
            view["subjects"] = subjects
    return view
