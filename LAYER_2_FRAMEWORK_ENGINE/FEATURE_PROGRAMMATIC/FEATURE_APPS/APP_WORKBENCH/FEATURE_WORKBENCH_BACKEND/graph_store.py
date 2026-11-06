# CA-R-2724@2
# CA-M-464@7
# CA-D-672@9
# CA-D-675@13

"""Trusted internal DuckPGQ mappings for the Workbench public row projection."""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
import hashlib
from typing import Any

from .relations import canonical


_EDGE_KEYS = (
    "source_kind", "source_ref", "target_kind", "target_ref", "relation_type", "derived",
)
_EDGE_FIELDS = frozenset(_EDGE_KEYS)
Edge = tuple[str, str, str, str, str, bool]
Reference = tuple[str, str]


@dataclass(frozen=True)
class GraphState:
    references: frozenset[Reference]
    edges: dict[str, frozenset[Edge]]
    tables: dict[str, str]


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


def graph_relations(connection: Any, *, has_edges: bool) -> dict[tuple[str, str], dict[str, list[dict[str, object]]]]:
    """Read outgoing facts from the native graph without exposing its tables."""
    if not has_edges:
        return {}
    descriptions = connection.execute("SELECT * FROM describe_property_graph('caprmedio')").fetchall()
    relation_types = sorted(
        row[2] for row in descriptions
        if row[3] is False and isinstance(row[2], str)
    )
    outgoing: dict[tuple[str, str], dict[str, list[dict[str, object]]]] = defaultdict(dict)
    for relation_type in relation_types:
        rows = connection.execute(
            "FROM GRAPH_TABLE (caprmedio "
            f"MATCH (source:Reference)-[edge:{quote_identifier(relation_type)}]->(target:Reference) "
            "COLUMNS (source.kind AS source_kind, source.ref AS source_ref, "
            "target.kind AS target_kind, target.ref AS target_ref, edge.derived AS derived)) "
            "ORDER BY source_kind, source_ref, target_kind, target_ref, derived"
        ).fetchall()
        for source_kind, source_ref, target_kind, target_ref, derived in rows:
            outgoing[(source_kind, source_ref)].setdefault(relation_type, []).append({
                "kind": target_kind,
                "reference": target_ref,
                "derived": derived,
            })
    return {source: dict(relations) for source, relations in outgoing.items()}


def graph_state(
    atom_rows: Iterable[Mapping[str, object]], scope_rows: Iterable[Mapping[str, object]],
    relation_types: set[str] | None = None,
) -> GraphState:
    """Describe the graph facts without changing the database."""
    atoms, scopes = list(atom_rows), list(scope_rows)
    edges = edge_records([*atoms, *scopes])
    references: set[Reference] = {(kind, ref) for kind, ref, _, _, _, _ in edges}
    references.update((kind, ref) for _, _, kind, ref, _, _ in edges)
    for row in atoms:
        if isinstance(ref := row.get("ref"), str):
            references.add(("Atom", ref))
    for row in scopes:
        if isinstance(name := row.get("name"), str):
            references.add(("Scope Unit", name))

    by_type: dict[str, set[Edge]] = defaultdict(set)
    for edge in edges:
        by_type[edge[4]].add(edge)
    if relation_types is not None:
        for relation_type in relation_types:
            by_type[relation_type]
    tables = {relation_type: quote_identifier(f"edge_{index}")
              for index, relation_type in enumerate(sorted(by_type), start=1)}
    return GraphState(frozenset(references), {name: frozenset(records) for name, records in by_type.items()}, tables)


def build_graph(
    connection: Any, atom_rows: Iterable[Mapping[str, object]], scope_rows: Iterable[Mapping[str, object]],
    relation_types: set[str] | None = None,
) -> GraphState:
    """Create the disposable typed-reference graph over materialized row facts."""
    state = graph_state(atom_rows, scope_rows, relation_types)
    connection.execute("CREATE SCHEMA internal")
    connection.execute(
        "CREATE TABLE internal.reference(kind VARCHAR, ref VARCHAR, hash VARCHAR NOT NULL, "
        "PRIMARY KEY(kind, ref))"
    )
    if state.references:
        connection.executemany(
            "INSERT INTO internal.reference VALUES (?, ?, ?)",
        [(kind, ref, _hash({"kind": kind, "ref": ref})) for kind, ref in sorted(state.references)],
        )
    edge_definitions = []
    for relation_type, table in state.tables.items():
        label = quote_identifier(relation_type)
        connection.execute(
            f"CREATE TABLE internal.{table}(source_kind VARCHAR, source_ref VARCHAR, "
            "target_kind VARCHAR, target_ref VARCHAR, relation_type VARCHAR NOT NULL, "
            "derived BOOLEAN NOT NULL, hash VARCHAR NOT NULL)"
        )
        if state.edges[relation_type]:
            connection.executemany(
                f"INSERT INTO internal.{table} VALUES (?, ?, ?, ?, ?, ?, ?)",
                [(*edge, _hash(dict(zip(_EDGE_KEYS, edge)))) for edge in state.edges[relation_type]],
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
    return state


def update_graph(
    connection: Any, previous: GraphState, current: GraphState,
    atom_rows: Iterable[Mapping[str, object]], scope_rows: Iterable[Mapping[str, object]],
) -> GraphState:
    """Apply changed graph facts; a changed relation type layout needs a new graph declaration."""
    if set(previous.edges) != set(current.edges):
        connection.execute("DROP PROPERTY GRAPH caprmedio")
        connection.execute("DROP SCHEMA internal CASCADE")
        return build_graph(connection, atom_rows, scope_rows, set(current.edges))
    for relation_type, table in current.tables.items():
        removed = previous.edges[relation_type] - current.edges[relation_type]
        if removed:
            connection.executemany(
                f"DELETE FROM internal.{table} WHERE hash = ?",
                [(_hash(dict(zip(_EDGE_KEYS, edge))),) for edge in removed],
            )
    for kind, ref in previous.references - current.references:
        connection.execute("DELETE FROM internal.reference WHERE kind = ? AND ref = ?", [kind, ref])
    for kind, ref in current.references - previous.references:
        connection.execute(
            "INSERT INTO internal.reference VALUES (?, ?, ?)",
            [kind, ref, _hash({"kind": kind, "ref": ref})],
        )
    for relation_type, table in current.tables.items():
        added = current.edges[relation_type] - previous.edges[relation_type]
        if added:
            connection.executemany(
                f"INSERT INTO internal.{table} VALUES (?, ?, ?, ?, ?, ?, ?)",
                [(*edge, _hash(dict(zip(_EDGE_KEYS, edge)))) for edge in added],
            )
    return current
