# CA-R-2726@5
# CA-M-465@19
# CA-M-500@1
# CA-D-672@12
# CA-E-677@14

"""Apply the materialized source delta to the public Workbench projection."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .graph_store import GraphState, apply_graph_delta, graph_state, update_graph
from .content_schema import ContentSchema
from .header_columns import HeaderSchema
from .index_delta import MaterializationDelta
from .public_rows import SCOPE_FIELDS, atom_fields, atom_key, projected_rows
from .relations import canonical


@dataclass(frozen=True)
class ProjectionSnapshot:
    atoms: dict[tuple[str, str], dict[str, Any]]
    scopes: dict[str, dict[str, Any]]
    graph: GraphState
    header_schema: HeaderSchema
    content_schema: ContentSchema
    atom_sources: dict[tuple[str, str], dict[str, Any]]


@dataclass(frozen=True)
class ProjectionChange:
    deleted_atoms: int
    deleted_scopes: int
    inserted_atoms: int
    inserted_scopes: int
    graph_rows: int
    reference: str | None


def snapshot(
    atom_rows: list[dict[str, Any]], scope_rows: list[dict[str, Any]], relation_types: set[str] | None,
    header_schema: HeaderSchema, content_schema: ContentSchema, previous: ProjectionSnapshot | None = None,
) -> ProjectionSnapshot:
    reuse = None
    if previous is not None and previous.header_schema == header_schema and previous.content_schema == content_schema:
        reuse = {
            key: (source, previous.atoms[key])
            for key, source in previous.atom_sources.items()
            if key in previous.atoms
        }
    public_atoms, public_scopes = projected_rows(
        atom_rows, scope_rows, header_schema, content_schema, previous_atoms=reuse,
    )
    atom_sources = {
        (row["relative path"], row["filename"]): source
        for row, source in zip(public_atoms, atom_rows, strict=True)
    }
    return ProjectionSnapshot(
        {(row["relative path"], row["filename"]): row for row in public_atoms},
        {row["name"]: row for row in public_scopes},
        graph_state(atom_rows, scope_rows, relation_types), header_schema, content_schema, atom_sources,
    )


def _insert_rows(
    connection: Any, name: str, fields: tuple[str, ...], rows: list[dict[str, Any]], *, json_fields: frozenset[str],
) -> None:
    if rows:
        connection.executemany(
            f"INSERT INTO main.{name} VALUES ({','.join('?' for _ in fields)})",
            [
                tuple(canonical(row[field]) if field in json_fields and row[field] is not None else row[field]
                      for field in fields)
                for row in rows
            ],
        )


def _same_header_layout(left: HeaderSchema, right: HeaderSchema) -> bool:
    return tuple((column.name, column.format) for column in left.columns) == tuple(
        (column.name, column.format) for column in right.columns
    )


def _delta_snapshot(
    previous: ProjectionSnapshot, delta: MaterializationDelta,
    header_schema: HeaderSchema, content_schema: ContentSchema,
) -> ProjectionSnapshot:
    """Copy and patch public maps from already-materialized changed source rows."""
    if not _same_header_layout(previous.header_schema, header_schema) or previous.content_schema.shape != content_schema.shape:
        raise ValueError("projection schema changed; full projection rebuild is required")
    atoms = dict(previous.atoms)
    atom_sources = dict(previous.atom_sources)
    for row in delta.old_atoms.values():
        key = atom_key(row)
        atoms.pop(key, None)
        atom_sources.pop(key, None)
    new_atoms, new_scopes = projected_rows(
        list(delta.new_atoms.values()), list(delta.new_scopes.values()), header_schema, content_schema,
    )
    for public, source in zip(new_atoms, delta.new_atoms.values(), strict=True):
        key = (public["relative path"], public["filename"])
        atoms[key] = public
        atom_sources[key] = source
    scopes = dict(previous.scopes)
    for name in delta.old_scopes:
        scopes.pop(name, None)
    scopes.update({row["name"]: row for row in new_scopes})
    return ProjectionSnapshot(atoms, scopes, previous.graph, header_schema, content_schema, atom_sources)


def _changed_keys(
    previous: dict[Any, dict[str, Any]], current: dict[Any, dict[str, Any]],
) -> set[Any]:
    return {
        key for key in set(previous) | set(current)
        if previous.get(key, {}).get("hash") != current.get(key, {}).get("hash")
    }


def _write_public_delta(
    connection: Any, previous: ProjectionSnapshot, current: ProjectionSnapshot,
    changed_atoms: set[tuple[str, str]] | None = None, changed_scopes: set[str] | None = None,
) -> tuple[set[tuple[str, str]], set[str], int, int]:
    changed_atoms = changed_atoms if changed_atoms is not None else _changed_keys(previous.atoms, current.atoms)
    changed_scopes = changed_scopes if changed_scopes is not None else _changed_keys(previous.scopes, current.scopes)
    deleted_atoms = 0
    for path, filename in changed_atoms:
        if (path, filename) in previous.atoms:
            connection.execute('DELETE FROM main.atoms WHERE "relative path" = ? AND filename = ?', [path, filename])
            deleted_atoms += 1
    deleted_scopes = 0
    for name in changed_scopes:
        if name in previous.scopes:
            connection.execute("DELETE FROM main.scope_units WHERE name = ?", [name])
            deleted_scopes += 1
    _insert_rows(
        connection, "atoms", atom_fields(current.header_schema, current.content_schema),
        [current.atoms[key] for key in changed_atoms if key in current.atoms],
        json_fields=current.header_schema.json_names | {"header_relations"},
    )
    _insert_rows(
        connection, "scope_units", SCOPE_FIELDS,
        [current.scopes[key] for key in changed_scopes if key in current.scopes],
        json_fields=frozenset({"relations"}),
    )
    return changed_atoms, changed_scopes, deleted_atoms, deleted_scopes


def _delta_keys(delta: MaterializationDelta) -> tuple[set[tuple[str, str]], set[str]]:
    return (
        {atom_key(row) for row in [*delta.old_atoms.values(), *delta.new_atoms.values()]},
        set(delta.old_scopes) | set(delta.new_scopes),
    )


def _changed_delta_keys(
    previous: ProjectionSnapshot, current: ProjectionSnapshot, delta: MaterializationDelta,
) -> tuple[set[tuple[str, str]], set[str]]:
    atom_keys, scope_names = _delta_keys(delta)
    return (
        {key for key in atom_keys if previous.atoms.get(key, {}).get("hash") != current.atoms.get(key, {}).get("hash")},
        {name for name in scope_names if previous.scopes.get(name, {}).get("hash") != current.scopes.get(name, {}).get("hash")},
    )


def apply(
    connection: Any, previous: ProjectionSnapshot, atom_rows: list[dict[str, Any]],
    scope_rows: list[dict[str, Any]], relation_types: set[str], header_schema: HeaderSchema,
    content_schema: ContentSchema, *, delta: MaterializationDelta | None = None,
) -> tuple[ProjectionSnapshot, ProjectionChange]:
    """Delete changed public rows before inserting their replacements in one transaction."""
    current = (_delta_snapshot(previous, delta, header_schema, content_schema)
               if delta is not None
               else snapshot(atom_rows, scope_rows, relation_types, header_schema, content_schema, previous))
    changed_atoms, changed_scopes = (_changed_delta_keys(previous, current, delta) if delta is not None
                                     else (_changed_keys(previous.atoms, current.atoms),
                                           _changed_keys(previous.scopes, current.scopes)))
    if delta is None and not changed_atoms and not changed_scopes and previous.graph == current.graph:
        return current, ProjectionChange(0, 0, 0, 0, 0, None)
    changed_atoms, changed_scopes, deleted_atoms, deleted_scopes = _write_public_delta(
        connection, previous, current, changed_atoms, changed_scopes,
    )
    inserted_atoms = sum(key in current.atoms for key in changed_atoms)
    inserted_scopes = sum(key in current.scopes for key in changed_scopes)
    if delta is None:
        next_graph = update_graph(connection, previous.graph, current.graph, atom_rows, scope_rows)
        graph_rows = len(previous.graph.references ^ next_graph.references) + sum(
            len(previous.graph.edges[name] ^ next_graph.edges[name]) for name in next_graph.edges
        )
    else:
        next_graph, graph_rows = apply_graph_delta(connection, previous.graph, delta, relation_types)
    current = ProjectionSnapshot(
        current.atoms, current.scopes, next_graph, header_schema, content_schema, current.atom_sources,
    )
    references = {
        row["reference"]
        for key in changed_atoms
        for row in (previous.atoms.get(key), current.atoms.get(key))
        if row is not None and isinstance(row.get("reference"), str)
    }
    return current, ProjectionChange(
        deleted_atoms, deleted_scopes, inserted_atoms, inserted_scopes, graph_rows,
        next(iter(references)) if len(references) == 1 else None,
    )
