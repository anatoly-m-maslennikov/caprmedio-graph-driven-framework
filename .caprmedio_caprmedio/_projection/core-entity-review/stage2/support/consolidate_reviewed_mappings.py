#!/usr/bin/env python3
"""Create-only CA-P-2086 current-frontier working Subject mapping drafts."""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys
import tomllib
from typing import Any, Iterable

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from inventory_current_subjects import (  # strict Core parser and frontier rules
    ATOM_ID,
    FILENAME_ATOM_ID,
    ROLE_DIRS,
    ROLES,
    SUBJECT_FIELDS,
    UPDATED_AT,
    CarrierError,
    ROOT,
    checked_relative_path,
    directory_role,
    parse_carrier,
    source_files,
    updated_at,
)

STAGE = Path(".caprmedio_caprmedio/_projection/core-entity-review/stage2")
BASELINE = STAGE / "current-subjects.mapping-ledger.json"
DRIFT = STAGE / "current-grammar-source-drift.json"
CONTRACTS = (
    STAGE / "current-subjects.contract.md",
    STAGE / "current-subjects.review.contract.md",
    STAGE / "current-subjects.supplements.contract.md",
    STAGE / "working-ledger.contract.md",
)
WORKING = STAGE / "working-ledger"
LEDGER = WORKING / "working-mapping-ledger.json"
FRONTIER = WORKING / "source-frontier.json"
DIAGNOSTICS = WORKING / "diagnostics.json"
STRUCTURE = Path(".caprmedio_caprmedio/project_structure.toml")

# Each record is consumed only when the recorded independently accepted output
# pin equals the actual current file.  CA-P-2058 is validation-only.
LAYER_SPECS = (
    ("CA-P-2048", STAGE / "supplements/substance.review.json", "substance"),
    ("CA-P-2072", STAGE / "semantic-reviews/task-2072.review.json", "semantic"),
    ("CA-P-2073", STAGE / "semantic-reviews/task-2073.review.json", "semantic"),
    ("CA-P-2074", STAGE / "semantic-reviews/task-2074.review.json", "semantic"),
    ("CA-P-2075", STAGE / "semantic-reviews/task-2075.review.json", "semantic"),
    ("CA-P-2076", STAGE / "semantic-reviews/task-2076.review.json", "semantic"),
    ("CA-P-2078", STAGE / "semantic-reviews/task-2078.research.json", "research"),
    ("CA-P-2079", STAGE / "semantic-reviews/task-2079.research.json", "research"),
    ("CA-P-2080", STAGE / "semantic-reviews/task-2080.research.json", "research"),
    ("CA-P-2082", STAGE / "semantic-reviews/task-2082.research.json", "research"),
    ("CA-P-2083", STAGE / "semantic-reviews/task-2083.research.json", "research"),
    ("CA-P-2084", STAGE / "semantic-reviews/task-2084.research.json", "research"),
    ("CA-P-2085", STAGE / "semantic-reviews/task-2085.research.json", "research"),
)
ACTOR_SUBSET = STAGE / "semantic-reviews/task-2058.accepted-subset.json"


def fail(message: str) -> None:
    raise ValueError(message)


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def pin(relative: Path) -> dict[str, str]:
    path = checked_relative_path(relative, "input")
    if not path.is_file() or path.is_symlink():
        fail(f"required regular input missing: {relative}")
    return {"path": relative.as_posix(), "sha256": sha(path.read_bytes())}


def read_json(relative: Path) -> dict[str, Any]:
    path = checked_relative_path(relative, "JSON input")
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        raise ValueError(f"invalid JSON input: {relative}") from error
    if not isinstance(value, dict):
        fail(f"JSON object required: {relative}")
    return value


def json_bytes(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=True, indent=2, sort_keys=True).encode("utf-8") + b"\n"


def body_evidence(path: Path, raw: bytes) -> list[dict[str, Any]]:
    lines = raw.splitlines(keepends=True)
    separators = [index for index, line in enumerate(lines) if line.rstrip(b"\r\n") == b"---"]
    if len(separators) < 2:
        fail(f"missing frontmatter boundary: {rel(path)}")
    start = separators[1] + 2
    body = b"".join(lines[separators[1] + 1 :])
    return [{
        "path": rel(path), "sha256": sha(raw), "start_line": start,
        "end_line": len(lines), "span_sha256": sha(body),
        "reason": "Current full Main Content pin for required semantic recheck.",
    }]


