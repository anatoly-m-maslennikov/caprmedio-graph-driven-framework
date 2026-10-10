"""Read-only structural verification for CA-P-2060 mapping supplements.

This one-off checker validates frozen-ledger ownership, byte pins and evidence
spans.  It deliberately does not decide whether a proposed Subject has the
right meaning; that remains independent semantic review.
"""
from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[5]
STAGE = ".caprmedio_caprmedio/_projection/core-entity-review/stage2"
LEDGER_REL = f"{STAGE}/current-subjects.mapping-ledger.json"
OWNERSHIP_REL = f"{STAGE}/current-subjects.research-ownership.json"
CANDIDATE_REL = ".caprmedio_caprmedio/_projection/core-entity-review/presentation/operator.entity-graph.candidate.json"
SUPPLEMENT_CONTRACT_REL = f"{STAGE}/current-subjects.supplements.contract.md"
DECISION_REL = f"{STAGE}/operator.subject-decisions.2026-10-11.json"
BASE_LEDGER_SHA = "4d094ce89390e31290ce6ae7248cde78701376085bbe3078e33a228055e2eb39"


class VerificationError(AssertionError):
    """A deterministic evidence/coverage violation."""


@dataclass(frozen=True)
class ReportSpec:
    name: str
    task_id: str
    selection: str
    group: str | None = None

    @property
    def path(self) -> str:
        return f"{STAGE}/supplements/{self.name}.review.json"


SPECS = (
    ReportSpec("history", "CA-P-2050", "research", "history"),
    ReportSpec("content_roles", "CA-P-2051", "research", "content_roles"),
    ReportSpec("operations", "CA-P-2052", "research", "operations"),
    ReportSpec("relations_subjects", "CA-P-2053", "research", "relations_subjects"),
    ReportSpec("carriers", "CA-P-2054", "research", "carriers"),
    ReportSpec("methodology", "CA-P-2055", "research", "methodology"),
    ReportSpec("other_fields", "CA-P-2056", "research", "other_fields"),
    ReportSpec("substance", "CA-P-2048", "substance"),
    ReportSpec("actor_types", "CA-P-2058", "actor"),
)


