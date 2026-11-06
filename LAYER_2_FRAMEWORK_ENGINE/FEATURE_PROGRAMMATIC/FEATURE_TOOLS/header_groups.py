"""Declared Header paths and ordered authoring, independent of Carrier storage."""

# implementation of: CA-D-657

from copy import deepcopy
from typing import Any


GROUP_FIELDS = {
    "identity": ("atom_id", "ref_id"),
    "context": ("container", "role", "form", "label", "topics", "tier"),
    "state": ("status", "version", "updated_at"),
}
ROLE_FIELDS = {"concern": ("priority",),
               "plan": ("work_sequence_number", "ai_agent_confidence_threshold")}
GROUP_ORDER = ("identity", "context", "relations", "state", "destination")
TOPIC_SUBJECT_FIELDS = {"main_subject": ("active", "governs"),
                        "dependencies": ("passive", "depends_on")}
ALIASES = {"content_role": "role", "type": "form", "carrier_destination": "destination",
           "autonomous_confidence_threshold": "ai_agent_confidence_threshold"}


def equal_values(left: Any, right: Any) -> bool:
    if type(left) is not type(right):
        return False
    if isinstance(left, dict):
        return left.keys() == right.keys() and all(equal_values(left[k], right[k]) for k in left)
    if isinstance(left, list):
        return len(left) == len(right) and all(equal_values(a, b) for a, b in zip(left, right))
    return bool(left == right)


def path_value(metadata: dict[str, Any], path: tuple[str, ...]) -> tuple[bool, Any]:
    current: Any = metadata
    for part in path:
        if not isinstance(current, dict) or part not in current:
            return False, None
        current = current[part]
    return True, current


def _role(metadata: dict[str, Any]) -> str | None:
    for path in (("context", "role"), ("role",), ("content_role",)):
        present, value = path_value(metadata, path)
        if present and isinstance(value, str):
            return value
    present, identity = header_value(metadata, "atom_id")
    if isinstance(identity, str):
        return {"C": "Concern", "P": "Plan"}.get(identity.split("-")[1] if "-" in identity else "")
    return None


def _canonical_path(name: str, metadata: dict[str, Any]) -> tuple[str, ...]:
    if name == "atom_id" and path_value(metadata, ("identity", "id"))[0]:
        return "identity", "id"
    parts = tuple(name.split("."))
    if len(parts) > 1:
        if parts[0] in ("identity", "context", "state", "destination", "relations"):
            return parts
        return _canonical_path(parts[0], metadata) + parts[1:]
    name = ALIASES.get(name, name)
    for group, fields in GROUP_FIELDS.items():
        if name in fields:
            return group, name
    if name == "priority" and _role(metadata) == "Concern":
        return "context", "concern", name
    if name in ROLE_FIELDS["plan"] and _role(metadata) == "Plan":
        return "context", "plan", name
    return (name,)


def header_field_paths(name: str, metadata: dict[str, Any]) -> tuple[tuple[str, ...], ...]:
    """Return canonical then historical candidates; undeclared fields stay at root."""
    for topic, aliases in TOPIC_SUBJECT_FIELDS.items():
        if name in tuple(f"subjects.{alias}" for alias in aliases) + (f"topics.{topic}", f"context.topics.{topic}"):
            return (("context", "topics", topic), ("topics", topic),
                    *(("subjects", alias) for alias in aliases))
    if name in ("atom_id", "identity.id", "identity.atom_id"):
        identity_paths = (("identity", "id"), ("identity", "atom_id"), ("atom_id",))
        existing = tuple(path for path in identity_paths if path_value(metadata, path)[0])
        if existing:
            return existing + tuple(path for path in identity_paths if path not in existing)
        return {"identity.id": (identity_paths[0],),
                "identity.atom_id": (identity_paths[1],),
                "atom_id": (identity_paths[1], identity_paths[2], identity_paths[0])}[name]
    canonical = _canonical_path(name, metadata)
    leaf = canonical[-1]
    alias_names = tuple(old for old, new in ALIASES.items() if new == leaf)
    paths = [canonical]
    if canonical[0] == "destination":
        paths.append(("carrier_destination",) + canonical[1:])
    elif len(canonical) > 1 and canonical[0] in GROUP_FIELDS:
        historical = canonical[1:] if canonical[0] != "context" or canonical[1] not in ROLE_FIELDS else canonical[2:]
        paths.append(historical)
        if len(historical) == 1:
            paths.extend((key,) for key in alias_names)
    elif "." not in name:
        paths.extend((key,) for key in alias_names)
    return tuple(dict.fromkeys(paths))


