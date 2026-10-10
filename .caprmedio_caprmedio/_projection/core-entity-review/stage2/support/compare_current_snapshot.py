#!/usr/bin/env python3
"""Create-only byte/evidence comparison of current Core RMEDO against the frozen capture."""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
import sys
import tomllib
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[5]
STAGE2 = ROOT / ".caprmedio_caprmedio/_projection/core-entity-review/stage2"
OUTPUT = STAGE2 / "current-snapshot.delta.json"
STRUCTURE = ROOT / ".caprmedio_caprmedio/project_structure.toml"
BASELINE = ROOT / ".caprmedio_caprmedio/_projection/core-entity-review/baseline.inventory.json"
SNAPSHOT_SUPPORT = (
    ROOT / ".caprmedio_caprmedio/_projection/core-entity-review/nodes/support"
)
VALIDATE_ATOMS = ROOT / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/VALIDATE_ATOMS"
ROLES = {"Requirement", "Method", "Evaluation", "Delivery", "Operations"}
EXCLUDED_DIRS = {"archive", "archived", "drafts", "resolved"}

sys.path.insert(0, str(VALIDATE_ATOMS))
sys.path.insert(0, str(SNAPSHOT_SUPPORT))

from validate_atoms_workers.parsing import CarrierError, ParsedCarrier, parse_carrier  # noqa: E402
import snapshot_sources  # noqa: E402


def sha_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")


def digest(value: Any) -> str:
    return sha_bytes(canonical_bytes(value))


def file_pin(path: Path, kind: str) -> dict[str, Any]:
    if not path.is_file() or path.is_symlink():
        raise RuntimeError(f"required pin is not a regular file: {path}")
    raw = path.read_bytes()
    return {
        "kind": kind,
        "path": path.relative_to(ROOT).as_posix(),
        "sha256": sha_bytes(raw),
        "bytes": len(raw),
    }


def load_current_source_root() -> tuple[str, Path, dict[str, Any]]:
    structure_raw = STRUCTURE.read_bytes()
    structure = tomllib.loads(structure_raw.decode("utf-8"))
    matches = [
        row
        for row in structure.get("scope_units", [])
        if row.get("scope_unit_name") == "CORE_META_MODEL"
    ]
    if len(matches) != 1:
        raise RuntimeError(f"expected one CORE_META_MODEL declaration, got {len(matches)}")
    authority_path = matches[0].get("authority_path")
    if not isinstance(authority_path, str) or authority_path.startswith("/"):
        raise RuntimeError("CORE_META_MODEL authority_path must be a relative string")
    source_root = ROOT / authority_path
    if source_root.is_symlink() or not source_root.is_dir():
        raise RuntimeError(f"current authority path is unavailable or symlinked: {source_root}")
    return authority_path, source_root, matches[0]


def subject_stats(metadata: dict[str, Any]) -> tuple[str | None, int | None, str | None]:
    subjects = metadata.get("subjects")
    if not isinstance(subjects, dict):
        return None, None, "subjects_not_mapping"
    count = 0
    for field in ("governs", "depends_on"):
        value = subjects.get(field)
        if isinstance(value, str):
            count += 1
        elif isinstance(value, list):
            for item in value:
                if not isinstance(item, str):
                    return None, None, f"{field}_contains_non_string"
            count += len(value)
        elif value is not None:
            return None, None, f"{field}_invalid"
    try:
        return digest(subjects), count, None
    except (TypeError, ValueError):
        return None, None, "subjects_not_json_serializable"


