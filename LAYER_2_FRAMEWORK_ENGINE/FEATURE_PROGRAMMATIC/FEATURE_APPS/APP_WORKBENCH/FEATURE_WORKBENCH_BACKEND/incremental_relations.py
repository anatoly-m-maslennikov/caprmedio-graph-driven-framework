# CA-R-2724@5
# CA-M-465@29
# CA-M-509@7
# CA-D-672@22

"""Copy-on-write relation materialization for an incremental source batch."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

from .index_delta import MaterializationDelta
from .relations import (
    ATOM, SCOPE, _atom_facts, _materialized_row, _scope_facts,
    _scope_references, _support_facts, _support_for_fact, _graph_sources,
    _carrier_facts, _materialized_atom,
)
from .relation_registry import (
    RelationRegistry, RegistryCompilation, RegistryContribution, _unambiguous_aliases,
    _warn_colliding_uses, compile_registry, registry_contribution, registry_from_contributions,
)


@dataclass(frozen=True)
class RelationState:
    raw_by_path: dict[str, dict]
    refs: dict[str, str]
    direct_facts: dict[str, tuple[tuple, ...]]
    outgoing: dict[tuple[str, str], frozenset[tuple]]
    atom_rows: dict[str, dict]
    atom_order: tuple[str, ...]
    scope_rows: dict[str, dict]
    scope_order: tuple[str, ...]
    scope_signature: tuple[tuple[str, str | None, str | None], ...]
    registered: frozenset[str]
    inverse: dict[str, str]
    aliases: dict[str, str]
    excluded_paths: frozenset[str]
    duplicate_refs: frozenset[str]
    registry_contributions: dict[str, RegistryContribution]
    collisions: frozenset[str]
    fact_contributors: dict[tuple, frozenset[tuple[str, str]]]
    facts_by_endpoint: dict[tuple[str, str], frozenset[tuple]]
    support: dict[tuple[str, str], frozenset[tuple]]
    static_registry: bool


def _scope_signature(scopes: list[dict]) -> tuple[tuple[str, str | None, str | None], ...]:
    return tuple((row["name"], row.get("scope_unit_id"), row.get("parent_name")) for row in scopes)


def _registry(
    contributions: Mapping[str, RegistryContribution],
) -> RelationRegistry:
    names, inverse, collisions = registry_from_contributions(contributions)
    return RelationRegistry(frozenset(names), inverse, _unambiguous_aliases(contributions, names), frozenset(collisions))


def _fact_contributors(
    scopes: list[dict], registry: RelationRegistry, direct: Mapping[str, tuple[tuple, ...]],
) -> dict[tuple, frozenset[tuple[str, str]]]:
    contributors: dict[tuple, set[tuple[str, str]]] = {}
    for fact in _scope_facts(scopes, registry):
        contributors.setdefault(fact, set()).add(("scope", fact[1]))
    for path, facts in direct.items():
        for fact in facts:
            contributors.setdefault(fact, set()).add(("atom", path))
    return {fact: frozenset(owners) for fact, owners in contributors.items()}


def _facts_by_endpoint(contributors: Mapping[tuple, object]) -> dict[tuple[str, str], frozenset[tuple]]:
    indexed: dict[tuple[str, str], set[tuple]] = {}
    for fact in contributors:
        for endpoint in (fact[:2], fact[3:]):
            indexed.setdefault(endpoint, set()).add(fact)
    return {endpoint: frozenset(facts) for endpoint, facts in indexed.items()}


def _index_fact(
    indexed: dict[tuple[str, str], frozenset[tuple]], fact: tuple, *, add: bool,
) -> None:
    for endpoint in {fact[:2], fact[3:]}:
        facts = set(indexed.get(endpoint, ()))
        if add:
            facts.add(fact)
        else:
            facts.discard(fact)
        if facts:
            indexed[endpoint] = frozenset(facts)
        else:
            indexed.pop(endpoint, None)


def _refresh_support(
    support: dict[tuple[str, str], frozenset[tuple]], fact: tuple, registry: RelationRegistry,
    present: set[tuple[str, str]], *, active: bool,
) -> set[tuple[str, str]]:
    """Replace this fact's support edges without enumerating unrelated facts."""
    inverse = registry.inverse.get(fact[2])
    if inverse is None:
        return set()
    reverse = (fact[3], fact[4], inverse, fact[0], fact[1])
    affected: set[tuple[str, str]] = set()
    for owner in (fact[:2], reverse[:2]):
        before = support.get(owner)
        if before is None:
            continue
        edges = set(before)
        edges.discard((*fact, False))
        edges.discard((*reverse, True))
        if edges:
            support[owner] = frozenset(edges)
        else:
            support.pop(owner, None)
        if before != frozenset(edges):
            affected.add(owner)
    for owner, edges in (_support_for_fact(fact, registry, present).items() if active else ()):
        before = support.get(owner, frozenset())
        current = set(before)
        current.update(edges)
        support[owner] = frozenset(current)
        if before != support[owner]:
            affected.add(owner)
    return affected


