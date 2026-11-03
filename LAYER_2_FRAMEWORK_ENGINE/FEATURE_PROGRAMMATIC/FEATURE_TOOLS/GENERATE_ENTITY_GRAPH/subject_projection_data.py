"""Source-bound subject projections without CFEL evaluation or inheritance resolution."""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Mapping
from dataclasses import replace
from typing import Any

import subject_notation as notation
from carrier_aliases import carrier_read_view
from contract_graph import compose_contract_graph
from current_subject_graph import compose_narrowing_graph


Record = dict[str, Any]


def _view(carrier: Mapping[str, Any]) -> Mapping[str, Any]:
    value = carrier.get("read_view")
    if isinstance(value, Mapping):
        return value
    metadata = carrier.get("metadata")
    return carrier_read_view(dict(metadata)) if isinstance(metadata, Mapping) else {}


def _detail_declarations(carriers: list[Record]) -> list[Record]:
    """Admit only the exact Current declaration role/form for property detail."""

    return [
        carrier for carrier in carriers
        if _view(carrier).get("content_role") == "Requirement" and _view(carrier).get("type") == "Declaration"
    ]


def _source_ref(source: Mapping[str, Any]) -> str:
    return f"{source['atom_id']}@{source['version']}"


def _source_rows(entries: list[Record]) -> tuple[list[Record], list[str]]:
    sources = [dict(entry["source"]) for entry in entries]
    return sources, sorted({_source_ref(source) for source in sources})


def _formal_claims(entries: list[Record]) -> list[Record]:
    return [
        {"source": dict(entry["source"]), "block": block["block"]}
        for entry in entries for block in entry["cfel_blocks"]
    ]


def _property_parts(target: str) -> tuple[str, str] | None:
    try:
        expression = notation.parse_subject_expression(target, subject_profile="approved").expression
    except notation.SubjectNotationError:
        return None
    if not isinstance(expression, notation.Path):
        return None
    for index, step in enumerate(expression.steps):
        if step.operator == ".":
            origin = replace(expression, steps=expression.steps[:index], value_format=None, value_cardinality=None)
            suffix = replace(expression, head=step.operand, steps=expression.steps[index + 1:],
                             value_format=None, value_cardinality=None)
            return notation.render_subject(origin), notation.render_subject(suffix)
    return None


def _property_record(row: Record) -> Record | None:
    parts = _property_parts(row["target"])
    if parts is None:
        return None
    sources, refs = _source_rows(row["own"])
    return {
        "identity": row["target"], "relative_name": parts[1], "origin_entity": parts[0],
        "inherited": False, "source_refs": sources, "declaration_refs": refs,
        **({"multiple_applicable": True} if len(refs) > 1 else {}),
        "contracts": [
            clause for entry in row["own"] for clause in entry["clauses"]
            if clause.get("kind") in {"property_constraint", "allowed_literal"}
        ],
        "formal_claims": _formal_claims(row["own"]),
    }


def _ancestors(tree: Mapping[str, Any]) -> dict[str, list[str]]:
    nodes = {row["id"]: row["identity"] for row in tree["nodes"]}
    parents: dict[str, list[str]] = defaultdict(list)
    for edge in tree["edges"]:
        parents[nodes[edge["relation_source"]]].append(nodes[edge["relation_target"]])

    def collect(identity: str, seen: frozenset[str] = frozenset()) -> list[str]:
        result: list[str] = []
        for parent in parents.get(identity, []):
            if parent not in seen:
                result.append(parent)
                result.extend(collect(parent, seen | {parent}))
        return list(dict.fromkeys(result))

    return {identity: collect(identity) for identity in nodes.values()}