def parsed_summary(
    *,
    atom_id: str,
    path: str,
    raw: bytes,
    parsed: ParsedCarrier,
    role: str | None,
    status: str | None,
    scope: str | None,
    source_kind: str,
) -> tuple[dict[str, Any], str | None]:
    subjects_sha, occurrence_count, subject_error = subject_stats(parsed.metadata)
    body_raw = parsed.body.encode("utf-8")
    record = {
        "atom_id": atom_id,
        "source_kind": source_kind,
        "relative_path": path,
        "version": parsed.metadata.get("version"),
        "role": role,
        "status": status,
        "current_scope_unit": scope,
        "full_file_sha256": sha_bytes(raw),
        "subjects_sha256": subjects_sha,
        "subject_occurrence_count": occurrence_count,
        "main_content_sha256": sha_bytes(body_raw),
        "main_content_bytes": len(body_raw),
    }
    return record, subject_error


def discover_current(source_root: Path) -> tuple[dict[str, dict[str, Any]], dict[str, Any]]:
    selected: dict[str, dict[str, Any]] = {}
    excluded_reasons: collections.Counter[str] = collections.Counter()
    parse_errors: list[dict[str, str]] = []
    invalid_selected: list[dict[str, str]] = []
    duplicate_ids: list[dict[str, str]] = []
    scanned = 0

    for path in sorted(source_root.rglob("*.md")):
        if any(part.lower() in EXCLUDED_DIRS for part in path.relative_to(source_root).parts):
            continue
        scanned += 1
        raw = path.read_bytes()
        relative_path = path.relative_to(ROOT).as_posix()
        try:
            parsed = parse_carrier(raw, path)
        except CarrierError as error:
            parse_errors.append(
                {"relative_path": relative_path, "code": error.code}
            )
            continue

        metadata = parsed.metadata
        role = metadata.get("content_role")
        status = metadata.get("status")
        scope = metadata.get("current_scope_unit")
        if role not in ROLES or status != "Active" or scope != "CORE_META_MODEL":
            if role not in ROLES:
                excluded_reasons["role_not_RMEDO"] += 1
            elif status != "Active":
                excluded_reasons["status_not_Active"] += 1
            else:
                excluded_reasons["scope_not_CORE_META_MODEL"] += 1
            continue

        atom_id = metadata.get("atom_id")
        if not isinstance(atom_id, str) or not atom_id:
            invalid_selected.append(
                {"relative_path": relative_path, "reason": "missing_or_invalid_atom_id"}
            )
            continue
        record, subject_error = parsed_summary(
            atom_id=atom_id,
            path=relative_path,
            raw=raw,
            parsed=parsed,
            role=role,
            status=status,
            scope=scope,
            source_kind="current",
        )
        if subject_error:
            invalid_selected.append(
                {"relative_path": relative_path, "reason": subject_error}
            )
        if atom_id in selected:
            duplicate_ids.append(
                {
                    "atom_id": atom_id,
                    "first_path": selected[atom_id]["relative_path"],
                    "second_path": relative_path,
                }
            )
            continue
        selected[atom_id] = {"record": record, "raw": raw, "parsed": parsed}

    discovery = {
        "source_root": source_root.relative_to(ROOT).as_posix(),
        "scanned_markdown_files": scanned,
        "selected_sources": len(selected),
        "excluded_sources": sum(excluded_reasons.values()),
        "excluded_reasons": dict(sorted(excluded_reasons.items())),
        "parse_errors": parse_errors,
        "invalid_selected": invalid_selected,
        "duplicate_ids": duplicate_ids,
    }
    return selected, discovery