def _duplicate_membership(atoms: list[dict]) -> tuple[frozenset[str], frozenset[str]]:
    paths_by_ref: dict[str, set[str]] = {}
    first_paths: dict[str, str] = {}
    for row in atoms:
        ref, path = row.get("ref"), row.get("source_path")
        if isinstance(ref, str) and isinstance(path, str):
            paths_by_ref.setdefault(ref, set()).add(path)
            first_paths.setdefault(ref, path)
    duplicate_refs = frozenset(ref for ref, paths in paths_by_ref.items() if len(paths) > 1)
    return (
        frozenset(path for ref, paths in paths_by_ref.items() if ref in duplicate_refs
                  for path in paths if path != first_paths[ref]),
        duplicate_refs,
    )


def _add(outgoing: dict[tuple[str, str], set[tuple]], fact: tuple, inverse: Mapping[str, str]) -> set[tuple[str, str]]:
    affected = {fact[:2]}
    outgoing.setdefault(fact[:2], set()).add((*fact, False))
    if fact[2] in inverse:
        reverse = (fact[3], fact[4], inverse[fact[2]], fact[0], fact[1])
        outgoing.setdefault(reverse[:2], set()).add((*reverse, True))
        affected.add(reverse[:2])
    return affected


def _remove(outgoing: dict[tuple[str, str], set[tuple]], fact: tuple, inverse: Mapping[str, str]) -> set[tuple[str, str]]:
    affected = {fact[:2]}
    outgoing.get(fact[:2], set()).discard((*fact, False))
    if fact[2] in inverse:
        reverse = (fact[3], fact[4], inverse[fact[2]], fact[0], fact[1])
        outgoing.get(reverse[:2], set()).discard((*reverse, True))
        affected.add(reverse[:2])
    return affected


def _delta_edge(
    outgoing: dict[tuple[str, str], frozenset[tuple]], fact: tuple, inverse: Mapping[str, str], *, add: bool,
) -> set[tuple[str, str]]:
    affected = {fact[:2]}
    edges = set(outgoing.get(fact[:2], ()))
    (edges.add if add else edges.discard)((*fact, False))
    if edges:
        outgoing[fact[:2]] = frozenset(edges)
    else:
        outgoing.pop(fact[:2], None)
    if fact[2] in inverse:
        reverse = (fact[3], fact[4], inverse[fact[2]], fact[0], fact[1])
        edges = set(outgoing.get(reverse[:2], ()))
        (edges.add if add else edges.discard)((*reverse, True))
        if edges:
            outgoing[reverse[:2]] = frozenset(edges)
        else:
            outgoing.pop(reverse[:2], None)
        affected.add(reverse[:2])
    return affected


