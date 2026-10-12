"""Build the CA-P-2048 bare ``Atom/Claim`` mapping supplement.

This is a one-off, preview-first evidence artifact.  It neither changes
current sources nor treats the candidate mapping as an executable migration.
"""
from __future__ import annotations

import argparse
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[5]
STAGE2 = ".caprmedio_caprmedio/_projection/core-entity-review/stage2"
LEDGER_REL = f"{STAGE2}/current-subjects.mapping-ledger.json"
DECISION_REL = f"{STAGE2}/operator.subject-decisions.2026-10-11.json"
CANDIDATE_REL = ".caprmedio_caprmedio/_projection/core-entity-review/presentation/operator.entity-graph.candidate.json"
CONTRACT_REL = f"{STAGE2}/current-subjects.contract.md"
REVIEW_CONTRACT_REL = f"{STAGE2}/current-subjects.review.contract.md"
SUPPLEMENT_CONTRACT_REL = f"{STAGE2}/current-subjects.supplements.contract.md"
OUTPUT_REL = f"{STAGE2}/supplements/substance.review.json"

EXPECTED_LEDGER_SHA256 = "4d094ce89390e31290ce6ae7248cde78701376085bbe3078e33a228055e2eb39"
EXPECTED_DECISION_SHA256 = "743fd63f5c8c8ea19b0f1ffae1fa1d89d81504308c7f5345e2809fe7cef15ffc"
EXPECTED_CANDIDATE_SHA256 = "99e7710f5ef83df2b1f3ec1ef4142547655e63bef7415266c5521380da7fa99b"
OLD_VALUE = "Atom/Claim"
TARGET_VALUE = "Atom.Substance"
EXPECTED_OCCURRENCES = 143
EXPECTED_SOURCES = 142
EXPECTED_CHANGED = 137
EXPECTED_ALIGNED = 6

CANDIDATE_BASIS = [
    {
        "pointer": "/dependent_entities/compact_examples/3",
        "reason": "The candidate's dependent-entity compact example is the exact owner-and-field notation Atom.Substance.",
    },
    {
        "pointer": "/content_direction/umbrella",
        "reason": "The candidate names Substance as the content umbrella.",
    },
    {
        "pointer": "/content_direction/role_labels/RMED",
        "reason": "The candidate describes Claim as the RMED role label, not a separate dependent identity or Substance allowed value.",
    },
]
OPERATOR_DECISION_BASIS = [
    {
        "pointer": "/decisions/substance/exact_legacy_field_candidate/Atom~1Claim",
        "reason": "The latest actual Operator decision supplies the exact legacy-field candidate Atom/Claim -> Atom.Substance.",
    },
    {
        "pointer": "/decisions/substance/preserve_owning_atom_content_role",
        "reason": "The decision keeps the owning Atom Content Role separate from the shared Substance field.",
    },
    {
        "pointer": "/decisions/substance/compound_path_boundary",
        "reason": "The decision excludes compound paths and other components from this narrowly mechanical supplement.",
    },
]


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def resolve_relative(root: Path, relative: str) -> Path:
    path = (root / relative).resolve()
    require(path.is_relative_to(root.resolve()), f"path escapes repository: {relative}")
    return path


def read_bytes(root: Path, relative: str) -> bytes:
    path = resolve_relative(root, relative)
    require(path.is_file(), f"missing pinned input: {relative}")
    return path.read_bytes()


def read_json(root: Path, relative: str, expected_sha256: str | None = None) -> tuple[dict[str, Any], str]:
    raw = read_bytes(root, relative)
    actual = digest(raw)
    if expected_sha256 is not None:
        require(actual == expected_sha256, f"stale pinned input: {relative}")
    value = json.loads(raw)
    require(isinstance(value, dict), f"JSON object required: {relative}")
    return value, actual


def pointer_value(document: Any, pointer: str) -> Any:
    require(isinstance(pointer, str) and pointer.startswith("/"), "exact JSON pointer required")
    value = document
    for part in pointer[1:].split("/"):
        part = part.replace("~1", "/").replace("~0", "~")
        if isinstance(value, list):
            require(part.isdigit() and int(part) < len(value), f"missing list pointer: {pointer}")
            value = value[int(part)]
        else:
            require(isinstance(value, dict) and part in value, f"missing object pointer: {pointer}")
            value = value[part]
    return value


