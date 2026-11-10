# CA-R-2726@6
# CA-M-500@3
# CA-D-672@19

"""Project transient parser records into the two public SQL tables."""

from __future__ import annotations

import hashlib
from pathlib import PurePosixPath
from typing import Any

from .content_columns import content_columns
from .content_schema import ContentSchema
from .graph_store import build_graph, quote_identifier
from .header_columns import HeaderSchema
from .relations import canonical


ATOM_METADATA_FIELDS = ("relative_path", "filename", "status_group", "reference")
ATOM_TRAILER_FIELDS = ("header.relations", "hash")
SCOPE_FIELDS = (
    "name", "scope_unit_id", "parent_name", "declared_label", "ordered",
    "order_number", "declaration_source_path", "declaration_version", "relations", "hash",
)
Row = dict[str, Any]
Outgoing = dict[tuple[str, str], dict[str, list[dict[str, object]]]]


def atom_fields(header_schema: HeaderSchema, content_schema: ContentSchema) -> tuple[str, ...]:
    return (*ATOM_METADATA_FIELDS, *header_schema.names, *content_schema.names, *ATOM_TRAILER_FIELDS)


def _atom(row: Row, outgoing: Outgoing, header_schema: HeaderSchema, content_schema: ContentSchema) -> Row:
    path = PurePosixPath(row["source_path"])
    reference = row.get("ref")
    public: Row = {
        "relative_path": path.parent.as_posix(),
        "filename": path.name,
        "status_group": row["status_group"],
        "reference": reference,
        **{column.name: header_schema.value(row, column) for column in header_schema.columns},
        **content_columns(row, content_schema),
        "header.relations": outgoing.get(("Atom", reference), {}) if isinstance(reference, str) else {},
    }
    public["hash"] = hashlib.sha256(canonical(public).encode("utf-8")).hexdigest()
    return public


def _scope(row: Row, outgoing: Outgoing) -> Row:
    public: Row = {field: row[field] for field in SCOPE_FIELDS if field not in {"relations", "hash"}}
    name = row.get("name")
    public["relations"] = outgoing.get(("Scope Unit", name), {}) if isinstance(name, str) else {}
    public["hash"] = hashlib.sha256(canonical(public).encode("utf-8")).hexdigest()
    return public


def atom_key(row: Row) -> tuple[str, str]:
    path = PurePosixPath(row["source_path"])
    return path.parent.as_posix(), path.name


def projected_rows(
    atoms: list[Row], scopes: list[Row], header_schema: HeaderSchema, content_schema: ContentSchema,
    *, previous_atoms: dict[tuple[str, str], tuple[Row, Row]] | None = None,
) -> tuple[list[Row], list[Row]]:
    """Return public rows from the already-materialized source graph."""
    outgoing: Outgoing = {}
    for row in [*atoms, *scopes]:
        for edge in row["relation_edges_json"]:
            source = (str(edge["source_kind"]), str(edge["source_ref"]))
            relation_type = str(edge["relation_type"])
            outgoing.setdefault(source, {}).setdefault(relation_type, []).append({
                "kind": edge["target_kind"], "reference": edge["target_ref"], "derived": edge["derived"],
            })
    for relations in outgoing.values():
        for targets in relations.values():
            targets.sort(key=lambda target: (target["kind"], target["reference"], target["derived"]))
    public_atoms = []
    for row in atoms:
        cached = (previous_atoms or {}).get(atom_key(row))
        public_atoms.append(cached[1] if cached is not None and cached[0] is row
                            else _atom(row, outgoing, header_schema, content_schema))
    return public_atoms, [_scope(row, outgoing) for row in scopes]


def _insert(
    connection: Any, name: str, fields: tuple[str, ...], rows: list[Row], *, json_fields: frozenset[str],
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


def insert_rows(
    connection: Any, atoms: list[Row], scopes: list[Row], *, header_schema: HeaderSchema,
    content_schema: ContentSchema,
    relation_types: set[str] | None = None,
) -> tuple[list[Row], list[Row]]:
    """Create public tables and return the inserted rows."""
    build_graph(connection, atoms, scopes, relation_types)
    fields = atom_fields(header_schema, content_schema)
    atom_rows, scope_rows = projected_rows(atoms, scopes, header_schema, content_schema)
    header_ddl = [f"{quote_identifier(column.name)} {column.format}" for column in header_schema.columns]
    content_ddl = [f"{quote_identifier(name)} VARCHAR" for name in content_schema.names]
    columns = [
        '"relative_path" VARCHAR NOT NULL', "filename VARCHAR NOT NULL", "status_group VARCHAR NOT NULL",
        "reference VARCHAR UNIQUE", *header_ddl, *content_ddl, '"header.relations" JSON NOT NULL',
        "hash VARCHAR NOT NULL", 'PRIMARY KEY("relative_path", filename)',
    ]
    connection.execute(f"CREATE TABLE main.atoms({', '.join(columns)})")
    connection.execute("""CREATE TABLE main.scope_units(
        name VARCHAR PRIMARY KEY, scope_unit_id VARCHAR UNIQUE, parent_name VARCHAR,
        declared_label VARCHAR, ordered BOOLEAN NOT NULL, order_number BIGINT,
        declaration_source_path VARCHAR NOT NULL UNIQUE, declaration_version BIGINT NOT NULL,
        relations JSON NOT NULL, hash VARCHAR NOT NULL
    )""")
    _insert(connection, "atoms", fields, atom_rows, json_fields=header_schema.json_names | {"header.relations"})
    _insert(connection, "scope_units", SCOPE_FIELDS, scope_rows, json_fields=frozenset({"relations"}))
    return atom_rows, scope_rows