def current_frontier() -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]], dict[str, str]]:
    structure_path = checked_relative_path(STRUCTURE, "authoritative Structure")
    try:
        structure = tomllib.loads(structure_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, tomllib.TOMLDecodeError) as error:
        raise ValueError("authoritative Structure is unreadable") from error
    units = structure.get("scope_units") if isinstance(structure, dict) else None
    matches = [unit for unit in units or [] if isinstance(unit, dict) and unit.get("scope_unit_name") == "CORE_META_MODEL"]
    if len(matches) != 1 or not isinstance(matches[0].get("authority_path"), str):
        fail("CORE_META_MODEL authority path missing or ambiguous")
    source_root = checked_relative_path(Path(matches[0]["authority_path"]), "CORE_META_MODEL authority")
    if not source_root.is_dir() or source_root.is_symlink():
        fail("CORE_META_MODEL authority root is unsafe")

    sources: list[dict[str, Any]] = []
    occurrences: list[dict[str, Any]] = []
    excluded: list[dict[str, Any]] = []
    for path in source_files(source_root):
        relative = rel(path)
        if "archive" in path.relative_to(source_root).parts:
            excluded.append({"relative_path": relative, "reason": "archived_lifecycle_copy"})
            continue
        raw = path.read_bytes()
        try:
            parsed = parse_carrier(raw, path)
            metadata = parsed.metadata
        except CarrierError as error:
            filename = FILENAME_ATOM_ID.match(path.stem)
            if filename is None:
                excluded.append({"relative_path": relative, "reason": "strict_parse_error", "code": error.code})
                continue
            role = next((name for name, code in ROLES.items() if code == filename.group(2)), None)
            if role is None:
                excluded.append({"relative_path": relative, "reason": "strict_parse_error", "code": error.code})
                continue
            sources.append({"relative_path": relative, "full_file_sha256": sha(raw), "atom_id": None,
                            "version": None, "role": role, "owner": None, "status": None,
                            "quarantined": True, "findings": [f"strict_parse_error:{error.code}"]})
            continue
        role = metadata.get("content_role")
        owner = metadata.get("current_scope_unit")
        status = metadata.get("status")
        if owner != "CORE_META_MODEL" or status != "Active" or role not in ROLES:
            excluded.append({"relative_path": relative, "reason": "outside_original_active_rmedo_frontier",
                             "content_role": role, "current_scope_unit": owner, "status": status})
            continue
        findings: list[str] = []
        atom_id = metadata.get("atom_id")
        atom_match = ATOM_ID.fullmatch(atom_id) if isinstance(atom_id, str) else None
        if atom_match is None:
            findings.append("missing_or_invalid_atom_id")
        else:
            if ROLES[role] != atom_match.group(1):
                findings.append("atom_id_role_mismatch")
            if not (path.stem == atom_id or path.stem.startswith(f"{atom_id}-")):
                findings.append("filename_atom_id_mismatch")
        if directory_role(source_root, path) != role:
            findings.append("directory_role_mismatch")
        version = metadata.get("version")
        if not isinstance(version, int) or isinstance(version, bool) or version <= 0:
            findings.append("missing_or_invalid_version")
        raw_updated, _ = updated_at(parsed.frontmatter)
        if raw_updated is None or not isinstance(metadata.get("updated_at"), str) or not UPDATED_AT.fullmatch(raw_updated):
            findings.append("updated_at_invalid_or_naive")
        subjects = metadata.get("subjects")
        valid: list[tuple[str, int | None, str]] = []
        if not isinstance(subjects, dict):
            findings.append("subjects_not_mapping")
            subjects = {}
        else:
            for field in sorted(set(subjects).difference(SUBJECT_FIELDS)):
                findings.append(f"unknown_subjects_field:{field}")
        governs = subjects.get("governs")
        if isinstance(governs, str) and governs.strip():
            valid.append(("governs", None, governs))
        else:
            findings.append("governs_missing_or_invalid")
        depends = subjects.get("depends_on")
        if depends is not None:
            if isinstance(depends, list) and all(isinstance(item, str) and item.strip() for item in depends) and len(set(depends)) == len(depends):
                valid.extend(("depends_on", index, value) for index, value in enumerate(depends))
            else:
                findings.append("depends_on_missing_or_invalid_unique_string_list")
        source = {"relative_path": relative, "full_file_sha256": sha(raw), "atom_id": atom_id,
                  "version": version, "role": role, "owner": owner, "status": status,
                  "quarantined": bool(findings), "findings": findings, "body_evidence": body_evidence(path, raw)}
        sources.append(source)
        for field, index, old_value in valid:
            suffix = f"subjects.{field}" + (f"[{index}]" if index is not None else "")
            occurrences.append({"occurrence_id": f"{relative}#{suffix}", "source_path": relative,
                                "source_atom_id": atom_id, "source_version": version,
                                "source_sha256": source["full_file_sha256"], "field": field,
                                "index": index, "old_value": old_value, "quarantined": source["quarantined"]})
    sources.sort(key=lambda item: item["relative_path"])
    occurrences.sort(key=lambda item: item["occurrence_id"])
    excluded.sort(key=lambda item: item["relative_path"])
    return sources, occurrences, excluded, {"path": STRUCTURE.as_posix(), "sha256": sha(structure_path.read_bytes())}


