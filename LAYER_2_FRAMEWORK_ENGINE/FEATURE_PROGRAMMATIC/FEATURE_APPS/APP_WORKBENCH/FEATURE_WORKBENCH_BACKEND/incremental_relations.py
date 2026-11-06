# CA-M-465@19
# CA-E-677@14

"""Copy-on-write relation materialization for an incremental source batch."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

from .index_delta import MaterializationDelta
from .relations import (
    ATOM, SCOPE, _atom_facts, _materialized_row, _scope_facts,
    _scope_references, _unique_references, _warn_colliding_uses,
    registry_contribution, registry_from_contributions,
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
    excluded_paths: frozenset[str]
    duplicate_refs: frozenset[str]
    registry_contributions: dict[str, tuple[frozenset[str], tuple[tuple[str, str], ...]]]
    collisions: frozenset[str]


def _scope_signature(scopes: list[dict]) -> tuple[tuple[str, str | None, str | None], ...]:
    return tuple((row["name"], row.get("scope_unit_id"), row.get("parent_name")) for row in scopes)


def _duplicate_membership(atoms: list[dict]) -> tuple[frozenset[str], frozenset[str]]:
    paths_by_ref: dict[str, set[str]] = {}
    for row in atoms:
        ref, path = row.get("ref"), row.get("source_path")
        if isinstance(ref, str) and isinstance(path, str):
            paths_by_ref.setdefault(ref, set()).add(path)
    duplicate_refs = frozenset(ref for ref, paths in paths_by_ref.items() if len(paths) > 1)
    return (
        frozenset(path for ref, paths in paths_by_ref.items() if ref in duplicate_refs for path in paths),
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
    outgoing[fact[:2]] = frozenset(edges)
    if fact[2] in inverse:
        reverse = (fact[3], fact[4], inverse[fact[2]], fact[0], fact[1])
        edges = set(outgoing.get(reverse[:2], ()))
        (edges.add if add else edges.discard)((*reverse, True))
        outgoing[reverse[:2]] = frozenset(edges)
        affected.add(reverse[:2])
    return affected


def _full_state(atoms: list[dict], scopes: list[dict]) -> RelationState:
    excluded_paths, duplicate_refs = _duplicate_membership(atoms)
    atoms = _unique_references(atoms)
    contributions = {row["source_path"]: registry_contribution(row) for row in atoms if isinstance(row.get("source_path"), str)}
    registered, inverse, collisions = registry_from_contributions(contributions)
    _warn_colliding_uses(atoms, collisions)
    aliases = _scope_references(scopes)
    raw_by_path = {row["source_path"]: row for row in atoms if isinstance(row.get("source_path"), str)}
    direct = {path: tuple(_atom_facts(row, aliases, registered)) for path, row in raw_by_path.items()}
    outgoing: dict[tuple[str, str], set[tuple]] = {}
    for fact in _scope_facts(scopes, registered):
        _add(outgoing, fact, inverse)
    for facts in direct.values():
        for fact in facts:
            _add(outgoing, fact, inverse)
    atom_rows = {}
    for path, row in raw_by_path.items():
        materialized = _materialized_row(ATOM, row, tuple(sorted(outgoing.get((ATOM, row["ref"]), ()))))
        if materialized is not None:
            atom_rows[path] = materialized
    scope_rows = {}
    for row in scopes:
        materialized = _materialized_row(SCOPE, row, tuple(sorted(outgoing.get((SCOPE, row["name"]), ()))))
        if materialized is not None:
            scope_rows[row["name"]] = materialized
    return RelationState(
        raw_by_path, {row["ref"]: path for path, row in raw_by_path.items() if row["ref"] is not None}, direct,
        {key: frozenset(value) for key, value in outgoing.items()}, atom_rows, tuple(raw_by_path),
        scope_rows, tuple(scope_rows), _scope_signature(scopes), frozenset(registered), dict(inverse),
        excluded_paths, duplicate_refs, contributions, frozenset(collisions),
    )


def _requires_full(state: RelationState, scopes: list[dict], changes: Mapping[str, dict | None]) -> bool:
    if state.scope_signature != _scope_signature(scopes):
        return True
    changed_refs: dict[str, set[str]] = {}
    released_refs: set[str] = set()
    for path, new in changes.items():
        old = state.raw_by_path.get(path)
        old_ref = old.get("ref") if old else None
        new_ref = new.get("ref") if new else None
        if isinstance(new_ref, str):
            changed_refs.setdefault(new_ref, set()).add(path)
        if isinstance(old_ref, str) and old_ref != new_ref:
            released_refs.add(old_ref)
    if any(len(paths) > 1 for paths in changed_refs.values()):
        return True
    for path, new in changes.items():
        old = state.raw_by_path.get(path)
        new_ref = new.get("ref") if new is not None else None
        if path in state.excluded_paths or (isinstance(new_ref, str) and new_ref in state.duplicate_refs):
            return True
        old_ref = old.get("ref") if old else None
        owner = state.refs.get(new_ref) if isinstance(new_ref, str) else None
        if old_ref != new_ref and owner is not None and owner != path and new_ref not in released_refs:
            return True
        if old_ref is not None and old_ref != new_ref and state.refs.get(old_ref) != path:
            return True
    return False


def _next_registry(
    state: RelationState, changes: Mapping[str, dict | None],
) -> tuple[dict[str, tuple[frozenset[str], tuple[tuple[str, str], ...]]], set[str], dict[str, str], set[str]]:
    contributions = dict(state.registry_contributions)
    for path, row in changes.items():
        if row is None:
            contributions.pop(path, None)
        else:
            contributions[path] = registry_contribution(row)
    registered, inverse, collisions = registry_from_contributions(contributions)
    return contributions, registered, inverse, collisions


def _rows(state: RelationState) -> tuple[list[dict], list[dict]]:
    return ([state.atom_rows[path] for path in state.atom_order if path in state.atom_rows],
            [state.scope_rows[name] for name in state.scope_order if name in state.scope_rows])


def materialize_delta(  # noqa: C901
    atoms: list[dict], scopes: list[dict], previous_state: RelationState | None = None,
    changes: Mapping[str, dict | None] | None = None,
) -> tuple[list[dict], list[dict], set[str], dict[str, str], RelationState, MaterializationDelta | None]:
    """Return a full build or a changed-source relation delta without source mutation."""
    if previous_state is None or changes is None or _requires_full(previous_state, scopes, changes):
        state = _full_state(atoms, scopes)
        rows, scope_rows = _rows(state)
        return rows, scope_rows, set(state.registered), dict(state.inverse), state, None

    contributions, registered, inverse, collisions = _next_registry(previous_state, changes)
    if (frozenset(registered), inverse, frozenset(collisions)) != (
        previous_state.registered, previous_state.inverse, previous_state.collisions,
    ):
        state = _full_state(atoms, scopes)
        rows, scope_rows = _rows(state)
        return rows, scope_rows, set(state.registered), dict(state.inverse), state, None

    aliases = _scope_references(scopes)
    raw = dict(previous_state.raw_by_path)
    direct = dict(previous_state.direct_facts)
    outgoing = dict(previous_state.outgoing)
    refs = dict(previous_state.refs)
    affected: set[tuple[str, str]] = set()
    changed_paths = set(changes)
    for path, new in changes.items():
        old = raw.get(path)
        if old is not None and old.get("ref") is not None and refs.get(old["ref"]) == path:
            refs.pop(old["ref"])
        for fact in direct.pop(path, ()):
            affected.update(_delta_edge(outgoing, fact, previous_state.inverse, add=False))
        raw.pop(path, None)
        if new is not None:
            raw[path] = new
            facts = tuple(_atom_facts(new, aliases, set(previous_state.registered)))
            direct[path] = facts
            for fact in facts:
                affected.update(_delta_edge(outgoing, fact, previous_state.inverse, add=True))
            if new.get("ref") is not None:
                affected.add((ATOM, new["ref"]))
                refs[new["ref"]] = path
            _warn_colliding_uses([new], collisions)

    atom_rows = dict(previous_state.atom_rows)
    old_atoms = {path: previous_state.atom_rows[path] for path in changed_paths if path in previous_state.atom_rows}
    new_atoms: dict[str, dict] = {}
    atom_paths = {refs[ref] for kind, ref in affected if kind == ATOM and ref in refs} | {path for path in changed_paths if path in raw}
    for path in atom_paths:
        if path in atom_rows:
            old_atoms.setdefault(path, atom_rows[path])
        ref = raw[path].get("ref")
        row = _materialized_row(ATOM, raw[path], tuple(sorted(outgoing.get((ATOM, ref), ()))) if ref is not None else ())
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
        row = _materialized_row(SCOPE, scope_sources[name], tuple(sorted(outgoing.get((SCOPE, name), ()))))
        if row is not None:
            scope_rows[name] = row
            new_scopes[name] = row

    order = tuple(path for path in previous_state.atom_order if path in raw) + tuple(path for path in changes if path in raw and path not in previous_state.raw_by_path)
    state = RelationState(raw, refs, direct, outgoing, atom_rows, order, scope_rows, previous_state.scope_order, previous_state.scope_signature, previous_state.registered, previous_state.inverse, previous_state.excluded_paths, previous_state.duplicate_refs, contributions, previous_state.collisions)
    rows, scope_output = _rows(state)
    return rows, scope_output, set(state.registered), dict(state.inverse), state, MaterializationDelta(old_atoms, new_atoms, old_scopes, new_scopes)
