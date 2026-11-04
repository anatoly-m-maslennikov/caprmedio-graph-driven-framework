# CA-R-2723@3
# CA-R-2724@2
# CA-R-2725@2
# CA-M-464@7
# CA-M-465@10
# CA-D-672@8

"""Materialize authored references and literal declared inverse bindings in memory."""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Mapping
import datetime as dt
import hashlib
import json
import re
import sys
from typing import Any

from markdown_it import MarkdownIt

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
    subjects = header.get("subjects", {})
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


def relation_registry(atoms: list[dict[str, Any]]) -> tuple[set[str], dict[str, str]]:
    """Project only literal Relation metadata, without evaluating CFEL formulas."""
    registered: set[str] = set()
    bindings = []
    for row in atoms:
        if row["status_group"] != "Current" or row["role"] != "Requirement":
            continue
        if row["form"] not in {"Declaration", "Definition", "Entity Definition", "Relation Definition"}:
            continue
        names = {name for subject in _subjects(row["header_json"]) for name in _RELATION.findall(subject)}
        if names:
            registered.update(names)
            bindings.extend(_literal_bindings(row["content_markdown"]))
    admitted = [(direct, derived) for direct, derived in bindings
                if direct in registered and derived in registered]
    return registered, _unambiguous_inverses(admitted)


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


def _direct_facts(atoms, scopes, registered):
    scope_references = {
        reference: row["name"]
        for row in scopes
        for reference in (row["name"], row["scope_unit_id"])
        if isinstance(reference, str) and reference
    }
    containment = _relation_name("IS_CONTAINED_BY", registered)
    for row in scopes:
        if containment and row["parent_name"]:
            yield SCOPE, row["name"], containment, SCOPE, row["parent_name"]
    for row in atoms:
        if row["ref"] is None:
            continue
        scope_name = scope_references.get(row["current_scope_unit"])
        if containment and scope_name:
            yield ATOM, row["ref"], containment, SCOPE, scope_name
        relations = row["header_json"].get("relations", {})
        if not isinstance(relations, dict):
            continue
        for name, values in relations.items():
            relation = _relation_name(name, registered, row["source_path"])
            if relation:
                for kind, ref in _targets(values, scope_references):
                    yield ATOM, row["ref"], relation, kind, ref


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


def materialize(atoms: list[dict], scopes: list[dict]) -> tuple[list[dict], list[dict]]:
    """Assign each row its outgoing facts, then hash its final canonical data."""
    atoms = _unique_references(atoms)
    registered, inverse = relation_registry(atoms)
    outgoing: dict[tuple[str, str], set[tuple]] = defaultdict(set)
    for fact in _direct_facts(atoms, scopes, registered):
        outgoing[fact[:2]].add((*fact, False))
        if fact[2] in inverse:
            reverse = (fact[3], fact[4], inverse[fact[2]], fact[0], fact[1])
            outgoing[reverse[:2]].add((*reverse, True))
    results = []
    for kind, rows in ((ATOM, atoms), (SCOPE, scopes)):
        result = []
        for source in rows:
            row = dict(source)
            ref = row["ref"] if kind == ATOM else row["name"]
            row["relation_edges_json"] = [_edge(fact[:-1], fact[-1]) for fact in sorted(outgoing[(kind, ref)])]
            if kind == ATOM:
                row["updated_at"] = _timestamp(row["updated_at"])
            try:
                payload = {key: value for key, value in row.items() if key != "hash"}
                row["hash"] = hashlib.sha256(canonical(payload).encode("utf-8")).hexdigest()
                result.append(row)
            except (TypeError, ValueError) as error:
                path = row.get("source_path", row.get("declaration_source_path"))
                print(f"Workbench: {path}: {error}", file=sys.stderr)
        results.append(result)
    return results[0], results[1]