def receipt_pin(task_id: str, report_pin: dict[str, str]) -> dict[str, str]:
    relative = STAGE / f"task-{task_id.removeprefix('CA-P-')}.receipt.json"
    receipt = read_json(relative)
    if receipt.get("task") != task_id:
        fail(f"invalid receipt identity: {task_id}")
    if task_id != "CA-P-2048" and receipt.get("non_authoritative") is not True:
        fail(f"invalid non-authoritative receipt boundary: {task_id}")
    if not str(receipt.get("result", "")).startswith("PASS"):
        fail(f"receipt is not an accepted result: {task_id}")
    if task_id == "CA-P-2048":
        if receipt.get("output") != report_pin:
            fail(f"receipt output pin mismatch: {task_id}")
        checks = receipt.get("checks")
        if not isinstance(checks, dict) or not str(checks.get("independent_semantic_review", "")).startswith("PASS"):
            fail(f"independent semantic acceptance missing: {task_id}")
        return pin(relative)
    if task_id == "CA-P-2058":
        if receipt.get("output") != report_pin:
            fail(f"receipt output pin mismatch: {task_id}")
        accepted = receipt.get("independent_acceptance")
        if not isinstance(accepted, list) or not accepted:
            fail(f"independent accepted coverage missing: {task_id}")
        return pin(relative)
    verification = receipt.get("verification")
    if not isinstance(verification, dict):
        fail(f"missing receipt verification: {task_id}")
    output = verification.get("review") or verification.get("output")
    if output != report_pin:
        fail(f"receipt output pin mismatch: {task_id}")
    independent = receipt.get("independent_review")
    if independent is not None and (not isinstance(independent, dict) or not str(independent.get("result", "")).startswith("PASS")):
        fail(f"independent semantic acceptance missing: {task_id}")
    return pin(relative)


def layer_rows(kind: str, report: dict[str, Any]) -> Iterable[dict[str, Any]]:
    rows = report.get("occurrences") if kind == "substance" else report.get("rows")
    if not isinstance(rows, list):
        fail(f"missing rows for {report.get('task_id')}")
    return rows


def normalized_decision(kind: str, row: dict[str, Any]) -> tuple[str, str | None, float]:
    if kind == "semantic":
        disposition = row.get("disposition")
        if disposition == "accepted":
            value = row.get("proposed_value")
            confidence = row.get("confidence")
            if not isinstance(value, str) or not value or not isinstance(confidence, (int, float)) or confidence < 0.90:
                fail("invalid accepted semantic row")
            return "proposed", value, float(confidence)
        if disposition in {"rejected", "unresolved", "stale"}:
            return "unresolved", None, 0.0
        fail("unknown semantic disposition")
    decision = row.get("decision")
    value = row.get("proposed_value")
    confidence = row.get("confidence")
    if decision == "proposed":
        if not isinstance(value, str) or not value or not isinstance(confidence, (int, float)) or confidence < 0.90:
            fail("invalid proposed layer row")
        return "proposed", value, float(confidence)
    if decision in {"unresolved", "rejected", "stale"}:
        return "unresolved", None, float(confidence) if isinstance(confidence, (int, float)) else 0.0
    fail("unknown layer decision")


def no_inferred_syntax(value: str | None) -> None:
    if value is not None and any(token in value for token in ("@", "(", ")", "&", "|", "=")):
        fail(f"inferred selector or unsupported syntax: {value}")