def current_body_evidence(root: Path, row: dict[str, Any]) -> dict[str, Any]:
    relative = row["source_path"]
    raw = read_bytes(root, relative)
    require(digest(raw) == row["source_sha256"], f"stale current source: {relative}")
    lines = raw.splitlines(keepends=True)
    require(bool(lines) and lines[0].strip() == b"---", f"frontmatter start required: {relative}")
    closing = next((number for number, line in enumerate(lines[1:], start=2) if line.strip() == b"---"), None)
    require(closing is not None and closing < len(lines), f"nonempty Main Content required: {relative}")
    start_line = closing + 1
    body = b"".join(lines[start_line - 1:])
    require(body.strip(), f"nonempty Main Content required: {relative}")
    return {
        "path": relative,
        "sha256": row["source_sha256"],
        "start_line": start_line,
        "end_line": len(lines),
        "span_sha256": digest(body),
        "reason": "Full current Main Content is the source-specific meaning evidence for the exact bare Atom/Claim Subject occurrence.",
    }


def input_pins(root: Path) -> list[dict[str, str]]:
    return [
        {"path": CANDIDATE_REL, "sha256": digest(read_bytes(root, CANDIDATE_REL))},
        {"path": DECISION_REL, "sha256": digest(read_bytes(root, DECISION_REL))},
        {"path": CONTRACT_REL, "sha256": digest(read_bytes(root, CONTRACT_REL))},
        {"path": REVIEW_CONTRACT_REL, "sha256": digest(read_bytes(root, REVIEW_CONTRACT_REL))},
        {"path": SUPPLEMENT_CONTRACT_REL, "sha256": digest(read_bytes(root, SUPPLEMENT_CONTRACT_REL))},
    ]


def selected_rows(ledger: dict[str, Any]) -> list[dict[str, Any]]:
    rows = ledger.get("occurrences")
    require(isinstance(rows, list), "ledger occurrence list required")
    selected = [row for row in rows if isinstance(row, dict) and row.get("old_value") == OLD_VALUE]
    require(len(selected) == EXPECTED_OCCURRENCES, "exact bare Atom/Claim ledger coverage changed")
    require(len({row.get("occurrence_id") for row in selected}) == EXPECTED_OCCURRENCES, "duplicate bare Atom/Claim ledger ID")
    require(len({row.get("source_path") for row in selected}) == EXPECTED_SOURCES, "bare Atom/Claim source coverage changed")
    return sorted(selected, key=lambda row: row["occurrence_id"])


def selection_digest(rows: list[dict[str, Any]]) -> str:
    return digest("\n".join(row["occurrence_id"] for row in rows).encode("utf-8"))


def validate_authority_inputs(root: Path) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], str]:
    ledger, ledger_sha256 = read_json(root, LEDGER_REL, EXPECTED_LEDGER_SHA256)
    decision, _ = read_json(root, DECISION_REL, EXPECTED_DECISION_SHA256)
    candidate, _ = read_json(root, CANDIDATE_REL, EXPECTED_CANDIDATE_SHA256)
    require(pointer_value(candidate, "/dependent_entities/compact_examples/3") == TARGET_VALUE, "candidate Atom.Substance basis changed")
    require(pointer_value(candidate, "/content_direction/umbrella") == "Substance", "candidate Substance umbrella changed")
    require(pointer_value(candidate, "/content_direction/role_labels/RMED") == "Claim", "candidate Claim role-label basis changed")
    require(pointer_value(decision, "/decisions/substance/exact_legacy_field_candidate/Atom~1Claim") == TARGET_VALUE, "Operator exact legacy decision changed")
    require(pointer_value(decision, "/decisions/substance/preserve_owning_atom_content_role") is True, "Operator content-role boundary changed")
    require(isinstance(pointer_value(decision, "/decisions/substance/compound_path_boundary"), str), "Operator compound boundary missing")
    return ledger, decision, candidate, ledger_sha256


