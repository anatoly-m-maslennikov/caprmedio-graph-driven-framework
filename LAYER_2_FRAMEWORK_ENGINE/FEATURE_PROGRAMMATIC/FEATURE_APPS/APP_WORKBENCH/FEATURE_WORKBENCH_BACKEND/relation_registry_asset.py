# CA-M-509@1
# CA-D-705@1
# CA-E-804@1

"""Validate and consume the delivered relation-registry metadata asset."""
from __future__ import annotations

import json
from pathlib import Path

from .generate_relation_registry import registry_asset
from .relation_registry import RegistryCompilation, RelationRegistry


def load_registry_asset(
    path: Path, atoms: list[dict], compilation: RegistryCompilation,
) -> RelationRegistry | None:
    """Return the delivered registry only when it exactly matches admitted sources."""
    try:
        if path.is_symlink() or not path.is_file():
            return None
        raw = path.read_bytes()
        if raw != registry_asset(atoms, compilation):
            return None
        payload = json.loads(raw)
        inverse = {
            item["direct"]: item["inverse"]
            for item in payload["inverse_bindings"]
        }
        aliases = {
            item["alias"]: item["canonical"]
            for item in payload["inverse_aliases"]
        }
        return RelationRegistry(
            frozenset(payload["registered_names"]), inverse, aliases, compilation.registry.collisions,
        )
    except (KeyError, OSError, TypeError, UnicodeError, ValueError, json.JSONDecodeError):
        return None