def historical_origin(row: dict[str, Any]) -> dict[str, Any]:
    return {key: row.get(key) for key in (
        "occurrence_id", "source_path", "source_atom_id", "source_version", "source_sha256",
        "field", "index", "old_value", "quarantined", "decision", "proposed_value",
        "confidence", "originating_review_path", "originating_review_sha256", "task_id", "batch_id",
    )}


def declared_grammar_effects(drift: dict[str, Any]) -> tuple[dict[str, dict[str, Any]], dict[str, str]]:
    """Return only the five audited current-source effects, fail closed otherwise."""
    current_effects: dict[str, dict[str, Any]] = {}
    replacement: dict[str, str] = {}
    records = drift.get("changed_or_missing")
    if not isinstance(records, list) or len(records) != 5:
        fail("expected exactly five audited grammar effects")
    for record in records:
        if record.get("classified") != "approved_grammar_effect" or not isinstance(record.get("atom_id"), str):
            fail("unapproved grammar drift")
        atom_id = record["atom_id"]
        effect = record.get("declared_effect")
        if not isinstance(effect, dict):
            fail("grammar effect missing declaration")
        before = effect.get("before")
        if not isinstance(before, dict) or any(not isinstance(before.get(field), expected) for field, expected in (("path", str), ("version", int), ("sha256", str))):
            fail("grammar effect missing complete before pin")
        if (record.get("path"), record.get("baseline_version"), record.get("baseline_sha256")) != (before["path"], before["version"], before["sha256"]):
            fail("grammar effect record/before pin disagreement")
        if effect.get("operation") == "replace_with_new_id":
            after = effect.get("after")
            if not isinstance(after, dict) or any(not isinstance(after.get(field), expected) for field, expected in (("atom_id", str), ("path", str), ("version", int), ("sha256", str))):
                fail("replacement grammar effect missing new Atom ID")
            current_atom_id = after["atom_id"]
            if current_atom_id in replacement:
                fail("duplicate replacement current Atom ID")
            replacement[current_atom_id] = atom_id
        elif effect.get("operation") == "revise_active_atom":
            after = effect.get("after")
            if not isinstance(after, dict) or any(not isinstance(after.get(field), expected) for field, expected in (("path", str), ("version", int), ("sha256", str))):
                fail("revision grammar effect missing complete after pin")
            current_atom_id = atom_id
        else:
            fail("unsupported grammar effect")
        if current_atom_id in current_effects:
            fail("duplicate grammar current Atom ID")
        current_effects[current_atom_id] = {"historic_atom_id": atom_id, "operation": effect["operation"], "before": before, "after": after}
    return current_effects, replacement


def source_index(sources: list[dict[str, Any]], label: str) -> dict[str, dict[str, Any]]:
    indexed = {source.get("relative_path"): source for source in sources if isinstance(source.get("relative_path"), str)}
    if len(indexed) != len(sources):
        fail(f"duplicate or invalid {label} source path")
    return indexed


def source_matches_pin(source: dict[str, Any], atom_id: str, pin_value: dict[str, Any]) -> bool:
    return (source.get("atom_id") == atom_id and source.get("relative_path") == pin_value.get("path")
            and source.get("version") == pin_value.get("version") and source.get("full_file_sha256") == pin_value.get("sha256"))


