#!/usr/bin/env python3
"""Deterministic, read-only inventory of current Core RMEDO Subject fields."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import tomllib
from collections import defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[5]
STRUCTURE_RELATIVE = Path(".caprmedio_caprmedio/project_structure.toml")
OUT = ROOT / ".caprmedio_caprmedio/_projection/core-entity-review/stage2"
PIN_RELATIVE_PATHS = (
    Path(".caprmedio_caprmedio/_projection/core-entity-review/presentation/operator.entity-graph.candidate.json"),
    Path(".caprmedio_caprmedio/_projection/core-entity-review/consolidated/nodes.review.json"),
    Path(".caprmedio_caprmedio/_projection/core-entity-review/consolidated/contract.md"),
    Path(".caprmedio_caprmedio/_projection/core-entity-review/baseline.inventory.json"),
)
sys.path.insert(0, str(ROOT / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/VALIDATE_ATOMS"))
from validate_atoms_workers.parsing import CarrierError, parse_carrier


ROLES = {
    "Requirement": "R",
    "Method": "M",
    "Evaluation": "E",
    "Delivery": "D",
    "Operations": "O",
}
ROLE_DIRS = {
    "04_requirement": "Requirement",
    "05_method": "Method",
    "06_evaluation": "Evaluation",
    "07_delivery": "Delivery",
    "09_operations": "Operations",
    "09_ops": "Operations",
}
SUBJECT_FIELDS = ("governs", "depends_on")
ATOM_ID = re.compile(r"CA-([RMEDO])-\d+")
FILENAME_ATOM_ID = re.compile(r"^(CA-([RMEDO])-\d+)(?:-|$)")
UPDATED_AT = re.compile(
    r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} (?:[+-]\d{4}|[+-]\d{2}:\d{2}|Z)$"
)


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def json_bytes(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=True, indent=2, sort_keys=True).encode("utf-8") + b"\n"


def checked_relative_path(relative: str | Path, label: str) -> Path:
    """Resolve one repository-relative, non-symlink path without traversal."""

    value = Path(relative)
    if value.is_absolute() or ".." in value.parts:
        raise SystemExit(f"unsafe {label} path: {relative}")
    candidate = ROOT / value
    if candidate.is_symlink():
        raise SystemExit(f"unsafe {label} symlink: {candidate}")
    try:
        candidate.resolve(strict=False).relative_to(ROOT.resolve())
    except ValueError as error:
        raise SystemExit(f"unsafe {label} path outside repository: {relative}") from error
    return candidate


def required_pin(relative: Path, label: str) -> dict[str, str]:
    path = checked_relative_path(relative, label)
    if not path.is_file() or path.is_symlink():
        raise SystemExit(f"missing required {label}: {path}")
    return {"path": relative.as_posix(), "sha256": sha(path.read_bytes())}


def updated_at(frontmatter: str) -> tuple[str | None, str]:
    match = re.search(r"(?m)^updated_at:\s*(.*?)\s*$", frontmatter)
    if not match:
        return None, "missing"
    token = match.group(1).strip()
    return token.strip("\"'"), "quoted" if token[:1] in "\"'" else "plain"


def filename_atom_id(path: Path) -> tuple[str | None, str | None]:
    match = FILENAME_ATOM_ID.match(path.stem)
    return (match.group(1), match.group(2)) if match else (None, None)


def directory_role(source_root: Path, path: Path) -> str | None:
    for component in path.relative_to(source_root).parts[:-1]:
        if component in ROLE_DIRS:
            return ROLE_DIRS[component]
    return None


def source_files(source_root: Path) -> list[Path]:
    root_resolved = source_root.resolve()
    files: list[Path] = []
    for path in sorted(source_root.rglob("*.md")):
        if path.is_symlink():
            raise SystemExit(f"unsafe authority markdown symlink: {path}")
        try:
            path.resolve(strict=True).relative_to(root_resolved)
        except (FileNotFoundError, ValueError) as error:
            raise SystemExit(f"unsafe authority markdown path: {path}") from error
        if path.is_file():
            files.append(path)
    return files


def excluded_source(relative_path: str, reason: str, metadata: dict[str, Any] | None = None) -> dict[str, Any]:
    item: dict[str, Any] = {"relative_path": relative_path, "reason": reason}
    if metadata is not None:
        item.update(
            {
                "content_role": metadata.get("content_role"),
                "current_scope_unit": metadata.get("current_scope_unit"),
                "status": metadata.get("status"),
            }
        )
    return item


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--persist", action="store_true")
    args = parser.parse_args()

    structure = checked_relative_path(STRUCTURE_RELATIVE, "authoritative Structure")
    if not structure.is_file():
        raise SystemExit(f"missing authoritative structure: {structure}")
    try:
        config = tomllib.loads(structure.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, tomllib.TOMLDecodeError) as error:
        raise SystemExit("authoritative Structure is not readable TOML") from error
    units = config.get("scope_units") if isinstance(config, dict) else None
    matches = [
        unit
        for unit in units or []
        if isinstance(unit, dict) and unit.get("scope_unit_name") == "CORE_META_MODEL"
    ]
    if len(matches) != 1 or not isinstance(matches[0].get("authority_path"), str):
        raise SystemExit("CORE_META_MODEL authority_path missing or ambiguous")
    source_root = checked_relative_path(matches[0]["authority_path"], "CORE_META_MODEL authority")
    if not source_root.is_dir() or source_root.is_symlink():
        raise SystemExit(f"missing CORE_META_MODEL authority directory: {source_root}")

    selected: list[dict[str, Any]] = []
    excluded: list[dict[str, Any]] = []
    diagnostics: list[dict[str, Any]] = []
    pending_occurrences: list[tuple[dict[str, Any], list[tuple[str, int | None, str]]]] = []

    for path in source_files(source_root):
        relative_path = path.relative_to(ROOT).as_posix()
        if "archive" in path.relative_to(source_root).parts:
            excluded.append(excluded_source(relative_path, "archived_lifecycle_copy"))
            continue

        raw = path.read_bytes()
        try:
            parsed = parse_carrier(raw, path)
            metadata = parsed.metadata
        except CarrierError as error:
            filename_id, role_code = filename_atom_id(path)
            if filename_id is None or role_code is None:
                excluded.append(
                    {
                        "relative_path": relative_path,
                        "reason": "strict_parse_error",
                        "code": error.code,
                        "detail": str(error),
                    }
                )
                continue
            selected.append(
                {
                    "relative_path": relative_path,
                    "full_file_sha256": sha(raw),
                    "atom_id": None,
                    "filename_atom_id": filename_id,
                    "version": None,
                    "role": next(role for role, code in ROLES.items() if code == role_code),
                    "owner": None,
                    "author": None,
                    "status": None,
                    "updated_at": None,
                    "updated_at_type": "unavailable",
                    "quarantined": True,
                    "findings": [f"strict_parse_error:{error.code}"],
                }
            )
            pending_occurrences.append((selected[-1], []))
            continue

        role = metadata.get("content_role")
        owner = metadata.get("current_scope_unit")
        status = metadata.get("status")
        if owner != "CORE_META_MODEL":
            excluded.append(excluded_source(relative_path, "owner_mismatch", metadata))
            diagnostics.append(
                {
                    "relative_path": relative_path,
                    "code": "owner_mismatch",
                    "expected": "CORE_META_MODEL",
                    "actual": owner,
                }
            )
            continue
        if status != "Active":
            excluded.append(excluded_source(relative_path, "not_active_lifecycle", metadata))
            continue
        if role not in ROLES:
            excluded.append(excluded_source(relative_path, "not_rmedo_role", metadata))
            continue

        raw_updated_at, _ = updated_at(parsed.frontmatter)
        parsed_updated_at = metadata.get("updated_at")
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
        expected_directory_role = directory_role(source_root, path)
        if expected_directory_role != role:
            findings.append("directory_role_mismatch")
        version = metadata.get("version")
        if not isinstance(version, int) or isinstance(version, bool) or version <= 0:
            findings.append("missing_or_invalid_version")
        if raw_updated_at is None:
            findings.append("missing_updated_at")
        if not isinstance(parsed_updated_at, str) or not UPDATED_AT.fullmatch(raw_updated_at or ""):
            findings.append("updated_at_invalid_or_naive")

        subjects = metadata.get("subjects")
        valid_fields: list[tuple[str, int | None, str]] = []
        if not isinstance(subjects, dict):
            findings.append("subjects_not_mapping")
            subjects = {}
        else:
            for field in sorted(set(subjects).difference(SUBJECT_FIELDS)):
                findings.append(f"unknown_subjects_field:{field}")
        governs = subjects.get("governs")
        if isinstance(governs, str) and governs.strip():
            valid_fields.append(("governs", None, governs))
        else:
            findings.append("governs_missing_or_invalid")
        depends_on = subjects.get("depends_on")
        if depends_on is not None:
            if (
                isinstance(depends_on, list)
                and all(isinstance(value, str) and value.strip() for value in depends_on)
                and len(set(depends_on)) == len(depends_on)
            ):
                valid_fields.extend(("depends_on", index, value) for index, value in enumerate(depends_on))
            else:
                findings.append("depends_on_missing_or_invalid_unique_string_list")

        selected.append(
            {
                "relative_path": relative_path,
                "full_file_sha256": sha(raw),
                "atom_id": atom_id,
                "version": version,
                "role": role,
                "owner": owner,
                "author": metadata.get("author"),
                "status": status,
                "updated_at": raw_updated_at,
                "updated_at_type": type(parsed_updated_at).__name__,
                "quarantined": False,
                "findings": findings,
            }
        )
        pending_occurrences.append((selected[-1], valid_fields))

    selected.sort(key=lambda item: item["relative_path"])
    by_atom_id: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for source in selected:
        atom_id = source["atom_id"]
        if isinstance(atom_id, str) and ATOM_ID.fullmatch(atom_id):
            by_atom_id[atom_id].append(source)
    for atom_id, sources in by_atom_id.items():
        if len(sources) > 1:
            for source in sources:
                source["findings"].append("duplicate_atom_id")
            diagnostics.append(
                {
                    "code": "duplicate_atom_id",
                    "atom_id": atom_id,
                    "relative_paths": [source["relative_path"] for source in sources],
                }
            )

    occurrences: list[dict[str, Any]] = []
    for source, valid_fields in pending_occurrences:
        source["quarantined"] = bool(source["findings"])
        for field, index, old_value in valid_fields:
            suffix = f"subjects.{field}" + (f"[{index}]" if index is not None else "")
            occurrences.append(
                {
                    "occurrence_id": f"{source['relative_path']}#{suffix}",
                    "source_path": source["relative_path"],
                    "source_atom_id": source["atom_id"],
                    "source_version": source["version"],
                    "source_sha256": source["full_file_sha256"],
                    "field": field,
                    "index": index,
                    "old_value": old_value,
                    "quarantined": source["quarantined"],
                }
            )
    excluded.sort(key=lambda item: item["relative_path"])
    diagnostics.sort(key=lambda item: (item.get("relative_path", ""), item["code"]))
    occurrences.sort(key=lambda item: item["occurrence_id"])

    pins = {"structure": required_pin(STRUCTURE_RELATIVE, "authoritative Structure")}
    for relative in PIN_RELATIVE_PATHS:
        pins[relative.as_posix()] = required_pin(relative, f"required input {relative}")
    inventory = {
        "schema_version": 1,
        "non_authoritative": True,
        "source_migration": "not_performed",
        "native_admission": "not_performed",
        "input_pins": pins,
        "selected_sources": selected,
        "excluded_sources": excluded,
        "diagnostics": diagnostics,
        "occurrences": occurrences,
    }
    inventory_bytes = json_bytes(inventory)
    inventory_sha = sha(inventory_bytes)

    occurrences_by_source: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for occurrence in occurrences:
        occurrences_by_source[occurrence["source_path"]].append(occurrence)
    groups: list[list[dict[str, Any]]] = []
    current: list[dict[str, Any]] = []
    current_occurrence_count = 0
    for source in selected:
        count = len(occurrences_by_source[source["relative_path"]])
        if count > 120:
            raise SystemExit(f"oversized source at {source['relative_path']}")
        if current and (len(current) >= 20 or current_occurrence_count + count > 120):
            groups.append(current)
            current = []
            current_occurrence_count = 0
        current.append(source)
        current_occurrence_count += count
    if current:
        groups.append(current)
    if [source["relative_path"] for group in groups for source in group] != [
        source["relative_path"] for source in selected
    ]:
        raise SystemExit("selected source batch coverage is not exact")

    batch_contents: list[tuple[Path, bytes]] = []
    descriptors: list[dict[str, Any]] = []
    for number, sources in enumerate(groups, start=1):
        name = f"current-subjects.batch-{number:03d}.json"
        source_paths = {source["relative_path"] for source in sources}
        batch = {
            "schema_version": 1,
            "batch_id": name.removesuffix(".json"),
            "input_inventory_sha256": inventory_sha,
            "selected_sources": sources,
            "occurrences": [occurrence for occurrence in occurrences if occurrence["source_path"] in source_paths],
        }
        if len(sources) > 20 or len(batch["occurrences"]) > 120:
            raise SystemExit(f"oversized batch: {name}")
        batch_path = OUT / "inputs" / name
        batch_bytes = json_bytes(batch)
        batch_contents.append((batch_path, batch_bytes))
        descriptors.append(
            {
                "path": batch_path.relative_to(ROOT).as_posix(),
                "sha256": sha(batch_bytes),
                "source_count": len(sources),
                "occurrence_count": len(batch["occurrences"]),
            }
        )
    batches = {
        "schema_version": 1,
        "inventory_path": (OUT / "current-subjects.inventory.json").relative_to(ROOT).as_posix(),
        "batches": descriptors,
        "source_count": len(selected),
        "occurrence_count": len(occurrences),
    }

    if args.persist:
        contents = [
            (OUT / "current-subjects.inventory.json", inventory_bytes),
            (OUT / "current-subjects.batches.json", json_bytes(batches)),
            *batch_contents,
        ]
        expected_paths = {path for path, _ in contents}
        inputs = OUT / "inputs"
        if inputs.exists():
            for path in inputs.glob("current-subjects.batch-*.json"):
                if path not in expected_paths:
                    raise SystemExit(f"refusing unexpected existing output: {path}")
        for path, content in contents:
            if path.is_symlink() or (path.exists() and not path.is_file()):
                raise SystemExit(f"refusing non-regular output: {path}")
            if path.exists() and path.read_bytes() != content:
                raise SystemExit(f"refusing different existing output: {path}")
        for path, content in contents:
            if not path.exists():
                path.parent.mkdir(parents=True, exist_ok=True)
                with path.open("xb") as output:
                    output.write(content)
    else:
        timestamp_quarantines = [
            source["atom_id"]
            for source in selected
            if "updated_at_invalid_or_naive" in source["findings"]
        ]
        print(
            json.dumps(
                {
                    "batch_count": len(groups),
                    "diagnostic_count": len(diagnostics),
                    "excluded_count": len(excluded),
                    "occurrence_count": len(occurrences),
                    "quarantined_source_count": sum(source["quarantined"] for source in selected),
                    "quarantined_source_ids": [
                        source["atom_id"]
                        for source in selected
                        if source["quarantined"]
                    ],
                    "source_count": len(selected),
                    "timestamp_quarantine_count": len(timestamp_quarantines),
                    "timestamp_quarantine_ids": timestamp_quarantines,
                },
                sort_keys=True,
            )
        )


if __name__ == "__main__":
    main()