def _full_state(
    atoms: list[dict], scopes: list[dict], compilation: RegistryCompilation | None = None,
    registry: RelationRegistry | None = None,
) -> RelationState:
    excluded_paths, duplicate_refs = _duplicate_membership(atoms)
    graph_atoms = _graph_sources(atoms)
    static_registry = registry is not None
    if registry is None:
        compiled = compile_registry(graph_atoms) if compilation is None else compilation
        contributions = compiled.contributions
        registry = compiled.registry
    else:
        contributions = {}
    _warn_colliding_uses(graph_atoms, registry.collisions)
    aliases = _scope_references(scopes)
    raw_by_path = {row["source_path"]: row for row in atoms if isinstance(row.get("source_path"), str)}
    graph_paths = {row.get("source_path") for row in graph_atoms}
    direct = {path: tuple(_atom_facts(row, aliases, registry))
              for path, row in raw_by_path.items() if path in graph_paths}
    contributors = _fact_contributors(scopes, registry, direct)
    facts_by_endpoint = _facts_by_endpoint(contributors)
    outgoing: dict[tuple[str, str], set[tuple]] = {}
    for fact in contributors:
        _add(outgoing, fact, registry.inverse)
    support = _support_facts(graph_atoms, scopes, registry, direct)
    atom_rows = {}
    for path, row in raw_by_path.items():
        graph = path in graph_paths
        facts = (tuple(sorted((*outgoing.get((ATOM, row["ref"]), ()),
                               *support.get((ATOM, row["ref"]), ()))))
                 if graph else _carrier_facts(row, aliases, registry))
        materialized = _materialized_atom(row, facts, graph=graph)
        if materialized is not None:
            atom_rows[path] = materialized
    scope_rows = {}
    for row in scopes:
        facts = tuple(sorted((*outgoing.get((SCOPE, row["name"]), ()), *support.get((SCOPE, row["name"]), ()))))
        materialized = _materialized_row(SCOPE, row, facts)
        if materialized is not None:
            scope_rows[row["name"]] = materialized
    return RelationState(
        raw_by_path, {row["ref"]: row["source_path"] for row in graph_atoms if row["ref"] is not None}, direct,
        {key: frozenset(value) for key, value in outgoing.items()}, atom_rows, tuple(raw_by_path),
        scope_rows, tuple(scope_rows), _scope_signature(scopes), registry.names, dict(registry.inverse), dict(registry.aliases),
        excluded_paths, duplicate_refs, contributions, registry.collisions, contributors,
        facts_by_endpoint, {key: frozenset(value) for key, value in support.items()}, static_registry,
    )


def _requires_full(state: RelationState, scopes: list[dict], changes: Mapping[str, dict | None]) -> bool:
    if state.scope_signature != _scope_signature(scopes):
        return True
    changed_refs: dict[str, set[str]] = {}
    released_refs: set[str] = set()
    for path, new in changes.items():
        old = state.raw_by_path.get(path)
        old_ref = old.get("ref") if old and old.get("status_group") != "Archived" else None
        new_ref = new.get("ref") if new and new.get("status_group") != "Archived" else None
        if isinstance(new_ref, str):
            changed_refs.setdefault(new_ref, set()).add(path)
        if isinstance(old_ref, str) and old_ref != new_ref:
            released_refs.add(old_ref)
    if any(len(paths) > 1 for paths in changed_refs.values()):
        return True
    for path, new in changes.items():
        old = state.raw_by_path.get(path)
        old_ref = old.get("ref") if old and old.get("status_group") != "Archived" else None
        new_ref = new.get("ref") if new is not None and new.get("status_group") != "Archived" else None
        if path in state.excluded_paths or any(
            isinstance(reference, str) and reference in state.duplicate_refs
            for reference in (old_ref, new_ref)
        ):
            return True
        owner = state.refs.get(new_ref) if isinstance(new_ref, str) else None
        if old_ref != new_ref and owner is not None and owner != path and new_ref not in released_refs:
            return True
        if old_ref is not None and old_ref != new_ref and state.refs.get(old_ref) != path:
            return True
    return False