def validate_declared_drift(
    baseline_sources: list[dict[str, Any]], current_sources: list[dict[str, Any]], current_effects: dict[str, dict[str, Any]],
) -> None:
    """Require exact audited pins for every drift and reject all other source movement."""
    historic = source_index(baseline_sources, "baseline")
    current = source_index(current_sources, "current")
    effect_by_historic = {effect["historic_atom_id"]: (current_atom_id, effect) for current_atom_id, effect in current_effects.items()}
    for current_atom_id, effect in current_effects.items():
        before, after = effect["before"], effect["after"]
        historic_source = historic.get(before["path"])
        if historic_source is None or not source_matches_pin(historic_source, effect["historic_atom_id"], before):
            fail(f"declared grammar before pin does not match frozen baseline: {effect['historic_atom_id']}")
        active_source = current.get(after["path"])
        if active_source is None or not source_matches_pin(active_source, current_atom_id, after):
            fail(f"declared grammar current-after pin does not match live Core: {current_atom_id}")
    for path, historic_source in historic.items():
        active_source = current.get(path)
        if active_source is not None:
            if active_source.get("full_file_sha256") == historic_source.get("full_file_sha256"):
                continue
            current_atom_id = active_source.get("atom_id")
            effect = current_effects.get(current_atom_id) if isinstance(current_atom_id, str) else None
            if effect is None or effect["operation"] != "revise_active_atom" or not source_matches_pin(active_source, current_atom_id, effect["after"]):
                fail(f"unexpected current source hash drift: {path}")
            continue
        historic_atom_id = historic_source.get("atom_id")
        declared = effect_by_historic.get(historic_atom_id) if isinstance(historic_atom_id, str) else None
        if declared is None or declared[1]["operation"] != "replace_with_new_id" or not source_matches_pin(historic_source, historic_atom_id, declared[1]["before"]):
            fail(f"missing current source without declared replacement: {path}")
    for path, active_source in current.items():
        if path in historic:
            continue
        active_atom_id = active_source.get("atom_id")
        effect = current_effects.get(active_atom_id) if isinstance(active_atom_id, str) else None
        if effect is None or effect["operation"] != "replace_with_new_id" or not source_matches_pin(active_source, active_atom_id, effect["after"]):
            fail(f"unexpected current source path without declared replacement: {path}")


def matched_origin(
    current: dict[str, Any], baseline_by_id: dict[str, dict[str, Any]], baseline_by_atom_field: dict[tuple[Any, Any, Any, Any], list[dict[str, Any]]],
    replacement: dict[str, str],
) -> dict[str, Any]:
    origin = baseline_by_id.get(current["occurrence_id"])
    if origin is not None:
        if (origin.get("field"), origin.get("index"), origin.get("old_value")) != (current["field"], current["index"], current["old_value"]):
            fail(f"existing occurrence ID does not preserve field/index/text: {current['occurrence_id']}")
        return origin
    historic_atom_id = replacement.get(current.get("source_atom_id"))
    if historic_atom_id is None:
        fail(f"missing exact frozen baseline occurrence: {current['occurrence_id']}")
    candidates = baseline_by_atom_field.get((historic_atom_id, current["field"], current["index"], current["old_value"]), [])
    if len(candidates) != 1:
        fail(f"declared replacement lacks one exact field/index/text baseline counterpart: {current['occurrence_id']}")
    return candidates[0]


def run_negative_probes() -> None:
    """Isolated fail-closed probes; they do not read or write project inputs."""
    baseline_source = {"relative_path": "core/CA-R-1.md", "atom_id": "CA-R-1", "version": 1, "full_file_sha256": "a" * 64}

    def require_rejection(label: str, callback: Any) -> None:
        try:
            callback()
        except ValueError:
            return
        fail(f"negative probe unexpectedly accepted: {label}")

    require_rejection(
        "unexpected_same_id_hash",
        lambda: validate_declared_drift([baseline_source], [{**baseline_source, "full_file_sha256": "b" * 64}], {}),
    )
    require_rejection(
        "unexpected_path_move",
        lambda: validate_declared_drift([baseline_source], [{**baseline_source, "relative_path": "core/moved-CA-R-1.md"}], {}),
    )
    require_rejection(
        "missing_current_source",
        lambda: validate_declared_drift([baseline_source], [], {}),
    )
    historic_occurrence = {"occurrence_id": "core/CA-R-1.md#subjects.governs", "source_atom_id": "CA-R-1", "field": "governs", "index": None, "old_value": "Atom"}
    current_occurrence = {"occurrence_id": "core/CA-R-2.md#subjects.governs", "source_atom_id": "CA-R-2", "field": "governs", "index": None, "old_value": "Atom"}
    require_rejection(
        "unapproved_occurrence_rebind",
        lambda: matched_origin(current_occurrence, {historic_occurrence["occurrence_id"]: historic_occurrence}, {("CA-R-1", "governs", None, "Atom"): [historic_occurrence]}, {}),
    )
    require_rejection(
        "changed_text_at_existing_occurrence_id",
        lambda: matched_origin({**historic_occurrence, "old_value": "Claim"}, {historic_occurrence["occurrence_id"]: historic_occurrence}, {}, {}),
    )


