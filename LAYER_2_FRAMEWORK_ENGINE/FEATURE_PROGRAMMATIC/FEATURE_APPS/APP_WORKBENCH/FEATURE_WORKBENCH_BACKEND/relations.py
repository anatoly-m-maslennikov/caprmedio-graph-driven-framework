# CA-R-2724@5
# CA-M-464@9
# CA-M-465@29
# CA-M-509@7
# CA-D-672@22

"""Materialize authored references and literal declared inverse bindings in memory."""
from __future__ import annotations

from collections import defaultdict
from collections.abc import Mapping
import datetime as dt
import hashlib
import json
import sys
from typing import Any

from .markdown_content import source_markdown
from .relation_registry import (
    RelationRegistry, _warn_colliding_uses, carrier_read_view, compile_relation_registry,
)
from project_root_container import is_logical_container

ATOM = "Atom"
SCOPE = "Scope Unit"


def _graph_sources(atoms: list[dict]) -> list[dict]:
    selected = []
    seen = set()
    for atom in atoms:
        if atom.get("status_group") == "Archived":
            continue
        reference = atom.get("ref")
        if reference is not None and reference in seen:
            continue
        selected.append(atom)
        if reference is not None:
            seen.add(reference)
    return selected


def _carrier_facts(row: dict, aliases: Mapping[str, str], registry: RelationRegistry) -> tuple[tuple, ...]:
    outgoing = _outgoing_facts([], registry, {row["source_path"]: tuple(_atom_facts(row, aliases, registry))})
    return tuple(sorted(outgoing.get((ATOM, row.get("ref")), ())))


def _materialized_atom(row: dict, facts: tuple[tuple, ...], *, graph: bool) -> dict | None:
    if not graph:
        row = {**row, "_graph_excluded": True,
               "_carrier_relation_edges_json": [_edge(fact[:-1], fact[-1]) for fact in facts]}
        facts = ()
    return _materialized_row(ATOM, row, facts)


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


def relation_registry(atoms: list[dict[str, Any]]) -> tuple[set[str], dict[str, str]]:
    """Project only literal Relation metadata, without evaluating CFEL formulas."""
    registry = compile_relation_registry(atoms)
    _warn_colliding_uses(atoms, registry.collisions)
    return set(registry.names), dict(registry.inverse)


def _relation_name(
    value: str, registry: RelationRegistry, source_path: str | None = None,
) -> tuple[str, bool] | None:
    addresses = {name: (name, False) for name in registry.names} | {
        inverse: (direct, True) for direct, inverse in registry.inverse.items()
    } | {
        alias: (name, True) for alias, name in registry.aliases.items()
    }
    if value in addresses:
        return addresses[value]
    matches = sorted(name for name in addresses if name.casefold() == value.casefold())
    if len(matches) == 1:
        return addresses[matches[0]]
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


def _scope_facts(scopes: list[dict], registry: RelationRegistry):
    containment = _relation_name("IS_CONTAINED_BY", registry)
    for row in scopes:
        if containment and row["parent_name"]:
            relation, inverse = containment
            source = (SCOPE, row["name"])
            target = (SCOPE, row["parent_name"])
            yield (*target, relation, *source) if inverse else (*source, relation, *target)


def _atom_facts(row: dict, scope_references: Mapping[str, str], registry: RelationRegistry):
    if row["ref"] is None:
        return
    containment = _relation_name("IS_CONTAINED_BY", registry)
    container_kind, container_ref = _container(row, scope_references)
    if containment and container_kind is not None and container_ref is not None:
        relation, inverse = containment
        source = (ATOM, row["ref"])
        target = (container_kind, container_ref)
        yield (*target, relation, *source) if inverse else (*source, relation, *target)
    relations = row["header_json"].get("relations", {})
    if not isinstance(relations, dict):
        return
    for name, values in relations.items():
        resolved = _relation_name(name, registry, row["source_path"])
        if resolved:
            relation, inverse = resolved
            for kind, ref in _targets(values, scope_references):
                source = (ATOM, row["ref"])
                target = (kind, ref)
                yield (*target, relation, *source) if inverse else (*source, relation, *target)


def _container(
    row: Mapping[str, Any], scope_references: Mapping[str, str],
) -> tuple[str | None, str | None]:
    root_header = row.get("_project_root_header")
    container = carrier_read_view(dict(row["header_json"] if root_header is None else root_header)).get("container")
    if root_header is not None and not is_logical_container(container):
        return None, None
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


def _materialized_row(kind: str, source: dict, facts: tuple[tuple, ...]) -> dict | None:
    row = dict(source)
    row.pop("_project_root_header", None)
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
    atoms: list[dict], scope_references: Mapping[str, str], registry: RelationRegistry,
    context: tuple, previous_atoms: Mapping[str, dict[str, Any]],
) -> dict[str, tuple[tuple, ...]]:
    result = {}
    for source in atoms:
        path = source.get("source_path")
        cached = previous_atoms.get(path) if isinstance(path, str) else None
        facts = (
            cached["direct_facts"]
            if cached is not None and cached["raw"] is source and cached.get("context") == context
            else tuple(_atom_facts(source, scope_references, registry))
        )
        if isinstance(path, str):
            result[path] = facts
    return result


