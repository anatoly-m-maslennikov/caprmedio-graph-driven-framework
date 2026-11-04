# CA-R-2726@4
# CA-D-672@9

"""Project transient parser records into the two public SQL tables."""

from __future__ import annotations

import hashlib
from pathlib import PurePosixPath

from .content_columns import CONTENT_COLUMNS, content_columns
from .graph_store import build_graph, graph_relations, quote_identifier
from .relations import canonical


ATOM_FIELDS = (
    "relative path", "filename", "status_group", "id", "reference", "version",
    "status", "current_scope_unit", "claim_target_scope_unit", "role", "form",
    "tier", "updated_at", *CONTENT_COLUMNS, "relations", "hash",
)
SCOPE_FIELDS = (
    "name", "scope_unit_id", "parent_name", "declared_label", "ordered",
    "order_number", "declaration_source_path", "declaration_version", "relations", "hash",
)


def _atom(row, outgoing):
    path = PurePosixPath(row["source_path"])
    public = {field: row[field] for field in ATOM_FIELDS
              if field in row and field not in {"hash"}}
    public.update({
        "relative path": path.parent.as_posix(), "filename": path.name,
        "reference": row["ref"], **content_columns(row),
        "relations": outgoing.get(("Atom", row["ref"]), {}),
    })
    return public


def _scope(row, outgoing):
    public = {field: row[field] for field in SCOPE_FIELDS if field not in {"relations", "hash"}}
    public["relations"] = outgoing.get(("Scope Unit", row["name"]), {})
    return public


def _insert(connection, name, fields, rows):
    if not rows:
        return
    values = []
    for row in rows:
        row["hash"] = hashlib.sha256(canonical(row).encode("utf-8")).hexdigest()
        values.append(tuple(canonical(row[field]) if field == "relations" else row[field]
                            for field in fields))
    connection.executemany(
        f"INSERT INTO main.{name} VALUES ({','.join('?' for _ in fields)})", values,
    )


def insert_rows(connection, atoms, scopes):
    # The JSON columns are a view of the actual native graph, including its inverses.
    build_graph(connection, atoms, scopes)
    outgoing = graph_relations(connection, has_edges=any(
        row.get("relation_edges_json") for row in [*atoms, *scopes]
    ))
    content_ddl = ", ".join(f"{quote_identifier(name)} VARCHAR" for name in CONTENT_COLUMNS)
    connection.execute(f"""CREATE TABLE main.atoms(
        "relative path" VARCHAR NOT NULL, filename VARCHAR NOT NULL,
        status_group VARCHAR NOT NULL, id VARCHAR, reference VARCHAR UNIQUE,
        version BIGINT, status VARCHAR, current_scope_unit VARCHAR,
        claim_target_scope_unit VARCHAR, role VARCHAR, form VARCHAR, tier BIGINT,
        updated_at TIMESTAMPTZ, {content_ddl}, relations JSON NOT NULL,
        hash VARCHAR NOT NULL, PRIMARY KEY("relative path", filename)
    )""")
    connection.execute("""CREATE TABLE main.scope_units(
        name VARCHAR PRIMARY KEY, scope_unit_id VARCHAR UNIQUE, parent_name VARCHAR,
        declared_label VARCHAR, ordered BOOLEAN NOT NULL, order_number BIGINT,
        declaration_source_path VARCHAR NOT NULL UNIQUE, declaration_version BIGINT NOT NULL,
        relations JSON NOT NULL, hash VARCHAR NOT NULL
    )""")
    _insert(connection, "atoms", ATOM_FIELDS, [_atom(row, outgoing) for row in atoms])
    _insert(connection, "scope_units", SCOPE_FIELDS, [_scope(row, outgoing) for row in scopes])
