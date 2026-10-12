"""Pure native-ownership Entity Graph projection.

This module deliberately has no filesystem or request-schema dependency.  It
turns already-admitted Atom carrier and Subject-relation evidence into a small
projection while retaining Atom-owned metadata on its source record only.
"""

from __future__ import annotations

import json
from collections.abc import Mapping, Sequence
from importlib import import_module
from typing import Any


def _value(row: object, name: str, default: object = None) -> object:
    if isinstance(row, Mapping):
        return row.get(name, default)
    return getattr(row, name, default)


def _canonical(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), default=str)


def _copy(value: object) -> object:
    """Return JSON-shaped data with mapping keys in deterministic order."""

    if isinstance(value, Mapping):
        return {str(key): _copy(value[key]) for key in sorted(value, key=str)}
    if isinstance(value, (list, tuple)):
        return [_copy(item) for item in value]
    return value


def _lineage(relation: object, carriers_by_atom: Mapping[str, object]) -> dict[str, object]:
    atom_id = _value(relation, "atom_id", _value(relation, "source_atom_id"))
    carrier = carriers_by_atom.get(str(atom_id))
    return {
        "sourceAtomID": atom_id,
        "atom_revision": _value(relation, "atom_revision", _value(carrier, "version")),
        "carrier_path": _value(relation, "carrier_path", _value(carrier, "carrier_path")),
        "carrier_sha256": _value(relation, "carrier_sha256", _value(carrier, "sha256")),
    }


def _source_record(carrier: object, source_metadata: Mapping[str, Mapping[str, Any]]) -> dict[str, object]:
    atom_id = str(_value(carrier, "atom_id"))
    evidence = _value(carrier, "evidence")
    source = evidence() if callable(evidence) else {}
    # The input metadata is intentionally not lifted into Entity, relation, or
    # incidence records.  It describes this Atom/Carrier, not the governed
    # Entity (and notably must not promote an author onto a GOVERNS target).
    return {
        "atom_id": atom_id,
        "metadata": _copy(source_metadata.get(atom_id, {})),
        "source": _copy(source if isinstance(source, Mapping) else {}),
    }


def _trusted_context_payload(graph_fact_context: object) -> Mapping[str, object]:
    """Accept only the builder's validated, typed derived-fact context.

    A mapping from a caller is deliberately insufficient: admission decisions
    belong to the graph-fact-context provider, not to this projection helper.
    """

    try:
        module = import_module("graph_fact_context")
        context_type = getattr(module, "DerivedFactContext")
    except (ImportError, AttributeError) as error:
        raise ValueError("graph_fact_context is unavailable for trusted native-fact admission") from error
    if not isinstance(graph_fact_context, context_type):
        raise ValueError("graph_fact_context must be the validated DerivedFactContext instance")
    payload = graph_fact_context.as_dict()
    if not isinstance(payload, Mapping) or payload.get("context_kind") != "caprmedio.derived_fact_context":
        raise ValueError("graph_fact_context has no interoperable derived-fact payload")
    if payload.get("graph_kind") != "entities":
        raise ValueError("graph_fact_context graph_kind must be entities")
    return payload


def _native_facts(context: Mapping[str, object]) -> tuple[list[dict[str, object]], list[dict[str, object]], list[dict[str, object]]]:
    """Project only facts already admitted by the trusted context provider."""

    facts = list(context.get("admitted_facts", [])) + [
        row for row in context.get("derivations", [])
        if isinstance(row, Mapping) and row.get("disposition") == "admitted"
    ]
    entities: list[dict[str, object]] = []
    properties: list[dict[str, object]] = []
    relations: list[dict[str, object]] = []
    for fact in facts:
        if not isinstance(fact, Mapping):
            continue
        fact_class = fact.get("fact_class")
        payload = fact.get("payload")
        if not isinstance(payload, Mapping):
            continue
        record = {"fact_id": fact.get("fact_id", fact.get("derivation_id")), "payload": _copy(payload)}
        if fact_class == "entity_admission" and isinstance(payload.get("entity_identity"), str):
            entities.append({"identity": payload["entity_identity"], "fact_id": record["fact_id"]})
        elif fact_class == "entity_property":
            properties.append(record)
        elif fact_class == "relation":
            relations.append(record)
    return (
        sorted(entities, key=_canonical),
        sorted(properties, key=_canonical),
        sorted(relations, key=_canonical),
    )