def _namespace_contexts(carriers: list[Record]) -> list[Record]:
    """Keep one explicit CAPRMEDIO root context per namespace branch."""

    candidates: dict[str, list[tuple[int, Record]]] = defaultdict(list)
    for carrier in carriers:
        source = carrier.get("source")
        subjects = carrier.get("subjects")
        if not isinstance(source, Mapping) or not isinstance(subjects, Mapping):
            continue
        try:
            normalized = carrier_read_view({"subjects": dict(subjects)})["subjects"]
        except ValueError:
            continue
        for role in ("governs", "depends_on"):
            values = normalized.get(role, [])
            for subject in values if isinstance(values, list) else [values]:
                if not isinstance(subject, str):
                    continue
                try:
                    expression = notation.parse_subject_expression(subject, subject_profile="approved").expression
                except notation.SubjectNotationError:
                    continue
                if (isinstance(expression, notation.Path) and isinstance(expression.head, notation.Name)
                        and expression.head.value in {"CAPRMEDIO_MODEL", "CAPRMEDIO_STRUCTURE"}
                        and not expression.steps):
                    candidates[expression.head.value].append((0 if role == "governs" else 1, dict(source)))
                    continue
                local = notation.namespace_local_expression(expression)
                if local is None or not isinstance(expression, notation.RelationChain):
                    continue
                first = expression.endpoints[0]
                if isinstance(first.head, notation.Name) and first.head.value in {"CAPRMEDIO_MODEL", "CAPRMEDIO_STRUCTURE"}:
                    candidates[first.head.value].append((2, dict(source)))
                    continue
                namespace = expression.endpoints[1]
                if not isinstance(namespace.head, notation.Name):
                    continue
                root = f"CAPRMEDIO <+ {namespace.head.value}"
                direct = len(expression.endpoints) == 2
                priority = 0 if direct and role == "governs" else 1 if direct else 2
                candidates[root].append((priority, dict(source)))
    return [
        {"subject": root, "source": source}
        for root, rows in sorted(candidates.items())
        for _, source in [min(rows, key=lambda row: (row[0], _source_ref(row[1]), str(row[1].get("path", ""))))]
    ]


def build_subject_projection_data(carriers: list[Record]) -> Record:
    """Build additive source-bound views from the supplied Current frontier.

    Tree admission uses all supplied carriers. Property contracts and formal
    claims use only exact Requirement / Declaration carriers before CFEL
    extraction, so no other RMED body becomes declaration authority.
    """

    tree, tree_provenance = compose_narrowing_graph(carriers)
    detail_carriers = _detail_declarations(carriers)
    contracts = compose_contract_graph(detail_carriers)
    ancestors = _ancestors(tree)
    tree_identities = {node["identity"] for node in tree["nodes"]}
    property_rows = [row for row in contracts["entities"] if row["kind"] == "property"]
    properties = [property for row in property_rows if (property := _property_record(row)) is not None]
    properties_by_origin: dict[str, list[Record]] = defaultdict(list)
    for property in properties:
        properties_by_origin[property["origin_entity"]].append(property)

    primary_rows = {
        row["target"]: row for row in [
            *[row for row in contracts["entities"] if row["kind"] == "primary_node"],
            *[row for row in contracts["components"] if row["target"] in tree_identities],
        ]
    }
    entities = []
    for node in sorted(tree["nodes"], key=lambda row: row["identity"]):
        identity = node["identity"]
        own = primary_rows.get(identity, {}).get("own", [])
        sources, refs = _source_rows(own)
        direct = [dict(property) for property in properties_by_origin.get(identity, [])]
        inherited = [
            {**property, "inherited": True}
            for ancestor in ancestors.get(identity, [])
            for property in properties_by_origin.get(ancestor, [])
        ]
        slots: dict[str, int] = defaultdict(int)
        for property in [*direct, *inherited]:
            slots[property["relative_name"]] += 1
        for property in [*direct, *inherited]:
            if slots[property["relative_name"]] > 1:
                property["multiple_applicable"] = True
        entities.append({
            "identity": identity, "source_refs": sources, "declaration_refs": refs,
            "ancestors": ancestors.get(identity, []), "direct_properties": direct,
            "inherited_properties": inherited, "formal_claims": _formal_claims(own),
        })

    return {
        "tree": tree, "tree_provenance": tree_provenance, "namespaces": _namespace_contexts(carriers), "entities": entities,
        "declarations": {
            "primary_nodes": {target: row["own"] for target, row in primary_rows.items()},
            "properties": {row["target"]: row["own"] for row in property_rows},
            "instances": {
                row["target"]: row["own"] for row in contracts["entities"] if row["kind"] == "instance"
            },
            "relations": {row["target"]: row["own"] for row in contracts["relations"]},
            "components": {row["target"]: row["own"] for row in contracts["components"]},
        },
        "diagnostics": [
            *contracts["diagnostics"],
            *[
                {"code": "duplicate_exact_declaration", **conflict}
                for conflict in contracts["conflicts"]
            ],
        ],
        "coverage": {
            **contracts["coverage"], "tree_entities": len(entities),
            "detail_declaration_sources": len(detail_carriers),
            "entities_without_exact_declaration": sum(not entity["declaration_refs"] for entity in entities),
        },
    }
