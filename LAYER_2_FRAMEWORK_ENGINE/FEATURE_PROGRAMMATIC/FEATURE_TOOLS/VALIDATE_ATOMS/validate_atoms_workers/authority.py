"""Source-binding primitives retained by declaration graph extraction."""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from typing import Any

from carrier_aliases import carrier_read_view


Record = dict[str, Any]
_SOURCE_ROLES = {
    "C": "Concern", "A": "Analysis", "P": "Plan", "R": "Requirement",
    "M": "Method", "E": "Evaluation", "D": "Delivery", "O": "Operations",
}


@dataclass(frozen=True)
class Obligation:
    code: str
    authority: list[Record]
    supported: bool
    reason: str


@dataclass(frozen=True)
class AuthorityContext:
    bindings: list[Record]
    required: int
    supported: int
    unsupported: int
    gaps: list[Record]
    obligations: tuple[Obligation, ...]
    domains: dict[str, tuple[str, ...]]
    unclassified_sources: bool


def _verified(source: Record, entry: Record) -> bool:
    del entry  # A manifest pin is checked separately; this binds observed carrier bytes.
    binding, metadata = source.get("binding"), source.get("metadata")
    if not isinstance(binding, dict) or not isinstance(metadata, dict):
        return False
    try:
        metadata = carrier_read_view(metadata)
    except ValueError:
        return False
    version, text = binding.get("version"), source.get("text")
    identifier = binding.get("atom_id")
    identity = identifier.rsplit("-", 2) if isinstance(identifier, str) else []
    expected_role = _SOURCE_ROLES.get(identity[1]) if len(identity) == 3 else None
    return bool(
        type(version) is int
        and version > 0
        and type(metadata.get("version")) is int
        and metadata["version"] == version
        and isinstance(identifier, str)
        and identifier
        and metadata.get("atom_id") == identifier
        and expected_role is not None
        and metadata.get("content_role") == expected_role
        and metadata.get("status") in {"Active", "active"}
        and "projection" not in metadata
        and isinstance(binding.get("path"), str)
        and binding["path"]
        and isinstance(text, str)
        and hashlib.sha256(text.encode("utf-8")).hexdigest() == binding.get("sha256")
    )
