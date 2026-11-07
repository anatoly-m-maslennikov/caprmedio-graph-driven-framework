# CA-R-2723@3
# CA-R-2724@3
# CA-R-2725@3
# CA-M-464@8
# CA-M-465@23
# CA-D-672@12

"""Materialize authored references and literal declared inverse bindings in memory."""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Mapping
import datetime as dt
import hashlib
import json
from pathlib import Path
import re
import sys
from typing import Any

from markdown_it import MarkdownIt

from .markdown_content import source_markdown


TOOLS = Path(__file__).resolve().parents[3] / "FEATURE_TOOLS"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from carrier_aliases import carrier_read_view  # noqa: E402

ATOM = "Atom"
SCOPE = "Scope Unit"
_NAME = r"[A-Za-z_][A-Za-z_0-9]*"
_RELATION = re.compile(rf"Relation//({_NAME})(?![A-Za-z_0-9])")
_INVERSE = re.compile(
    rf"Relation//({_NAME})\s+(\(\(HAS_INVERSE\)\)|<\(\(HAS_INVERSE\)\)|<-->)"
    rf"\s+Relation//({_NAME})\s*;?\s*\Z"
)


def json_value(value: Any) -> Any:
    """Represent admitted YAML values without changing their source Header."""
    if isinstance(value, (dt.datetime, dt.date, dt.time)):
        return value.isoformat()
    if isinstance(value, dict):
        if any(not isinstance(key, str) for key in value):
            raise ValueError("JSON mapping keys must be strings")
        return {key: json_value(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [json_value(item) for item in value]
    return value


def canonical(value: Any) -> str:
    return json.dumps(json_value(value), ensure_ascii=False, sort_keys=True,
                      separators=(",", ":"), allow_nan=False)


def _subjects(header: Mapping[str, Any]) -> list[str]:
    subjects = carrier_read_view(dict(header)).get("subjects", {})
    active = subjects.get("active", subjects.get("governs", [])) if isinstance(subjects, dict) else []
    if isinstance(active, str):
        return [active]
    return [x for x in active if isinstance(x, str)] if isinstance(active, list) else []


def _literal_bindings(body: str) -> list[tuple[str, str]]:
    bindings = []
    for token in MarkdownIt("commonmark").parse(body):
        if token.type != "fence" or token.info.strip().upper() != "CFEL":
            continue
        for line in token.content.splitlines():
            match = _INVERSE.fullmatch(line.strip())
            if match is not None:
                left, operator, right = match.groups()
                bindings.append((right, left) if operator.startswith("<((") else (left, right))
    return bindings


def _unambiguous_inverses(bindings: list[tuple[str, str]]) -> dict[str, str]:
    pairs = set(bindings)
    targets_by_direct: dict[str, set[str]] = defaultdict(set)
    owners_by_target: dict[str, set[str]] = defaultdict(set)
    for direct, derived in pairs:
        targets_by_direct[direct].add(derived)
        owners_by_target[derived].add(direct)
    derived_as_direct = {
        direct for direct in targets_by_direct
        if any(owner != direct for owner in owners_by_target[direct])
    }
    rejected = {
        (direct, derived)
        for direct, derived in pairs
        if direct == derived
        or len(targets_by_direct[direct]) > 1
        or len(owners_by_target[derived]) > 1
        or direct in derived_as_direct
        or derived in derived_as_direct
    }
    for direct, derived in sorted(pairs):
        if direct == derived:
            print(f"Workbench: ambiguous inverse binding {direct} -> {derived}: self-pair", file=sys.stderr)
    for direct, targets in sorted(targets_by_direct.items()):
        if len(targets) > 1:
            print(f"Workbench: ambiguous inverse bindings for {direct}: "
                  f"multiple inverses {', '.join(sorted(targets))}", file=sys.stderr)
    for derived, owners in sorted(owners_by_target.items()):
        if len(owners) > 1:
            print(f"Workbench: ambiguous inverse bindings for {derived}: "
                  f"multiple direct owners {', '.join(sorted(owners))}", file=sys.stderr)
    for direct in sorted(derived_as_direct):
        print(f"Workbench: ambiguous inverse binding: derived Relation {direct} is declared direct", file=sys.stderr)
    return {direct: derived for direct, derived in pairs - rejected}


def registry_contribution(row: Mapping[str, Any]) -> tuple[frozenset[str], tuple[tuple[str, str], ...]]:
    """Return one source's literal registry input without evaluating CFEL."""
    if row.get("status_group") != "Current" or row.get("role") != "Requirement":
        return frozenset(), ()
    if row.get("form") not in {"Declaration", "Definition", "Entity Definition", "Relation Definition"}:
        return frozenset(), ()
    names = frozenset(name for subject in _subjects(row.get("header_json", {})) for name in _RELATION.findall(subject))
    return names, tuple(_literal_bindings(source_markdown(row) or "")) if names else ()


def registry_from_contributions(
    contributions: Mapping[str, tuple[frozenset[str], tuple[tuple[str, str], ...]]],
) -> tuple[set[str], dict[str, str], set[str]]:
    registered: set[str] = set()
    origins: dict[str, set[str]] = defaultdict(set)
    bindings = []
    for source, (names, source_bindings) in contributions.items():
        registered.update(names)
        for name in names:
            origins[name].add(source)
        bindings.extend(source_bindings)
    collisions = _case_collisions(registered, origins)
    registered.difference_update(collisions)
    admitted = [(direct, derived) for direct, derived in bindings
                if direct in registered and derived in registered]
    return registered, _unambiguous_inverses(admitted), collisions


def relation_registry(atoms: list[dict[str, Any]]) -> tuple[set[str], dict[str, str]]:
    """Project only literal Relation metadata, without evaluating CFEL formulas."""
    contributions = {
        row["source_path"]: registry_contribution(row)
        for row in atoms
        if isinstance(row.get("source_path"), str)
    }
    registered, inverse, collisions = registry_from_contributions(contributions)
    _warn_colliding_uses(atoms, collisions)
    return registered, inverse


def _case_collisions(
    registered: set[str], origins: Mapping[str, set[str]],
) -> set[str]:
    names_by_case: dict[str, set[str]] = defaultdict(set)
    for name in registered:
        names_by_case[name.casefold()].add(name)
    collisions = set()
    for names in sorted(names_by_case.values(), key=lambda value: sorted(value)):
        if len(names) < 2:
            continue
        collisions.update(names)
        detail = "; ".join(
            f"{name}: {', '.join(sorted(origins.get(name, ()) or ('<unknown>',)))}"
            for name in sorted(names)
        )
        print(
            "Workbench: ambiguous Relation definitions differ only by case: "
            f"{', '.join(sorted(names))}; sources: {detail}; links skipped",
            file=sys.stderr,
        )
    return collisions


def _warn_colliding_uses(atoms: list[dict[str, Any]], collisions: set[str]) -> None:
    variants_by_case: dict[str, list[str]] = defaultdict(list)
    for name in collisions:
        variants_by_case[name.casefold()].append(name)
    for row in atoms:
        relations = row.get("header_json", {}).get("relations", {})
        if not isinstance(relations, dict):
            continue
        source = row.get("source_path")
        if not isinstance(source, str):
            continue
        for name in sorted(key for key in relations if isinstance(key, str)):
            variants = variants_by_case.get(name.casefold())
            if variants:
                print(
                    f"Workbench: {source}: ambiguous registered Relation {name}; "
                    f"candidates: {', '.join(sorted(variants))}; link skipped",
                    file=sys.stderr,
                )


def _relation_name(value: str, registered: set[str], source_path: str | None = None) -> str | None:
    if value in registered:
        return value
    matches = sorted(name for name in registered if name.casefold() == value.casefold())
    if len(matches) == 1:
        return matches[0]
    if matches and source_path is not None:
        print(f"Workbench: {source_path}: ambiguous registered Relation {value}; "
              f"candidates: {', '.join(matches)}; link skipped", file=sys.stderr)
    return None


def _targets(value: Any, scope_references: Mapping[str, str], kind: str | None = None):
    if isinstance(value, str):
        if kind == SCOPE:
            yield SCOPE, scope_references.get(value, value)
        elif kind == ATOM:
            yield ATOM, value
        elif value in scope_references:
            yield SCOPE, scope_references[value]
        else:
            yield ATOM, value
    elif isinstance(value, list):
        for item in value:
            yield from _targets(item, scope_references, kind)
    elif isinstance(value, dict):
        for key, target_kind in (("atom", ATOM), ("scope_unit", SCOPE)):
            if key in value:
                yield from _targets(value[key], scope_references, target_kind)


def _scope_references(scopes: list[dict]) -> dict[str, str]:
    return {
        reference: row["name"]
        for row in scopes
        for reference in (row["name"], row["scope_unit_id"])
        if isinstance(reference, str) and reference
    }


def _scope_facts(scopes: list[dict], registered: set[str]):
    containment = _relation_name("IS_CONTAINED_BY", registered)
    for row in scopes:
        if containment and row["parent_name"]:
            yield SCOPE, row["name"], containment, SCOPE, row["parent_name"]


def _atom_facts(row: dict, scope_references: Mapping[str, str], registered: set[str]):
    if row["ref"] is None:
        return
    containment = _relation_name("IS_CONTAINED_BY", registered)
    container_kind, container_ref = _container(row, scope_references)
    if containment and container_kind is not None and container_ref is not None:
        yield ATOM, row["ref"], containment, container_kind, container_ref
    relations = row["header_json"].get("relations", {})
    if not isinstance(relations, dict):
        return
    for name, values in relations.items():
        relation = _relation_name(name, registered, row["source_path"])
        if relation:
            yield from ((ATOM, row["ref"], relation, kind, ref) for kind, ref in _targets(values, scope_references))


def _container(
    row: Mapping[str, Any], scope_references: Mapping[str, str],
) -> tuple[str | None, str | None]:
    container = carrier_read_view(dict(row["header_json"])).get("container")
    if isinstance(container, Mapping):
        scope = container.get("scope_unit")
        if isinstance(scope, str):
            return SCOPE, scope_references.get(scope, scope)
        atom = container.get("atom")
        if isinstance(atom, str):
            return ATOM, atom
    legacy = row.get("current_scope_unit")
    return (SCOPE, scope_references.get(legacy, legacy)) if isinstance(legacy, str) else (None, None)


def _edge(fact, derived: bool) -> dict[str, Any]:
    source_kind, source_ref, relation, target_kind, target_ref = fact
    return {"source_kind": source_kind, "source_ref": source_ref,
            "target_kind": target_kind, "target_ref": target_ref,
            "relation_type": relation, "derived": derived}


def _timestamp(value: Any) -> str | None:
    try:
        timestamp = value if isinstance(value, dt.datetime) else dt.datetime.fromisoformat(value)
    except (TypeError, ValueError):
        return None
    return timestamp.astimezone(dt.timezone.utc).isoformat() if timestamp.tzinfo else None


def _unique_references(atoms: list[dict]) -> list[dict]:
    references: dict[str, list[dict]] = defaultdict(list)
    for row in atoms:
        if row["ref"] is not None:
            references[row["ref"]].append(row)
    duplicates = {ref for ref, rows in references.items() if len(rows) > 1}
    for ref in sorted(duplicates):
        for row in references[ref]:
            print(f"Workbench: {row['source_path']}: ambiguous duplicate reference {ref}",
                  file=sys.stderr)
    return [row for row in atoms if row["ref"] not in duplicates]


def _materialized_row(kind: str, source: dict, facts: tuple[tuple, ...]) -> dict | None:
    row = dict(source)
    row["relation_edges_json"] = [_edge(fact[:-1], fact[-1]) for fact in facts]
    if kind == ATOM:
        row["updated_at"] = _timestamp(row["updated_at"])
    try:
        payload = {key: value for key, value in row.items() if key not in {"hash", "_content_bytes"}}
        if "_content_bytes" in row:
            payload["content_markdown"] = source_markdown(row)
        row["hash"] = hashlib.sha256(canonical(payload).encode("utf-8")).hexdigest()
        return row
    except (TypeError, ValueError) as error:
        path = row.get("source_path", row.get("declaration_source_path"))
        print(f"Workbench: {path}: {error}", file=sys.stderr)
        return None


def _direct_atom_facts(
    atoms: list[dict], scope_references: Mapping[str, str], registered: set[str],
    context: tuple, previous_atoms: Mapping[str, dict[str, Any]],
) -> dict[str, tuple[tuple, ...]]:
    result = {}
    for source in atoms:
        path = source.get("source_path")
        cached = previous_atoms.get(path) if isinstance(path, str) else None
        facts = (
            cached["direct_facts"]
            if cached is not None and cached["raw"] is source and cached.get("context") == context
            else tuple(_atom_facts(source, scope_references, registered))
        )
        if isinstance(path, str):
            result[path] = facts
    return result


def _outgoing_facts(
    scopes: list[dict], registered: set[str], inverse: Mapping[str, str],
    atom_direct_facts: Mapping[str, tuple[tuple, ...]],
) -> dict[tuple[str, str], set[tuple]]:
    outgoing: dict[tuple[str, str], set[tuple]] = defaultdict(set)
    for fact in (*_scope_facts(scopes, registered), *(fact for facts in atom_direct_facts.values() for fact in facts)):
        outgoing[fact[:2]].add((*fact, False))
        if fact[2] in inverse:
            reverse = (fact[3], fact[4], inverse[fact[2]], fact[0], fact[1])
            outgoing[reverse[:2]].add((*reverse, True))
    return outgoing


def _materialize_atoms(
    atoms: list[dict], outgoing: Mapping[tuple[str, str], set[tuple]], context: tuple,
    atom_direct_facts: Mapping[str, tuple[tuple, ...]], previous_atoms: Mapping[str, dict[str, Any]],
) -> tuple[list[dict], dict[str, dict[str, Any]]]:
    next_atoms: dict[str, dict[str, Any]] = {}
    rows = []
    for source in atoms:
        facts = tuple(sorted(outgoing[(ATOM, source["ref"])]))
        path = source.get("source_path")
        cached = previous_atoms.get(path) if isinstance(path, str) else None
        row = cached["row"] if cached is not None and cached["raw"] is source and cached["facts"] == facts else _materialized_row(ATOM, source, facts)
        if row is not None:
            rows.append(row)
            if isinstance(path, str):
                next_atoms[path] = {"raw": source, "context": context, "direct_facts": atom_direct_facts[path], "facts": facts, "row": row}
    return rows, next_atoms


def materialize_with_registry(
    atoms: list[dict], scopes: list[dict], previous_atoms: Mapping[str, dict[str, Any]] | None = None,
) -> tuple[list[dict], list[dict], set[str], dict[str, str], dict[str, dict[str, Any]]]:
    """Materialize one captured inventory and reuse unchanged Atom rows by identity."""
    atoms = _unique_references(atoms)
    registered, inverse = relation_registry(atoms)
    scope_references = _scope_references(scopes)
    context = (
        tuple(sorted(registered)),
        tuple(sorted(inverse.items())),
        tuple(sorted(scope_references.items())),
    )
    prior = previous_atoms or {}
    atom_direct_facts = _direct_atom_facts(atoms, scope_references, registered, context, prior)
    outgoing = _outgoing_facts(scopes, registered, inverse, atom_direct_facts)
    atom_rows, next_atoms = _materialize_atoms(atoms, outgoing, context, atom_direct_facts, prior)

    scope_rows = []
    for source in scopes:
        row = _materialized_row(SCOPE, source, tuple(sorted(outgoing[(SCOPE, source["name"])])))
        if row is not None:
            scope_rows.append(row)
    return atom_rows, scope_rows, registered, inverse, next_atoms


def materialize(atoms: list[dict], scopes: list[dict]) -> tuple[list[dict], list[dict]]:
    """Assign each row its outgoing facts, then hash its final canonical data."""
    rows, scope_rows, _registered, _inverse, _cache = materialize_with_registry(atoms, scopes)
    return rows, scope_rows
