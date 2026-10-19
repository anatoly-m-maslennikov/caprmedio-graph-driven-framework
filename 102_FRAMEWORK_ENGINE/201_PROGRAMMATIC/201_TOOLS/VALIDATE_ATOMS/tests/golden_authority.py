"""Pinned, test-only authority corpus for validator golden cases."""

from __future__ import annotations

from functools import lru_cache
import hashlib
import json
from pathlib import Path
import sys
from typing import Any

HERE = Path(__file__).resolve().parent
TOOL = HERE.parent
if str(TOOL) not in sys.path:
    sys.path.insert(0, str(TOOL))

from validate_atoms_workers.parsing import parse_carrier  # noqa: E402


FIXTURES = HERE / "fixtures"
MANIFEST = FIXTURES / "frozen_authority.json"
DEFAULT_GROUPS = (
    "registry",
    "schema_authority",
    "graph_authority",
    "structure_authority",
    "context_authority",
)
GROUP_FOLDERS = {
    "registry": "authority_checks",
    "schema_authority": "schema_authority",
    "graph_authority": "extended_authority",
    "structure_authority": "structure_authority",
    "context_authority": "context_authority",
}


@lru_cache(maxsize=1)
def manifest() -> dict[str, Any]:
    value = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if set(value) != {"schema_version", "groups"} or value["schema_version"] != 1:
        raise AssertionError("frozen authority manifest is malformed")
    if set(value["groups"]) != set(DEFAULT_GROUPS):
        raise AssertionError("frozen authority manifest groups are incomplete")
    return value


def entries(group: str) -> dict[str, dict[str, Any]]:
    rows = manifest()["groups"].get(group)
    if not isinstance(rows, dict):
        raise AssertionError("unknown frozen authority group: " + group)
    return rows


def _entry(identifier: str, *, graph: bool = False) -> tuple[str, dict[str, Any]]:
    groups = ("graph_authority",) if graph else (
        "registry", "context_authority", "structure_authority", "schema_authority", "graph_authority",
    )
    for group in groups:
        row = entries(group).get(identifier)
        if isinstance(row, dict):
            return group, row
    raise AssertionError("missing frozen authority fixture: " + identifier)


def frozen_entry(identifier: str, *, graph: bool = False) -> dict[str, Any]:
    """Return a static locator and pin for the fake selected Project only."""
    group, row = _entry(identifier, graph=graph)
    return {
        "source_path": (
            ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/"
            f"METHODOLOGY_SOURCES/frozen-authority/{identifier}.md"
        ),
        "version": row["version"],
        "sha256": row["sha256"],
    }


def _frozen_source(identifier: str, group: str, row: dict[str, Any]) -> dict[str, Any]:
    fixture = FIXTURES / row["fixture"]
    expected_folder = GROUP_FOLDERS[group]
    if fixture.parent != FIXTURES / expected_folder:
        raise AssertionError("frozen authority fixture is outside its group")
    raw = fixture.read_bytes()
    if hashlib.sha256(raw).hexdigest() != row["sha256"]:
        raise AssertionError("frozen authority fixture hash changed: " + identifier)
    parsed = parse_carrier(raw, fixture)
    if parsed.metadata.get("atom_id") != identifier or parsed.metadata.get("version") != row["version"]:
        raise AssertionError("frozen authority fixture identity changed: " + identifier)
    return {
        "binding": {
            "atom_id": identifier,
            "version": row["version"],
            "sha256": row["sha256"],
            "path": str(fixture),
        },
        "text": parsed.text,
        "metadata": parsed.metadata,
    }


def frozen_source(identifier: str, *, graph: bool = False) -> dict[str, Any]:
    group, row = _entry(identifier, graph=graph)
    return _frozen_source(identifier, group, row)


def frozen_sources(
    groups: tuple[str, ...] = DEFAULT_GROUPS, *, retain_first: bool = True,
) -> list[dict[str, Any]]:
    """Load the checked-in corpus; production manifests are deliberately not consulted."""
    selected: dict[str, tuple[str, dict[str, Any]]] = {}
    for group in groups:
        for identifier, row in entries(group).items():
            # R-793's historical identifier remains directly addressable for
            # legacy regressions, but it is no longer part of the current
            # governed-source inventory after normalization.
            if identifier == "CAPRMEDIO-R-793":
                continue
            if not retain_first:
                selected[identifier] = (group, row)
            else:
                selected.setdefault(identifier, (group, row))
    return [_frozen_source(identifier, group, row) for identifier, (group, row) in selected.items()]


def frozen_authority_fixture_bytes(identifier: str, *, graph: bool = False) -> bytes:
    group, row = _entry(identifier, graph=graph)
    raw = (FIXTURES / row["fixture"]).read_bytes()
    if hashlib.sha256(raw).hexdigest() != row["sha256"]:
        raise AssertionError("frozen authority fixture hash changed: " + identifier)
    return raw


def write_frozen_authority(
    root: Path, control: Path, identifiers: tuple[str, ...], *,
    graph_only_identifiers: frozenset[str] = frozenset(),
) -> None:
    """Place the static corpus at its static fake-selected-Project locators."""
    for identifier in dict.fromkeys(identifiers):
        variants = (True,) if identifier in graph_only_identifiers else (False,)
        for graph in variants:
            entry = frozen_entry(identifier, graph=graph)
            relative = Path(entry["source_path"])
            destination = root / control / relative.relative_to(".caprmedio_caprmedio")
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(frozen_authority_fixture_bytes(identifier, graph=graph))
