"""Read compatibility for carrier field names; never mutate the source mapping."""

from typing import Any

from header_groups import (GROUP_FIELDS, ROLE_FIELDS, TOPIC_SUBJECT_FIELDS, equal_values,
                           header_value, validate_header_groups)


_equal = equal_values


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