def _coverage_disposition(context: Mapping[str, object], fact_class: str) -> str:
    """Read one provider coverage row without deriving coverage from facts."""

    rows = context.get("coverage")
    if not isinstance(rows, list):
        return "unknown"
    matches = [row for row in rows if isinstance(row, Mapping) and row.get("fact_class") == fact_class]
    if len(matches) != 1:
        return "unknown"
    disposition = matches[0].get("disposition")
    return disposition if disposition in {"complete", "incomplete", "unknown"} else "unknown"


def build_entity_projection(
    carriers: Sequence[object],
    subject_relations: Sequence[object],
    source_metadata: Mapping[str, Mapping[str, Any]],
    project_structure: Sequence[object],
    graph_fact_context: object | None = None,
) -> dict[str, object]:
    """Build a deterministic, non-authoritative native Entity projection.

    Subject rows remain source evidence only.  Native Entity, Property, and
    Relation records are emitted solely from an optional, typed context whose
    provider has already verified admission and bindings.  This pure helper
    does not re-establish currentness; the builder must pass only its already
    verified ``DerivedFactContext``.  No metadata or caller flag can promote a
    source candidate into a native fact.
    """

    carriers_by_atom: dict[str, object] = {}
    for carrier in carriers:
        atom_id = _value(carrier, "atom_id")
        if not isinstance(atom_id, str) or not atom_id:
            raise ValueError("carrier identity must be a nonempty string")
        if atom_id in carriers_by_atom:
            raise ValueError("carrier identities must be unique")
        carriers_by_atom[atom_id] = carrier
    incidences: list[dict[str, object]] = []
    entity_candidates: list[dict[str, object]] = []
    external_references: list[dict[str, object]] = []

    for relation in subject_relations:
        kind = _value(relation, "kind")
        subject_path = _value(relation, "subject_path", _value(relation, "target_entity"))
        if kind not in {"GOVERNS", "DEPENDS_ON"} or not isinstance(subject_path, str) or not subject_path:
            continue
        lineage = _lineage(relation, carriers_by_atom)
        incidence = {
            "relation": kind,
            "subject_path": subject_path,
            "source": lineage,
        }
        incidences.append(incidence)
        if kind == "GOVERNS":
            entity_candidates.append(
                {
                    "candidate_identity": subject_path,
                    "source": lineage,
                    "disposition": "unresolved",
                    "reason": "Subject GOVERNS incidence is not Entity admission without verified fact context.",
                }
            )
        else:
            external_references.append(
                {
                    "relation": "DEPENDS_ON",
                    "subject_path": subject_path,
                    "source": lineage,
                }
            )

    if graph_fact_context is None:
        entities: list[dict[str, object]] = []
        native_properties: list[dict[str, object]] = []
        native_relations: list[dict[str, object]] = []
        context_evidence: object = {}
        admission_disposition = "unknown"
        property_disposition = "not-covered"
        relation_disposition = "not-covered"
    else:
        context = _trusted_context_payload(graph_fact_context)
        entities, native_properties, native_relations = _native_facts(context)
        context_evidence = {
            key: _copy(context[key])
            for key in ("context_sha256", "provider", "source_binding", "coverage")
            if key in context
        }
        admission_disposition = _coverage_disposition(context, "entity_admission")
        property_disposition = _coverage_disposition(context, "entity_property")
        relation_disposition = _coverage_disposition(context, "relation")
    source_atoms = sorted(
        (_source_record(carrier, source_metadata) for carrier in carriers),
        key=lambda record: str(record["atom_id"]),
    )
    return {
        "entities": entities,
        "native_properties": native_properties,
        "native_relations": native_relations,
        "atom_incidence": sorted(incidences, key=_canonical),
        "entity_candidates": sorted(entity_candidates, key=_canonical),
        "source_atoms": source_atoms,
        "project_structure": sorted((_copy(row) for row in project_structure), key=_canonical),
        "external_references": sorted(external_references, key=_canonical),
        "source_fact_context_evidence": context_evidence,
        "coverage": {
            "entity_admission": {
                "status": admission_disposition,
                "disposition": "Native Entity membership requires a verified derived-fact context; Subject incidence alone is unresolved.",
            },
            "properties": {
                "status": property_disposition,
                "disposition": "No Atom/Carrier metadata was promoted; only verified admitted Entity Property facts may appear.",
            },
            "native_relations": {
                "status": relation_disposition,
                "disposition": "Subject GOVERNS and DEPENDS_ON evidence is retained as Atom incidence, not fabricated native Entity relations.",
            },
        },
    }
