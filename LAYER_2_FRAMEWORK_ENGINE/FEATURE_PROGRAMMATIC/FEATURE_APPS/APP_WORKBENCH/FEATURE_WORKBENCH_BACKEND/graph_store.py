# CA-R-2724@2
# CA-M-464@7
# CA-D-672@8
# CA-D-675@8

"""Trusted internal DuckPGQ mappings for the Workbench public row projection."""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Iterable, Mapping
import hashlib

from .relations import canonical


_EDGE_KEYS = (
    "source_kind", "source_ref", "target_kind", "target_ref", "relation_type", "derived",
)
_EDGE_FIELDS = frozenset(_EDGE_KEYS)


def quote_identifier(name: str) -> str:
    if not isinstance(name, str) or not name or "\x00" in name:
        raise ValueError("invalid generated identifier")
    return '"' + name.replace('"', '""') + '"'


def _hash(payload: Mapping[str, object]) -> str:
    return hashlib.sha256(canonical(payload).encode("utf-8")).hexdigest()


def edge_records(rows: Iterable[Mapping[str, object]]) -> list[tuple[str, str, str, str, str, bool]]:
    records = []
    for row in rows:
        edges = row.get("relation_edges_json", [])
        if not isinstance(edges, list):
            raise ValueError("relation_edges_json must be a list")
        for edge in edges:
            if not isinstance(edge, Mapping) or set(edge) != _EDGE_FIELDS:
                raise ValueError("relation edge must contain exactly the declared fields")
            relation_type = edge["relation_type"]
            endpoint_values = (edge["source_kind"], edge["source_ref"], edge["target_kind"], edge["target_ref"])
            if not isinstance(relation_type, str) or not relation_type or not all(isinstance(value, str) for value in endpoint_values):
                raise ValueError("relation edge endpoints and type must be non-empty strings")
            if not all(endpoint_values) or type(edge["derived"]) is not bool:
                raise ValueError("relation edge endpoints must be non-empty and derived must be boolean")
            records.append((*endpoint_values, relation_type, edge["derived"]))
    return records


def build_graph(connection, atom_rows: Iterable[Mapping[str, object]], scope_rows: Iterable[Mapping[str, object]]) -> None:
    """Create the disposable typed-reference graph over materialized row facts."""
    atoms, scopes = list(atom_rows), list(scope_rows)
    edges = edge_records([*atoms, *scopes])
    references = {(kind, ref) for kind, ref, _, _, _, _ in edges}
    references.update((kind, ref) for _, _, kind, ref, _, _ in edges)
    references.update(("Atom", row["ref"]) for row in atoms if row["ref"] is not None)
    references.update(("Scope Unit", row["name"]) for row in scopes)

    connection.execute("CREATE SCHEMA internal")
    connection.execute(
        "CREATE TABLE internal.reference(kind VARCHAR, ref VARCHAR, hash VARCHAR NOT NULL, "
        "PRIMARY KEY(kind, ref))"
    )
    if references:
        connection.executemany(
            "INSERT INTO internal.reference VALUES (?, ?, ?)",
            [(kind, ref, _hash({"kind": kind, "ref": ref})) for kind, ref in sorted(references)],
        )

    by_type: dict[str, list[tuple[str, str, str, str, str, bool]]] = defaultdict(list)
    for source_kind, source_ref, target_kind, target_ref, relation_type, derived in edges:
        by_type[relation_type].append(
            (source_kind, source_ref, target_kind, target_ref, relation_type, derived)
        )
    edge_definitions = []
    for index, relation_type in enumerate(sorted(by_type), start=1):
        table = quote_identifier(f"edge_{index}")
        label = quote_identifier(relation_type)
        connection.execute(
            f"CREATE TABLE internal.{table}(source_kind VARCHAR, source_ref VARCHAR, "
            "target_kind VARCHAR, target_ref VARCHAR, relation_type VARCHAR NOT NULL, "
            "derived BOOLEAN NOT NULL, hash VARCHAR NOT NULL)"
        )
        connection.executemany(
            f"INSERT INTO internal.{table} VALUES (?, ?, ?, ?, ?, ?, ?)",
            [(*edge, _hash(dict(zip(_EDGE_KEYS, edge)))) for edge in by_type[relation_type]],
        )
        edge_definitions.append(
            f"internal.{table} SOURCE KEY(source_kind, source_ref) "
            "REFERENCES internal.reference(kind, ref) "
            "DESTINATION KEY(target_kind, target_ref) REFERENCES internal.reference(kind, ref) "
            f"LABEL {label}"
        )
    graph_sql = "CREATE PROPERTY GRAPH caprmedio VERTEX TABLES (internal.reference LABEL Reference)"
    if edge_definitions:
        graph_sql += " EDGE TABLES (" + ", ".join(edge_definitions) + ")"
    connection.execute(graph_sql)
