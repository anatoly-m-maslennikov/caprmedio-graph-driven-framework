"""Reviewed support-source pins for retained Graph Rule extraction."""

from __future__ import annotations

import json
from dataclasses import replace
from functools import lru_cache
from pathlib import Path
from typing import Any, cast

from .authority import _verified
from .check_support import Check


MANIFESTS = (
    "schema_authority.json", "graph_authority.json", "structure_authority.json",
    "context_authority.json",
)


@lru_cache(maxsize=1)
def support_sources() -> dict[str, Any]:
    result: dict[str, Any] = {}
    for name in MANIFESTS:
        path = Path(__file__).with_name(name)
        if not path.is_file():
            continue
        for identifier, entry in json.loads(path.read_text())["sources"].items():
            old = result.get(identifier)
            if old and old.get("source_path") != entry.get("source_path"):
                raise ValueError("Conflicting installed support-source bindings.")
            result[identifier] = entry
    return result


def exact_source(inputs: dict[str, Any], identifier: str) -> dict[str, Any] | None:
    entry = support_sources().get(identifier)
    if entry is None:
        return None
    rows = [row for row in inputs.get("sources", [])
            if row.get("binding", {}).get("atom_id") == identifier]
    if len(rows) != 1:
        return None
    row = cast(dict[str, Any], rows[0])
    if not _verified(row, entry):
        return None
    return row


def require_sources(check: Check, identifiers: tuple[str, ...]) -> bool:
    sources = [exact_source(check.inputs, identifier) for identifier in identifiers]
    missing = [identifier for identifier, source in zip(identifiers, sources) if source is None]
    if missing:
        check.gap(
            "authority", "Missing or changed supporting authority: " + ", ".join(missing) + "."
        )
        return False
    bindings = list(check.obligation.authority)
    for source in sources:
        assert source is not None
        if source["binding"] not in bindings:
            bindings.append(source["binding"])
    check.obligation = replace(check.obligation, authority=bindings)
    return True