# These are the only origin layouts emitted by the nine existing reports.  A
# permissive generic "find any matching key" rule would mask lost provenance.
ORIGIN_LAYOUTS = {
    "history": "direct",
    "content_roles": "review_only",
    "operations": "originating",
    "relations_subjects": "originating",
    "carriers": "direct",
    "methodology": "baseline_task",
    "other_fields": "baseline_task",
    "substance": "direct",
    "actor_types": "baseline_origin",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def id_digest(ids: Iterable[str]) -> str:
    return digest(json.dumps(sorted(ids), ensure_ascii=False, separators=(",", ":")).encode())


def relative_file(root: Path, relative: Any, label: str) -> Path:
    require(isinstance(relative, str) and relative and not Path(relative).is_absolute(), f"{label}: relative path")
    root = root.resolve()
    path = (root / relative).resolve()
    require(path.is_relative_to(root), f"{label}: path escapes root")
    require(path.is_file() and not path.is_symlink(), f"{label}: regular file")
    return path


def read_json(root: Path, relative: str, label: str) -> dict[str, Any]:
    try:
        value = json.loads(relative_file(root, relative, label).read_bytes())
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise VerificationError(f"{label}: JSON object") from error
    require(isinstance(value, dict), f"{label}: JSON object")
    return value


def pin_bytes(root: Path, pin: Any, label: str) -> bytes:
    require(isinstance(pin, dict), f"{label}: pin object")
    path = relative_file(root, pin.get("path"), label)
    raw = path.read_bytes()
    require(isinstance(pin.get("sha256"), str) and digest(raw) == pin["sha256"], f"{label}: current SHA-256")
    return raw


def normalize_pins(value: Any, label: str) -> list[dict[str, Any]]:
    if isinstance(value, list):
        pins = value
    elif isinstance(value, dict):
        # The named maps in methodology/other_fields are an explicit supported
        # report form; nested lists or arbitrary values are not.
        pins = list(value.values())
    else:
        raise VerificationError(f"{label}: list or named pin map")
    require(all(isinstance(pin, dict) for pin in pins), f"{label}: pin objects")
    return pins


def pointer(document: Any, value: Any, label: str) -> Any:
    require(isinstance(value, str), f"{label}: JSON pointer string")
    value = value.removeprefix("#")
    require(value.startswith("/") and value != "/", f"{label}: non-root JSON pointer")
    current = document
    for part in value[1:].split("/"):
        part = part.replace("~1", "/").replace("~0", "~")
        if isinstance(current, list):
            require(part.isdigit() and int(part) < len(current), f"{label}: list pointer")
            current = current[int(part)]
        else:
            require(isinstance(current, dict) and part in current, f"{label}: object pointer")
            current = current[part]
    return current


def body_start(raw: bytes, label: str) -> int:
    lines = raw.splitlines(keepends=True)
    require(lines and lines[0].strip() == b"---", f"{label}: frontmatter start")
    for index, line in enumerate(lines[1:], 1):
        if line.strip() == b"---":
            return index + 2  # one-based first body line
    raise VerificationError(f"{label}: frontmatter end")


def validate_span(root: Path, span: Any, label: str, *, require_body: bool) -> tuple[str, str]:
    require(isinstance(span, dict), f"{label}: evidence object")
    raw = pin_bytes(root, span, label)
    lines = raw.splitlines(keepends=True)
    start, end = span.get("start_line"), span.get("end_line")
    require(type(start) is int and type(end) is int and 1 <= start <= end <= len(lines), f"{label}: line range")
    require(isinstance(span.get("span_sha256"), str) and digest(b"".join(lines[start - 1 : end])) == span["span_sha256"], f"{label}: span SHA-256")
    require(isinstance(span.get("reason"), str) and span["reason"].strip(), f"{label}: span reason")
    if require_body:
        require(start >= body_start(raw, label), f"{label}: content rather than metadata span")
    return span["path"], span["sha256"]


def expected_rows(ledger: dict[str, Any], ownership: dict[str, Any], spec: ReportSpec) -> list[dict[str, Any]]:
    rows = ledger.get("occurrences")
    require(isinstance(rows, list) and all(isinstance(row, dict) for row in rows), "ledger occurrence rows")
    if spec.selection == "substance":
        return [row for row in rows if row.get("old_value") == "Atom/Claim"]
    if spec.selection == "actor":
        return [
            row
            for row in rows
            if row.get("decision") == "proposed" and row.get("proposed_value") in {"Actor/Operator", "Actor/AI Agent"}
        ]
    require(spec.group is not None, "research group")
    task = next((item for item in ownership.get("research_tasks", []) if item.get("task_id") == spec.task_id and item.get("group") == spec.group), None)
    require(isinstance(task, dict), f"{spec.name}: ownership task")
    values = task.get("old_values")
    require(isinstance(values, list) and all(isinstance(item, str) for item in values), f"{spec.name}: owned old values")
    result = [row for row in rows if row.get("decision") == "unresolved" and row.get("old_value") != "Atom/Claim" and row.get("old_value") in set(values)]
    require(len(result) == task.get("occurrences"), f"{spec.name}: owned occurrence count")
    require(len({row["source_path"] for row in result}) == task.get("sources"), f"{spec.name}: owned source count")
    require(id_digest(row["occurrence_id"] for row in result) == task.get("occurrence_ids_sha256"), f"{spec.name}: owned occurrence digest")
    return result


def validate_origin(row: dict[str, Any], baseline: dict[str, Any], spec: ReportSpec, label: str) -> None:
    expected = {
        "batch_id": baseline["batch_id"],
        "task_id": baseline["task_id"],
        "originating_review_path": baseline["originating_review_path"],
        "originating_review_sha256": baseline["originating_review_sha256"],
    }
    layout = ORIGIN_LAYOUTS[spec.name]
    if layout == "direct":
        actual = {key: row.get(key) for key in expected}
    elif layout == "originating":
        actual = {
            "batch_id": row.get("originating_batch_id"),
            "task_id": row.get("originating_task_id"),
            "originating_review_path": row.get("originating_review_path"),
            "originating_review_sha256": row.get("originating_review_sha256"),
        }
    elif layout == "baseline_task":
        actual = {
            "batch_id": row.get("batch_id"),
            "task_id": row.get("baseline_task_id"),
            "originating_review_path": row.get("originating_review_path"),
            "originating_review_sha256": row.get("originating_review_sha256"),
        }
    elif layout == "baseline_origin":
        actual = row.get("baseline_origin")
    elif layout == "review_only":
        actual = {
            "batch_id": expected["batch_id"],
            "task_id": expected["task_id"],
            "originating_review_path": row.get("originating_review_path"),
            "originating_review_sha256": row.get("originating_review_sha256"),
        }
    else:  # defensive: this is a fixed internal mapping, never user input
        raise VerificationError(f"{label}: unsupported origin layout")
    require(isinstance(actual, dict) and actual == expected, f"{label}: exact baseline origin")


def validate_report(
    root: Path,
    ledger: dict[str, Any],
    ownership: dict[str, Any],
    candidate: dict[str, Any],
    decision: dict[str, Any],
    spec: ReportSpec,
) -> dict[str, Any]:
    report = read_json(root, spec.path, f"{spec.name} report")
    label = spec.name
    require(report.get("schema_version") == 1 and report.get("task_id") == spec.task_id, f"{label}: report identity")
    require(report.get("non_authoritative") is True, f"{label}: non-authoritative")
    require(report.get("source_migration") == report.get("native_admission") == "not_performed", f"{label}: no source/native effects")
    base = report.get("base_ledger")
    require(isinstance(base, dict) and base.get("path") == LEDGER_REL and base.get("sha256") == BASE_LEDGER_SHA, f"{label}: frozen baseline pin")

    pins = normalize_pins(report.get("evidence_pins"), f"{label}: evidence pins")
    paths: set[str] = set()
    for pin in pins:
        require(pin.get("path") not in paths, f"{label}: unique evidence pins")
        paths.add(pin.get("path"))
        pin_bytes(root, pin, f"{label}: evidence pin")
    require(CANDIDATE_REL in paths and SUPPLEMENT_CONTRACT_REL in paths, f"{label}: candidate and supplement contract pins")

    # Explicit optional source-pin lists are also byte-checked.  A report may
    # use row source SHA/evidence spans instead, which is an observed format.
    for field in ("source_pins", "support_source_pins"):
        if field in report:
            for pin in normalize_pins(report[field], f"{label}: {field}"):
                pin_bytes(root, pin, f"{label}: {field}")

    basis = report.get("operator_decision_basis")
    if basis is not None:
        require(DECISION_REL in paths, f"{label}: actual decision pin")
        require(isinstance(basis, list) and basis, f"{label}: actual decision references")
        for item in basis:
            require(isinstance(item, dict) and isinstance(item.get("reason"), str) and item["reason"].strip(), f"{label}: decision basis reason")
            pointer(decision, item.get("pointer"), f"{label}: decision basis")
    if spec.selection == "substance":
        require(basis is not None, f"{label}: substance decision references")

    expected = expected_rows(ledger, ownership, spec)
    rows = report.get("occurrences")
    require(isinstance(rows, list) and all(isinstance(row, dict) for row in rows), f"{label}: occurrence rows")
    expected_by_id = {row["occurrence_id"]: row for row in expected}
    require(Counter(row.get("occurrence_id") for row in rows) == Counter(expected_by_id.keys()), f"{label}: exact owned occurrence coverage")

    decisions: Counter[str] = Counter()
    for index, row in enumerate(rows):
        occurrence_id = row["occurrence_id"]
        baseline = expected_by_id[occurrence_id]
        row_label = f"{label}:{occurrence_id}"
        for key in ("occurrence_id", "source_path", "source_atom_id", "source_version", "source_sha256", "field", "index", "old_value", "quarantined"):
            require(row.get(key) == baseline.get(key), f"{row_label}: copied {key}")
        validate_origin(row, baseline, spec, row_label)
        require(row.get("baseline_decision") == baseline.get("decision") and row.get("baseline_proposed_value") == baseline.get("proposed_value"), f"{row_label}: copied baseline decision")
        source_raw = relative_file(root, row["source_path"], f"{row_label}: current source").read_bytes()
        require(digest(source_raw) == row["source_sha256"], f"{row_label}: current source SHA-256")

        decision_value = row.get("decision")
        confidence = row.get("confidence")
        proposed = row.get("proposed_value")
        require(decision_value in {"unchanged", "proposed", "unresolved"}, f"{row_label}: decision")
        require(type(confidence) in (int, float) and 0 <= confidence <= 1, f"{row_label}: confidence")
        require(row.get("executable") is False, f"{row_label}: non-executable")
        require(isinstance(row.get("reason"), str) and row["reason"].strip(), f"{row_label}: reason")
        require(row.get("question") is None or isinstance(row["question"], str), f"{row_label}: question")
        distinctions = row.get("preserved_distinctions")
        require(isinstance(distinctions, list) and all(isinstance(item, str) and item for item in distinctions), f"{row_label}: preserved distinctions")
        if decision_value == "unresolved" or confidence < 0.90:
            require(decision_value == "unresolved" and proposed is None, f"{row_label}: unresolved confidence/value")
        elif decision_value == "unchanged":
            require(proposed == baseline["old_value"], f"{row_label}: unchanged value")
        else:
            require(isinstance(proposed, str) and proposed.strip() and proposed != baseline["old_value"], f"{row_label}: proposed value")

        candidate_basis = row.get("candidate_basis", [])
        require(isinstance(candidate_basis, list), f"{row_label}: candidate basis list")
        if decision_value == "proposed":
            require(candidate_basis, f"{row_label}: proposal candidate basis")
        for item in candidate_basis:
            require(isinstance(item, dict) and isinstance(item.get("reason"), str) and item["reason"].strip(), f"{row_label}: candidate basis reason")
            pointer(candidate, item.get("pointer"), f"{row_label}: candidate basis")

        evidence = row.get("evidence")
        require(isinstance(evidence, list) and evidence, f"{row_label}: evidence")
        own_spans = 0
        for evidence_index, span in enumerate(evidence):
            path, span_sha = validate_span(root, span, f"{row_label}: evidence {evidence_index}", require_body=span.get("path") == row["source_path"])
            if path == row["source_path"] and span_sha == row["source_sha256"]:
                own_spans += 1
        require(own_spans > 0, f"{row_label}: owning current evidence")
        decisions[decision_value] += 1

    # Content-role reports alone retain source-review objects.  Verify those
    # byte spans without forcing that extra representation on other reports.
    if "source_reviews" in report:
        source_reviews = report["source_reviews"]
        require(isinstance(source_reviews, list), f"{label}: source review list")
        for source in source_reviews:
            require(isinstance(source, dict), f"{label}: source review object")
            read = source.get("main_content_read")
            if isinstance(read, dict):
                validate_span(root, read, f"{label}: source read", require_body=True)
            else:
                require(read is True, f"{label}: source content read")
    return {"report": spec.path, "task_id": spec.task_id, "occurrences": len(rows), "decisions": dict(sorted(decisions.items()))}


def verify_supplements(root: Path = ROOT, specifications: Iterable[ReportSpec] = SPECS) -> dict[str, Any]:
    """Validate the fixed supplement set.  Raises VerificationError on any defect."""
    root = root.resolve()
    ledger_path = relative_file(root, LEDGER_REL, "baseline ledger")
    require(digest(ledger_path.read_bytes()) == BASE_LEDGER_SHA, "baseline ledger: frozen SHA-256")
    ledger = read_json(root, LEDGER_REL, "baseline ledger")
    ownership = read_json(root, OWNERSHIP_REL, "research ownership")
    require(ownership.get("base_ledger", {}).get("sha256") == BASE_LEDGER_SHA, "research ownership: frozen baseline")
    candidate = read_json(root, CANDIDATE_REL, "candidate")
    decision = read_json(root, DECISION_REL, "actual operator decision")
    summaries = [validate_report(root, ledger, ownership, candidate, decision, spec) for spec in specifications]
    total = sum(item["occurrences"] for item in summaries)
    return {
        "outcome": "PASS",
        "reports": len(summaries),
        "occurrences": total,
        "report_summaries": summaries,
        "scope": "structural pins, coverage, provenance and evidence only; not semantic acceptance",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="repository root (read-only)")
    args = parser.parse_args()
    try:
        print(json.dumps(verify_supplements(args.root), sort_keys=True))
    except (VerificationError, OSError, ValueError, KeyError, TypeError) as error:
        print(json.dumps({"outcome": "FAIL", "reason": str(error)}, sort_keys=True))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