def build() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    baseline = read_json(BASELINE)
    if baseline.get("non_authoritative") is not True or baseline.get("source_migration") != "not_performed":
        fail("baseline ledger boundary")
    baseline_rows = baseline.get("occurrences")
    if not isinstance(baseline_rows, list) or len({row.get("occurrence_id") for row in baseline_rows}) != len(baseline_rows):
        fail("baseline occurrence coverage invalid")
    baseline_sources = baseline.get("source_reviews")
    if not isinstance(baseline_sources, list):
        fail("baseline source coverage invalid")
    baseline_by_id = {row["occurrence_id"]: row for row in baseline_rows}
    baseline_by_atom_field: dict[tuple[Any, Any, Any, Any], list[dict[str, Any]]] = {}
    for row in baseline_rows:
        key = (row.get("source_atom_id"), row.get("field"), row.get("index"), row.get("old_value"))
        baseline_by_atom_field.setdefault(key, []).append(row)
    drift = read_json(DRIFT)
    current_effects, replacement = declared_grammar_effects(drift)
    sources, current_rows, excluded, structure_pin = current_frontier()
    validate_declared_drift(baseline_sources, sources, current_effects)
    current_by_id = {row["occurrence_id"]: row for row in current_rows}
    if len(current_by_id) != len(current_rows):
        fail("duplicate current occurrence ID")
    current_body_evidence = {source["relative_path"]: source["body_evidence"] for source in sources}

    states: dict[str, dict[str, Any]] = {}
    matched_baseline_ids: set[str] = set()
    for current in current_rows:
        origin = matched_origin(current, baseline_by_id, baseline_by_atom_field, replacement)
        matched_baseline_ids.add(origin["occurrence_id"])
        source_unchanged = origin.get("source_sha256") == current.get("source_sha256")
        if not source_unchanged and current.get("source_atom_id") not in current_effects:
            fail(f"unexpected occurrence source hash drift: {current['occurrence_id']}")
        needs_recheck = current.get("source_atom_id") in current_effects
        state = {"decision": origin.get("decision"), "proposed_value": origin.get("proposed_value"),
                 "confidence": origin.get("confidence"), "reason": origin.get("reason"),
                 "evidence": origin.get("evidence", []), "candidate_basis": origin.get("candidate_basis", []),
                 "preserved_distinctions": origin.get("preserved_distinctions", []), "question": origin.get("question"),
                 "applied_layers": [{"layer": "baseline", "decision": origin.get("decision"),
                                     "proposed_value": origin.get("proposed_value"), "accepted": False,
                                     "reason": "Captured baseline retained as historical provenance, not independent follow-up acceptance."}],
                 "historical_origin": historical_origin(origin), "source_unchanged_from_baseline": source_unchanged}
        states[current["occurrence_id"]] = {"current": current, "state": state, "needs_recheck": needs_recheck}

    missing_current_counterparts = sorted(set(baseline_by_id).difference(matched_baseline_ids))
    if missing_current_counterparts:
        fail(f"frozen baseline occurrences missing current counterpart: {missing_current_counterparts[0]}")

    accepted_layers: list[dict[str, Any]] = []
    for priority, (task_id, report_rel, kind) in enumerate(LAYER_SPECS, start=1):
        report = read_json(report_rel)
        report_pin = pin(report_rel)
        if report.get("task_id") != task_id or report.get("non_authoritative") is not True:
            fail(f"layer report boundary: {task_id}")
        receipt = receipt_pin(task_id, report_pin)
        rows = list(layer_rows(kind, report))
        ids = [row.get("occurrence_id") for row in rows]
        if not all(isinstance(item, str) for item in ids) or len(set(ids)) != len(ids):
            fail(f"duplicate layer ownership: {task_id}")
        for row in rows:
            occurrence_id = row["occurrence_id"]
            if occurrence_id not in states:
                fail(f"layer occurrence missing current counterpart: {task_id} {occurrence_id}")
            decision, value, confidence = normalized_decision(kind, row)
            no_inferred_syntax(value)
            target = states[occurrence_id]["state"]
            target["applied_layers"].append({"layer": task_id, "priority": priority, "report": report_pin,
                                             "receipt": receipt, "decision": decision, "proposed_value": value,
                                             "accepted": decision == "proposed"})
            target.update({"decision": decision, "proposed_value": value, "confidence": confidence,
                           "reason": row.get("reason"), "evidence": row.get("evidence", []),
                           "candidate_basis": row.get("candidate_basis", []),
                           "preserved_distinctions": row.get("preserved_distinctions", []),
                           "question": row.get("question"), "selected_layer_row": {"task": task_id, "kind": kind}})
        accepted_layers.append({"task": task_id, "priority": priority, "report": report_pin, "receipt": receipt,
                                "rows": len(rows), "kind": kind})

    actor_report = read_json(ACTOR_SUBSET)
    actor_pin = pin(ACTOR_SUBSET)
    actor_receipt = receipt_pin("CA-P-2058", actor_pin)
    actor_rows = actor_report.get("rows")
    if not isinstance(actor_rows, list) or len(actor_rows) != 43:
        fail("Actor subset coverage")
    for row in actor_rows:
        state = states.get(row.get("occurrence_id"))
        if state is None or state["state"].get("proposed_value") != row.get("proposed_value"):
            fail("Actor subset canonical target disagreement")
    accepted_layers.append({"task": "CA-P-2058", "priority": "coverage_only", "report": actor_pin,
                            "receipt": actor_receipt, "rows": 43, "kind": "canonical_target_check"})

    grammar_rechecks: list[dict[str, Any]] = []
    for occurrence_id, record in states.items():
        if not record["needs_recheck"]:
            continue
        state = record["state"]
        state["applied_layers"].append({"layer": "CA-P-2087", "status": "not_independently_accepted",
                                        "decision": "unresolved", "proposed_value": None})
        state.update({"decision": "unresolved", "proposed_value": None, "confidence": 0.0,
                      "reason": "Current source is one of the five audited grammar changed/replaced sources; without independently accepted CA-P-2087 current-grammar Subject evidence its mapping is reset to null.",
                      "evidence": next(source["body_evidence"] for source in sources if source["relative_path"] == record["current"]["source_path"]),
                      "candidate_basis": [], "preserved_distinctions": ["Historical baseline and selected-layer hypotheses remain provenance only.", "No old source hash is treated as current semantic evidence.", "No selector or grammar rebind is inferred."], "question": None,
                      "current_source_semantic_recheck_required": True})
        grammar_rechecks.append({"occurrence_id": occurrence_id, "source_atom_id": record["current"].get("source_atom_id"),
                                 "source_path": record["current"]["source_path"]})

    rows: list[dict[str, Any]] = []
    for occurrence_id in sorted(states):
        record = states[occurrence_id]
        current = record["current"]
        state = record["state"]
        decision = state.get("decision")
        value = state.get("proposed_value")
        confidence = state.get("confidence")
        if decision not in {"unchanged", "proposed", "unresolved"} or not isinstance(confidence, (int, float)):
            fail("final decision shape")
        if decision == "unresolved" and value is not None:
            fail("unresolved target must be null")
        if decision in {"unchanged", "proposed"} and (not isinstance(value, str) or confidence < 0.90):
            fail("decided target invalid")
        no_inferred_syntax(value)
        evidence = list(state.get("evidence", []))
        if decision != "unresolved":
            live = current_body_evidence.get(current["source_path"])
            if not live:
                fail("current source evidence unavailable")
            if not any(item.get("path") == live[0]["path"] and item.get("sha256") == live[0]["sha256"]
                       and item.get("span_sha256") == live[0]["span_sha256"] for item in evidence if isinstance(item, dict)):
                evidence.extend(live)
        row = {**current, **state, "evidence": evidence, "executable": False}
        historic = row.get("historical_origin")
        if isinstance(historic, dict) and (historic.get("occurrence_id") != current["occurrence_id"] or historic.get("source_sha256") != current["source_sha256"]):
            row["replacement_lineage"] = {
                "historic_occurrence_id": historic.get("occurrence_id"),
                "current_occurrence_id": current["occurrence_id"],
                "historic_source_sha256": historic.get("source_sha256"),
                "current_source_sha256": current["source_sha256"],
                "field": current["field"], "index": current["index"], "old_value": current["old_value"],
            }
        rows.append(row)
    decisions = Counter(row["decision"] for row in rows)
    source_by_path = {source["relative_path"]: source for source in sources}
    source_rows = []
    for path, source in sorted(source_by_path.items()):
        source_rows.append({key: value for key, value in source.items() if key != "body_evidence"})

    input_pins = {"baseline": pin(BASELINE), "grammar_drift": pin(DRIFT), "structure": structure_pin,
                  "contracts": [pin(item) for item in CONTRACTS], "accepted_layers": accepted_layers}
    diagnostic = {
        "schema_version": 1, "task_id": "CA-P-2086", "non_authoritative": True,
        "source_migration": "not_performed", "native_admission": "not_performed",
        "counts": {"current_sources": len(sources), "current_occurrences": len(rows),
                   "quarantined_sources": sum(source["quarantined"] for source in sources),
                   "quarantined_occurrences": sum(row["quarantined"] for row in rows),
                   "grammar_recheck_occurrences": len(grammar_rechecks),
                   "missing_baseline_counterparts": 0,
                   "missing_current_counterparts": len(missing_current_counterparts),
                   "decisions": dict(sorted(decisions.items()))},
        "grammar_recheck_required": grammar_rechecks, "missing_baseline_counterparts": [],
        "missing_current_counterparts": missing_current_counterparts,
        "excluded_sources": excluded,
        "limits": ["CA-P-2087 is not independently accepted; all five grammar changed/replaced source occurrences are explicit nulls.", "This derived draft is not migration approval or native admission."],
    }
    frontier = {"schema_version": 1, "task_id": "CA-P-2086", "non_authoritative": True,
                "source_migration": "not_performed", "native_admission": "not_performed",
                "input_pins": {"structure": structure_pin, "grammar_drift": pin(DRIFT)},
                "authority_path": ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL",
                "selected_sources": source_rows, "excluded_sources": excluded,
                "occurrence_count": len(rows)}
    ledger = {"schema_version": 1, "task_id": "CA-P-2086", "non_authoritative": True,
              "source_migration": "not_performed", "native_admission": "not_performed",
              "scope": "Create-only current-frontier working mapping ledger; not semantic final acceptance or source migration.",
              "input_pins": input_pins, "layer_priority": [item[0] for item in LAYER_SPECS] + ["CA-P-2058 coverage_only", "CA-P-2087 recheck_gate"],
              "counts": {"sources": len(source_rows), "occurrences": len(rows), "quarantined_sources": sum(source["quarantined"] for source in source_rows),
                         "quarantined_occurrences": sum(row["quarantined"] for row in rows), "decisions": dict(sorted(decisions.items())),
                         "unresolved": decisions["unresolved"], "grammar_recheck_required": len(grammar_rechecks)},
              "source_reviews": source_rows, "occurrences": rows,
              "remaining_gaps": {"diagnostics_path": (WORKING / "diagnostics.json").as_posix(), "grammar_recheck_occurrences": len(grammar_rechecks),
                                 "unresolved_occurrences": decisions["unresolved"]}}
    return ledger, frontier, diagnostic


