#!/usr/bin/env python3
"""Build and verify the bounded CA-P-2053 relations/Subjects supplement.

This one-off evidence report reads frozen and live inputs only.  Its output is
non-authoritative, non-executable review evidence; it never changes source
Atoms, candidate authority, or the baseline ledger.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
STAGE2 = ROOT / ".caprmedio_caprmedio/_projection/core-entity-review/stage2"
LEDGER = STAGE2 / "current-subjects.mapping-ledger.json"
OWNERSHIP = STAGE2 / "current-subjects.research-ownership.json"
CANDIDATE = ROOT / ".caprmedio_caprmedio/_projection/core-entity-review/presentation/operator.entity-graph.candidate.json"
OPERATOR = STAGE2 / "operator.subject-decisions.2026-10-11.json"
SUPPLEMENT_CONTRACT = STAGE2 / "current-subjects.supplements.contract.md"
CURRENT_CONTRACT = STAGE2 / "current-subjects.contract.md"
REVIEW_CONTRACT = STAGE2 / "current-subjects.review.contract.md"
OUTPUT = Path(__file__).with_suffix(".json")
BASE_LEDGER_SHA256 = "4d094ce89390e31290ce6ae7248cde78701376085bbe3078e33a228055e2eb39"
SUPPORT_SOURCE_PATHS = {
    "CA-R-1198": ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1198-CORE_META_MODEL-CORE-REQUIREMENT--define-atom-subjects.md",
    "CA-R-1281": ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1281-CORE_META_MODEL-CORE-REQUIREMENT--define-atom-subjects-graph.md",
    "CA-R-1335": ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1335-CORE_META_MODEL-CORE-REQUIREMENT--define-terms-graph.md",
}


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def pin(path: Path) -> dict[str, str]:
    return {"path": str(path.relative_to(ROOT)), "sha256": sha256_file(path)}


def main_content_span(source: Path) -> dict[str, object]:
    """Return the complete current body after frontmatter, never metadata."""
    raw = source.read_bytes()
    lines = raw.splitlines(keepends=True)
    start = 1
    if lines and lines[0].strip() == b"---":
        for position, line in enumerate(lines[1:], start=2):
            if line.strip() == b"---":
                start = position + 1
                break
        else:
            raise ValueError(f"unterminated frontmatter: {source}")
    if start > len(lines):
        raise ValueError(f"missing Main Content: {source}")
    body = b"".join(lines[start - 1 :])
    return {
        "path": str(source.relative_to(ROOT)),
        "sha256": sha256_bytes(raw),
        "start_line": start,
        "end_line": len(lines),
        "span_sha256": sha256_bytes(body),
    }


def candidate_basis(*items: tuple[str, str]) -> list[dict[str, str]]:
    return [{"pointer": pointer, "reason": reason} for pointer, reason in items]


ATOM_SUBJECTS = {
    "value": "Atom.Subjects",
    "confidence": 0.96,
    "reason": (
        "CA-R-1198 explicitly defines Atom Subjects as the Atom Property that "
        "records its direct GOVERNS and DEPENDS_ON Subject Relations. The "
        "confirmed dependent-Entity identity rule preserves the Atom owner and "
        "the Subjects field without making an individual Subject Relation or its "
        "target into the aggregate Property."
    ),
    "basis": (
        ("#/root_entities/0/narrower_entities/0", "Atom is the confirmed governed dependent Entity under Artifact."),
        ("#/dependent_entities/property_node_vs_relation", "A Property is a dependent Entity node; its relation to the owner remains distinct."),
        ("#/entity_identity_model/dependent_entity", "A dependent Entity is identified by owner selector plus dependent field."),
    ),
    "distinctions": (
        "Atom.Subjects remains the aggregate Atom Property, not an individual GOVERNS or DEPENDS_ON Relation.",
        "Each direct Subject Relation and its canonical target remain distinct from the aggregate Property.",
    ),
    "support_atom": "CA-R-1198",
}

ATOM_SUBJECTS_GRAPH = {
    "value": "Projection.Type: Atom Subjects Graph",
    "confidence": 0.95,
    "reason": (
        "CA-R-1281 expressly defines Atom Subjects Graph as the Type value under "
        "Projection. The confirmed Projection model and dependent-Entity identity "
        "rule preserve the Projection owner, Type field, and exact allowed value; "
        "they do not turn the derived graph into authority or a Terms Graph."
    ),
    "basis": (
        ("#/projection_member_model", "Projection is a confirmed managed whole of derived instances with its own lifecycle."),
        ("#/entity_identity_model/dependent_entity", "A confirmed dependent Entity is identified by owner selector plus field."),
    ),
    "distinctions": (
        "Atom Subjects Graph remains a non-authoritative Projection Type, not a native Relation owner.",
        "Its represented GOVERNS and DEPENDS_ON links remain distinct from target nodes and intermediate Subject objects.",
        "Atom Subjects Graph remains distinct from the separate Terms Graph.",
    ),
    "support_atom": "CA-R-1281",
}

TERMS_GRAPH = {
    "value": "Projection.Type: Terms Graph",
    "confidence": 0.95,
    "reason": (
        "CA-R-1335 expressly defines Terms Graph as the Type value under Projection. "
        "The confirmed Projection model and dependent-Entity identity rule preserve "
        "the Projection owner, Type field, and exact allowed value, while the Terms "
        "Graph boundary keeps Terms outside the Entities Graph."
    ),
    "basis": (
        ("#/projection_member_model", "Projection is a confirmed managed whole of derived instances with its own lifecycle."),
        ("#/entity_identity_model/dependent_entity", "A confirmed dependent Entity is identified by owner selector plus field."),
        ("#/terms_graph_boundary", "Terms belong to a graph separate from the Entities Graph."),
    ),
    "distinctions": (
        "Terms Graph remains a Projection Type and does not make Term an Entities-Graph root.",
        "Terms Graph source authority and graph-qualified Relation authority remain separate from an Entities-Graph mapping.",
    ),
    "support_atom": "CA-R-1335",
}

ARTIFACT_PROPERTY = {
    "value": "Artifact.Property",
    "confidence": 0.92,
    "reason": (
        "CA-D-267 expressly concerns non-Atom Artifact Properties. The confirmed "
        "Property-as-dependent-node and owner-plus-field rules support the "
        "notation-preserving Artifact.Property target without recasting a Carrier "
        "address as an Artifact identity or a relation kind."
    ),
    "basis": (
        ("#/root_entities/0", "Artifact is the confirmed governed lifecycle root containing named dependent Entities."),
        ("#/dependent_entities/property_node_vs_relation", "A Property is a dependent Entity node, while property-of is the connecting relation."),
        ("#/entity_identity_model/dependent_entity", "A confirmed dependent Entity is identified by owner selector plus field."),
    ),
    "distinctions": (
        "The non-Atom qualification remains explicit; this does not identify an Atom Property.",
        "Carrier addresses remain representations and do not become Artifact identity.",
    ),
    "support_atom": None,
}

ATOM_SUMMARY = {
    "value": "Atom.Summary",
    "confidence": 0.95,
    "reason": (
        "CA-R-1465 explicitly defines Summary as a non-authoritative Property of "
        "one Atom with no independent identity, lifecycle, or authority. The "
        "dependent-Entity rule therefore supports Atom.Summary and preserves the "
        "Atom owner rather than flattening Summary to a root Entity."
    ),
    "basis": (
        ("#/root_entities/0/narrower_entities/0", "Atom is the confirmed governed dependent Entity under Artifact."),
        ("#/dependent_entities/property_node_vs_relation", "A Property is a dependent Entity node rather than a separate relation or root."),
        ("#/entity_identity_model/dependent_entity", "A confirmed dependent Entity is identified by owner selector plus field."),
    ),
    "distinctions": (
        "Summary remains non-authoritative navigation content, not the Atom Claim or Scope.",
        "Summary has no independent identity, lifecycle, or authority apart from its Atom.",
    ),
    "support_atom": None,
}


def unresolved_reason(baseline: dict) -> str:
    old = baseline["old_value"]
    if old.startswith("CCE") or old == "CCE":
        return (
            f"Current Main Content for {old!r} retains a CCE grammar, operator, or "
            "role qualification. The candidate confirms no CCE owner/field/value "
            "model that preserves that qualification, so a Property or Relation "
            "target would be invented."
        )
    if "Relation" in old or old in {"Subject", "Subject Assignment", "Subject Path", "Subject Expression"}:
        return (
            f"Current Main Content for {old!r} requires a typed Relation, endpoint, "
            "path, or role distinction. The candidate confirms only the generic "
            "Relation root and endpoint constraints, not a target retaining this "
            "specific relation qualification; no aggregate Subjects Property is substituted."
        )
    if "Term" in old or old in {"General Term", "Root Term", "semantics"}:
        return (
            f"Current Main Content for {old!r} concerns Terms or their graph-specific "
            "authority. The candidate expressly keeps Terms outside the Entities "
            "Graph and supplies no owner-qualified target preserving this meaning."
        )
    if old.startswith("Structural Entity") or old in {"Entity", "Entity Taxonomy", "Primary Entity", "Relational Atom"}:
        return (
            f"Current Main Content for {old!r} retains an Entity-kind or structural "
            "qualification. The candidate root list alone does not establish a "
            "canonical target with that qualifier, so no hierarchy or Property path is inferred."
        )
    if "Carrier" in old:
        return (
            f"Current Main Content for {old!r} retains a representation/carrier "
            "boundary. Carrier is a separate candidate root, but no confirmed "
            "owner-qualified dependent field preserves this exact carrier semantics."
        )
    return (
        f"Current Main Content for {old!r} was retained as live evidence, but it does "
        "not provide an owner-qualified dependent field or typed-relation target that "
        "the candidate confirms without discarding the source qualifier."
    )


def rule_for(baseline: dict) -> dict | None:
    old = baseline["old_value"]
    if old == "Atom/Subjects":
        return ATOM_SUBJECTS
    if old == "Projection/Type: Atom Subjects Graph":
        return ATOM_SUBJECTS_GRAPH
    if old == "Projection/Type: Terms Graph":
        return TERMS_GRAPH
    if old == "Artifact/Property":
        return ARTIFACT_PROPERTY
    if baseline["source_atom_id"] == "CA-R-1198" and old == "Property":
        return ATOM_SUBJECTS
    if baseline["source_atom_id"] == "CA-R-1465" and old == "Property":
        return ATOM_SUMMARY
    return None


def build_report() -> dict:
    if sha256_file(LEDGER) != BASE_LEDGER_SHA256:
        raise ValueError("baseline ledger pin is stale")
    ledger = json.loads(LEDGER.read_text())
    ownership = json.loads(OWNERSHIP.read_text())
    task = next(row for row in ownership["research_tasks"] if row["task_id"] == "CA-P-2053")
    values = set(task["old_values"])
    rows = sorted(
        (row for row in ledger["occurrences"] if row["decision"] == "unresolved" and row["old_value"] in values),
        key=lambda row: row["occurrence_id"],
    )
    identifiers = [row["occurrence_id"] for row in rows]
    identifiers_sha = sha256_bytes(json.dumps(identifiers, separators=(",", ":")).encode())
    if len(rows) != task["occurrences"] or identifiers_sha != task["occurrence_ids_sha256"]:
        raise ValueError("relations_subjects research ownership selection is stale")
    if len({row["source_path"] for row in rows}) != task["sources"]:
        raise ValueError("relations_subjects source coverage differs from ownership")

    selected_by_atom = {row["source_atom_id"]: row for row in rows}
    additional_support_sources: set[Path] = set()
    reviewed = []
    for baseline in rows:
        source = ROOT / baseline["source_path"]
        if sha256_file(source) != baseline["source_sha256"]:
            raise ValueError(f"current source pin is stale: {source}")
        evidence = [{
            **main_content_span(source),
            "reason": f"Current Main Content for {baseline['source_atom_id']} is the direct meaning evidence for {baseline['old_value']!r}.",
        }]
        rule = rule_for(baseline)
        if rule and rule["support_atom"] and rule["support_atom"] != baseline["source_atom_id"]:
            support = selected_by_atom.get(rule["support_atom"])
            if support is None:
                support_path = ROOT / SUPPORT_SOURCE_PATHS[rule["support_atom"]]
                additional_support_sources.add(support_path)
            else:
                support_path = ROOT / support["source_path"]
                if sha256_file(support_path) != support["source_sha256"]:
                    raise ValueError(f"support source pin is stale: {support_path}")
            evidence.append({
                **main_content_span(support_path),
                "reason": f"Current Main Content for {rule['support_atom']} supplies the explicit owner/field/value definition used for this proposal.",
            })
        base = {
            "occurrence_id": baseline["occurrence_id"],
            "source_path": baseline["source_path"],
            "source_atom_id": baseline["source_atom_id"],
            "source_version": baseline["source_version"],
            "source_sha256": baseline["source_sha256"],
            "field": baseline["field"],
            "index": baseline["index"],
            "old_value": baseline["old_value"],
            "quarantined": baseline["quarantined"],
            "originating_batch_id": baseline["batch_id"],
            "originating_task_id": baseline["task_id"],
            "originating_review_path": baseline["originating_review_path"],
            "originating_review_sha256": baseline["originating_review_sha256"],
            "baseline_decision": baseline["decision"],
            "baseline_proposed_value": baseline["proposed_value"],
            "baseline_confidence": baseline["confidence"],
            "baseline_reason": baseline["reason"],
            "baseline_question": baseline["question"],
            "evidence": evidence,
            "question": None,
            "executable": False,
        }
        if rule is None:
            reviewed.append({
                **base,
                "decision": "unresolved",
                "proposed_value": None,
                "confidence": 0.5,
                "reason": unresolved_reason(baseline),
                "candidate_basis": [],
                "preserved_distinctions": [
                    f"The exact legacy identity {baseline['old_value']!r} and its current source context remain visible for later research.",
                    "The full current source qualification remains preserved; no candidate identity is invented.",
                ],
            })
        else:
            reviewed.append({
                **base,
                "decision": "proposed",
                "proposed_value": rule["value"],
                "confidence": rule["confidence"],
                "reason": rule["reason"],
                "candidate_basis": candidate_basis(*rule["basis"]),
                "preserved_distinctions": list(rule["distinctions"]),
            })

    sources = sorted({row["source_path"] for row in reviewed})
    report = {
        "schema_version": 1,
        "task_id": "CA-P-2053",
        "non_authoritative": True,
        "source_migration": "not_performed",
        "native_admission": "not_performed",
        "base_ledger": {"path": str(LEDGER.relative_to(ROOT)), "sha256": BASE_LEDGER_SHA256},
        "research_ownership": {
            **pin(OWNERSHIP),
            "group": "relations_subjects",
            "occurrence_ids_sha256": identifiers_sha,
        },
        "evidence_pins": [pin(CANDIDATE), pin(OPERATOR), pin(SUPPLEMENT_CONTRACT), pin(CURRENT_CONTRACT), pin(REVIEW_CONTRACT)],
        "coverage": {
            "occurrences": len(reviewed),
            "sources": len(sources),
            "old_values": len(values),
            "occurrence_ids_sha256": identifiers_sha,
        },
        "source_pins": [
            {"path": source, "sha256": next(row["source_sha256"] for row in reviewed if row["source_path"] == source)}
            for source in sources
        ],
        "support_source_pins": [pin(source) for source in sorted(additional_support_sources)],
        "occurrences": reviewed,
    }
    verify_report(report, task)
    return report


def verify_report(report: dict, task: dict) -> None:
    rows = report["occurrences"]
    assert report["coverage"]["occurrences"] == task["occurrences"] == len(rows)
    assert report["coverage"]["sources"] == task["sources"] == len(report["source_pins"])
    assert report["coverage"]["old_values"] == len(task["old_values"])
    assert report["coverage"]["occurrence_ids_sha256"] == task["occurrence_ids_sha256"]
    assert len({row["occurrence_id"] for row in rows}) == len(rows)
    for support in report["support_source_pins"]:
        assert sha256_file(ROOT / support["path"]) == support["sha256"]
    for row in rows:
        assert row["baseline_decision"] == "unresolved" and row["baseline_proposed_value"] is None
        assert row["executable"] is False and row["evidence"] and row["question"] is None
        for evidence in row["evidence"]:
            source = ROOT / evidence["path"]
            raw = source.read_bytes()
            lines = raw.splitlines(keepends=True)
            assert sha256_bytes(raw) == evidence["sha256"]
            assert sha256_bytes(b"".join(lines[evidence["start_line"] - 1 : evidence["end_line"]])) == evidence["span_sha256"]
            assert evidence["start_line"] > 1
        if row["decision"] == "proposed":
            assert row["proposed_value"] and row["confidence"] >= 0.90 and row["candidate_basis"]
        else:
            assert row["decision"] == "unresolved" and row["proposed_value"] is None
            assert row["confidence"] < 0.90 and not row["candidate_basis"]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    report = build_report()
    rendered = json.dumps(report, indent=2) + "\n"
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text() != rendered:
            raise ValueError("report differs from the verified derived output")
    else:
        OUTPUT.write_text(rendered)
    print(json.dumps({
        "output": str(OUTPUT.relative_to(ROOT)),
        "sha256": sha256_file(OUTPUT) if OUTPUT.exists() else sha256_bytes(rendered.encode()),
        "decisions": Counter(row["decision"] for row in report["occurrences"]),
        "coverage": report["coverage"],
    }, default=dict, sort_keys=True))


if __name__ == "__main__":
    main()
