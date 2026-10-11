"""Independent verifier for the derived CA-P-2086 working Subject ledger.

This module deliberately does not import the consolidator.  It re-enumerates
the active Core RMEDO frontier through the strict carrier parser, then checks
that the derived files preserve that frontier and make every current Subject
occurrence accountable.  It is a read-only acceptance gate, not a mapping
producer or a source writer.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import tomllib
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[5]
STAGE2_REL = Path(".caprmedio_caprmedio/_projection/core-entity-review/stage2")
WORKING_REL = STAGE2_REL / "working-ledger"
LEDGER_REL = WORKING_REL / "working-mapping-ledger.json"
FRONTIER_REL = WORKING_REL / "source-frontier.json"
DIAGNOSTICS_REL = WORKING_REL / "diagnostics.json"
BASELINE_REL = STAGE2_REL / "current-subjects.mapping-ledger.json"
GRAMMAR_DRIFT_REL = STAGE2_REL / "current-grammar-source-drift.json"
ACTOR_SUBSET_REL = STAGE2_REL / "semantic-reviews/task-2058.accepted-subset.json"
STRUCTURE_REL = Path(".caprmedio_caprmedio/project_structure.toml")
VALIDATOR_ROOT = ROOT / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/VALIDATE_ATOMS"
if str(VALIDATOR_ROOT) not in sys.path:
    sys.path.insert(0, str(VALIDATOR_ROOT))

from validate_atoms_workers.parsing import CarrierError, parse_carrier  # noqa: E402


ROLES = {"Requirement", "Method", "Evaluation", "Delivery", "Operations"}
ROLE_DIRS = {
    "04_requirement": "Requirement",
    "05_method": "Method",
    "06_evaluation": "Evaluation",
    "07_delivery": "Delivery",
    "09_operations": "Operations",
    "09_ops": "Operations",
}
ROLE_BY_ID_KIND = {"R": "Requirement", "M": "Method", "E": "Evaluation", "D": "Delivery", "O": "Operations"}
ATOM_ID_RE = re.compile(r"^CA-([RMEDO])-([0-9]+)$")
FILENAME_ID_RE = re.compile(r"^(CA-([RMEDO])-[0-9]+)(?:-|$)")
SHA_RE = re.compile(r"^[0-9a-f]{64}$")
FORBIDDEN_TARGET_RE = re.compile(r"[@\[\]{}()=]")
LAYER_SPECS = (
    ("CA-P-2048", "substance"),
    ("CA-P-2072", "semantic"), ("CA-P-2073", "semantic"),
    ("CA-P-2074", "semantic"), ("CA-P-2075", "semantic"),
    ("CA-P-2076", "semantic"),
    ("CA-P-2078", "research"), ("CA-P-2079", "research"),
    ("CA-P-2080", "research"), ("CA-P-2082", "research"),
    ("CA-P-2083", "research"), ("CA-P-2084", "research"),
    ("CA-P-2085", "research"),
)
LAYER_PRIORITY = [task for task, _kind in LAYER_SPECS] + ["CA-P-2058 coverage_only", "CA-P-2087 recheck_gate"]


class VerificationError(AssertionError):
    """A deterministic, concise acceptance-gate failure."""


def require(condition: bool, label: str) -> None:
    if not condition:
        raise VerificationError(label)


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _is_sha(value: Any) -> bool:
    return isinstance(value, str) and SHA_RE.fullmatch(value) is not None


def relative_path(root: Path, value: Any, label: str) -> Path:
    require(isinstance(value, str) and value and not Path(value).is_absolute(), f"{label} relative path")
    relative = Path(value)
    require(".." not in relative.parts, f"{label} path traversal")
    candidate = root / relative
    try:
        candidate.resolve(strict=False).relative_to(root.resolve())
        relative = candidate.relative_to(root)
    except ValueError as error:
        raise VerificationError(f"{label} escapes repository root") from error
    probe = root
    for part in relative.parts:
        probe /= part
        require(not probe.is_symlink(), f"{label} symlink")
    return candidate


def read_json(path: Path, label: str) -> dict[str, Any]:
    require(path.is_file() and not path.is_symlink(), f"{label} exists as regular file")
    try:
        value = json.loads(path.read_bytes())
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise VerificationError(f"{label} valid JSON") from error
    require(isinstance(value, dict), f"{label} JSON object")
    return value


def _updated_at(frontmatter: str) -> tuple[str | None, str]:
    match = re.search(r"(?m)^updated_at:\s*(.*?)\s*$", frontmatter)
    if match is None:
        return None, "missing"
    text = match.group(1).strip()
    return text.strip("\"'"), "quoted" if text[:1] in "\"'" else "plain"


def _directory_role(source_root: Path, path: Path) -> str | None:
    for component in path.relative_to(source_root).parts[:-1]:
        if component in ROLE_DIRS:
            return ROLE_DIRS[component]
    return None


def current_authority_path(root: Path) -> tuple[Path, Path]:
    structure = relative_path(root, STRUCTURE_REL.as_posix(), "authoritative Structure")
    require(structure.is_file(), "authoritative Structure exists")
    try:
        document = tomllib.loads(structure.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, tomllib.TOMLDecodeError) as error:
        raise VerificationError("authoritative Structure parses as TOML") from error
    rows = document.get("scope_units") if isinstance(document, dict) else None
    require(isinstance(rows, list), "Structure scope_units list")
    matches = [row for row in rows if isinstance(row, dict) and row.get("scope_unit_name") == "CORE_META_MODEL"]
    require(len(matches) == 1, "one CORE_META_MODEL Structure row")
    source_root = relative_path(root, matches[0].get("authority_path"), "CORE_META_MODEL authority")
    require(source_root.is_dir(), "CORE_META_MODEL authority directory")
    return structure, source_root


def enumerate_current_frontier(root: Path) -> dict[str, Any]:  # noqa: C901 - mirrors the strict frontier partition deliberately.
    """Strictly reconstruct active Core RMEDO sources and Subject occurrences."""

    structure, source_root = current_authority_path(root)
    selected: list[dict[str, Any]] = []
    excluded: list[dict[str, Any]] = []
    diagnostics: list[dict[str, Any]] = []
    occurrences: list[dict[str, Any]] = []
    for path in sorted(source_root.rglob("*.md")):
        rel = path.relative_to(root).as_posix()
        if "archive" in path.parts:
            excluded.append({"relative_path": rel, "reason": "archived_lifecycle_copy"})
            continue
        raw = path.read_bytes()
        try:
            parsed = parse_carrier(raw, path)
            metadata = parsed.metadata
        except CarrierError as error:
            filename_match = FILENAME_ID_RE.match(path.stem)
            if filename_match is None:
                excluded.append({"relative_path": rel, "reason": "strict_parse_error", "code": error.code, "detail": str(error)})
            else:
                selected.append({
                    "relative_path": rel, "full_file_sha256": sha(raw), "atom_id": None,
                    "filename_atom_id": filename_match.group(1), "version": None,
                    "role": ROLE_BY_ID_KIND[filename_match.group(2)], "owner": None,
                    "author": None, "status": None, "updated_at": None,
                    "updated_at_type": "unavailable", "quarantined": True,
                    "findings": [f"strict_parse_error:{error.code}"],
                })
            continue
        role = metadata.get("content_role")
        scope = metadata.get("current_scope_unit")
        status = metadata.get("status")
        if scope != "CORE_META_MODEL":
            excluded.append({"relative_path": rel, "reason": "owner_mismatch", "content_role": role, "current_scope_unit": scope, "status": status})
            diagnostics.append({"relative_path": rel, "code": "owner_mismatch", "expected": "CORE_META_MODEL", "actual": scope})
            continue
        if status != "Active":
            excluded.append({"relative_path": rel, "reason": "not_active_lifecycle", "content_role": role, "current_scope_unit": scope, "status": status})
            continue
        if role not in ROLES:
            excluded.append({"relative_path": rel, "reason": "not_rmedo_role", "content_role": role, "current_scope_unit": scope, "status": status})
            continue
        updated_at, _ = _updated_at(parsed.frontmatter)
        findings: list[str] = []
        atom_id = metadata.get("atom_id")
        atom_match = ATOM_ID_RE.fullmatch(atom_id) if isinstance(atom_id, str) else None
        if atom_match is None or int(atom_match.group(2)) < 1:
            findings.append("missing_or_invalid_atom_id")
        else:
            if ROLE_BY_ID_KIND[atom_match.group(1)] != role:
                findings.append("atom_id_role_mismatch")
            if not (path.stem == atom_id or path.stem.startswith(f"{atom_id}-")):
                findings.append("filename_atom_id_mismatch")
        if _directory_role(source_root, path) != role:
            findings.append("directory_role_mismatch")
        if not isinstance(metadata.get("version"), int) or isinstance(metadata.get("version"), bool) or metadata["version"] <= 0:
            findings.append("missing_or_invalid_version")
        if updated_at is None:
            findings.append("missing_updated_at")
        if not isinstance(metadata.get("updated_at"), str) or not re.search(r"(?:[+-]\d{2}:?\d{2}|Z)$", updated_at or ""):
            findings.append("updated_at_invalid_or_naive")
        subjects = metadata.get("subjects")
        valid_subjects: list[tuple[str, int | None, str]] = []
        if not isinstance(subjects, dict):
            findings.append("subjects_not_mapping")
            subjects = {}
        governs = subjects.get("governs")
        if isinstance(governs, str) and governs.strip():
            valid_subjects.append(("governs", None, governs))
        else:
            findings.append("governs_missing_or_invalid")
        depends_on = subjects.get("depends_on")
        if depends_on is not None:
            if isinstance(depends_on, list) and all(isinstance(value, str) and value.strip() for value in depends_on) and len(set(depends_on)) == len(depends_on):
                valid_subjects.extend(("depends_on", index, value) for index, value in enumerate(depends_on))
            else:
                findings.append("depends_on_missing_or_invalid_unique_string_list")
        full_sha = sha(raw)
        selected.append({
            "relative_path": rel, "full_file_sha256": full_sha, "atom_id": atom_id,
            "version": metadata.get("version"), "role": role, "owner": scope,
            "author": metadata.get("author"), "status": status, "updated_at": updated_at,
            "updated_at_type": type(metadata.get("updated_at")).__name__,
            "quarantined": bool(findings), "findings": findings,
        })
        for field, index, old_value in valid_subjects:
            suffix = f"subjects.{field}" + (f"[{index}]" if index is not None else "")
            occurrences.append({
                "occurrence_id": f"{rel}#{suffix}", "source_path": rel,
                "source_atom_id": atom_id, "source_version": metadata.get("version"),
                "source_sha256": full_sha, "field": field, "index": index,
                "old_value": old_value, "quarantined": bool(findings),
            })
    counts: dict[str, int] = {}
    for source in selected:
        if isinstance(source["atom_id"], str) and ATOM_ID_RE.fullmatch(source["atom_id"]):
            counts[source["atom_id"]] = counts.get(source["atom_id"], 0) + 1
    duplicate_paths: set[str] = set()
    for atom_id in sorted(atom_id for atom_id, count in counts.items() if count > 1):
        copies = [source for source in selected if source["atom_id"] == atom_id]
        for source in copies:
            source["findings"].append("duplicate_atom_id")
            source["quarantined"] = True
            duplicate_paths.add(source["relative_path"])
        diagnostics.append({"code": "duplicate_atom_id", "atom_id": atom_id, "relative_paths": [source["relative_path"] for source in copies]})
    quarantined_paths = {source["relative_path"] for source in selected if source["quarantined"]} | duplicate_paths
    for occurrence in occurrences:
        occurrence["quarantined"] = occurrence["source_path"] in quarantined_paths
    selected.sort(key=lambda value: value["relative_path"])
    excluded.sort(key=lambda value: value["relative_path"])
    diagnostics.sort(key=lambda value: (value.get("relative_path", ""), value["code"]))
    occurrences.sort(key=lambda value: value["occurrence_id"])
    return {
        "structure_path": structure.relative_to(root).as_posix(),
        "structure_sha256": sha(structure.read_bytes()),
        "selected_sources": selected, "excluded_sources": excluded,
        "diagnostics": diagnostics, "occurrences": occurrences,
    }


def _source_view(source: dict[str, Any]) -> dict[str, Any]:
    """The compact derived frontier must preserve every source truth it exposes."""

    return {key: source.get(key) for key in (
        "relative_path", "full_file_sha256", "atom_id", "version", "role", "owner",
        "status", "quarantined", "findings",
    )}


def _verify_frontier(root: Path, frontier: dict[str, Any], expected: dict[str, Any]) -> None:
    require(frontier.get("schema_version") == 1, "frontier schema version")
    require(frontier.get("non_authoritative") is True, "frontier non-authoritative")
    require(frontier.get("source_migration") == "not_performed", "frontier source migration")
    require(frontier.get("native_admission") == "not_performed", "frontier native admission")
    pins = frontier.get("input_pins")
    require(isinstance(pins, dict) and pins.get("structure") == {
        "path": expected["structure_path"], "sha256": expected["structure_sha256"],
    }, "frontier live Structure pin")
    require(frontier.get("selected_sources") == [_source_view(source) for source in expected["selected_sources"]], "exact current frontier source pins")
    excluded = frontier.get("excluded_sources")
    require(isinstance(excluded, list), "frontier excluded source list")
    require({item.get("relative_path") for item in excluded if isinstance(item, dict)} == {item["relative_path"] for item in expected["excluded_sources"]}, "exact current excluded source coverage")
    require(frontier.get("occurrence_count") == len(expected["occurrences"]), "frontier occurrence count")


def _span_matches(root: Path, evidence: dict[str, Any], expected: dict[str, Any], label: str) -> bool:
    if not isinstance(evidence, dict) or evidence.get("path") != expected["source_path"] or evidence.get("sha256") != expected["source_sha256"]:
        return False
    start, end = evidence.get("start_line"), evidence.get("end_line")
    if not isinstance(start, int) or isinstance(start, bool) or not isinstance(end, int) or isinstance(end, bool) or start < 1 or end < start or not _is_sha(evidence.get("span_sha256")):
        return False
    path = relative_path(root, evidence["path"], label)
    if not path.is_file() or sha(path.read_bytes()) != evidence["sha256"]:
        return False
    lines = path.read_bytes().splitlines(keepends=True)
    return end <= len(lines) and sha(b"".join(lines[start - 1 : end])) == evidence["span_sha256"]


def _verify_lineage(
    row: dict[str, Any],
    expected: dict[str, Any],
    baseline_rows: dict[str, dict[str, Any]],
    grammar_effects: dict[str, dict[str, Any]],
    label: str,
) -> dict[str, Any]:
    historic = row.get("historical_origin")
    require(isinstance(historic, dict), f"{label} historical origin")
    historic_id = historic.get("occurrence_id")
    require(isinstance(historic_id, str) and historic_id in baseline_rows, f"{label} baseline historic occurrence")
    baseline = baseline_rows[historic_id]
    for field in ("occurrence_id", "source_path", "source_atom_id", "source_version", "source_sha256", "field", "index", "old_value", "quarantined", "decision", "proposed_value", "confidence"):
        require(historic.get(field) == baseline.get(field), f"{label} exact frozen baseline {field}")
    require(historic["field"] == expected["field"] and historic["index"] == expected["index"] and historic["old_value"] == expected["old_value"], f"{label} exact counterpart field/index/text")
    changed = historic["occurrence_id"] != expected["occurrence_id"] or historic["source_sha256"] != expected["source_sha256"]
    same_source_identity = historic["source_atom_id"] == expected["source_atom_id"] and historic["source_path"] == expected["source_path"]
    if not changed:
        require(same_source_identity and historic["source_version"] == expected["source_version"], f"{label} unchanged exact source counterpart")
    if changed:
        effect = grammar_effects.get(expected["source_atom_id"])
        require(isinstance(effect, dict), f"{label} declared grammar source change")
        before, after = effect.get("before"), effect.get("after")
        require(isinstance(before, dict) and isinstance(after, dict), f"{label} declared grammar before/after")
        require(after.get("path") == expected["source_path"] and after.get("version") == expected["source_version"] and after.get("sha256") == expected["source_sha256"], f"{label} declared grammar current source")
        require(before.get("path") == historic["source_path"] and before.get("version") == historic["source_version"] and before.get("sha256") == historic["source_sha256"], f"{label} declared grammar historic source")
        if same_source_identity:
            require(effect.get("operation") == "revise_active_atom", f"{label} same-ID grammar revision")
        else:
            require(effect.get("operation") == "replace_with_new_id" and effect.get("atom_id") == historic["source_atom_id"] and after.get("atom_id") == expected["source_atom_id"], f"{label} sole declared replacement counterpart")
        lineage = row.get("replacement_lineage")
        require(isinstance(lineage, dict), f"{label} replacement lineage")
        require(lineage.get("historic_occurrence_id") == historic["occurrence_id"], f"{label} lineage historic occurrence")
        require(lineage.get("current_occurrence_id") == expected["occurrence_id"], f"{label} lineage current occurrence")
        require(lineage.get("historic_source_sha256") == historic["source_sha256"], f"{label} lineage historic pin")
        require(lineage.get("current_source_sha256") == expected["source_sha256"], f"{label} lineage current pin")
        require(lineage.get("field") == expected["field"] and lineage.get("index") == expected["index"] and lineage.get("old_value") == expected["old_value"], f"{label} lineage field/index/text")
    return baseline


def _normalized_layer_row(kind: str, row: dict[str, Any], label: str) -> tuple[str, str | None, float]:
    if kind == "semantic":
        disposition = row.get("disposition")
        if disposition == "accepted":
            target, confidence = row.get("proposed_value"), row.get("confidence")
            require(isinstance(target, str) and target and isinstance(confidence, (int, float)) and not isinstance(confidence, bool) and confidence >= .9, f"{label} accepted semantic value")
            return "proposed", target, float(confidence)
        require(disposition in {"rejected", "unresolved", "stale"}, f"{label} semantic disposition")
        return "unresolved", None, 0.0
    decision = row.get("decision")
    if decision == "proposed":
        target, confidence = row.get("proposed_value"), row.get("confidence")
        require(isinstance(target, str) and target and isinstance(confidence, (int, float)) and not isinstance(confidence, bool) and confidence >= .9, f"{label} proposed value")
        return "proposed", target, float(confidence)
    require(decision in {"unresolved", "rejected", "stale"}, f"{label} layer decision")
    confidence = row.get("confidence")
    return "unresolved", None, float(confidence) if isinstance(confidence, (int, float)) and not isinstance(confidence, bool) else 0.0


def _verify_layers(
    row: dict[str, Any],
    label: str,
    layer_rows: dict[str, dict[str, tuple[str, str | None, float]]],
    baseline: dict[str, Any] | None,
    grammar_effects: dict[str, dict[str, Any]],
) -> None:
    layers = row.get("applied_layers")
    require(isinstance(layers, list), f"{label} applied layers")
    required = (["baseline"] if baseline is not None else []) + [
        task for task, _kind in LAYER_SPECS if row["occurrence_id"] in layer_rows.get(task, {})
    ]
    if row["source_atom_id"] in grammar_effects:
        required.append("CA-P-2087")
    require([layer.get("layer") if isinstance(layer, dict) else None for layer in layers] == required, f"{label} complete selected-layer sequence")
    final_decision, final_target, final_confidence = ("unresolved", None, 0.0)
    if baseline is not None:
        final_decision = baseline["decision"]
        final_target = baseline["proposed_value"]
        final_confidence = float(baseline["confidence"])
    for index, layer in enumerate(layers):
        require(isinstance(layer, dict), f"{label} layer mapping")
        task = layer.get("layer")
        if task == "baseline":
            require(index == 0 and layer.get("accepted") is False, f"{label} baseline lineage only")
            require(layer.get("decision") == final_decision and layer.get("proposed_value") == final_target, f"{label} baseline decision/target")
        elif task == "CA-P-2087":
            require(index == len(layers) - 1 and layer.get("status") == "not_independently_accepted", f"{label} grammar recheck gate")
            require(layer.get("decision") == "unresolved" and layer.get("proposed_value") is None, f"{label} grammar recheck null")
            final_decision, final_target, final_confidence = "unresolved", None, 0.0
        else:
            require(isinstance(task, str) and task in layer_rows, f"{label} known accepted layer")
            rank = layer.get("priority")
            require(rank == LAYER_PRIORITY.index(task) + 1, f"{label} accepted layer priority")
            expected = layer_rows[task].get(row["occurrence_id"])
            require(expected is not None, f"{label} selected layer occurrence")
            decision, target, confidence = expected
            require(layer.get("decision") == decision and layer.get("proposed_value") == target, f"{label} layer target")
            final_decision, final_target, final_confidence = decision, target, confidence
    require(row.get("decision") == final_decision, f"{label} final selected-layer decision")
    require(row.get("proposed_value") == final_target, f"{label} final selected-layer target")
    require(row.get("confidence") == final_confidence, f"{label} final selected-layer confidence")


def _verify_rows(
    root: Path,
    rows: Any,
    expected: list[dict[str, Any]],
    baseline_rows: dict[str, dict[str, Any]],
    layer_rows: dict[str, dict[str, tuple[str, str | None, float]]],
    actor_targets: dict[str, str],
    grammar_effects: dict[str, dict[str, Any]],
) -> dict[str, int]:
    require(isinstance(rows, list), "ledger rows list")
    expected_by_id = {row["occurrence_id"]: row for row in expected}
    actual_by_id: dict[str, dict[str, Any]] = {}
    for number, row in enumerate(rows):
        label = f"ledger row {number}"
        require(isinstance(row, dict), f"{label} mapping")
        occurrence_id = row.get("occurrence_id")
        require(isinstance(occurrence_id, str) and occurrence_id in expected_by_id, f"{label} expected occurrence")
        require(occurrence_id not in actual_by_id, f"{label} duplicate occurrence")
        actual_by_id[occurrence_id] = row
    require(set(actual_by_id) == set(expected_by_id), "exact current occurrence coverage")
    counts = {"proposed": 0, "unchanged": 0, "unresolved": 0}
    for occurrence_id, expected_row in expected_by_id.items():
        row = actual_by_id[occurrence_id]
        label = f"ledger occurrence {occurrence_id}"
        require({key: row.get(key) for key in expected_row} == expected_row, f"{label} exact current origin/pin")
        decision = row.get("decision")
        require(decision in counts, f"{label} explicit decision")
        target = row.get("proposed_value")
        if decision == "proposed":
            require(isinstance(target, str) and target.strip(), f"{label} proposal target")
            require(FORBIDDEN_TARGET_RE.search(target) is None and "selector" not in target.lower(), f"{label} inferred selector or at target")
            require(isinstance(row.get("confidence"), (int, float)) and not isinstance(row.get("confidence"), bool) and .9 <= row["confidence"] <= 1, f"{label} proposal confidence")
        elif decision == "unchanged":
            require(isinstance(target, str) and target.strip(), f"{label} unchanged target")
            require(isinstance(row.get("confidence"), (int, float)) and not isinstance(row.get("confidence"), bool) and .9 <= row["confidence"] <= 1, f"{label} unchanged confidence")
        else:
            require(target is None, f"{label} explicit null target")
            require(isinstance(row.get("confidence"), (int, float)) and not isinstance(row.get("confidence"), bool) and 0 <= row["confidence"] < .9, f"{label} non-proposal confidence")
        require(row.get("executable") is False, f"{label} non-executable")
        require(isinstance(row.get("reason"), str) and row["reason"].strip(), f"{label} reason")
        baseline = _verify_lineage(row, expected_row, baseline_rows, grammar_effects, label)
        _verify_layers(row, label, layer_rows, baseline, grammar_effects)
        if occurrence_id in actor_targets:
            require(decision == "proposed" and target == actor_targets[occurrence_id], f"{label} Actor canonical target")
        if decision != "unresolved":
            evidence = row.get("evidence")
            require(isinstance(evidence, list) and any(_span_matches(root, item, expected_row, label) for item in evidence), f"{label} live current source span")
        counts[decision] += 1
    return counts


def _layer_path(task: str) -> Path:
    if task == "CA-P-2048":
        return STAGE2_REL / "supplements/substance.review.json"
    suffix = ".review.json" if task in {"CA-P-2072", "CA-P-2073", "CA-P-2074", "CA-P-2075", "CA-P-2076"} else ".research.json"
    return STAGE2_REL / "semantic-reviews" / f"task-{task.removeprefix('CA-P-')}{suffix}"


def _descriptor(path: Path, relative: Path) -> dict[str, str]:
    return {"path": relative.as_posix(), "sha256": sha(path.read_bytes())}


def _read_baseline_rows(root: Path, ledger: dict[str, Any]) -> dict[str, dict[str, Any]]:
    path = relative_path(root, BASELINE_REL.as_posix(), "frozen baseline")
    baseline = read_json(path, "frozen baseline")
    pins = ledger.get("input_pins")
    require(isinstance(pins, dict) and pins.get("baseline") == _descriptor(path, BASELINE_REL), "frozen baseline pin")
    rows = baseline.get("occurrences")
    require(isinstance(rows, list), "frozen baseline occurrences")
    mapped: dict[str, dict[str, Any]] = {}
    for number, row in enumerate(rows):
        require(isinstance(row, dict) and isinstance(row.get("occurrence_id"), str), f"frozen baseline row {number}")
        occurrence_id = row["occurrence_id"]
        require(occurrence_id not in mapped, "frozen baseline duplicate occurrence")
        require(row.get("decision") in {"unchanged", "proposed", "unresolved"}, f"frozen baseline decision {occurrence_id}")
        mapped[occurrence_id] = row
    return mapped


def _grammar_effects(root: Path, ledger: dict[str, Any]) -> dict[str, dict[str, Any]]:
    path = relative_path(root, GRAMMAR_DRIFT_REL.as_posix(), "grammar drift")
    drift = read_json(path, "grammar drift")
    pins = ledger.get("input_pins")
    require(isinstance(pins, dict) and pins.get("grammar_drift") == _descriptor(path, GRAMMAR_DRIFT_REL), "grammar drift pin")
    records = drift.get("changed_or_missing")
    require(isinstance(records, list) and len(records) == 5, "five grammar effects")
    effects: dict[str, dict[str, Any]] = {}
    for number, record in enumerate(records):
        require(isinstance(record, dict) and record.get("classified") == "approved_grammar_effect", f"grammar effect {number}")
        atom_id = record.get("atom_id")
        effect = record.get("declared_effect")
        require(isinstance(atom_id, str) and isinstance(effect, dict), f"grammar effect {number} shape")
        if effect.get("operation") == "replace_with_new_id":
            after = effect.get("after")
            require(isinstance(after, dict) and isinstance(after.get("atom_id"), str), f"grammar replacement {number}")
            effects[after["atom_id"]] = effect
        else:
            require(effect.get("operation") == "revise_active_atom", f"grammar revision {number}")
            effects[atom_id] = effect
    require(len(effects) == 5, "five current grammar source identities")
    return effects


def _verify_receipt(task: str, kind: str, receipt: dict[str, Any], report_pin: dict[str, str]) -> None:
    require(receipt.get("task") == task and isinstance(receipt.get("result"), str) and receipt["result"].startswith("PASS"), f"accepted receipt identity {task}")
    if task == "CA-P-2048":
        checks = receipt.get("checks")
        require(receipt.get("output") == report_pin and isinstance(checks, dict), "CA-P-2048 output receipt")
        require(str(checks.get("independent_semantic_review", "")).startswith("PASS") and str(checks.get("independent_supplement_checker", "")).startswith("PASS"), "CA-P-2048 independent acceptance")
        return
    verification = receipt.get("verification")
    require(receipt.get("non_authoritative") is True and isinstance(verification, dict) and verification.get("task") == task, f"accepted receipt boundary {task}")
    if kind == "semantic":
        require(verification.get("review") == report_pin, f"semantic receipt output {task}")
        require(isinstance(receipt.get("review_method"), str) and "Independent" in receipt["review_method"], f"semantic receipt review method {task}")
        return
    require(verification.get("output") == report_pin and isinstance(verification.get("result"), str) and verification["result"].startswith("PASS"), f"research receipt output {task}")
    independent = receipt.get("independent_review")
    require(isinstance(independent, dict) and isinstance(independent.get("result"), str) and independent["result"].startswith("PASS"), f"research receipt independent review {task}")
    reviewed_sha = independent.get("reviewed_output_sha256")
    if reviewed_sha != report_pin["sha256"]:
        normalized = receipt.get("formatting_normalization")
        normalized_reviewed = normalized.get("reviewed_output_sha256") if isinstance(normalized, dict) else None
        if normalized_reviewed is None and isinstance(normalized, dict):
            normalized_reviewed = normalized.get("independently_reviewed_output_sha256")
        require(isinstance(normalized, dict) and normalized_reviewed == reviewed_sha and normalized.get("final_output_sha256") == report_pin["sha256"] and normalized.get("exact_reverse_hash_and_json_value_equality") == "PASS", f"research receipt normalization {task}")


def _read_actor_targets(root: Path, ledger: dict[str, Any]) -> dict[str, str]:
    pins = ledger.get("input_pins")
    accepted = pins.get("accepted_layers") if isinstance(pins, dict) else None
    require(isinstance(accepted, list) and len(accepted) == len(LAYER_SPECS) + 1, "Actor accepted manifest")
    item = accepted[-1]
    require(isinstance(item, dict) and item.get("task") == "CA-P-2058" and item.get("priority") == "coverage_only" and item.get("kind") == "canonical_target_check" and item.get("rows") == 43, "Actor subset manifest")
    report_path = relative_path(root, ACTOR_SUBSET_REL.as_posix(), "Actor subset")
    report = read_json(report_path, "Actor subset")
    report_pin = _descriptor(report_path, ACTOR_SUBSET_REL)
    require(item.get("report") == report_pin and report.get("task_id") == "CA-P-2058", "Actor subset report pin")
    receipt_rel = STAGE2_REL / "task-2058.receipt.json"
    receipt_path = relative_path(root, receipt_rel.as_posix(), "Actor subset receipt")
    receipt = read_json(receipt_path, "Actor subset receipt")
    require(item.get("receipt") == _descriptor(receipt_path, receipt_rel), "Actor subset receipt pin")
    checks = receipt.get("checks")
    require(receipt.get("task") == "CA-P-2058" and isinstance(receipt.get("result"), str) and receipt["result"].startswith("PASS") and receipt.get("non_authoritative") is True and receipt.get("output") == report_pin and isinstance(checks, dict) and str(checks.get("independent_baseline_selection", "")).startswith("PASS"), "Actor subset accepted receipt")
    rows = report.get("rows")
    require(isinstance(rows, list) and len(rows) == 43, "Actor subset exact coverage")
    targets: dict[str, str] = {}
    for number, row in enumerate(rows):
        require(isinstance(row, dict) and isinstance(row.get("occurrence_id"), str) and isinstance(row.get("proposed_value"), str) and row.get("executable") is False, f"Actor subset row {number}")
        occurrence_id = row["occurrence_id"]
        require(occurrence_id not in targets, "Actor subset duplicate occurrence")
        targets[occurrence_id] = row["proposed_value"]
    require({target: list(targets.values()).count(target) for target in set(targets.values())} == {"Actor.Type: Operator": 33, "Actor.Type: AI Agent": 10}, "Actor subset canonical targets")
    return targets


def _read_layer_rows(root: Path, ledger: dict[str, Any]) -> dict[str, dict[str, tuple[str, str | None, float]]]:
    pins = ledger.get("input_pins")
    require(isinstance(pins, dict), "ledger input pins")
    accepted = pins.get("accepted_layers")
    require(isinstance(accepted, list) and len(accepted) == len(LAYER_SPECS) + 1, "accepted layer manifest coverage")
    output: dict[str, dict[str, tuple[str, str | None, float]]] = {}
    for position, (task, kind) in enumerate(LAYER_SPECS):
        item = accepted[position]
        require(isinstance(item, dict) and item.get("task") == task and item.get("priority") == position + 1 and item.get("kind") == kind, f"accepted layer manifest {task}")
        relative = _layer_path(task)
        report_path = relative_path(root, relative.as_posix(), f"layer {task} report")
        report = read_json(report_path, f"layer {task} report")
        report_pin = {"path": relative.as_posix(), "sha256": sha(report_path.read_bytes())}
        require(item.get("report") == report_pin, f"accepted layer report pin {task}")
        receipt_relative = STAGE2_REL / f"task-{task.removeprefix('CA-P-')}.receipt.json"
        receipt_path = relative_path(root, receipt_relative.as_posix(), f"layer {task} receipt")
        receipt_pin = _descriptor(receipt_path, receipt_relative)
        require(item.get("receipt") == receipt_pin, f"accepted layer receipt pin {task}")
        _verify_receipt(task, kind, read_json(receipt_path, f"layer {task} receipt"), report_pin)
        rows = report.get("occurrences") if kind == "substance" else report.get("rows")
        require(isinstance(rows, list) and item.get("rows") == len(rows), f"accepted layer row count {task}")
        mapped: dict[str, tuple[str, str | None, float]] = {}
        for row_number, row in enumerate(rows):
            require(isinstance(row, dict) and isinstance(row.get("occurrence_id"), str), f"layer {task} row {row_number}")
            occurrence_id = row["occurrence_id"]
            require(occurrence_id not in mapped, f"layer {task} duplicate ownership")
            mapped[occurrence_id] = _normalized_layer_row(kind, row, f"layer {task} row {row_number}")
        output[task] = mapped
    return output


def verify_working_ledger(root: Path = ROOT) -> dict[str, Any]:
    """Verify the persisted derived ledger without importing its producer."""

    expected = enumerate_current_frontier(root)
    ledger_path = relative_path(root, LEDGER_REL.as_posix(), "working ledger")
    frontier_path = relative_path(root, FRONTIER_REL.as_posix(), "current frontier")
    diagnostics_path = relative_path(root, DIAGNOSTICS_REL.as_posix(), "working diagnostics")
    ledger = read_json(ledger_path, "working ledger")
    frontier = read_json(frontier_path, "current frontier")
    diagnostics = read_json(diagnostics_path, "working diagnostics")
    _verify_frontier(root, frontier, expected)
    require(ledger.get("schema_version") == 1, "ledger schema version")
    require(ledger.get("non_authoritative") is True, "ledger non-authoritative")
    require(ledger.get("source_migration") == "not_performed", "ledger source migration")
    require(ledger.get("native_admission") == "not_performed", "ledger native admission")
    require(ledger.get("layer_priority") == LAYER_PRIORITY, "ledger accepted layer priority")
    require(ledger.get("source_reviews") == [_source_view(source) for source in expected["selected_sources"]], "ledger exact current source pins")
    require(ledger.get("remaining_gaps", {}).get("diagnostics_path") == DIAGNOSTICS_REL.as_posix(), "ledger diagnostics reference")
    require(diagnostics.get("schema_version") == 1 and diagnostics.get("non_authoritative") is True, "diagnostics envelope")
    require(diagnostics.get("excluded_sources") == frontier.get("excluded_sources"), "diagnostics exclusions")
    require(diagnostics.get("counts", {}).get("quarantined_sources") == sum(source["quarantined"] for source in expected["selected_sources"]), "diagnostics quarantines")
    baseline_rows = _read_baseline_rows(root, ledger)
    grammar_effects = _grammar_effects(root, ledger)
    layer_rows = _read_layer_rows(root, ledger)
    actor_targets = _read_actor_targets(root, ledger)
    counts = _verify_rows(root, ledger.get("occurrences"), expected["occurrences"], baseline_rows, layer_rows, actor_targets, grammar_effects)
    actual_counts = ledger.get("counts")
    require(isinstance(actual_counts, dict), "ledger counts")
    require(actual_counts.get("sources") == len(expected["selected_sources"]) and actual_counts.get("occurrences") == len(expected["occurrences"]), "ledger exact coverage counts")
    require(actual_counts.get("decisions") == dict(sorted(counts.items())) and actual_counts.get("unresolved") == counts["unresolved"], "ledger exact decision counts")
    require(actual_counts.get("quarantined_sources") == sum(source["quarantined"] for source in expected["selected_sources"]), "ledger quarantine count")
    return {"outcome": "PASS", "sources": len(expected["selected_sources"]), "occurrences": len(expected["occurrences"]), **counts, "quarantined_sources": actual_counts["quarantined_sources"], "excluded_sources": len(frontier["excluded_sources"])}


def main() -> None:
    parser = argparse.ArgumentParser(description="Verify the one-off working Subject ledger.")
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    print(json.dumps(verify_working_ledger(args.root.resolve()), sort_keys=True))


if __name__ == "__main__":
    main()