def header_value(metadata: dict[str, Any], name: str) -> tuple[bool, Any]:
    values = [(path, value) for path in header_field_paths(name, metadata)
              for present, value in (path_value(metadata, path),) if present]
    if values and any(not equal_values(values[0][1], value) for _, value in values[1:]):
        raise ValueError(f"Conflicting Header aliases for {name}.")
    return (True, values[0][1]) if values else (False, None)


def header_path(name: str, metadata: dict[str, Any]) -> tuple[str, ...]:
    """Choose an existing path, or the declared path for an already grouped Header."""
    header_value(metadata, name)
    paths = header_field_paths(name, metadata)
    for path in paths:
        if path_value(metadata, path)[0]:
            return path
    grouped = any(group in metadata for group in ("identity", "context", "state", "destination"))
    return paths[0] if grouped else ((name,) if "." not in name else paths[-1])


def header_key_order(path: tuple[str, ...]) -> tuple[str, ...]:
    if not path:
        return GROUP_ORDER
    if path == ("context",):
        return GROUP_FIELDS["context"] + tuple(ROLE_FIELDS)
    if len(path) == 1 and path[0] in GROUP_FIELDS:
        return GROUP_FIELDS[path[0]]
    if len(path) == 2 and path[0] == "context":
        return ROLE_FIELDS.get(path[1], ())
    return ("file",) if path == ("destination",) else ("name", "path") if path == ("destination", "file") else ()


def _ordered(mapping: dict[str, Any], path: tuple[str, ...] = ()) -> dict[str, Any]:
    keys = tuple(key for key in header_key_order(path) if key in mapping)
    keys += tuple(key for key in mapping if key not in keys)
    return {key: _ordered(value, path + (key,)) if isinstance(value, dict) else deepcopy(value)
            for key in keys for value in (mapping[key],)}


def validate_header_groups(metadata: dict[str, Any]) -> None:
    for group in GROUP_ORDER:
        if group in metadata and not isinstance(metadata[group], dict):
            raise ValueError(f"Header {group} must be a mapping.")
    context = metadata.get("context", {})
    for role in ROLE_FIELDS:
        if role in context and not isinstance(context[role], dict):
            raise ValueError(f"Header context.{role} must be a mapping.")


def nested_header(metadata: dict[str, Any]) -> dict[str, Any]:
    """Author only declared groups, preserving all unmapped fields and absent values."""
    result = deepcopy(metadata)
    validate_header_groups(metadata)
    fields = tuple(field for values in GROUP_FIELDS.values() for field in values)
    fields += ("destination", "priority", *ROLE_FIELDS["plan"])
    for topic in TOPIC_SUBJECT_FIELDS:
        header_value(metadata, f"topics.{topic}")
    for name in fields:
        present, value = header_value(metadata, name)
        if not present:
            continue
        path = _canonical_path(name, metadata)
        if name in ("priority", *ROLE_FIELDS["plan"]) and len(path) == 1:
            continue
        if name == "atom_id" and path == ("identity", "id"):
            result["identity"].pop("atom_id", None)
            result.pop("atom_id", None)
        for candidate in header_field_paths(name, metadata):
            if len(candidate) == 1:
                result.pop(candidate[0], None)
        parent = result
        for part in path[:-1]:
            parent = parent.setdefault(part, {})
            if not isinstance(parent, dict):
                raise ValueError("Header Property parent must be a mapping.")
        parent[path[-1]] = deepcopy(value)
    return _ordered(result)