def supplement_row(root: Path, baseline: dict[str, Any]) -> dict[str, Any]:
    evidence = current_body_evidence(root, baseline)
    return {
        "batch_id": baseline["batch_id"],
        "candidate_basis": CANDIDATE_BASIS,
        "confidence": 0.99,
        "decision": "proposed",
        "evidence": [evidence],
        "executable": False,
        "field": baseline["field"],
        "index": baseline["index"],
        "occurrence_id": baseline["occurrence_id"],
        "old_value": baseline["old_value"],
        "originating_review_path": baseline["originating_review_path"],
        "originating_review_sha256": baseline["originating_review_sha256"],
        "preserved_distinctions": [
            "Atom remains the owner; Claim is a role-specific label for the shared Substance field, not a separate dependent identity.",
            "No Atom.Substance:Claim allowed-value binding, source-body rename, or native grammar adoption is inferred.",
            "Atom Content Role and every compound Claim-qualified path remain distinct and outside this supplement.",
        ],
        "proposed_value": TARGET_VALUE,
        "quarantined": baseline["quarantined"],
        "question": None,
        "reason": "The full current Main Content supplies the source-specific context. The latest actual Operator decision explicitly maps the exact bare legacy field Atom/Claim to Atom.Substance while retaining the owning Atom Content Role; the candidate independently names Substance as the umbrella and Claim as its RMED role label.",
        "source_atom_id": baseline["source_atom_id"],
        "source_path": baseline["source_path"],
        "source_sha256": baseline["source_sha256"],
        "source_version": baseline["source_version"],
        "task_id": baseline["task_id"],
        "baseline_decision": baseline["decision"],
        "baseline_proposed_value": baseline["proposed_value"],
    }


def build_supplement(root: Path = ROOT) -> dict[str, Any]:
    ledger, _decision, _candidate, ledger_sha256 = validate_authority_inputs(root)
    rows = selected_rows(ledger)
    occurrence_rows = [supplement_row(root, row) for row in rows]
    changed = sum(row["baseline_proposed_value"] != TARGET_VALUE for row in occurrence_rows)
    aligned = sum(row["baseline_proposed_value"] == TARGET_VALUE for row in occurrence_rows)
    require((changed, aligned) == (EXPECTED_CHANGED, EXPECTED_ALIGNED), "baseline decision counts changed")
    document = {
        "schema_version": 1,
        "task_id": "CA-P-2048",
        "non_authoritative": True,
        "source_migration": "not_performed",
        "native_admission": "not_performed",
        "base_ledger": {"path": LEDGER_REL, "sha256": ledger_sha256},
        "evidence_pins": input_pins(root),
        "operator_decision_basis": OPERATOR_DECISION_BASIS,
        "selection": {
            "old_value": OLD_VALUE,
            "target_value": TARGET_VALUE,
            "occurrence_count": len(occurrence_rows),
            "source_count": len({row["source_path"] for row in occurrence_rows}),
            "changed_from_baseline": changed,
            "already_aligned": aligned,
            "occurrence_id_sha256": selection_digest(rows),
            "excludes": [
                "Every compound Claim-qualified path, including Scope, Target, Scope Unit, Type, Content Role, Carrier, and other components.",
                "All non-Atom/Claim legacy values, including other Claim-bearing strings.",
            ],
        },
        "occurrences": occurrence_rows,
    }
    validate_supplement(document, root=root, ledger=ledger)
    return document