def _outgoing_facts(
    scopes: list[dict], registry: RelationRegistry,
    atom_direct_facts: Mapping[str, tuple[tuple, ...]],
) -> dict[tuple[str, str], set[tuple]]:
    outgoing: dict[tuple[str, str], set[tuple]] = defaultdict(set)
    for fact in (*_scope_facts(scopes, registry), *(fact for facts in atom_direct_facts.values() for fact in facts)):
        outgoing[fact[:2]].add((*fact, False))
        if fact[2] in registry.inverse:
            reverse = (fact[3], fact[4], registry.inverse[fact[2]], fact[0], fact[1])
            outgoing[reverse[:2]].add((*reverse, True))
    return outgoing


def _support_for_fact(
    fact: tuple, registry: RelationRegistry, present: set[tuple[str, str]],
) -> dict[tuple[str, str], set[tuple]]:
    """Keep both representations traversable when precisely one endpoint is absent."""
    inverse = registry.inverse.get(fact[2])
    if inverse is None:
        return {}
    reverse = (fact[3], fact[4], inverse, fact[0], fact[1])
    support: dict[tuple[str, str], set[tuple]] = defaultdict(set)
    if fact[:2] not in present and reverse[:2] in present:
        support[reverse[:2]].add((*fact, False))
    if reverse[:2] not in present and fact[:2] in present:
        support[fact[:2]].add((*reverse, True))
    return support


def _support_facts(
    atoms: list[dict], scopes: list[dict], registry: RelationRegistry,
    atom_direct_facts: Mapping[str, tuple[tuple, ...]],
) -> dict[tuple[str, str], set[tuple]]:
    """Keep direct and derived traversal edges if exactly one typed endpoint is absent."""
    present = {
        (ATOM, row["ref"])
        for row in atoms
        if isinstance(row.get("ref"), str)
    } | {
        (SCOPE, row["name"])
        for row in scopes
        if isinstance(row.get("name"), str)
    }
    support: dict[tuple[str, str], set[tuple]] = defaultdict(set)
    facts = (*_scope_facts(scopes, registry), *(fact for values in atom_direct_facts.values() for fact in values))
    for fact in facts:
        for owner, edges in _support_for_fact(fact, registry, present).items():
            support[owner].update(edges)
    return support


def _materialize_atoms(
    atoms: list[dict], outgoing: Mapping[tuple[str, str], set[tuple]], context: tuple,
    atom_direct_facts: Mapping[str, tuple[tuple, ...]], previous_atoms: Mapping[str, dict[str, Any]],
    support: Mapping[tuple[str, str], set[tuple]], graph_paths: set[str],
    aliases: Mapping[str, str], registry: RelationRegistry,
) -> tuple[list[dict], dict[str, dict[str, Any]]]:
    next_atoms: dict[str, dict[str, Any]] = {}
    rows = []
    for source in atoms:
        path = source.get("source_path")
        graph = path in graph_paths
        facts = (tuple(sorted((*outgoing.get((ATOM, source["ref"]), ()),
                               *support.get((ATOM, source["ref"]), ()))))
                 if graph else _carrier_facts(source, aliases, registry))
        cached = previous_atoms.get(path) if isinstance(path, str) else None
        row = (cached["row"] if cached is not None and cached["raw"] is source and cached["facts"] == facts
               and bool(cached["row"].get("_graph_excluded")) != graph
               else _materialized_atom(source, facts, graph=graph))
        if row is not None:
            rows.append(row)
            if isinstance(path, str):
                next_atoms[path] = {"raw": source, "context": context, "direct_facts": atom_direct_facts.get(path, ()), "facts": facts, "row": row}
    return rows, next_atoms


def materialize_with_registry(
    atoms: list[dict], scopes: list[dict], previous_atoms: Mapping[str, dict[str, Any]] | None = None,
) -> tuple[list[dict], list[dict], set[str], dict[str, str], dict[str, dict[str, Any]]]:
    """Materialize one captured inventory and reuse unchanged Atom rows by identity."""
    graph_atoms = _graph_sources(atoms)
    registry = compile_relation_registry(graph_atoms)
    _warn_colliding_uses(graph_atoms, registry.collisions)
    scope_references = _scope_references(scopes)
    context = (
        tuple(sorted(registry.names)),
        tuple(sorted(registry.inverse.items())),
        tuple(sorted(registry.aliases.items())),
        tuple(sorted(scope_references.items())),
    )
    prior = previous_atoms or {}
    atom_direct_facts = _direct_atom_facts(graph_atoms, scope_references, registry, context, prior)
    outgoing = _outgoing_facts(scopes, registry, atom_direct_facts)
    support = _support_facts(graph_atoms, scopes, registry, atom_direct_facts)
    graph_paths = {row.get("source_path") for row in graph_atoms}
    atom_rows, next_atoms = _materialize_atoms(atoms, outgoing, context, atom_direct_facts, prior, support,
                                               graph_paths, scope_references, registry)

    scope_rows = []
    for source in scopes:
        facts = tuple(sorted((*outgoing[(SCOPE, source["name"])], *support.get((SCOPE, source["name"]), ()))))
        row = _materialized_row(SCOPE, source, facts)
        if row is not None:
            scope_rows.append(row)
    return atom_rows, scope_rows, set(registry.names), dict(registry.inverse), next_atoms


def materialize(atoms: list[dict], scopes: list[dict]) -> tuple[list[dict], list[dict]]:
    """Assign each row its outgoing facts, then hash its final canonical data."""
    rows, scope_rows, _registered, _inverse, _cache = materialize_with_registry(atoms, scopes)
    return rows, scope_rows
