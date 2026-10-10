"""Independent read-only verification for the current Subject inventory.

The inventory producer is intentionally not imported here.  This verifier
re-reads the authoritative project structure, enumerates the current Core
authority directory, parses each carrier with the shared strict parser, and
reconstructs every expected source and Subject occurrence before checking the
derived inventory and batches.
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
SUBJECT_FIELDS = ("governs", "depends_on")
ROLE_BY_ID_KIND = {
    "R": "Requirement",
    "M": "Method",
    "E": "Evaluation",
    "D": "Delivery",
    "O": "Operations",
}
ATOM_ID_RE = re.compile(r"^CA-([RMEDO])-([0-9]+)$")
FILENAME_ID_RE = re.compile(r"^(CA-([RMEDO])-[0-9]+)(?:-|$)")
PIN_RELATIVE_PATHS = (
    Path(".caprmedio_caprmedio/_projection/core-entity-review/presentation/operator.entity-graph.candidate.json"),
    Path(".caprmedio_caprmedio/_projection/core-entity-review/consolidated/nodes.review.json"),
    Path(".caprmedio_caprmedio/_projection/core-entity-review/consolidated/contract.md"),
    Path(".caprmedio_caprmedio/_projection/core-entity-review/baseline.inventory.json"),
)


class VerificationError(AssertionError):
    """A deterministic contract failure with a short, actionable label."""


def require(condition: bool, label: str) -> None:
    if not condition:
        raise VerificationError(label)


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def relative_path(root: Path, value: str, label: str) -> Path:
    """Resolve a repository-relative path while rejecting traversal/symlinks."""

    require(isinstance(value, str) and value and not Path(value).is_absolute(), f"{label} relative path")
    path = Path(value)
    require(".." not in path.parts, f"{label} path traversal")
    candidate = root / path
    root_resolved = root.resolve()
    resolved = candidate.resolve(strict=False)
    try:
        resolved.relative_to(root_resolved)
    except ValueError as error:
        raise VerificationError(f"{label} escapes repository root") from error
    probe = root
    try:
        relative = candidate.relative_to(root)
    except ValueError as error:
        raise VerificationError(f"{label} escapes repository root") from error
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
    if not match:
        return None, "missing"
    text = match.group(1).strip()
    value = text.strip("\"'")
    return value, "quoted" if text[:1] in "\"'" else "plain"


def _directory_role(source_root: Path, path: Path) -> str | None:
    for component in path.relative_to(source_root).parts[:-1]:
        if component in ROLE_DIRS:
            return ROLE_DIRS[component]
    return None


def _structure_path(root: Path) -> Path:
    structure = relative_path(root, STRUCTURE_REL.as_posix(), "authoritative Structure")
    require(structure.is_file(), "authoritative Structure exists")
    return structure


def current_authority_path(root: Path) -> tuple[Path, Path]:
    """Return the exact registered CORE_META_MODEL authority directory."""

    structure = _structure_path(root)
    try:
        document = tomllib.loads(structure.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, tomllib.TOMLDecodeError) as error:
        raise VerificationError("authoritative Structure parses as TOML") from error
    units = document.get("scope_units") if isinstance(document, dict) else None
    require(isinstance(units, list), "Structure scope_units list")
    matches = [u for u in units if isinstance(u, dict) and u.get("scope_unit_name") == "CORE_META_MODEL"]
    require(len(matches) == 1, "one CORE_META_MODEL Structure row")
    authority = matches[0].get("authority_path")
    require(isinstance(authority, str) and authority, "CORE_META_MODEL authority_path")
    source_root = relative_path(root, authority, "CORE_META_MODEL authority")
    require(source_root.is_dir(), "CORE_META_MODEL authority directory")
    return structure, source_root


def enumerate_current_sources(root: Path) -> dict[str, Any]:
    """Build the expected selected/excluded source and occurrence rows."""

    structure, source_root = current_authority_path(root)
    files = sorted(source_root.rglob("*.md"))
    selected: list[dict[str, Any]] = []
    excluded: list[dict[str, Any]] = []
    diagnostics: list[dict[str, Any]] = []
    occurrences: list[dict[str, Any]] = []

    for path in files:
        rel = path.relative_to(root).as_posix()
        # Lifecycle history is excluded before parsing.  This is deliberate:
        # archived copies may be legacy or malformed carriers, but their
        # lifecycle location is sufficient evidence for exclusion and must not
        # turn them into selected-source parser failures.
        if "archive" in path.parts:
            excluded.append(
                {
                    "relative_path": rel,
                    "reason": "archived_lifecycle_copy",
                }
            )
            continue
        raw = path.read_bytes()
        try:
            parsed = parse_carrier(raw, path)
            metadata = parsed.metadata
        except CarrierError as error:
            filename_match = FILENAME_ID_RE.match(path.stem)
            if filename_match is not None:
                selected.append(
                    {
                        "relative_path": rel,
                        "full_file_sha256": sha(raw),
                        "atom_id": None,
                        "filename_atom_id": filename_match.group(1),
                        "version": None,
                        "role": ROLE_BY_ID_KIND[filename_match.group(2)],
                        "owner": None,
                        "author": None,
                        "status": None,
                        "updated_at": None,
                        "updated_at_type": "unavailable",
                        "quarantined": True,
                        "findings": [f"strict_parse_error:{error.code}"],
                    }
                )
                continue
            excluded.append(
                {
                    "relative_path": rel,
                    "reason": "strict_parse_error",
                    "code": error.code,
                    "detail": str(error),
                }
            )
            continue

        role = metadata.get("content_role")
        scope = metadata.get("current_scope_unit")
        status = metadata.get("status")
        if scope != "CORE_META_MODEL":
            excluded.append(
                {
                    "relative_path": rel,
                    "reason": "owner_mismatch",
                    "content_role": role,
                    "current_scope_unit": scope,
                    "status": status,
                }
            )
            diagnostics.append(
                {
                    "relative_path": rel,
                    "code": "owner_mismatch",
                    "expected": "CORE_META_MODEL",
                    "actual": scope,
                }
            )
            continue
        if status != "Active":
            excluded.append(
                {
                    "relative_path": rel,
                    "reason": "not_active_lifecycle",
                    "content_role": role,
                    "current_scope_unit": scope,
                    "status": status,
                }
            )
            continue
        if role not in ROLES:
            excluded.append(
                {
                    "relative_path": rel,
                    "reason": "not_rmedo_role",
                    "content_role": role,
                    "current_scope_unit": scope,
                    "status": status,
                }
            )
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
        if (
            not isinstance(metadata.get("version"), int)
            or isinstance(metadata.get("version"), bool)
            or metadata.get("version", 0) <= 0
        ):
            findings.append("missing_or_invalid_version")
        if updated_at is None:
            findings.append("missing_updated_at")
        if not isinstance(metadata.get("updated_at"), str) or not re.search(
            r"(?:[+-]\d{2}:?\d{2}|Z)$", updated_at or ""
        ):
            findings.append("updated_at_invalid_or_naive")

        subjects = metadata.get("subjects")
        valid_fields: list[tuple[str, int | None, str]] = []
        if not isinstance(subjects, dict):
            findings.append("subjects_not_mapping")
            subjects = {}
        for field in SUBJECT_FIELDS:
            value = subjects.get(field)
            if field == "governs":
                if isinstance(value, str) and value.strip():
                    valid_fields.append((field, None, value))
                else:
                    findings.append("governs_missing_or_invalid")
            elif value is not None:
                if (
                    isinstance(value, list)
                    and all(isinstance(item, str) and item.strip() for item in value)
                    and len(set(value)) == len(value)
                ):
                    valid_fields.extend((field, index, item) for index, item in enumerate(value))
                else:
                    findings.append("depends_on_missing_or_invalid_unique_string_list")

        full_sha = sha(raw)
        source = {
            "relative_path": rel,
            "full_file_sha256": full_sha,
            "atom_id": metadata.get("atom_id"),
            "version": metadata.get("version"),
            "role": role,
            "owner": scope,
            "author": metadata.get("author"),
            "status": status,
            "updated_at": updated_at,
            "updated_at_type": type(metadata.get("updated_at")).__name__,
            "quarantined": bool(findings),
            "findings": findings,
        }
        selected.append(source)
        for field, index, old_value in valid_fields:
            suffix = f"subjects.{field}" + (f"[{index}]" if index is not None else "")
            occurrences.append(
                {
                    "occurrence_id": f"{rel}#{suffix}",
                    "source_path": rel,
                    "source_atom_id": metadata.get("atom_id"),
                    "source_version": metadata.get("version"),
                    "source_sha256": full_sha,
                    "field": field,
                    "index": index,
                    "old_value": old_value,
                    "quarantined": bool(findings),
                }
            )

    # Duplicate valid current identities are review findings on every affected
    # source.  They do not disappear from the inventory or silently choose a
    # winner, and their occurrences inherit the source quarantine state.
    id_counts: dict[str, int] = {}
    for source in selected:
        atom_id = source["atom_id"]
        if isinstance(atom_id, str) and ATOM_ID_RE.fullmatch(atom_id):
            id_counts[atom_id] = id_counts.get(atom_id, 0) + 1
    duplicate_ids = {atom_id for atom_id, count in id_counts.items() if count > 1}
    duplicate_paths: set[str] = set()
    for atom_id in sorted(duplicate_ids):
        duplicate_sources = [source for source in selected if source["atom_id"] == atom_id]
        for source in duplicate_sources:
            source["findings"].append("duplicate_atom_id")
            duplicate_paths.add(source["relative_path"])
        diagnostics.append(
            {
                "code": "duplicate_atom_id",
                "atom_id": atom_id,
                "relative_paths": [source["relative_path"] for source in duplicate_sources],
            }
        )

    for source in selected:
        source["quarantined"] = bool(source["findings"])
    for occurrence in occurrences:
        occurrence["quarantined"] = occurrence["source_path"] in duplicate_paths or any(
            source["relative_path"] == occurrence["source_path"] and source["quarantined"]
            for source in selected
        )

    selected.sort(key=lambda item: item["relative_path"])
    excluded.sort(key=lambda item: item["relative_path"])
    diagnostics.sort(key=lambda item: (item.get("relative_path", ""), item["code"]))
    occurrences.sort(key=lambda item: item["occurrence_id"])
    return {
        "structure": structure,
        "source_root": source_root,
        "selected_sources": selected,
        "excluded_sources": excluded,
        "diagnostics": diagnostics,
        "occurrences": occurrences,
    }


def expected_input_pins(root: Path, structure: Path) -> dict[str, dict[str, str]]:
    """Return the required Structure, frozen candidate, and review pins."""

    pins: dict[str, dict[str, str]] = {
        "structure": {
            "path": structure.relative_to(root).as_posix(),
            "sha256": sha(structure.read_bytes()),
        }
    }
    for relative in PIN_RELATIVE_PATHS:
        path = relative_path(root, relative.as_posix(), f"required input {relative}")
        require(path.is_file(), f"required input {relative} exists")
        descriptor = {"path": relative.as_posix(), "sha256": sha(path.read_bytes())}
        pins[relative.as_posix()] = descriptor
    return pins


def _verify_pin_map(root: Path, actual: Any, expected: dict[str, dict[str, str]]) -> None:
    require(isinstance(actual, dict), "input_pins mapping")
    require(actual == expected, "exact Structure/candidate/review input pins")
    for key, descriptor in actual.items():
        require(isinstance(descriptor, dict), f"input pin {key} descriptor")
        require(isinstance(descriptor.get("path"), str), f"input pin {key} path")
        require(isinstance(descriptor.get("sha256"), str), f"input pin {key} sha256")
        require(key == "structure" or key == descriptor.get("path"), f"input pin key {key}")
        path = relative_path(root, descriptor["path"], f"input pin {key}")
        require(path.is_file(), f"input pin {key} file")
        require(sha(path.read_bytes()) == descriptor["sha256"], f"input pin {key} SHA")


def _batch_groups(selected: list[dict[str, Any]], occurrences: list[dict[str, Any]]) -> list[list[dict[str, Any]]]:
    by_source: dict[str, int] = {}
    for occurrence in occurrences:
        by_source[occurrence["source_path"]] = by_source.get(occurrence["source_path"], 0) + 1
    groups: list[list[dict[str, Any]]] = []
    current: list[dict[str, Any]] = []
    current_count = 0
    for source in selected:
        path = source["relative_path"]
        count = by_source.get(path, 0)
        require(count <= 120, f"source occurrence maximum {path}")
        if current and (len(current) >= 20 or current_count + count > 120):
            groups.append(current)
            current = []
            current_count = 0
        current.append(source)
        current_count += count
    if current:
        groups.append(current)
    return groups


def _verify_inventory_shape(inventory: dict[str, Any]) -> None:
    require(inventory.get("schema_version") == 1, "inventory schema_version")
    require(inventory.get("non_authoritative") is True, "inventory non_authoritative")
    require(inventory.get("source_migration") == "not_performed", "inventory source_migration")
    require(inventory.get("native_admission") == "not_performed", "inventory native_admission")
    for key in ("input_pins", "selected_sources", "excluded_sources", "diagnostics", "occurrences"):
        require(key in inventory, f"inventory {key}")
    require(isinstance(inventory["selected_sources"], list), "inventory selected_sources list")
    require(isinstance(inventory["excluded_sources"], list), "inventory excluded_sources list")
    require(isinstance(inventory["occurrences"], list), "inventory occurrences list")
    require(isinstance(inventory["diagnostics"], list), "inventory diagnostics list")


def verify_inventory(
    root: Path = ROOT,
    inventory_path: Path | None = None,
    batches_path: Path | None = None,
    input_dir: Path | None = None,
) -> dict[str, Any]:
    """Verify one inventory and all of its exact, source-preserving batches."""

    root = Path(root).resolve()
    require(root.is_dir(), "repository root exists")
    expected = enumerate_current_sources(root)
    structure = expected["structure"]
    required_pins = expected_input_pins(root, structure)
    inventory_path = inventory_path or root / STAGE2_REL / "current-subjects.inventory.json"
    batches_path = batches_path or root / STAGE2_REL / "current-subjects.batches.json"
    input_dir = input_dir or root / STAGE2_REL / "inputs"
    inventory_path = Path(inventory_path)
    batches_path = Path(batches_path)
    input_dir = Path(input_dir)

    inventory = read_json(inventory_path, "inventory")
    _verify_inventory_shape(inventory)
    _verify_pin_map(root, inventory["input_pins"], required_pins)
    require(inventory["selected_sources"] == expected["selected_sources"], "exact selected source inventory")
    require(inventory["excluded_sources"] == expected["excluded_sources"], "exact excluded source inventory")
    require(inventory["diagnostics"] == expected["diagnostics"], "exact inventory diagnostics")
    require(inventory["occurrences"] == expected["occurrences"], "exact Subject occurrence inventory")

    selected = expected["selected_sources"]
    occurrences = expected["occurrences"]
    expected_inventory_sha = sha(inventory_path.read_bytes())
    groups = _batch_groups(selected, occurrences)
    batches = read_json(batches_path, "batch manifest")
    require(batches.get("schema_version") == 1, "batch manifest schema_version")
    require(
        batches.get("inventory_path") == STAGE2_REL.joinpath("current-subjects.inventory.json").as_posix(),
        "batch manifest inventory_path",
    )
    require(batches.get("source_count") == len(selected), "batch manifest source_count")
    require(batches.get("occurrence_count") == len(occurrences), "batch manifest occurrence_count")
    descriptors = batches.get("batches")
    require(isinstance(descriptors, list) and len(descriptors) == len(groups), "batch manifest batch count")

    seen_sources: list[str] = []
    seen_occurrences: list[str] = []

    for number, (descriptor, group) in enumerate(zip(descriptors, groups), start=1):
        require(isinstance(descriptor, dict), f"batch {number} descriptor object")
        name = f"current-subjects.batch-{number:03d}.json"
        expected_rel = STAGE2_REL / "inputs" / name
        require(descriptor.get("path") == expected_rel.as_posix(), f"batch {number} path")
        batch_path = relative_path(root, descriptor["path"], f"batch {number}")
        require(batch_path.parent == input_dir.resolve(), f"batch {number} input directory")
        batch = read_json(batch_path, f"batch {number}")
        require(sha(batch_path.read_bytes()) == descriptor.get("sha256"), f"batch {number} descriptor SHA")
        require(batch.get("schema_version") == 1, f"batch {number} schema_version")
        require(batch.get("batch_id") == Path(name).stem, f"batch {number} batch_id")
        require(batch.get("input_inventory_sha256") == expected_inventory_sha, f"batch {number} inventory SHA")
        require(batch.get("selected_sources") == group, f"batch {number} source rows")
        group_paths = {source["relative_path"] for source in group}
        expected_occurrences = [o for o in occurrences if o["source_path"] in group_paths]
        require(batch.get("occurrences") == expected_occurrences, f"batch {number} occurrence rows")
        require(len(group) <= 20, f"batch {number} source maximum")
        require(len(expected_occurrences) <= 120, f"batch {number} occurrence maximum")
        require(descriptor.get("source_count") == len(group), f"batch {number} source_count")
        require(descriptor.get("occurrence_count") == len(expected_occurrences), f"batch {number} occurrence_count")
        seen_sources.extend(source["relative_path"] for source in group)
        seen_occurrences.extend(item["occurrence_id"] for item in expected_occurrences)

    require(seen_sources == [source["relative_path"] for source in selected], "source partition exact coverage")
    require(len(seen_sources) == len(set(seen_sources)), "source partition no overlap")
    require(seen_occurrences == [item["occurrence_id"] for item in occurrences], "occurrence partition exact coverage")
    require(len(seen_occurrences) == len(set(seen_occurrences)), "occurrence partition no overlap")
    require(
        len(seen_sources) == len(selected) and len(seen_occurrences) == len(occurrences),
        "source and occurrence partition maxima",
    )

    return {
        "outcome": "PASS",
        "scope": "CA-P-1972 current Core Subject inventory and batches",
        "selected_sources": len(selected),
        "excluded_sources": len(expected["excluded_sources"]),
        "occurrences": len(occurrences),
        "batches": len(groups),
        "source_partition": "exact, disjoint, lexical",
        "occurrence_partition": "exact, disjoint, source-contiguous",
        "input_pins": list(required_pins),
        "strict_parser": "shared validate_atoms parser",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--inventory", type=Path)
    parser.add_argument("--batches", type=Path)
    parser.add_argument("--inputs", type=Path)
    args = parser.parse_args(argv)
    try:
        result = verify_inventory(args.root, args.inventory, args.batches, args.inputs)
    except (OSError, VerificationError, KeyError, TypeError, ValueError) as error:
        print(json.dumps({"outcome": "FAIL", "reason": str(error)}, sort_keys=True), file=sys.stderr)
        return 1
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
