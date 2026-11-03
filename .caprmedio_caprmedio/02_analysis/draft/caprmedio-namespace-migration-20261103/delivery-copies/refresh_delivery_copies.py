#!/usr/bin/env python3
"""Stage reviewed Current delivery-copy refreshes without touching targets."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import re
import sys
from pathlib import Path
from typing import Any


sys.dont_write_bytecode = True

PACKET = Path(__file__).resolve().parent.parent
ROOT = PACKET.parents[3]
PARENT_PLAN = PACKET / "plan.json"
OUTPUT = Path(__file__).resolve().parent
CANDIDATES = OUTPUT / "candidates"

CANONICAL_SOURCE_PREFIX = Path(
    ".caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY"
    "/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES"
)
TARGETS = (
    ("layer1", ROOT / "LAYER_1_FRAMEWORK_METHODOLOGY"),
    ("framework", ROOT / ".caprmedio_caprmedio/000_CAPRMEDIO_framework"),
)
FORBIDDEN_PARTS = {
    "_projection",
    "archive",
    "archives",
    "draft",
    "drafts",
    "history",
    "historical",
    "release",
    "release-snapshot",
    "_release_materialized",
    "runtime",
    "service",
    "services",
}


def load_compiler() -> Any:
    tool = ROOT / (
        "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/"
        "COMPILE_APPLICABLE_METHODOLOGY/compile_applicable_methodology.py"
    )
    sys.path.insert(0, str(tool.parent.parent))
    spec = importlib.util.spec_from_file_location("delivery_copy_compiler", tool)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load compiler helper: {tool}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


COMPILER = load_compiler()


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_json(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise AssertionError(f"expected object: {path}")
    return value


def source_candidate(record: dict[str, Any]) -> bytes:
    before = ROOT / record["before_snapshot"]
    candidate = ROOT / record["candidate_bytes"]
    before_bytes = before.read_bytes()
    candidate_bytes = candidate.read_bytes()
    assert digest(before_bytes) == record["before_sha256"], record["base_id"]
    assert digest(candidate_bytes) == record["candidate_sha256"], record["base_id"]
    return candidate_bytes


def canonical_source_for_copy(root: Path, path: Path) -> Path | None:
    rel = path.relative_to(root)
    if not rel.parts or rel.parts[0] != "SUPERLAYER_1_METHODOLOGY_SOURCES":
        return None
    return ROOT / CANONICAL_SOURCE_PREFIX / Path(*rel.parts[1:])


def projection_fields(data: bytes, path: Path) -> dict[str, str]:
    frontmatter, _body = COMPILER.split_frontmatter(data, relative(path))
    if not re.search(r"(?m)^projection:\s*(?:$|\{)", frontmatter):
        return {}

    def scalar(key: str) -> str:
        value = COMPILER.top_scalar(frontmatter, key)
        if value is None:
            raise AssertionError(f"missing {key} in {path}")
        return value

    block = COMPILER.top_block(frontmatter, "projection")
    values: dict[str, str] = {}
    for key in ("source_carrier_path", "source_atom_id", "source_atom_revision", "source_sha256"):
        match = re.fullmatch(rf"\s{{2}}{re.escape(key)}:\s*(.+)", next((line for line in block if re.match(rf"\s{{2}}{re.escape(key)}:", line)), ""))
        if match is None:
            raise AssertionError(f"missing projection.{key} in {path}")
        values[key] = COMPILER.scalar_value(match.group(1))
    values["atom_id"] = scalar("atom_id")
    values["version"] = scalar("version")
    return values


def candidate_object(record: dict[str, Any], source: bytes) -> Any:
    frontmatter, _body = COMPILER.split_frontmatter(source, record["path"])
    return COMPILER.Candidate(
        layer="MIGRATION",
        layer_order=0,
        role="delivery",
        role_directory="07_delivery",
        atom_id=record["base_id"],
        version=int(record["version"]),
        source_path=record["path"],
        # The old digest admits this refresh; projection provenance must pin
        # the canonical source bytes that exist after the namespace migration.
        source_sha256=record["candidate_sha256"],
        basename=Path(record["path"]).name,
        priority=None,
        priority_group=None,
        replacements=(),
        incompatibilities=(),
        definition_term=None,
        definition_subject_path=None,
        original_relations_sha256=COMPILER.relations_digest(frontmatter),
    )


def projected_candidate(
    target: Path,
    record: dict[str, Any],
    source: bytes,
) -> tuple[bytes, str]:
    candidate = candidate_object(record, source)
    source_path = (ROOT / record["path"]).resolve()
    source_relative = Path(os.path.relpath(source_path, target.parent)).as_posix()
    projected = COMPILER.projection_bytes(source, source_relative, candidate)
    COMPILER.validate_projection_source_preservation(source, projected, source_relative, candidate)
    fields = projection_fields(projected, target)
    assert fields["source_carrier_path"] == source_relative
    assert fields["source_atom_id"] == record["base_id"]
    assert fields["source_atom_revision"] == str(record["version"])
    assert fields["source_sha256"] == digest(source)
    return projected, source_relative


def path_only_candidate(current: bytes, target: Path, source_path: Path) -> tuple[bytes, str]:
    source_relative = Path(os.path.relpath(source_path.resolve(), target.parent)).as_posix()
    match = re.search(rb"(?m)^(  source_carrier_path:)\s*[^\n]*$", current)
    if match is None:
        raise AssertionError(f"projection source path missing: {target}")
    replacement = match.group(1) + b" " + source_relative.encode("utf-8")
    candidate = current[: match.start()] + replacement + current[match.end() :]
    assert candidate != current
    assert current[: match.start()] == candidate[: match.start()]
    assert current[match.end() :] == candidate[match.start() + len(replacement) :]
    fields = projection_fields(candidate, target)
    assert fields["source_carrier_path"] == source_relative
    return candidate, source_relative


def stage_candidate(sequence: int, label: str, kind: str, target: Path, data: bytes) -> str:
    name = f"{sequence:04d}-{label}-{kind}-{target.stem}.txt"
    path = CANDIDATES / name
    path.write_bytes(data)
    assert path.suffix == ".txt"
    assert path.read_bytes() == data
    return path.relative_to(OUTPUT).as_posix()


def add_record(
    staged: list[dict[str, Any]],
    *,
    sequence: int,
    label: str,
    kind: str,
    action: str,
    target: Path,
    target_before: bytes,
    candidate: bytes,
    source_record: dict[str, Any] | None,
    source_relative: str | None,
    trace: dict[str, Any] | None = None,
) -> int:
    candidate_path = stage_candidate(sequence, label, kind, target, candidate)
    row: dict[str, Any] = {
        "root": label,
        "current_path": relative(target),
        "action": action,
        "candidate": candidate_path,
        "target_before_sha256": digest(target_before),
        "candidate_sha256": digest(candidate),
        "candidate_bytes_equal_source_candidate": action == "refresh_source_copy",
    }
    if source_record is not None:
        row.update(
            {
                "source_atom_id": source_record["base_id"],
                "source_revision": source_record["version"],
                "source_before_sha256": source_record["before_sha256"],
                "source_candidate_sha256": source_record["candidate_sha256"],
                "canonical_source_path": source_record["path"],
            }
        )
        if action == "refresh_projection":
            row["projection_source_sha256"] = source_record["candidate_sha256"]
    if source_relative is not None:
        row["source_carrier_path"] = source_relative
    if trace is not None:
        row["trace"] = trace
    staged.append(row)
    return sequence + 1


def main() -> None:
    parent_raw = PARENT_PLAN.read_bytes()
    parent = json.loads(parent_raw)
    if not isinstance(parent, dict) or parent.get("status") != "PREPARED_NO_SOURCE_APPLY":
        raise AssertionError("parent namespace plan is not the sealed preparation plan")
    records = parent.get("records")
    if not isinstance(records, list) or len(records) != 1173:
        raise AssertionError("expected 1173 parent records")
    by_before = {row["before_sha256"]: row for row in records}
    by_identity = {(row["base_id"], int(row["version"])): row for row in records}
    assert len(by_before) == len(records)
    assert len(by_identity) == len(records)
    for record in records:
        current_source = ROOT / record["path"]
        assert current_source.is_file(), current_source
        assert digest(current_source.read_bytes()) == record["candidate_sha256"], record["base_id"]

    OUTPUT.mkdir(parents=True, exist_ok=True)
    CANDIDATES.mkdir(parents=True, exist_ok=True)
    # This packet owns only its generated candidates; no Project target is removed.
    for old in CANDIDATES.glob("*.txt"):
        old.unlink()

    staged: list[dict[str, Any]] = []
    unchanged_plain: list[dict[str, Any]] = []
    unchanged_projection: list[dict[str, Any]] = []
    summaries: dict[str, dict[str, Any]] = {}
    sequence = 1

    for label, root in TARGETS:
        files = sorted(root.rglob("*.md"))
        selected_rows: list[dict[str, str]] = []
        plain = projected = eligible_plain = eligible_projected = 0
        unmatched_plain = unmatched_projected = 0

        for target in files:
            rel = target.relative_to(root)
            if FORBIDDEN_PARTS.intersection(part.casefold() for part in rel.parts):
                raise AssertionError(f"forbidden delivery-copy path selected: {target}")
            current = target.read_bytes()
            fields = projection_fields(current, target)
            if fields:
                projected += 1
                identity = (fields["source_atom_id"], int(fields["source_atom_revision"]))
                selected_rows.append(
                    {
                        "current_path": relative(target),
                        "source_atom_id": fields["source_atom_id"],
                        "source_atom_revision": fields["source_atom_revision"],
                        "source_sha256": fields["source_sha256"],
                    }
                )
                source_record = by_identity.get(identity)
                if source_record is not None and source_record["before_sha256"] == fields["source_sha256"]:
                    source = source_candidate(source_record)
                    candidate, source_relative = projected_candidate(target, source_record, source)
                    sequence = add_record(
                        staged,
                        sequence=sequence,
                        label=label,
                        kind="projection",
                        action="refresh_projection",
                        target=target,
                        target_before=current,
                        candidate=candidate,
                        source_record=source_record,
                        source_relative=source_relative,
                    )
                    eligible_projected += 1
                    continue

                # The fixed 1153-row selection retains 150 source pins outside this migration.
                counterpart = ROOT / "LAYER_1_FRAMEWORK_METHODOLOGY" / target.relative_to(root)
                counterpart_fields = projection_fields(counterpart.read_bytes(), counterpart)
                assert counterpart_fields == fields, (target, counterpart)
                source_path = (counterpart.parent / counterpart_fields["source_carrier_path"]).resolve()
                assert source_path.is_file(), source_path
                assert digest(source_path.read_bytes()) == fields["source_sha256"], source_path
                if label == "framework":
                    candidate, source_relative = path_only_candidate(current, target, source_path)
                    sequence = add_record(
                        staged,
                        sequence=sequence,
                        label=label,
                        kind="projection-path",
                        action="refresh_projection_source_path_only",
                        target=target,
                        target_before=current,
                        candidate=candidate,
                        source_record=None,
                        source_relative=source_relative,
                        trace={
                            "counterpart_product_path": relative(counterpart),
                            "canonical_source_path": relative(source_path),
                            "source_atom_id": fields["source_atom_id"],
                            "source_revision": fields["source_atom_revision"],
                            "source_sha256": fields["source_sha256"],
                            "all_other_metadata_and_body_unchanged": True,
                        },
                    )
                else:
                    unchanged_projection.append(
                        {
                            "root": label,
                            "current_path": relative(target),
                            "action": "verified_unchanged_projection",
                            "current_sha256": digest(current),
                            "canonical_source_path": relative(source_path),
                            "source_atom_id": fields["source_atom_id"],
                            "source_revision": fields["source_atom_revision"],
                            "source_sha256": fields["source_sha256"],
                            "counterpart_trace_verified": True,
                        }
                    )
                unmatched_projected += 1
                continue

            plain += 1
            before_record = by_before.get(digest(current))
            if before_record is not None:
                candidate = source_candidate(before_record)
                assert digest(candidate) == before_record["candidate_sha256"]
                sequence = add_record(
                    staged,
                    sequence=sequence,
                    label=label,
                    kind="source",
                    action="refresh_source_copy",
                    target=target,
                    target_before=current,
                    candidate=candidate,
                    source_record=before_record,
                    source_relative=None,
                )
                eligible_plain += 1
                continue

            unmatched_plain += 1
            canonical_source = canonical_source_for_copy(root, target)
            assert canonical_source is not None and canonical_source.is_file(), target
            assert digest(current) == digest(canonical_source.read_bytes()), target
            unchanged_plain.append(
                {
                    "root": label,
                    "current_path": relative(target),
                    "action": "verified_unchanged_source_copy",
                    "current_sha256": digest(current),
                    "canonical_source_path": relative(canonical_source),
                    "canonical_source_sha256": digest(canonical_source.read_bytes()),
                    "outside_migrated_source_set": True,
                }
            )

        assert projected == 1153, (label, projected)
        assert plain == 1156, (label, plain)
        assert eligible_plain == 1005, (label, eligible_plain)
        assert eligible_projected == 1003, (label, eligible_projected)
        assert unmatched_plain == 151, (label, unmatched_plain)
        assert unmatched_projected == 150, (label, unmatched_projected)
        selection_identity_rows = sorted(
            (row["source_atom_id"], row["source_atom_revision"], row["source_sha256"])
            for row in selected_rows
        )
        summaries[label] = {
            "root": relative(root),
            "scanned_markdown": len(files),
            "source_copies": plain,
            "projected_copies": projected,
            "eligible_source_refreshes": eligible_plain,
            "eligible_projection_refreshes": eligible_projected,
            "path_only_projection_refreshes": 150 if label == "framework" else 0,
            "verified_unchanged_source_copies": unmatched_plain,
            "verified_unchanged_projections": 150 if label == "layer1" else 0,
            "fixed_selection_count": len(selected_rows),
            "fixed_selection_identity_sha256": digest(canonical_json(selection_identity_rows)),
            "fixed_selection_paths_sha256": digest(canonical_json(selected_rows)),
        }

    assert len(staged) == 4166, len(staged)
    assert len(unchanged_plain) == 302, len(unchanged_plain)
    assert len(unchanged_projection) == 150, len(unchanged_projection)
    plan = {
        "schema": "caprmedio-namespace-delivery-copies-plan/v1",
        "status": "PREPARED_NO_DELIVERY_APPLY",
        "parent_plan": relative(PARENT_PLAN),
        "parent_plan_sha256": digest(parent_raw),
        "scope": {
            "roots": [relative(root) for _label, root in TARGETS],
            "canonical_source_root": ".caprmedio_caprmedio/",
            "source_selection_fixed": True,
            "selected_projection_rows_per_root": 1153,
            "excluded": [
                "Draft/archive/history/release-snapshot/runtime/service trees",
                "historical _projection/APPLICABLE_METHODOLOGY trees",
                "authoritative source atoms and official graph",
                "compiled Applicable Methodology selection and declarations",
            ],
        },
        "counts": {
            "staged_candidates": len(staged),
            "source_copy_refreshes": 2010,
            "projection_refreshes_from_migrated_sources": 2006,
            "installed_projection_path_only_refreshes": 150,
            "verified_unchanged_plain_copies": len(unchanged_plain),
            "verified_unchanged_layer1_projections": len(unchanged_projection),
            "uncertain_outputs": 0,
        },
        "roots": summaries,
        "candidates": staged,
        "verified_unchanged_plain": unchanged_plain,
        "verified_unchanged_layer1_projections": unchanged_projection,
        "acceptance": {
            "candidate_files_are_txt": all(row["candidate"].endswith(".txt") for row in staged),
            "all_candidate_hashes_match_written_bytes": True,
            "migrated_source_identity_version_pins_validated": True,
            "canonical_current_sources_match_candidate_hashes": True,
            "migrated_projection_source_preservation_validated": True,
            "migrated_projection_source_sha256_matches_current_canonical": True,
            "installed_path_only_projection_changes_only_source_carrier_path": True,
            "fixed_selection_1153_rows_per_root": all(
                summary["fixed_selection_count"] == 1153 for summary in summaries.values()
            ),
            "no_uncertain_outputs": True,
            "no_delivery_target_writes": True,
        },
    }
    (OUTPUT / "plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"staged_candidates": len(staged), "verified_plain": len(unchanged_plain), "verified_layer1_projections": len(unchanged_projection), "uncertain": 0}, sort_keys=True))


if __name__ == "__main__":
    main()
