#!/usr/bin/env python3
"""Build CA-P-2051's bounded, non-authoritative content-role supplement.

This is an ad-hoc projection helper for one assigned research lane.  It does
not parse or modify Core carriers, admit grammar, or implement a migration.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[5]
STAGE = ROOT / ".caprmedio_caprmedio/_projection/core-entity-review/stage2"
OWNERSHIP = STAGE / "current-subjects.research-ownership.json"
LEDGER = STAGE / "current-subjects.mapping-ledger.json"
CONTRACT = STAGE / "current-subjects.supplements.contract.md"
CURRENT_CONTRACT = STAGE / "current-subjects.contract.md"
REVIEW_CONTRACT = STAGE / "current-subjects.review.contract.md"
CANDIDATE = (
    ROOT
    / ".caprmedio_caprmedio/_projection/core-entity-review/presentation/"
    "operator.entity-graph.candidate.json"
)
OPERATOR_DECISION = STAGE / "operator.subject-decisions.2026-10-11.json"
PLAN = (
    ROOT
    / ".caprmedio_caprmedio/03_plan/18-CA-P-1959-EPIC--improve-entity-model-stage-2/"
    "08-CA-P-1966-EPIC--map-current-core-subject-origins/"
    "56-CA-P-2049-TASK--resolve-remaining-subject-mappings/"
    "02-CA-P-2051-TASK--resolve-content-role-and-type-subject-mappings.md"
)
OUTPUT = STAGE / "supplements/content_roles.review.json"

TASK_ID = "CA-P-2051"
BASE_LEDGER_SHA256 = "4d094ce89390e31290ce6ae7248cde78701376085bbe3078e33a228055e2eb39"
CANDIDATE_SHA256 = "99e7710f5ef83df2b1f3ec1ef4142547655e63bef7415266c5521380da7fa99b"

# These source definitions are current, explicit evidence for the reusable
# field distinctions.  They are evidence, not a replacement for the owning
# source's current Main Content span recorded for every occurrence.
DEFINITION_PATHS = {
    "CA-R-1283": ROOT
    / ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/"
    "METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/"
    "CA-R-1283-CORE_META_MODEL-CORE-REQUIREMENT--register-content-role-values.md",
    "CA-R-1338": ROOT
    / ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/"
    "METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/"
    "CA-R-1338-CORE_META_MODEL-CORE-REQUIREMENT--define-plan-content-role.md",
    "CA-R-1348": ROOT
    / ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/"
    "METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/"
    "CA-R-1348-CORE_META_MODEL-CORE-REQUIREMENT--reuse-type-in-qualified-subjects.md",
    "CA-R-1349": ROOT
    / ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/"
    "METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/"
    "CA-R-1349-CORE_META_MODEL-CORE-REQUIREMENT--identify-one-type-property-slot.md",
    "CA-R-1574": ROOT
    / ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/"
    "METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/"
    "CA-R-1574-CORE_META_MODEL-CORE-REQUIREMENT--define-the-common-plan-atom.md",
    "CA-R-1594": ROOT
    / ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/"
    "METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/"
    "CA-R-1594-CORE_META_MODEL-CORE-REQUIREMENT--define-label.md",
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def pin(path: Path) -> dict[str, str]:
    return {"path": rel(path), "sha256": sha256(path.read_bytes())}


def main_content_span(path: Path, reason: str) -> dict[str, Any]:
    """Return an exact full Main Content span, retaining original line endings."""
    data = path.read_bytes()
    lines = data.splitlines(keepends=True)
    separators = [
        line_number
        for line_number, line in enumerate(lines)
        if line.rstrip(b"\r\n") == b"---"
    ]
    if len(separators) < 2:
        raise ValueError(f"missing YAML frontmatter delimiters: {rel(path)}")
    start_index = separators[1] + 1
    if start_index >= len(lines):
        raise ValueError(f"missing Main Content: {rel(path)}")
    span = b"".join(lines[start_index:])
    return {
        "path": rel(path),
        "sha256": sha256(data),
        "start_line": start_index + 1,
        "end_line": len(lines),
        "span_sha256": sha256(span),
        "reason": reason,
    }


def occurrence_digest(ids: list[str]) -> str:
    return sha256(
        json.dumps(sorted(ids), ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    )


def excluded_reason(old_value: str) -> str | None:
    if "Carrier" in old_value or "Filename" in old_value or "filename" in old_value or "Stem" in old_value:
        return (
            "The current source concerns Carrier or serialized storage detail. "
            "The candidate keeps Carrier as a separate root and supplies no "
            "source-specific binding identity here; a dependent-field rewrite "
            "would invent the prohibited per-property Carrier registry."
        )
    if "Claim/Target Scope Unit" in old_value:
        return (
            "The latest Operator decision explicitly leaves Target Scope Unit "
            "outside the Content Role clarification. The current source is not "
            "enough to choose its canonical owner or relation expression."
        )
    if "/Reference" in old_value:
        return (
            "The current source describes a reference/binding rather than a "
            "confirmed dependent Atom field identity. No target is invented."
        )
    if old_value.endswith("/authoring") or old_value.endswith("/grouping"):
        return (
            "The current source uses this as an authoring or grouping concern, "
            "not an explicit dependent Atom field definition; the generic rule "
            "does not establish a canonical field identity."
        )
    if old_value in {"Type", "Atom/Type"}:
        return (
            "The source does not identify the Type bearer and qualified domain "
            "needed for a canonical target. A bare Type is not safely assigned "
            "to Atom or another Entity."
        )
    return None


def proposed_target(old_value: str) -> str | None:
    """Translate only explicit Content Role field composition to candidate notation."""
    if not old_value.startswith("Atom/Content Role") or excluded_reason(old_value):
        return None
    parts = old_value.split("/")
    if parts[0] != "Atom" or not parts[1].startswith("Content Role"):
        return None
    target = "Atom"
    for part in parts[1:]:
        if ":" in part:
            field, value = part.split(":", 1)
            target += f".{field.strip()}: {value.strip()}"
        else:
            target += f".{part.strip()}"
    return target


def requires_owner_qualification_resolution(target: str | None) -> bool:
    """Identify a field asserted after a Content Role allowed-value selector.

    The candidate supports dependent fields, but it does not decide whether a
    legacy ``Content Role: <value> / <field>`` means an Atom-owned field
    selected by the role, or a field dependent on that allowed value.  Keeping
    that distinction unresolved prevents a notation rewrite from deciding the
    owner or losing the qualifier.
    """
    prefix = "Atom.Content Role: "
    if target is None or not target.startswith(prefix):
        return False
    return "." in target[len(prefix) :]


def owner_qualification_reason(old_value: str) -> str:
    return (
        "The current Main Content and shared definitions establish the Content "
        f"Role and the trailing field in `{old_value}`, but do not establish the "
        "conjunctive owner/qualification: whether the field is Atom-owned and "
        "selected by the role, or dependent on that allowed value. The candidate "
        "has no selector-versus-defined-kind rule and the actual Operator answer "
        "is pending; a target would invent that syntax or owner."
    )


def field_distinctions(old_value: str) -> list[str]:
    parts = old_value.split("/")
    distinctions = [
        "Preserves Atom as bearer and Content Role as its dependent Property.",
        "Preserves every role value, Type qualification, and nested field rather than substituting Substance or a display alias.",
        "Uses candidate notation only; it neither admits grammar nor a native relation.",
    ]
    if len(parts) > 2:
        distinctions.insert(1, f"Retains the complete legacy qualification: {' / '.join(parts[1:])}.")
    return distinctions


def definition_atoms(old_value: str) -> list[str]:
    ids = ["CA-R-1283"]
    if "/Type" in old_value:
        ids.extend(["CA-R-1348", "CA-R-1349"])
    if "Content Role: Plan" in old_value:
        ids.append("CA-R-1338")
    if "Content Role: Plan/Type: Plan" in old_value:
        ids.append("CA-R-1574")
    if old_value.endswith("/Label"):
        ids.append("CA-R-1594")
    return ids


def build() -> dict[str, Any]:
    ownership = load_json(OWNERSHIP)
    ledger = load_json(LEDGER)
    decision = load_json(OPERATOR_DECISION)
    task = next(item for item in ownership["research_tasks"] if item["task_id"] == TASK_ID)
    old_values = set(task["old_values"])

    if sha256(LEDGER.read_bytes()) != BASE_LEDGER_SHA256:
        raise ValueError("baseline ledger pin does not match the contract")
    if sha256(CANDIDATE.read_bytes()) != CANDIDATE_SHA256:
        raise ValueError("candidate pin does not match the Operator decision record")
    if decision["decisions"]["substance"]["preserve_owning_atom_content_role"] is not True:
        raise ValueError("latest Operator record does not preserve owning Content Role")

    baseline_rows = [
        row
        for row in ledger["occurrences"]
        if row["decision"] == "unresolved" and row["old_value"] in old_values
    ]
    baseline_rows.sort(key=lambda row: row["occurrence_id"])
    ids = [row["occurrence_id"] for row in baseline_rows]
    if len(baseline_rows) != task["occurrences"]:
        raise ValueError(f"expected {task['occurrences']} rows, got {len(baseline_rows)}")
    if occurrence_digest(ids) != task["occurrence_ids_sha256"]:
        raise ValueError("owned occurrence digest differs from research ownership")

    source_records = {record["relative_path"]: record for record in ledger["source_reviews"]}
    path_spans: dict[str, dict[str, Any]] = {}
    source_reviews: dict[str, dict[str, Any]] = {}
    for row in baseline_rows:
        source_path = ROOT / row["source_path"]
        current_sha = sha256(source_path.read_bytes())
        if current_sha != row["source_sha256"]:
            raise ValueError(f"stale source pin: {row['source_path']}")
        if row["source_path"] not in path_spans:
            path_spans[row["source_path"]] = main_content_span(
                source_path,
                "Entire current Main Content was read for this source-specific Content Role/Type mapping.",
            )
        baseline_source = source_records.get(row["source_path"])
        if baseline_source is None:
            raise ValueError(f"missing ledger source review: {row['source_path']}")
        if row["source_path"] not in source_reviews:
            source_reviews[row["source_path"]] = {
                "relative_path": row["source_path"],
                "full_file_sha256": current_sha,
                "atom_id": row["source_atom_id"],
                "version": row["source_version"],
                "quarantined": row["quarantined"],
                "findings": baseline_source["findings"],
                "finding_dispositions": baseline_source["finding_dispositions"],
                "main_content_read": path_spans[row["source_path"]],
                "questions": baseline_source["questions"],
            }

    definition_spans = {
        atom_id: main_content_span(
            path,
            "Current explicit shared field definition read for CA-P-2051 mapping evidence.",
        )
        for atom_id, path in DEFINITION_PATHS.items()
    }

    occurrences: list[dict[str, Any]] = []
    for row in baseline_rows:
        old_value = row["old_value"]
        target = proposed_target(old_value)
        source_evidence = path_spans[row["source_path"]]
        common = {
            "occurrence_id": row["occurrence_id"],
            "originating_review_path": row["originating_review_path"],
            "originating_review_sha256": row["originating_review_sha256"],
            "source_path": row["source_path"],
            "source_atom_id": row["source_atom_id"],
            "source_version": row["source_version"],
            "source_sha256": row["source_sha256"],
            "field": row["field"],
            "index": row["index"],
            "old_value": old_value,
            "quarantined": row["quarantined"],
            "baseline_decision": row["decision"],
            "baseline_proposed_value": row["proposed_value"],
            "baseline_confidence": row["confidence"],
            "baseline_reason": row["reason"],
            "evidence": [source_evidence],
            "executable": False,
        }
        if target is None:
            reason = excluded_reason(old_value)
            if reason is None:
                raise ValueError(f"unclassified owned value: {old_value}")
            common.update(
                {
                    "decision": "unresolved",
                    "proposed_value": None,
                    "confidence": 0.0,
                    "reason": reason,
                    "candidate_basis": [],
                    "operator_decision_basis": [],
                    "supporting_definition_atoms": [],
                    "preserved_distinctions": field_distinctions(old_value),
                    "question": None,
                }
            )
        elif requires_owner_qualification_resolution(target):
            definition_ids = definition_atoms(old_value)
            common.update(
                {
                    "decision": "unresolved",
                    "proposed_value": None,
                    "confidence": 0.0,
                    "reason": owner_qualification_reason(old_value),
                    "candidate_basis": [],
                    "operator_decision_basis": [
                        {
                            "pointer": "/decisions/substance/preserve_owning_atom_content_role",
                            "reason": "The actual Operator decision preserves the Content Role but does not resolve the trailing field's owner or qualifier.",
                        }
                    ],
                    "supporting_definition_atoms": definition_ids,
                    "preserved_distinctions": field_distinctions(old_value),
                    "question": None,
                }
            )
        else:
            definition_ids = definition_atoms(old_value)
            common.update(
                {
                    "decision": "proposed",
                    "proposed_value": target,
                    "confidence": 0.95,
                    "reason": (
                        "The current source Main Content was re-read for this exact "
                        "occurrence. Its Content Role/Type field composition remains "
                        "a named dependent Atom field; the target changes only candidate "
                        "notation, retaining every role value and nested qualification."
                    ),
                    "candidate_basis": [
                        {
                            "pointer": "/dependent_entities/meaning",
                            "reason": "The candidate permits named dependent Entities inside an Artifact, including Properties.",
                        },
                        {
                            "pointer": "/dependent_entities/compact_examples",
                            "reason": "The candidate demonstrates Atom.<dependent-field> display notation; the source definitions establish the field omitted from that example list.",
                        },
                    ],
                    "operator_decision_basis": [
                        {
                            "pointer": "/decisions/substance/preserve_owning_atom_content_role",
                            "reason": "The latest Operator decision keeps the owning Atom Content Role rather than collapsing it into the Substance label.",
                        }
                    ],
                    "supporting_definition_atoms": definition_ids,
                    "preserved_distinctions": field_distinctions(old_value),
                    "question": None,
                }
            )
        occurrences.append(common)

    if len(source_reviews) != task["sources"]:
        raise ValueError(f"expected {task['sources']} sources, got {len(source_reviews)}")
    proposed_count = sum(row["decision"] == "proposed" for row in occurrences)
    unresolved_count = sum(row["decision"] == "unresolved" for row in occurrences)
    evidence_pins = [
        pin(LEDGER),
        pin(OWNERSHIP),
        pin(CANDIDATE),
        pin(OPERATOR_DECISION),
        pin(CONTRACT),
        pin(CURRENT_CONTRACT),
        pin(REVIEW_CONTRACT),
        pin(PLAN),
    ]
    return {
        "schema_version": 1,
        "task_id": TASK_ID,
        "non_authoritative": True,
        "source_migration": "not_performed",
        "native_admission": "not_performed",
        "base_ledger": pin(LEDGER),
        "research_ownership": pin(OWNERSHIP),
        "selection": {
            "baseline_decision": "unresolved",
            "old_values": sorted(old_values),
            "occurrence_ids_sha256": occurrence_digest(ids),
            "occurrences": len(occurrences),
            "sources": len(source_reviews),
        },
        "evidence_pins": evidence_pins,
        "shared_current_definitions": definition_spans,
        "source_reviews": [source_reviews[path] for path in sorted(source_reviews)],
        "occurrences": occurrences,
        "counts": {
            "occurrences": len(occurrences),
            "sources": len(source_reviews),
            "proposed": proposed_count,
            "unchanged": 0,
            "unresolved": unresolved_count,
            "executable": 0,
        },
    }


def validate(report: dict[str, Any]) -> None:
    rows = report["occurrences"]
    ids = [row["occurrence_id"] for row in rows]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate occurrence ID")
    if report["selection"]["occurrence_ids_sha256"] != occurrence_digest(ids):
        raise ValueError("output occurrence digest mismatch")
    if any(row["executable"] is not False for row in rows):
        raise ValueError("a report row is executable")
    for row in rows:
        if row["decision"] == "proposed":
            if not row["proposed_value"] or row["confidence"] < 0.90 or not row["candidate_basis"]:
                raise ValueError(f"invalid proposal: {row['occurrence_id']}")
        elif row["decision"] == "unresolved":
            if row["proposed_value"] is not None or row["confidence"] >= 0.90:
                raise ValueError(f"invalid unresolved row: {row['occurrence_id']}")
            target = proposed_target(row["old_value"])
            if requires_owner_qualification_resolution(target) and row["candidate_basis"]:
                raise ValueError(f"qualified unresolved row has candidate basis: {row['occurrence_id']}")
        else:
            raise ValueError(f"unexpected decision: {row['decision']}")
        source_span = row["evidence"][0]
        if source_span["path"] != row["source_path"] or source_span["sha256"] != row["source_sha256"]:
            raise ValueError(f"source evidence mismatch: {row['occurrence_id']}")
    counts = report["counts"]
    if counts["occurrences"] != len(rows):
        raise ValueError("count mismatch")
    if counts["proposed"] + counts["unresolved"] != len(rows):
        raise ValueError("decision count mismatch")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="create the owned supplement output")
    parser.add_argument(
        "--replace-owned-output",
        action="store_true",
        help="replace an existing output produced by this helper after validation",
    )
    parser.add_argument(
        "--verify-output",
        action="store_true",
        help="rebuild from pinned inputs and compare the existing owned output exactly",
    )
    args = parser.parse_args()
    report = build()
    validate(report)
    rendered = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.verify_output:
        if not OUTPUT.exists():
            raise FileNotFoundError(f"missing output: {rel(OUTPUT)}")
        if OUTPUT.read_text(encoding="utf-8") != rendered:
            raise ValueError("output does not exactly match fresh pinned-input reconstruction")
        print(json.dumps({"verified": True, "output": rel(OUTPUT), "sha256": sha256(rendered.encode()), "counts": report["counts"]}))
        return 0
    if args.write:
        if OUTPUT.exists() and not args.replace_owned_output:
            raise FileExistsError(f"refusing to replace existing output: {rel(OUTPUT)}")
        OUTPUT.write_text(rendered, encoding="utf-8")
        print(json.dumps({"output": rel(OUTPUT), "sha256": sha256(rendered.encode()), "counts": report["counts"]}))
    else:
        print(json.dumps({"valid": True, "counts": report["counts"], "occurrence_digest": report["selection"]["occurrence_ids_sha256"]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
