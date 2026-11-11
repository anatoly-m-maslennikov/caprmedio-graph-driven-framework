#!/usr/bin/env python3
"""Prepare a byte-preserving CAPRMEDIO namespace migration plan.

This script only reads the pinned Current sources and writes this packet.  It
does not apply source changes, promote Drafts, rebuild projections, or touch
Git.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

import yaml


PACKET = Path(__file__).resolve().parent
ROOT = PACKET.parents[3]
FRONTIER = (
    ROOT
    / ".caprmedio_caprmedio/02_analysis/draft/role-projection-completion-20261102"
    / "current-source-frontier.json"
)
INVENTORY = Path("/private/tmp/caprmedio-namespace-inventory.json")
EXPECTED_FRONTIER_SHA256 = "51168bb75c6e49bb7ff32bfd027c2d93ab62ff8598dcb14f036e9265ef8da2d1"
EXPECTED_INVENTORY_SHA256 = "081803bfdb13b550f0139a49d9aeb23e4718c6755b3c15e4987f8b9ae984ef46"

MODEL_PREFIX = "CAPRMEDIO <+ MODEL"
STRUCTURE_PREFIX = "CAPRMEDIO <+ STRUCTURE"
TARGET_SUBJECT_KEYS = ("active", "passive")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def root_relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def frontmatter_parts(text: str) -> tuple[str, str, str, str]:
    separators = list(re.finditer(r"(?m)^---[ \t]*(?:\r?\n|$)", text))
    if len(separators) < 2 or separators[0].start() != 0:
        raise ValueError("expected a two-delimiter YAML frontmatter")
    first, second = separators[:2]
    return (
        text[first.end() : second.start()],
        text[second.end() :],
        text[: first.end()],
        text[second.start() : second.end()],
    )


def scalar_nodes_under_subjects(
    frontmatter: str,
) -> tuple[list[tuple[str, yaml.nodes.ScalarNode]], list[str]]:
    root = yaml.compose(frontmatter, Loader=yaml.SafeLoader)
    if not isinstance(root, yaml.nodes.MappingNode):
        raise ValueError("frontmatter root is not a mapping")

    subjects_node: yaml.nodes.Node | None = None
    for key, value in root.value:
        if key.value == "subjects":
            subjects_node = value
            break
    if subjects_node is None:
        return [], []
    if not isinstance(subjects_node, yaml.nodes.MappingNode):
        raise ValueError("subjects is not a mapping")

    result: list[tuple[str, yaml.nodes.ScalarNode]] = []

    def visit(node: yaml.nodes.Node, path: tuple[str | int, ...]) -> None:
        if isinstance(node, yaml.nodes.ScalarNode):
            result.append((".".join(map(str, path)), node))
        elif isinstance(node, yaml.nodes.SequenceNode):
            for index, child in enumerate(node.value):
                visit(child, path + (index,))
        elif isinstance(node, yaml.nodes.MappingNode):
            for key, child in node.value:
                visit(child, path + (key.value,))

    for key, value in subjects_node.value:
        if key.value in TARGET_SUBJECT_KEYS:
            visit(value, (key.value,))
    present = [
        key.value
        for key, _value in subjects_node.value
        if key.value in TARGET_SUBJECT_KEYS
    ]
    return result, present


def quoted_scalar(raw: str, value: str) -> str:
    stripped = raw.strip()
    leading = raw[: len(raw) - len(raw.lstrip())]
    trailing = raw[len(raw.rstrip()) :]
    if len(stripped) >= 2 and stripped[0] == "'" and stripped[-1] == "'":
        encoded = "'" + value.replace("'", "''") + "'"
    elif len(stripped) >= 2 and stripped[0] == '"' and stripped[-1] == '"':
        encoded = json.dumps(value, ensure_ascii=False)
    else:
        encoded = yaml.safe_dump(
            value,
            default_flow_style=True,
            allow_unicode=True,
            width=1_000_000,
        ).strip()
        encoded_lines = encoded.splitlines()
        if encoded_lines and encoded_lines[-1] == "...":
            encoded = "\n".join(encoded_lines[:-1])
    return leading + encoded + trailing


def normalize_root(value: str) -> str | None:
    compact = re.sub(r"\s*//\s*", "//", value.strip())
    if compact in {"MODEL", "MODEL//CAPRMEDIO"}:
        return MODEL_PREFIX
    if compact == "PROJECT STRUCTURE//CAPRMEDIO":
        return STRUCTURE_PREFIX
    if compact == "PROJECT STRUCTURE":
        return f"{MODEL_PREFIX} <+ PROJECT STRUCTURE"
    return None


def is_aspects_chain(value: str) -> bool:
    return bool(re.match(r"^Aspects(?:\s|<\+|$)", value))


def is_structure_named_instance(value: str) -> bool:
    patterns = (
        r"^Scope Unit\s*//",
        r"^Project\s*//",
        r"^PROJECT\s*//",
        r"^Named Selection\s*//",
        r"/Selection\s*//",
        r"/Action\s*//",
        r"/Workflow\s*//",
        r"/Type:\s*Action\s*//",
        r"/Type:\s*Workflow\s*//",
        r"^Action\s*//",
        r"^Workflow\s*//",
        r"^Projection\s*//",
        r"^Node/Continuant\s*//CAPRMEDIO Framework$",
    )
    return any(re.search(pattern, value) for pattern in patterns)


def is_model_named_instance(value: str) -> bool:
    # These are model declarations, including the legacy Entity/.../Term form.
    return bool(
        re.search(r"CFEL", value)
        or re.search(r"(?:^|[/ ])Term\s*//", value)
        or re.search(r"(?:^|[ <+])Relation\s*//", value)
        or re.search(r"(?:^|[ <+])Operator\s*//", value)
        or re.search(r"(?:^|[ <+])Format\s*//", value)
    )


def classify_subject(value: str) -> tuple[str, str, str, bool]:
    """Return candidate, rule, placement, and whether a decision is open."""
    if value.startswith("CAPRMEDIO"):
        return value, "already_caprmedio_prefix", "ALREADY_CAPRMEDIO", False

    root = normalize_root(value)
    if root is not None:
        if value.strip() == "PROJECT STRUCTURE":
            return root, "bare_model_kind", "MODEL", False
        return root, "root_recode", "STRUCTURE" if root == STRUCTURE_PREFIX else "MODEL", False

    if is_aspects_chain(value) or is_structure_named_instance(value):
        return f"{STRUCTURE_PREFIX} <+ {value}", "structure_named_instance", "STRUCTURE", False

    if "//" in value and is_model_named_instance(value):
        return f"{MODEL_PREFIX} <+ {value}", "model_named_definition", "MODEL", False

    if "//" in value:
        # The explicit fallback is the requested mechanical MODEL namespace;
        # the record remains open so a later review can change placement.
        return (
            f"{MODEL_PREFIX} <+ {value}",
            "named_instance_placement_pending",
            "MODEL_PENDING_REVIEW",
            True,
        )

    return f"{MODEL_PREFIX} <+ {value}", "default_model_prefix", "MODEL", False


def transform_document(text: str) -> tuple[str, dict[str, Any]]:
    frontmatter, body, opening, closing = frontmatter_parts(text)
    before_data = yaml.safe_load(frontmatter) or {}
    spans: list[dict[str, Any]] = []
    placement_decisions: list[dict[str, Any]] = []
    transformed_frontmatter = frontmatter

    nodes, present_subject_keys = scalar_nodes_under_subjects(frontmatter)
    replacements: list[tuple[int, int, str]] = []
    for path, node in nodes:
        raw = frontmatter[node.start_mark.index : node.end_mark.index]
        value = node.value
        if node.tag != "tag:yaml.org,2002:str":
            spans.append(
                {
                    "path": path,
                    "before": value,
                    "candidate": value,
                    "rule": "non_string_scalar_unchanged",
                    "placement": "UNCHANGED",
                    "uncertain": False,
                    "raw_before": raw,
                    "raw_candidate": raw,
                }
            )
            continue
        if value == "" and not raw.strip():
            continue
        candidate, rule, placement, uncertain = classify_subject(value)
        if candidate == value:
            new_raw = raw
        else:
            new_raw = quoted_scalar(raw, candidate)
            replacements.append((node.start_mark.index, node.end_mark.index, new_raw))
        spans.append(
            {
                "path": path,
                "before": value,
                "candidate": candidate,
                "rule": rule,
                "placement": placement,
                "uncertain": uncertain,
                "raw_before": raw,
                "raw_candidate": new_raw,
            }
        )
        if "//" in value:
            placement_decisions.append(
                {
                    "subject": value,
                    "candidate": candidate,
                    "placement": placement,
                    "rule": rule,
                    "uncertain": uncertain,
                }
            )

    for start, end, new_raw in sorted(replacements, reverse=True):
        transformed_frontmatter = transformed_frontmatter[:start] + new_raw + transformed_frontmatter[end:]

    # The current scope is literal subjects.active and subjects.passive only.
    # The body is deliberately carried byte-for-byte without namespace edits.
    candidate_text = opening + transformed_frontmatter + closing + body
    after_frontmatter, after_body, _opening, _closing = frontmatter_parts(candidate_text)
    after_data = yaml.safe_load(after_frontmatter) or {}

    before_without_subjects = dict(before_data)
    after_without_subjects = dict(after_data)
    before_without_subjects.pop("subjects", None)
    after_without_subjects.pop("subjects", None)
    assert before_without_subjects == after_without_subjects
    assert after_body == body
    before_subjects = before_data.get("subjects") or {}
    after_subjects = after_data.get("subjects") or {}
    assert isinstance(before_subjects, dict) and isinstance(after_subjects, dict)
    for key in set(before_subjects) | set(after_subjects):
        if key not in TARGET_SUBJECT_KEYS:
            assert before_subjects.get(key) == after_subjects.get(key)

    # The only frontmatter edits are the exact YAML scalar marks collected above.
    replacement_positions: list[tuple[int, int, str, str]] = []
    forward_delta = 0
    for start, end, new_raw in sorted(replacements, key=lambda item: item[0]):
        original_raw = frontmatter[start:end]
        replacement_positions.append(
            (start + forward_delta, end + forward_delta, new_raw, original_raw)
        )
        forward_delta += len(new_raw) - len(original_raw)
    restored_frontmatter = transformed_frontmatter
    for current_start, current_end, new_raw, original_raw in sorted(
        replacement_positions, reverse=True
    ):
        assert restored_frontmatter[current_start : current_start + len(new_raw)] == new_raw
        restored_frontmatter = (
            restored_frontmatter[:current_start]
            + original_raw
            + restored_frontmatter[current_start + len(new_raw) :]
        )
    assert restored_frontmatter == frontmatter

    return candidate_text, {
        "subject_spans": spans,
        "subjects_present": present_subject_keys,
        "subjects_missing": [
            key for key in TARGET_SUBJECT_KEYS if key not in present_subject_keys
        ],
        "placement_decisions": placement_decisions,
        "metadata_assertions": {
            "frontmatter_non_subject_equal": True,
            "atom_id_equal": before_data.get("atom_id") == after_data.get("atom_id"),
            "version_equal": before_data.get("version") == after_data.get("version"),
            "summary_equal": before_data.get("summary") == after_data.get("summary"),
            "status_equal": before_data.get("status") == after_data.get("status"),
            "other_metadata_equal": before_without_subjects == after_without_subjects,
            "other_subject_keys_equal": all(
                before_subjects.get(key) == after_subjects.get(key)
                for key in set(before_subjects) | set(after_subjects)
                if key not in TARGET_SUBJECT_KEYS
            ),
            "body_unchanged": after_body == body,
            "unrelated_bytes_equal": True,
        },
    }


def source_records() -> tuple[list[dict[str, Any]], str, int]:
    inventory_raw = INVENTORY.read_bytes()
    inventory_hash = sha256_bytes(inventory_raw)
    if inventory_hash != EXPECTED_INVENTORY_SHA256:
        raise AssertionError(f"canonical Current inventory changed: {inventory_hash}")
    inventory = json.loads(inventory_raw)
    if not isinstance(inventory, list):
        raise AssertionError("namespace inventory must be a list")

    records: list[dict[str, Any]] = []
    seen: set[str] = set()
    seen_ids: set[str] = set()
    selected_inventory_rows = 0
    excluded_parts = {
        "archive",
        "archives",
        "history",
        "historical",
        "evidence",
        "test",
        "tests",
        "fixture",
        "fixtures",
        "runtime",
        "installedcopies",
        "projected",
        "draft",
        "drafts",
    }
    for item in inventory:
        subjects = item.get("subjects") or []
        if not any(subject.get("field") in TARGET_SUBJECT_KEYS for subject in subjects):
            continue
        selected_inventory_rows += 1
        rel = item["path"]
        if rel in seen:
            raise AssertionError(f"duplicate inventory path: {rel}")
        seen.add(rel)
        atom_id = item.get("atom_id")
        if not isinstance(atom_id, str) or not atom_id:
            raise AssertionError(f"missing inventory atom_id: {rel}")
        if atom_id in seen_ids:
            raise AssertionError(f"duplicate inventory atom_id: {atom_id}")
        seen_ids.add(atom_id)
        path = ROOT / rel
        if not path.is_file():
            raise FileNotFoundError(path)
        if any(part.lower() in excluded_parts for part in Path(rel).parts):
            raise AssertionError(f"excluded non-canonical copy path in inventory: {rel}")
        raw = path.read_bytes()
        actual_hash = sha256_bytes(raw)
        text = raw.decode("utf-8")
        frontmatter, _body, _opening, _closing = frontmatter_parts(text)
        data = yaml.safe_load(frontmatter) or {}
        if data.get("atom_id") != atom_id:
            raise AssertionError(f"inventory atom_id mismatch for {rel}")
        if data.get("version") != item.get("version"):
            raise AssertionError(f"inventory version mismatch for {rel}")
        records.append(
            {
                "base_id": atom_id,
                "version": item.get("version"),
                "status": data.get("status"),
                "path": rel,
                "source_sha256": actual_hash,
                "source_path": path,
            }
        )
    if selected_inventory_rows != len(records):
        raise AssertionError("inventory selection count mismatch")
    return records, inventory_hash, len(inventory)


def run() -> None:
    frontier_raw = FRONTIER.read_bytes()
    frontier_hash = sha256_bytes(frontier_raw)
    if frontier_hash != EXPECTED_FRONTIER_SHA256:
        raise AssertionError(f"fixed frontier changed: {frontier_hash}")
    frontier = json.loads(frontier_raw)
    if len(frontier.get("operations", [])) != 1132 or frontier.get("selected_source_count") != 1132:
        raise AssertionError("fixed frontier row count changed")
    records, inventory_hash, inventory_total_rows = source_records()

    before_dir = PACKET / "before"
    candidate_dir = PACKET / "candidates"
    for artifact_dir in (before_dir, candidate_dir):
        artifact_dir.mkdir(exist_ok=True)
        for stale_artifact in artifact_dir.glob("*.txt"):
            stale_artifact.unlink()

    plan_records: list[dict[str, Any]] = []
    global_subject_counts: Counter[str] = Counter()
    global_rule_counts: Counter[str] = Counter()
    global_placements: dict[str, dict[str, Any]] = {}
    files_lacking_subject_keys: list[dict[str, Any]] = []
    errors: list[dict[str, str]] = []

    original_hashes: dict[Path, str] = {}
    for index, record in enumerate(records, 1):
        path = record["source_path"]
        raw = path.read_bytes()
        original_hashes[path] = sha256_bytes(raw)
        artifact_name = f"{index:04d}-{record['base_id']}-{record['source_sha256'][:12]}.txt"
        before_path = before_dir / artifact_name
        candidate_path = candidate_dir / artifact_name
        before_path.write_bytes(raw)
        try:
            text = raw.decode("utf-8")
            candidate, detail = transform_document(text)
            candidate_raw = candidate.encode("utf-8")
            # Idempotence is an executable acceptance check, not just a report.
            second_candidate, second_detail = transform_document(candidate)
            assert second_candidate == candidate
            assert all(item["candidate"] == item["before"] for item in second_detail["subject_spans"])
            assert second_detail["subjects_missing"] == detail["subjects_missing"]
            candidate_path.write_bytes(candidate_raw)
        except Exception as exc:  # Keep a deterministic error record for review.
            errors.append({"path": record["path"], "error": repr(exc)})
            continue

        subject_spans = detail["subject_spans"]
        changed_subjects = [item for item in subject_spans if item["candidate"] != item["before"]]
        for item in changed_subjects:
            global_subject_counts[item["rule"]] += 1
            global_rule_counts[item["placement"]] += 1
            if item["uncertain"]:
                key = item["before"]
                global_placements.setdefault(
                    key,
                    {
                        "subject": key,
                        "candidate": item["candidate"],
                        "placement": item["placement"],
                        "rule": item["rule"],
                        "uncertain": True,
                    },
                )
        for item in detail["placement_decisions"]:
            key = item["subject"]
            if key not in global_placements:
                global_placements[key] = item
            else:
                global_placements[key]["occurrences"] = global_placements[key].get("occurrences", 1) + 1

        candidate_hash = sha256_bytes(candidate_raw)
        after_data = yaml.safe_load(candidate.split("---", 2)[1]) or {}
        before_data = yaml.safe_load(text.split("---", 2)[1]) or {}
        assert after_data.get("atom_id") == before_data.get("atom_id") == record["base_id"]
        assert after_data.get("version") == before_data.get("version") == record["version"]
        assert path.read_bytes() == raw
        plan_records.append(
            {
                "base_id": record["base_id"],
                "version": record["version"],
                "status": record["status"],
                "path": record["path"],
                "before_sha256": record["source_sha256"],
                "candidate_sha256": candidate_hash,
                "before_snapshot": root_relative(before_path),
                "candidate_bytes": root_relative(candidate_path),
                "subjects_scalar_count": len(subject_spans),
                "subjects_changed_count": len(changed_subjects),
                "subjects_present": detail["subjects_present"],
                "subjects_missing": detail["subjects_missing"],
                "transform_counts": {
                    "subjects_by_rule": dict(sorted(Counter(item["rule"] for item in changed_subjects).items())),
                },
                "metadata_assertions": detail["metadata_assertions"],
                "placement_decisions": detail["placement_decisions"],
                "errors": [],
            }
        )
        if detail["subjects_missing"]:
            files_lacking_subject_keys.append(
                {"path": record["path"], "missing": detail["subjects_missing"]}
            )

    for path, expected_hash in original_hashes.items():
        assert sha256_bytes(path.read_bytes()) == expected_hash
    if errors:
        raise AssertionError(json.dumps({"errors": errors}, indent=2))
    assert len(plan_records) == len(records) == 1173
    status_counts = Counter(record["status"] for record in records)
    subject_scalar_count = sum(row["subjects_scalar_count"] for row in plan_records)
    changed_subject_count = sum(row["subjects_changed_count"] for row in plan_records)

    # Count all named-instance occurrences, not only unique placement rows.
    placement_occurrences: Counter[str] = Counter()
    for row in plan_records:
        for item in row["placement_decisions"]:
            placement_occurrences[item["subject"]] += 1
    placement_rows = []
    for subject, item in sorted(global_placements.items()):
        row = dict(item)
        row["occurrences"] = placement_occurrences.get(subject, 0)
        placement_rows.append(row)
    artifacts_are_txt = all(
        (ROOT / row["before_snapshot"]).suffix == ".txt"
        and (ROOT / row["candidate_bytes"]).suffix == ".txt"
        for row in plan_records
    )
    no_md_draft_carriers = not any(
        path.is_file() and path.suffix == ".md" for path in PACKET.rglob("*")
    )

    plan = {
        "schema": "caprmedio-namespace-migration-plan/v1",
        "status": "PREPARED_NO_SOURCE_APPLY",
        "scope": {
            "fixed_frontier": root_relative(FRONTIER),
            "fixed_frontier_sha256": frontier_hash,
            "fixed_frontier_source_count": 1132,
            "canonical_current_inventory": str(INVENTORY),
            "canonical_current_inventory_sha256": inventory_hash,
            "canonical_current_inventory_total_rows": inventory_total_rows,
            "planned_source_count": len(plan_records),
            "included_statuses": dict(sorted(status_counts.items())),
            "excluded": [
                "Draft",
                "archive/history/evidence/test/runtime/projected copies",
                "duplicate atom_id rows",
                "installedcopies",
                "sourceapply",
            ],
        },
        "rules": {
            "already_caprmedio": "idempotent",
            "model_root": "MODEL or MODEL//CAPRMEDIO -> CAPRMEDIO <+ MODEL",
            "bare_project_structure": "PROJECT STRUCTURE -> CAPRMEDIO <+ MODEL <+ PROJECT STRUCTURE",
            "structure_root": "PROJECT STRUCTURE//CAPRMEDIO -> CAPRMEDIO <+ STRUCTURE",
            "structure_named": "Aspects chains and named Scope Unit/Project/known structural instances -> CAPRMEDIO <+ STRUCTURE <+ oldsubject",
            "model_default": "else -> CAPRMEDIO <+ MODEL <+ oldsubject",
            "model_named_definitions": "CFEL, Term, Relation, Operator, and Format definitions remain under MODEL",
            "scope": "literal subjects.active and subjects.passive scalars only; body and all other fields are unchanged",
        },
        "placement_decisions": placement_rows,
        "source_rows": len(plan_records),
        "subject_scalar_count": subject_scalar_count,
        "changed_subject_count": changed_subject_count,
        "transform_counts": {
            "subjects_by_rule": dict(sorted(global_subject_counts.items())),
            "subjects_by_placement": dict(sorted(global_rule_counts.items())),
            "source_rows": len(plan_records),
        },
        "files_lacking_subject_keys": files_lacking_subject_keys,
        "uncertain_placements": [row for row in placement_rows if row.get("uncertain")],
        "errors": errors,
        "acceptance": {
            "all_sources_pinned": True,
            "all_metadata_unchanged": all(
                all(value is True for value in row["metadata_assertions"].values()) for row in plan_records
            ),
            "all_candidates_idempotent": True,
            "all_current_source_bytes_unchanged": True,
            "candidate_and_before_artifacts_are_txt": artifacts_are_txt,
            "no_md_draft_carriers": no_md_draft_carriers,
        },
        "records": plan_records,
    }
    assert plan["acceptance"]["all_metadata_unchanged"]
    assert plan["acceptance"]["no_md_draft_carriers"]

    (PACKET / "plan.json").write_text(json.dumps(plan, indent=2, ensure_ascii=False) + "\n")
    report = {
        "schema": "caprmedio-namespace-migration-report/v1",
        "status": plan["status"],
        "frontier": plan["scope"],
        "source_rows": len(plan_records),
        "subject_scalar_count": subject_scalar_count,
        "changed_subject_count": changed_subject_count,
        "transform_counts": plan["transform_counts"],
        "files_lacking_subject_keys_count": len(files_lacking_subject_keys),
        "files_lacking_subject_keys_plan_field": "plan.records[].subjects_missing",
        "uncertain_placements": plan["uncertain_placements"],
        "errors": errors,
        "acceptance": plan["acceptance"],
        "plan": root_relative(PACKET / "plan.json"),
    }
    (PACKET / "report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps(report, ensure_ascii=False, separators=(",", ":")))


if __name__ == "__main__":
    run()
