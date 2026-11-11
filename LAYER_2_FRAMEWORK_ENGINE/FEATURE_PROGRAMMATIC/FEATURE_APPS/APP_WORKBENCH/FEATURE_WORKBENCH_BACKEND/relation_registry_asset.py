# CA-M-509@6

"""Validate and consume the delivered relation-registry metadata asset."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from .relation_registry import RelationRegistry
from .relations import canonical


def _pairs(items, key, value):
    if not isinstance(items, list):
        raise ValueError("invalid relation registry mappings")
    result = {}
    for item in items:
        if not isinstance(item, dict) or not isinstance(item.get(key), str) or not item[key] or not isinstance(item.get(value), str) or not item[value] or item[key] in result:
            raise ValueError("invalid relation registry mapping")
        result[item[key]] = item[value]
    return result

def load_registry_asset(path: Path) -> RelationRegistry:
    """Load the delivered registry without compiling or consulting Project sources."""
    path = Path(path)
    if path.is_symlink():
        raise ValueError("relation registry asset must not be a symlink")
    try:
        payload = json.loads(path.read_bytes())
        if not isinstance(payload, dict) or payload.get("schema_version") != 1:
            raise ValueError("unsupported relation registry asset schema")
        digest = payload.get("input_digest")
        content = {key: value for key, value in payload.items() if key != "input_digest"}
        if not isinstance(digest, str) or digest != hashlib.sha256(canonical(content).encode("utf-8")).hexdigest():
            raise ValueError("relation registry asset digest mismatch")
        names = payload["registered_names"]
        bindings = payload["inverse_bindings"]
        aliases = payload["inverse_aliases"]
        if not isinstance(names, list) or any(not isinstance(name, str) or not name for name in names) or len(set(names)) != len(names):
            raise ValueError("invalid registered relation names")
        inverse = _pairs(bindings, "direct", "inverse")
        alias_map = _pairs(aliases, "alias", "canonical")
        if not set(inverse).issubset(names) or not set(alias_map.values()).issubset(names):
            raise ValueError("relation registry mapping references an unknown relation")
        return RelationRegistry(frozenset(names), inverse, alias_map, frozenset())
    except (KeyError, TypeError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError("invalid relation registry asset") from exc