def captured_records() -> tuple[dict[str, dict[str, Any]], dict[str, Any]]:
    pins = {
        atom_id: pin
        for atom_id, pin in snapshot_sources.source_pins().items()
        if pin.get("content_role") in ROLES
        and pin.get("status") == "Active"
        and pin.get("current_scope_unit") == "CORE_META_MODEL"
    }
    selected: dict[str, dict[str, Any]] = {}
    parse_errors: list[dict[str, str]] = []
    invalid_subjects: list[dict[str, str]] = []
    for atom_id, pin in sorted(pins.items()):
        raw = snapshot_sources.read_source(atom_id)
        path = Path(pin["carrier_path"])
        try:
            parsed = parse_carrier(raw, path)
        except CarrierError as error:
            parse_errors.append({"atom_id": atom_id, "code": error.code})
            continue
        record, subject_error = parsed_summary(
            atom_id=atom_id,
            path=pin["carrier_path"],
            raw=raw,
            parsed=parsed,
            role=pin.get("content_role"),
            status=pin.get("status"),
            scope=pin.get("current_scope_unit"),
            source_kind="captured",
        )
        record["baseline_pinned_sha256"] = pin["carrier_sha256"]
        if record["full_file_sha256"] != pin["carrier_sha256"]:
            raise RuntimeError(f"captured pin mismatch after snapshot verification: {atom_id}")
        if subject_error:
            invalid_subjects.append({"atom_id": atom_id, "reason": subject_error})
        selected[atom_id] = {"record": record, "raw": raw, "parsed": parsed}
    return selected, {
        "selected_sources": len(selected),
        "parse_errors": parse_errors,
        "invalid_subjects": invalid_subjects,
    }


def public_set_digest(records: dict[str, dict[str, Any]]) -> str:
    rows = [
        {
            "atom_id": atom_id,
            "path": row["record"]["relative_path"],
            "version": row["record"]["version"],
            "sha256": row["record"]["full_file_sha256"],
        }
        for atom_id, row in sorted(records.items())
    ]
    return digest(rows)


def compare_row(
    atom_id: str,
    current: dict[str, Any],
    captured: dict[str, Any],
) -> dict[str, Any]:
    current_record = current["record"]
    captured_record = captured["record"]
    equality = {
        "bytes": current["raw"] == captured["raw"],
        "subjects": current_record["subjects_sha256"]
        == captured_record["subjects_sha256"],
        "main_content": current_record["main_content_sha256"]
        == captured_record["main_content_sha256"],
    }
    dimensions = [name for name, equal in equality.items() if not equal]
    return {
        "atom_id": atom_id,
        "current": current_record,
        "captured": captured_record,
        "equality": equality,
        "difference_dimensions": dimensions,
    }