def write_create_only(values: dict[Path, dict[str, Any]]) -> None:
    for relative in values:
        target = checked_relative_path(relative, "derived output")
        if target.exists() or target.is_symlink():
            fail(f"create-only output already exists: {relative}")
        if target.parent.exists() and target.parent.is_symlink():
            fail(f"unsafe output parent: {target.parent}")
    for relative, value in values.items():
        target = checked_relative_path(relative, "derived output")
        target.parent.mkdir(parents=True, exist_ok=True)
        try:
            with target.open("xb") as handle:
                handle.write(json_bytes(value))
        except FileExistsError as error:
            raise ValueError(f"create-only output already exists: {relative}") from error


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--persist", action="store_true", help="create three working-ledger drafts once")
    parser.add_argument("--negative-probes", action="store_true", help="run isolated fail-closed drift probes without project I/O")
    args = parser.parse_args(argv)
    try:
        if args.negative_probes:
            if args.persist:
                fail("negative probes cannot persist outputs")
            run_negative_probes()
            print(json.dumps({"outcome": "NEGATIVE_PROBES_PASS"}, sort_keys=True))
            return 0
        ledger, frontier, diagnostic = build()
        if args.persist:
            write_create_only({LEDGER: ledger, FRONTIER: frontier, DIAGNOSTICS: diagnostic})
        print(json.dumps({"outcome": "CREATED" if args.persist else "PREVIEW", "counts": ledger["counts"],
                          "would_create": [path.as_posix() for path in (LEDGER, FRONTIER, DIAGNOSTICS)]}, sort_keys=True))
    except (ValueError, OSError, KeyError, TypeError) as error:
        print(json.dumps({"outcome": "FAIL", "reason": str(error)}, sort_keys=True), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
