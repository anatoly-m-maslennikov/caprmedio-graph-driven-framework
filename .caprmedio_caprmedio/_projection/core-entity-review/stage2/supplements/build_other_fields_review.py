#!/usr/bin/env python3
"""Build and verify the bounded CA-P-2056 other-fields research supplement.

This is an ad-hoc report builder, not a reusable mapping tool.  It retains every
assigned baseline-unresolved occurrence and only proposes the five direct Tier
field/value families whose current definitions and the generic candidate rule
are both explicit.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any


REPO = Path(__file__).resolve().parents[5]
STAGE2 = REPO / ".caprmedio_caprmedio/_projection/core-entity-review/stage2"
LEDGER_PATH = STAGE2 / "current-subjects.mapping-ledger.json"
OWNERSHIP_PATH = STAGE2 / "current-subjects.research-ownership.json"
CANDIDATE_PATH = REPO / ".caprmedio_caprmedio/_projection/core-entity-review/presentation/operator.entity-graph.candidate.json"
DECISION_PATH = STAGE2 / "operator.subject-decisions.2026-10-11.json"
PREPARATION_CONTRACT = STAGE2 / "current-subjects.contract.md"
REVIEW_CONTRACT = STAGE2 / "current-subjects.review.contract.md"
SUPPLEMENTS_CONTRACT = STAGE2 / "current-subjects.supplements.contract.md"
OUTPUT_PATH = STAGE2 / "supplements/other_fields.review.json"

TASK_ID = "CA-P-2056"
TASK_GROUP = "other_fields"
EXPECTED_LEDGER_SHA = "4d094ce89390e31290ce6ae7248cde78701376085bbe3078e33a228055e2eb39"
EXPECTED_OCCURRENCE_DIGEST = "11cbb83661d715d78bf54e91195b2c07a9caa62533057d2706b837077d5943ce"

# These five direct old-field families have explicit current definitions.  This
# deliberately excludes Atom/Scope, ownership/target Scope Unit, identity and
# identifier terms: each has multiple non-equivalent meanings in live bodies.
TIER_RULES = {
    "Atom/Local Tier": ("Atom.Local Tier", "local_tier", None),
    "Atom/Global Tier": ("Atom.Global Tier", "global_tier", None),
    "Atom/Local Tier: General": ("Atom.Local Tier: General", "local_tier", "general"),
    "Atom/Local Tier: Principle": ("Atom.Local Tier: Principle", "local_tier", "principle"),
    "Atom/Local Tier: Standard": ("Atom.Local Tier: Standard", "local_tier", "standard"),
}

DEFINITION_SPANS = {
    "local_tier": (
        ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1287-CORE_META_MODEL-CORE-REQUIREMENT--define-local-tier-as-an-atom-property.md",
        24,
        32,
        "CA-R-1287 explicitly defines Local Tier as an Atom Property, distinct from Claim Scope, Content Role, Type, and Methodology Source ownership.",
    ),
    "global_tier": (
        ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1444-CORE_META_MODEL-CORE--define-global-tier.md",
        22,
        30,
        "CA-R-1444 explicitly defines Global Tier as an Atom Property derived from Atom Scope and, where present, Local Tier.",
    ),
    "local_tier_values": (
        ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-155-CORE_META_MODEL-CORE--give-every-non-project-goal-atom-one-local-tier.md",
        25,
        32,
        "CA-R-155 explicitly constrains the Local Tier Property to Principle, Core, General, or Standard for non-Project-Goal Atoms.",
    ),
}


def rel(path: Path) -> str:
    return path.relative_to(REPO).as_posix()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def source_span(relative_path: str, start_line: int, end_line: int, reason: str) -> dict[str, Any]:
    path = REPO / relative_path
    data = path.read_bytes()
    lines = data.splitlines(keepends=True)
    if start_line < 1 or end_line < start_line or end_line > len(lines):
        raise ValueError(f"invalid span {relative_path}:{start_line}-{end_line}")
    return {
        "path": relative_path,
        "sha256": sha256_bytes(data),
        "start_line": start_line,
        "end_line": end_line,
        "span_sha256": sha256_bytes(b"".join(lines[start_line - 1 : end_line])),
        "reason": reason,
    }


def baseline_current_evidence(row: dict[str, Any]) -> dict[str, Any]:
    for evidence in row["evidence"]:
        if evidence["path"] == row["source_path"]:
            current = source_span(
                evidence["path"],
                evidence["start_line"],
                evidence["end_line"],
                "The complete live Main Content was re-read as current meaning evidence; frozen baseline evidence remains separate.",
            )
            if current["sha256"] != row["source_sha256"]:
                raise ValueError(f"stale source pin: {row['occurrence_id']}")
            if current["span_sha256"] != evidence["span_sha256"]:
                raise ValueError(f"stale source span: {row['occurrence_id']}")
            return current
    raise ValueError(f"missing owning current evidence: {row['occurrence_id']}")


def source_text(evidence: dict[str, Any]) -> str:
    path = REPO / evidence["path"]
    lines = path.read_text(encoding="utf-8").splitlines()
    return "\n".join(lines[evidence["start_line"] - 1 : evidence["end_line"]]).lower()


def definition_evidence(key: str) -> dict[str, Any]:
    path, start, end, reason = DEFINITION_SPANS[key]
    return source_span(path, start, end, reason)


def selected_rows(ledger: dict[str, Any], task: dict[str, Any]) -> list[dict[str, Any]]:
    values = set(task["old_values"])
    rows = [
        row
        for row in ledger["occurrences"]
        if row["decision"] == "unresolved" and row["old_value"] in values
    ]
    rows.sort(key=lambda row: row["occurrence_id"])
    digest = sha256_bytes(
        json.dumps([row["occurrence_id"] for row in rows], separators=(",", ":")).encode("utf-8")
    )
    if len(rows) != task["occurrences"] or digest != task["occurrence_ids_sha256"]:
        raise ValueError(
            f"ownership selection mismatch: {len(rows)} rows digest={digest}"
        )
    return rows


def copy_baseline(row: dict[str, Any]) -> dict[str, Any]:
    fields = (
        "batch_id", "field", "index", "occurrence_id", "old_value",
        "originating_review_path", "originating_review_sha256", "quarantined",
        "source_atom_id", "source_path", "source_sha256", "source_version",
    )
    result = {field: row[field] for field in fields}
    result.update(
        {
            "baseline_task_id": row["task_id"],
            "baseline_decision": row["decision"],
            "baseline_proposed_value": row["proposed_value"],
            "baseline_confidence": row["confidence"],
            "baseline_reason": row["reason"],
            "baseline_evidence": row["evidence"],
            "baseline_candidate_basis": row["candidate_basis"],
            "baseline_preserved_distinctions": row["preserved_distinctions"],
            "baseline_question": row["question"],
        }
    )
    return result


def proposal_for(row: dict[str, Any], evidence: dict[str, Any]) -> dict[str, Any] | None:
    rule = TIER_RULES.get(row["old_value"])
    if rule is None:
        return None
    proposed_value, definition_key, allowed_value = rule
    body = source_text(evidence)
    required = ["local tier" if definition_key == "local_tier" else "global tier"]
    if allowed_value:
        required.append(allowed_value)
    if not all(fragment in body for fragment in required):
        return None
    definition_key_for_value = "local_tier_values" if allowed_value else definition_key
    extra = definition_evidence(definition_key)
    if definition_key_for_value != definition_key:
        extra_value = definition_evidence(definition_key_for_value)
        evidence_list = [evidence, extra, extra_value]
    else:
        evidence_list = [evidence, extra]
    value_clause = (
        f" and its explicit {allowed_value.title()} allowed value"
        if allowed_value
        else ""
    )
    return {
        "decision": "proposed",
        "proposed_value": proposed_value,
        "confidence": 0.9,
        "reason": (
            f"The re-read current Main Content explicitly names {row['old_value']}. "
            f"The pinned current definition establishes {definition_key.replace('_', ' ').title()} "
            f"as an Atom Property{value_clause}; the candidate's generic dependent-Entity rule "
            f"supports this named Atom field although it is absent from the display examples. "
            "This is a candidate-only, non-executable proposal."
        ),
        "evidence": evidence_list,
        "candidate_basis": [
            {
                "pointer": "#/dependent_entities/property_node_vs_relation",
                "reason": "The candidate states that a Property is a named dependent Entity node connected to its owning Entity.",
            },
            {
                "pointer": "#/root_entities/0/narrower_entities/0",
                "reason": "The candidate defines Atom as an Entity made of named dependent Entities; the current definitions identify the exact named Tier field/value.",
            },
            {
                "pointer": "#/entity_vs_syntax_rules/0",
                "reason": "The notation distinguishes dependent-field and allowed-value display without admitting native grammar or migration.",
            },
        ],
        "preserved_distinctions": [
            "Local Tier and Global Tier remain distinct Atom properties.",
            "A Tier allowed value remains qualified by its Local Tier bearer.",
            "Atom ownership Scope Unit and textual Substance Scope remain separate.",
            "No source rewrite, native grammar admission, Carrier registry, or live migration is inferred.",
        ],
        "question": None,
        "executable": False,
    }


def unresolved_for(row: dict[str, Any], evidence: dict[str, Any]) -> dict[str, Any]:
    old = row["old_value"]
    if old == "Atom/Scope":
        reason = (
            "The current literal is an Atom Scope reference. The candidate defines Substance Scope "
            "as content applicability and permits omission only for the whole governed Subject and "
            "whole owning Scope Unit; it does not collapse Atom ownership, GOVERNS target, Claim "
            "Target Scope Unit, and textual applicability. This source-specific scope meaning cannot "
            "be blindly rewritten to Atom.Substance Scope."
        )
        distinctions = [
            "Atom Scope remains distinct from Substance Scope applicability.",
            "Owning Scope Unit, GOVERNS target, and Claim Target Scope Unit remain distinct.",
            "No global slash-to-dot rewrite is inferred.",
        ]
    elif old == "Atom/Claim/Target Scope Unit":
        reason = (
            "The current literal names an explicit Claim Target Scope Unit, which remains distinct "
            "from the owning Scope Unit and from Substance Scope applicability. The candidate has "
            "no confirmed dependent Atom target-field identity preserving this relation-qualified "
            "meaning, so a display path would be unsupported."
        )
        distinctions = [
            "Claim Target Scope Unit remains distinct from owning Scope Unit.",
            "Target selection remains distinct from textual Substance Scope applicability.",
            "No display-only Artifact prefix or dot binding is inferred.",
        ]
    elif old in {"Atom/Identity", "Atom/Identifier"}:
        reason = (
            "The live sources use this literal across Atom, Revision, Carrier, draft-history, and "
            "projection contexts. The candidate's generic dependent-Entity rule does not determine "
            "which identity-bearing subject is meant for this occurrence; Atom.Identity or "
            "Atom.Identifier would lose a source-specific historical or carrier qualification."
        )
        distinctions = [
            "Atom identity remains distinct from Revision, Carrier, and Draft-history identity.",
            "No unsupported identity field or registry is introduced.",
            "No native grammar admission or migration is inferred.",
        ]
    else:
        reason = (
            "The baseline current Main Content was re-read, but this bounded lane has not established "
            "a candidate identity, owner, and qualification that preserve the literal's source-specific "
            "meaning. It remains explicit research rather than a guessed display rewrite."
        )
        distinctions = [
            f"The exact current Subject text {old!r} remains visible as unresolved research.",
            "No root, owner, Carrier binding, grammar admission, or live migration is inferred.",
        ]
    return {
        "decision": "unresolved",
        "proposed_value": None,
        "confidence": min(float(row["confidence"]), 0.5),
        "reason": reason,
        "evidence": [evidence],
        "candidate_basis": [],
        "preserved_distinctions": distinctions,
        "question": None,
        "executable": False,
    }


def pin(path: Path) -> dict[str, str]:
    return {"path": rel(path), "sha256": sha256_file(path)}


def build() -> dict[str, Any]:
    ledger = load_json(LEDGER_PATH)
    ownership = load_json(OWNERSHIP_PATH)
    if sha256_file(LEDGER_PATH) != EXPECTED_LEDGER_SHA:
        raise ValueError("base ledger SHA differs from the supplement contract pin")
    task = next(item for item in ownership["research_tasks"] if item["task_id"] == TASK_ID)
    if task["group"] != TASK_GROUP or task["occurrence_ids_sha256"] != EXPECTED_OCCURRENCE_DIGEST:
        raise ValueError("unexpected research ownership entry")
    rows = selected_rows(ledger, task)
    output_rows: list[dict[str, Any]] = []
    for baseline in rows:
        current_evidence = baseline_current_evidence(baseline)
        row = copy_baseline(baseline)
        row.update(proposal_for(baseline, current_evidence) or unresolved_for(baseline, current_evidence))
        output_rows.append(row)
    decisions = Counter(row["decision"] for row in output_rows)
    selected_sources = sorted({row["source_path"] for row in output_rows})
    if len(selected_sources) != task["sources"]:
        raise ValueError("source coverage mismatch")
    remaining_by_value: dict[str, list[str]] = {}
    for row in output_rows:
        if row["decision"] == "unresolved":
            remaining_by_value.setdefault(row["old_value"], []).append(row["occurrence_id"])
    remaining_groups = [
        {
            "old_value": old_value,
            "occurrences": len(occurrence_ids),
            "occurrence_ids": occurrence_ids,
        }
        for old_value, occurrence_ids in sorted(remaining_by_value.items())
    ]
    return {
        "schema_version": 1,
        "task_id": TASK_ID,
        "non_authoritative": True,
        "source_migration": "not_performed",
        "native_admission": "not_performed",
        "base_ledger": pin(LEDGER_PATH),
        "research_ownership": {
            **pin(OWNERSHIP_PATH),
            "group": task["group"],
            "occurrence_ids_sha256": task["occurrence_ids_sha256"],
            "occurrences": task["occurrences"],
            "sources": task["sources"],
            "old_values": task["old_values"],
        },
        "evidence_pins": {
            "frozen_candidate": pin(CANDIDATE_PATH),
            "operator_decision": pin(DECISION_PATH),
            "supplements_contract": pin(SUPPLEMENTS_CONTRACT),
            "preparation_contract": pin(PREPARATION_CONTRACT),
            "review_contract": pin(REVIEW_CONTRACT),
        },
        "research_status": {
            "state": "partial",
            "reason": "Only direct Tier field/value families were resolved in this bounded pass; all other assigned rows remain explicit research.",
            "not_task_completion": True,
        },
        "remaining_research": {
            "occurrences": decisions["unresolved"],
            "by_old_value": remaining_groups,
            "highest_blast_radius": [
                group
                for group in remaining_groups
                if group["old_value"]
                in {
                    "Atom/Scope",
                    "Atom/Claim/Target Scope Unit",
                    "Atom/Identity",
                    "Atom/Identifier",
                }
            ],
        },
        "counts": {
            "occurrences": len(output_rows),
            "sources": len(selected_sources),
            "old_values": len(task["old_values"]),
            "decisions": {
                "proposed": decisions["proposed"],
                "unchanged": decisions["unchanged"],
                "unresolved": decisions["unresolved"],
            },
        },
        "occurrences": output_rows,
    }


def verify(report: dict[str, Any]) -> None:
    ledger = load_json(LEDGER_PATH)
    ownership = load_json(OWNERSHIP_PATH)
    task = next(item for item in ownership["research_tasks"] if item["task_id"] == TASK_ID)
    rows = selected_rows(ledger, task)
    expected_ids = [row["occurrence_id"] for row in rows]
    actual_ids = [row["occurrence_id"] for row in report["occurrences"]]
    if actual_ids != expected_ids:
        raise ValueError("output occurrence coverage/order mismatch")
    if report["task_id"] != TASK_ID or report["counts"]["occurrences"] != len(rows):
        raise ValueError("task or count mismatch")
    if report["base_ledger"]["sha256"] != sha256_file(LEDGER_PATH):
        raise ValueError("stale base ledger pin")
    if report["research_ownership"]["sha256"] != sha256_file(OWNERSHIP_PATH):
        raise ValueError("stale ownership pin")
    remaining_ids = sorted(
        occurrence_id
        for group in report["remaining_research"]["by_old_value"]
        for occurrence_id in group["occurrence_ids"]
    )
    unresolved_ids = sorted(
        row["occurrence_id"] for row in report["occurrences"] if row["decision"] == "unresolved"
    )
    if remaining_ids != unresolved_ids:
        raise ValueError("remaining-research index mismatch")
    baseline_by_id = {row["occurrence_id"]: row for row in rows}
    for row in report["occurrences"]:
        baseline = baseline_by_id[row["occurrence_id"]]
        for field in (
            "source_path", "source_atom_id", "source_version", "source_sha256",
            "field", "index", "old_value", "quarantined", "originating_review_path",
            "originating_review_sha256",
        ):
            if row[field] != baseline[field]:
                raise ValueError(f"baseline-origin mismatch: {row['occurrence_id']}:{field}")
        if row["baseline_decision"] != baseline["decision"] or row["baseline_proposed_value"] != baseline["proposed_value"]:
            raise ValueError(f"baseline-decision mismatch: {row['occurrence_id']}")
        if row["executable"] is not False:
            raise ValueError(f"executable row: {row['occurrence_id']}")
        if row["decision"] == "proposed":
            if row["old_value"] not in TIER_RULES or row["confidence"] < 0.9:
                raise ValueError(f"unsupported proposal: {row['occurrence_id']}")
            if not row["candidate_basis"]:
                raise ValueError(f"proposal without candidate basis: {row['occurrence_id']}")
        elif row["proposed_value"] is not None or row["confidence"] >= 0.9:
            raise ValueError(f"invalid unresolved row: {row['occurrence_id']}")
        if not any(evidence["path"] == row["source_path"] for evidence in row["evidence"]):
            raise ValueError(f"missing owning evidence: {row['occurrence_id']}")
        for evidence in row["evidence"]:
            current = source_span(evidence["path"], evidence["start_line"], evidence["end_line"], evidence["reason"])
            if current["sha256"] != evidence["sha256"] or current["span_sha256"] != evidence["span_sha256"]:
                raise ValueError(f"stale evidence: {row['occurrence_id']}")
    counted = Counter(row["decision"] for row in report["occurrences"])
    if report["counts"]["decisions"] != {
        "proposed": counted["proposed"],
        "unchanged": counted["unchanged"],
        "unresolved": counted["unresolved"],
    }:
        raise ValueError("decision counts mismatch")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if args.verify:
        report = load_json(OUTPUT_PATH)
        verify(report)
        print(json.dumps({"outcome": "PASS", **report["counts"]}, sort_keys=True))
        return
    report = build()
    OUTPUT_PATH.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    verify(report)
    print(json.dumps({"outcome": "PASS", "output": rel(OUTPUT_PATH), **report["counts"]}, sort_keys=True))


if __name__ == "__main__":
    main()