def _next_registry(
    state: RelationState, changes: Mapping[str, dict | None],
) -> tuple[dict[str, RegistryContribution], RelationRegistry]:
    contributions = dict(state.registry_contributions)
    for path, row in changes.items():
        if row is None:
            contributions.pop(path, None)
        else:
            if row.get("status_group") != "Archived":
                contributions[path] = registry_contribution(row)
            else:
                contributions.pop(path, None)
    return contributions, _registry(contributions)


def _rows(state: RelationState) -> tuple[list[dict], list[dict]]:
    return ([state.atom_rows[path] for path in state.atom_order if path in state.atom_rows],
            [state.scope_rows[name] for name in state.scope_order if name in state.scope_rows])


def materialize_delta(  # noqa: C901
    atoms: list[dict], scopes: list[dict], previous_state: RelationState | None = None,
    changes: Mapping[str, dict | None] | None = None,
    initial_compilation: RegistryCompilation | None = None,
    registry: RelationRegistry | None = None,
) -> tuple[list[dict], list[dict], set[str], dict[str, str], RelationState, MaterializationDelta | None]:
    """Return a full build or a changed-source relation delta without source mutation."""
    if previous_state is not None and previous_state.static_registry:
        registry = RelationRegistry(previous_state.registered, previous_state.inverse, previous_state.aliases, previous_state.collisions)
    if previous_state is None or changes is None or _requires_full(previous_state, scopes, changes):
        state = _full_state(atoms, scopes, initial_compilation if previous_state is None else None, registry)
        rows, scope_rows = _rows(state)
        return rows, scope_rows, set(state.registered), dict(state.inverse), state, None

    if previous_state.static_registry:
        contributions = previous_state.registry_contributions
        registry = RelationRegistry(previous_state.registered, previous_state.inverse, previous_state.aliases, previous_state.collisions)
    else:
        contributions, registry = _next_registry(previous_state, changes)
    if (registry.names, registry.inverse, registry.aliases, registry.collisions) != (
        previous_state.registered, previous_state.inverse, previous_state.aliases, previous_state.collisions,
    ):
        state = _full_state(atoms, scopes)
        rows, scope_rows = _rows(state)
        return rows, scope_rows, set(state.registered), dict(state.inverse), state, None

    aliases = _scope_references(scopes)
    raw = dict(previous_state.raw_by_path)
    direct = dict(previous_state.direct_facts)
    contributors = dict(previous_state.fact_contributors)
    facts_by_endpoint = dict(previous_state.facts_by_endpoint)
    outgoing = dict(previous_state.outgoing)
    refs = dict(previous_state.refs)
    affected: set[tuple[str, str]] = set()
    changed_paths = set(changes)
    changed_facts: set[tuple] = set()
    touched_refs: set[str] = set()
    # A carrier rename retains its reference. Remove every old source fact
    # before any replacement fact can use that reference.
    for path in changes:
        old = raw.get(path)
        if old is not None and old.get("ref") is not None and refs.get(old["ref"]) == path:
            refs.pop(old["ref"])
            touched_refs.add(old["ref"])
        for fact in direct.pop(path, ()):
            owners = set(contributors.get(fact, ()))
            owners.discard(("atom", path))
            if owners:
                contributors[fact] = frozenset(owners)
            else:
                contributors.pop(fact, None)
                _index_fact(facts_by_endpoint, fact, add=False)
                changed_facts.add(fact)
                affected.update(_delta_edge(outgoing, fact, previous_state.inverse, add=False))
        raw.pop(path, None)
    for path, new in changes.items():
        if new is not None:
            raw[path] = new
            graph = new.get("status_group") != "Archived"
            facts = tuple(_atom_facts(new, aliases, registry)) if graph else ()
            direct[path] = facts
            for fact in facts:
                owners = set(contributors.get(fact, ()))
                if not owners:
                    _index_fact(facts_by_endpoint, fact, add=True)
                    changed_facts.add(fact)
                    affected.update(_delta_edge(outgoing, fact, registry.inverse, add=True))
                owners.add(("atom", path))
                contributors[fact] = frozenset(owners)
            if graph and new.get("ref") is not None:
                affected.add((ATOM, new["ref"]))
                refs[new["ref"]] = path
                touched_refs.add(new["ref"])
            _warn_colliding_uses([new], registry.collisions)

    changed_endpoints = {(ATOM, ref) for ref in touched_refs if (ref in previous_state.refs) != (ref in refs)}
    for endpoint in changed_endpoints:
        changed_facts.update(previous_state.facts_by_endpoint.get(endpoint, ()))
        changed_facts.update(facts_by_endpoint.get(endpoint, ()))
    scope_names = {row["name"] for row in scopes}
    present = {
        endpoint for fact in changed_facts for endpoint in (fact[:2], fact[3:])
        if (endpoint[0] == ATOM and endpoint[1] in refs)
        or (endpoint[0] == SCOPE and endpoint[1] in scope_names)
    }
    support = dict(previous_state.support)
    for fact in changed_facts:
        affected.update(_refresh_support(support, fact, registry, present, active=fact in contributors))

    atom_rows = dict(previous_state.atom_rows)
    old_atoms = {path: previous_state.atom_rows[path] for path in changed_paths if path in previous_state.atom_rows}
    new_atoms: dict[str, dict] = {}
    atom_paths = {refs[ref] for kind, ref in affected if kind == ATOM and ref in refs} | {path for path in changed_paths if path in raw}
    for path in atom_paths:
        if path in atom_rows:
            old_atoms.setdefault(path, atom_rows[path])
        ref = raw[path].get("ref")
        graph = raw[path].get("status_group") != "Archived"
        facts = (_carrier_facts(raw[path], aliases, registry) if not graph else
                 (() if ref is None else tuple(sorted(
                     (*outgoing.get((ATOM, ref), ()), *support.get((ATOM, ref), ())),
                 ))))
        row = _materialized_atom(raw[path], facts, graph=graph)
        if row is not None:
            atom_rows[path] = row
            new_atoms[path] = row
    for path in changed_paths:
        if path not in raw:
            atom_rows.pop(path, None)

    scope_rows = dict(previous_state.scope_rows)
    old_scopes: dict[str, dict] = {}
    new_scopes: dict[str, dict] = {}
    scope_sources = {row["name"]: row for row in scopes}
    for kind, name in affected:
        if kind != SCOPE or name not in scope_sources:
            continue
        if name in scope_rows:
            old_scopes[name] = scope_rows[name]
        facts = tuple(sorted((*outgoing.get((SCOPE, name), ()), *support.get((SCOPE, name), ()))))
        row = _materialized_row(SCOPE, scope_sources[name], facts)
        if row is not None:
            scope_rows[name] = row
            new_scopes[name] = row

    order = tuple(path for path in previous_state.atom_order if path in raw) + tuple(path for path in changes if path in raw and path not in previous_state.raw_by_path)
    state = RelationState(
        raw, refs, direct, outgoing, atom_rows, order, scope_rows, previous_state.scope_order,
        previous_state.scope_signature, registry.names, dict(registry.inverse), dict(registry.aliases),
        previous_state.excluded_paths, previous_state.duplicate_refs, contributions, registry.collisions,
        contributors, facts_by_endpoint,
        support, previous_state.static_registry,
    )
    rows, scope_output = _rows(state)
    return rows, scope_output, set(state.registered), dict(state.inverse), state, MaterializationDelta(old_atoms, new_atoms, old_scopes, new_scopes)
