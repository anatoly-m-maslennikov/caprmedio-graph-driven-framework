"""Reviewed support-source pins; never admit arbitrary supplied rule parameters."""

from functools import lru_cache
from dataclasses import replace
import hashlib
import json
from pathlib import Path
from typing import Any, cast

from .check_support import Check
from .authority import _verified

MANIFESTS = (
    "schema_authority.json",
    "graph_authority.json",
    "structure_authority.json",
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
    rows = [
        row
        for row in inputs.get("sources", [])
        if row.get("binding", {}).get("atom_id") == identifier
    ]
    if len(rows) != 1:
        return None
    row = cast(dict[str, Any], rows[0])
    if not _verified(row, entry):
        return None
    return row


def matches_source_pin(source: dict[str, Any], entry: dict[str, Any]) -> bool:
    """Require the installed reviewed revision, not merely self-consistent bytes."""
    binding = source.get("binding")
    return (
        _verified(source, entry)
        and isinstance(binding, dict)
        and type(entry.get("version")) is int
        and isinstance(entry.get("sha256"), str)
        and binding.get("version") == entry["version"]
        and binding.get("sha256") == entry["sha256"]
    )


def require_sources(check: Check, identifiers: tuple[str, ...]) -> bool:
    missing = [
        identifier for identifier in identifiers if exact_source(check.inputs, identifier) is None
    ]
    if missing:
        check.gap(
            "authority", "Missing or changed supporting authority: " + ", ".join(missing) + "."
        )
        return False
    # Include the dependencies in the check's diagnostic provenance without
    # changing the shared context or the obligation on other targets.
    bindings = list(check.obligation.authority)
    for identifier in identifiers:
        source = exact_source(check.inputs, identifier)
        if source is not None and source["binding"] not in bindings:
            bindings.append(source["binding"])
    check.obligation = replace(check.obligation, authority=bindings)
    return True


def matching_pin(raw: bytes, path: Path) -> dict[str, Any] | None:
    digest = hashlib.sha256(raw).hexdigest()
    found = [
        (identifier, row)
        for identifier, row in support_sources().items()
        if row["sha256"] == digest
    ]
    if len(found) != 1:
        return None
    identifier, row = found[0]
    return dict(atom_id=identifier, version=row["version"], sha256=digest, path=str(path))


_REVIEWED_HEADER_BODIES = {'CA-R-2508': ('215f8fc61c27bab49ea1aa7aeb842c7129307345db1870ea0a98c3f55ca8ecc6', 'dee613cbd5064933153ad79f22160232c73e161d85c15b072a2b2aa779e06639'), 'CA-R-2511': ('37c6a6d369be4021c6265f8d5ea67aab53c56d2b81f28f024d1bd301d69a2c2c', '1aeea7995e58fd349693aeddd36af41e525469647f2f0155f47be558f10578c8'), 'CA-D-378': ('bba9fbdd1ea3318375323583ca613f44dd7e6f5e8a29faa9e4920baf2b95cab5', '8a294fde2e79275b7013262ae568bbef39d299de0e0f46a699b5cb3dd56345be'), 'CA-R-2523': ('1a10948b57c238ce82abda199f3aca43fe9322cc56c8ff92193593913feddb24',)}

def matches_reviewed_header_source(source: dict[str, Any]) -> bool:
    """Accept only reviewed bodies after Header regrouping, preserving byte pins for history."""
    if not _verified(source, {}):
        return False
    text = source.get("text")
    identifier = source.get("binding", {}).get("atom_id")
    return (isinstance(text, str) and hashlib.sha256(text.split("---", 2)[-1].encode()).hexdigest()
            in _REVIEWED_HEADER_BODIES.get(identifier, ()))
