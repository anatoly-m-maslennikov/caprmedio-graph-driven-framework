# CA-R-2726@5
# CA-M-465@17
# CA-M-500@1
# CA-D-672@12

"""Apply the materialized source delta to the public Workbench projection."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .graph_store import GraphState, graph_state, update_graph
from .content_schema import ContentSchema
from .header_columns import HeaderSchema
from .public_rows import SCOPE_FIELDS, atom_fields, projected_rows
from .relations import canonical


@dataclass(frozen=True)
class ProjectionSnapshot:
    atoms: dict[tuple[str, str], dict[str, Any]]
    scopes: dict[str, dict[str, Any]]
    graph: GraphState
    header_schema: HeaderSchema
    content_schema: ContentSchema


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
    header_schema: HeaderSchema, content_schema: ContentSchema,
) -> ProjectionSnapshot:
    public_atoms, public_scopes = projected_rows(atom_rows, scope_rows, header_schema, content_schema)
    return ProjectionSnapshot(
        {(row["relative path"], row["filename"]): row for row in public_atoms},
        {row["name"]: row for row in public_scopes},
        graph_state(atom_rows, scope_rows, relation_types), header_schema, content_schema,
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


def apply(
    connection: Any, previous: ProjectionSnapshot, atom_rows: list[dict[str, Any]],
    scope_rows: list[dict[str, Any]], relation_types: set[str], header_schema: HeaderSchema,
    content_schema: ContentSchema,
) -> tuple[ProjectionSnapshot, ProjectionChange]:
    """Delete changed public rows before inserting their replacements in one transaction."""
    current = snapshot(atom_rows, scope_rows, relation_types, header_schema, content_schema)
    changed_atoms = {
        key for key in set(previous.atoms) | set(current.atoms)
        if previous.atoms.get(key, {}).get("hash") != current.atoms.get(key, {}).get("hash")
    }
    changed_scopes = {
        key for key in set(previous.scopes) | set(current.scopes)
        if previous.scopes.get(key, {}).get("hash") != current.scopes.get(key, {}).get("hash")
    }
    if not changed_atoms and not changed_scopes and previous.graph == current.graph:
        return current, ProjectionChange(0, 0, 0, 0, 0, None)
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
    inserted_atoms = [current.atoms[key] for key in changed_atoms if key in current.atoms]
    inserted_scopes = [current.scopes[key] for key in changed_scopes if key in current.scopes]
    _insert_rows(
        connection, "atoms", atom_fields(header_schema, content_schema), inserted_atoms,
        json_fields=header_schema.json_names | {"header_relations"},
    )
    _insert_rows(connection, "scope_units", SCOPE_FIELDS, inserted_scopes, json_fields=frozenset({"relations"}))
    graph_rows = len(previous.graph.references ^ current.graph.references) + sum(
        len(previous.graph.edges[name] ^ current.graph.edges[name]) for name in current.graph.edges
    )
    current = ProjectionSnapshot(
        current.atoms, current.scopes,
        update_graph(connection, previous.graph, current.graph, atom_rows, scope_rows),
        header_schema, content_schema,
    )
    references = {
        row["reference"]
        for key in changed_atoms
        for row in (previous.atoms.get(key), current.atoms.get(key))
        if row is not None and isinstance(row.get("reference"), str)
    }
    return current, ProjectionChange(
        deleted_atoms, deleted_scopes, len(inserted_atoms), len(inserted_scopes), graph_rows,
        next(iter(references)) if len(references) == 1 else None,
    )