def validate_supplement(document: dict[str, Any], *, root: Path = ROOT, ledger: dict[str, Any] | None = None) -> None:
    require(document.get("schema_version") == 1, "supplement schema version")
    require(document.get("task_id") == "CA-P-2048", "supplement Task ID")
    require(document.get("non_authoritative") is True, "supplement remains non-authoritative")
    require(document.get("source_migration") == document.get("native_admission") == "not_performed", "no migration/admission")
    if ledger is None:
        ledger, _decision, _candidate, _ledger_sha = validate_authority_inputs(root)
    expected_rows = selected_rows(ledger)
    expected_by_id = {row["occurrence_id"]: row for row in expected_rows}
    require(document.get("base_ledger") == {"path": LEDGER_REL, "sha256": EXPECTED_LEDGER_SHA256}, "stale base ledger pin")
    require(document.get("evidence_pins") == input_pins(root), "stale or incomplete input pins")
    decision, _ = read_json(root, DECISION_REL, EXPECTED_DECISION_SHA256)
    candidate, _ = read_json(root, CANDIDATE_REL, EXPECTED_CANDIDATE_SHA256)
    require(document.get("operator_decision_basis") == OPERATOR_DECISION_BASIS, "exact Operator basis required")
    for item in document["operator_decision_basis"]:
        pointer_value(decision, item["pointer"])
    selection = document.get("selection")
    require(isinstance(selection, dict), "selection required")
    require(selection.get("old_value") == OLD_VALUE and selection.get("target_value") == TARGET_VALUE, "exact bare mapping selection")
    require(selection.get("occurrence_count") == EXPECTED_OCCURRENCES, "selection occurrence count")
    require(selection.get("source_count") == EXPECTED_SOURCES, "selection source count")
    require(selection.get("changed_from_baseline") == EXPECTED_CHANGED and selection.get("already_aligned") == EXPECTED_ALIGNED, "selection baseline counts")
    require(selection.get("occurrence_id_sha256") == selection_digest(expected_rows), "selection occurrence IDs")
    rows = document.get("occurrences")
    require(isinstance(rows, list) and len(rows) == EXPECTED_OCCURRENCES, "exact supplement occurrence coverage")
    require(Counter(row.get("occurrence_id") for row in rows) == Counter(expected_by_id.keys()), "missing or extra supplement occurrence")
    changed = aligned = 0
    source_cache: dict[str, dict[str, Any]] = {}
    for row in rows:
        require(isinstance(row, dict), "supplement occurrence object")
        baseline = expected_by_id[row["occurrence_id"]]
        for key in (
            "batch_id", "field", "index", "occurrence_id", "old_value", "originating_review_path",
            "originating_review_sha256", "quarantined", "source_atom_id", "source_path", "source_sha256",
            "source_version", "task_id",
        ):
            require(row.get(key) == baseline.get(key), f"baseline origin changed: {key}")
        require(row["old_value"] == OLD_VALUE, "compound or non-bare Claim mapping is excluded")
        require(row.get("baseline_decision") == baseline["decision"], "baseline decision copy")
        require(row.get("baseline_proposed_value") == baseline["proposed_value"], "baseline value copy")
        require(row.get("decision") == "proposed" and row.get("proposed_value") == TARGET_VALUE, "exact Atom.Substance proposal")
        require(row.get("confidence") == 0.99, "confidence is fixed by exact Operator rule")
        require(row.get("question") is None and row.get("executable") is False, "candidate-only no-question supplement")
        require(row.get("candidate_basis") == CANDIDATE_BASIS, "exact candidate basis")
        for item in row["candidate_basis"]:
            pointer_value(candidate, item["pointer"])
        require(isinstance(row.get("reason"), str) and row["reason"].strip(), "specific mapping reason")
        require(isinstance(row.get("preserved_distinctions"), list) and len(row["preserved_distinctions"]) == 3, "preserved boundaries")
        evidence = row.get("evidence")
        require(isinstance(evidence, list) and len(evidence) == 1, "one owning current evidence span")
        if row["source_path"] not in source_cache:
            source_cache[row["source_path"]] = current_body_evidence(root, baseline)
        require(evidence[0] == source_cache[row["source_path"]], "exact source-specific Main Content span")
        if row["baseline_proposed_value"] == TARGET_VALUE:
            aligned += 1
        else:
            changed += 1
    require((changed, aligned) == (EXPECTED_CHANGED, EXPECTED_ALIGNED), "baseline aligned/change split")
    require(len(source_cache) == EXPECTED_SOURCES, "exact current source coverage")


def serialized(document: dict[str, Any]) -> bytes:
    return (json.dumps(document, indent=2, sort_keys=True) + "\n").encode("utf-8")


def output_path(root: Path, supplied: str) -> Path:
    path = Path(supplied)
    if not path.is_absolute():
        path = root / path
    path = path.resolve()
    require(path.is_relative_to(root.resolve()), "output must remain inside the repository")
    return path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Create the supplement after the preview has been reviewed.")
    parser.add_argument("--output", default=OUTPUT_REL, help="Repository-relative create-only supplement path.")
    args = parser.parse_args()
    try:
        document = build_supplement()
        validate_supplement(document)
        raw = serialized(document)
        target = output_path(ROOT, args.output)
        result = {
            "mode": "write" if args.write else "preview",
            "output": str(target.relative_to(ROOT)),
            "sha256": digest(raw),
            "occurrences": EXPECTED_OCCURRENCES,
            "sources": EXPECTED_SOURCES,
            "changed_from_baseline": EXPECTED_CHANGED,
            "already_aligned": EXPECTED_ALIGNED,
        }
        if args.write:
            require(not target.exists(), f"create-only output already exists: {target.relative_to(ROOT)}")
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(raw)
        print(json.dumps(result, sort_keys=True))
    except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError) as error:
        print(json.dumps({"outcome": "FAIL", "reason": str(error)}, sort_keys=True))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