def build() -> dict[str, Any]:
    authority_path, source_root, authority_record = load_current_source_root()
    current, current_discovery = discover_current(source_root)
    captured_verification = snapshot_sources.verify_snapshot()
    captured, captured_discovery = captured_records()

    if current_discovery["parse_errors"] or current_discovery["duplicate_ids"]:
        raise RuntimeError("current source discovery has parse errors or duplicate IDs")
    if current_discovery["invalid_selected"]:
        raise RuntimeError("current selected source has invalid metadata or Subjects")
    if captured_discovery["parse_errors"] or captured_discovery["invalid_subjects"]:
        raise RuntimeError("captured selected source cannot be compared safely")

    current_ids = set(current)
    captured_ids = set(captured)
    common_ids = sorted(current_ids & captured_ids)
    same: list[dict[str, Any]] = []
    changed: list[dict[str, Any]] = []
    for atom_id in common_ids:
        row = compare_row(atom_id, current[atom_id], captured[atom_id])
        if row["equality"]["bytes"]:
            same.append(row)
        else:
            changed.append(row)

    new = [
        {"atom_id": atom_id, "current": current[atom_id]["record"], "captured": None}
        for atom_id in sorted(current_ids - captured_ids)
    ]
    missing = [
        {"atom_id": atom_id, "current": None, "captured": captured[atom_id]["record"]}
        for atom_id in sorted(captured_ids - current_ids)
    ]

    baseline = json.loads(BASELINE.read_bytes())
    current_occurrences = sum(
        row["record"]["subject_occurrence_count"] or 0 for row in current.values()
    )
    captured_occurrences = sum(
        row["record"]["subject_occurrence_count"] or 0 for row in captured.values()
    )

    current_pins = [
        file_pin(STRUCTURE, "current_structure"),
        file_pin(
            ROOT
            / ".caprmedio_caprmedio/_projection/core-entity-review/presentation/operator.entity-graph.candidate.json",
            "candidate",
        ),
        file_pin(
            ROOT
            / ".caprmedio_caprmedio/_projection/core-entity-review/consolidated/manifest.json",
            "consolidated_manifest",
        ),
        file_pin(
            ROOT
            / ".caprmedio_caprmedio/_projection/core-entity-review/consolidated/contract.md",
            "consolidated_contract",
        ),
        file_pin(
            ROOT
            / ".caprmedio_caprmedio/_projection/core-entity-review/consolidated/review.summary.txt",
            "consolidated_review_summary",
        ),
    ]
    captured_pins = [
        file_pin(BASELINE, "captured_baseline_inventory"),
        file_pin(
            ROOT
            / ".caprmedio_caprmedio/_projection/core-entity-review/nodes/support/snapshot_sources.py",
            "captured_snapshot_reader",
        ),
        {
            "kind": "captured_git_snapshot",
            "commit": captured_verification["git_commit"],
            "source_pins_checked": captured_verification["source_pins_checked"],
            "verification": captured_verification["verification"],
        },
    ]

    return {
        "schema_version": 1,
        "comparison_kind": "current_core_rmedo_against_captured_snapshot",
        "non_authoritative": True,
        "source_migration": "not_performed",
        "native_admission": "not_performed",
        "semantic_mapping": "not_performed",
        "current_structure": {
            "authority_path": authority_path,
            "scope_unit": authority_record,
            "source_set_sha256": public_set_digest(current),
        },
        "captured_snapshot": {
            "git_commit": captured_verification["git_commit"],
            "source_set_sha256": public_set_digest(captured),
            "baseline_claimed_selected_sources": baseline["counts"]["selected_sources"],
            "baseline_claimed_occurrences": baseline["counts"]["occurrences"],
            "derived_selected_sources": len(captured),
            "derived_occurrences": captured_occurrences,
        },
        "pins": {"current": current_pins, "captured": captured_pins},
        "discovery": {
            "current": current_discovery,
            "captured": captured_discovery,
        },
        "counts": {
            "current_selected_sources": len(current),
            "captured_selected_sources": len(captured),
            "same_exact_bytes": len(same),
            "changed_exact_bytes": len(changed),
            "new_current_ids": len(new),
            "missing_current_ids": len(missing),
            "current_derived_subject_occurrences": current_occurrences,
            "captured_derived_subject_occurrences": captured_occurrences,
        },
        "same": same,
        "changed": changed,
        "new": new,
        "missing": missing,
        "limitations": [
            "The captured snapshot is immutable evidence read from Git commit a971d0e00c33c779f485fc8cad63194894d440fb.",
            "Equality or byte differences do not authorize grammar adoption, Subject migration, or source edits.",
            "Subjects are compared by exact structured-value hash and occurrence count; no Subject value or proposed replacement is emitted.",
            "Main Content is compared by parsed body hash; exact file bytes are compared independently.",
            "The baseline inventory claims 4534 occurrences, while this independent parse derives the captured RMEDO subset count; any discrepancy remains diagnostic rather than silently reconciled.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--persist", action="store_true")
    args = parser.parse_args()
    data = build()
    if args.persist:
        if OUTPUT.exists() or OUTPUT.is_symlink():
            raise SystemExit(f"refusing existing output: {OUTPUT}")
        if STAGE2.is_symlink() or not STAGE2.is_dir():
            raise SystemExit(f"refusing unavailable stage2 output directory: {STAGE2}")
        with OUTPUT.open("xb") as handle:
            handle.write(json.dumps(data, ensure_ascii=False, sort_keys=True, indent=2).encode("utf-8"))
            handle.write(b"\n")
    print(
        json.dumps(
            {
                "outcome": "created" if args.persist else "dry_run",
                "output": OUTPUT.relative_to(ROOT).as_posix(),
                "counts": data["counts"],
                "current_source_set_sha256": data["current_structure"]["source_set_sha256"],
                "captured_source_set_sha256": data["captured_snapshot"]["source_set_sha256"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
