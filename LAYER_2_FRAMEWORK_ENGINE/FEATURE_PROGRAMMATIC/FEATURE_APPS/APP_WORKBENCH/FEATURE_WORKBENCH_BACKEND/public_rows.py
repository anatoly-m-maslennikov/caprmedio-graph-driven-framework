# CA-R-2726@4
# CA-D-672@9

"""Project transient parser records into the two public SQL tables."""

from __future__ import annotations

import hashlib
from pathlib import PurePosixPath
from typing import Any

from .content_columns import CONTENT_COLUMNS, content_columns
from .graph_store import build_graph, quote_identifier
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
Row = dict[str, Any]
Outgoing = dict[tuple[str, str], dict[str, list[dict[str, object]]]]


def _atom(row: Row, outgoing: Outgoing) -> Row:
    path = PurePosixPath(row["source_path"])
    public: Row = {
        field: row[field] for field in ATOM_FIELDS if field in row and field != "hash"
    }
    reference = row.get("ref")
    public.update({
        "relative path": path.parent.as_posix(), "filename": path.name,
        "reference": reference, **content_columns(row),
        "relations": outgoing.get(("Atom", reference), {}) if isinstance(reference, str) else {},
    })
    return public


def _scope(row: Row, outgoing: Outgoing) -> Row:
    public: Row = {field: row[field] for field in SCOPE_FIELDS if field not in {"relations", "hash"}}
    name = row.get("name")
    public["relations"] = outgoing.get(("Scope Unit", name), {}) if isinstance(name, str) else {}
    return public


def projected_rows(atoms: list[Row], scopes: list[Row]) -> tuple[list[Row], list[Row]]:
    """Return public rows from the already-materialized source graph."""
    outgoing: Outgoing = {}
    for row in [*atoms, *scopes]:
        for edge in row["relation_edges_json"]:
            source = (str(edge["source_kind"]), str(edge["source_ref"]))
            relation_type = str(edge["relation_type"])
            outgoing.setdefault(source, {}).setdefault(relation_type, []).append({
                "kind": edge["target_kind"],
                "reference": edge["target_ref"],
                "derived": edge["derived"],
            })
    for relations in outgoing.values():
        for targets in relations.values():
            targets.sort(key=lambda target: (target["kind"], target["reference"], target["derived"]))
    atom_rows = [_atom(row, outgoing) for row in atoms]
    scope_rows = [_scope(row, outgoing) for row in scopes]
    for row in [*atom_rows, *scope_rows]:
        row["hash"] = hashlib.sha256(canonical(row).encode("utf-8")).hexdigest()
    return atom_rows, scope_rows


def _insert(connection: Any, name: str, fields: tuple[str, ...], rows: list[Row]) -> None:
    if not rows:
        return
    values = []
    for row in rows:
        values.append(tuple(canonical(row[field]) if field == "relations" else row[field]
                            for field in fields))
    connection.executemany(
        f"INSERT INTO main.{name} VALUES ({','.join('?' for _ in fields)})", values,
    )


def insert_rows(
    connection: Any, atoms: list[Row], scopes: list[Row], *, relation_types: set[str] | None = None,
) -> None:
    # The JSON columns are a view of the actual native graph, including its inverses.
    build_graph(connection, atoms, scopes, relation_types)
    atom_rows, scope_rows = projected_rows(atoms, scopes)
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
    _insert(connection, "atoms", ATOM_FIELDS, atom_rows)
    _insert(connection, "scope_units", SCOPE_FIELDS, scope_rows)
