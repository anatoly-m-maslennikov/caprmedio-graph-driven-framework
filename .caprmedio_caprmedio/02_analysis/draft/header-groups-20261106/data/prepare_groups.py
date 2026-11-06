from __future__ import annotations

import collections
import hashlib
import json
import re
from pathlib import Path
from typing import Any

import yaml
from yaml.nodes import MappingNode


REPO = Path.cwd()
ROOT = REPO / ".caprmedio_caprmedio"
PACKET = ROOT / "02_analysis/draft/header-groups-20261106/data"
OLD_BASE = ROOT / "02_analysis/draft/epic-completion-20261104/coverage/ordered-source-migration-20261105"
OLD_SNAPSHOT = OLD_BASE / "property-audit/snapshot.json"
LEGACY_ROOTS = OLD_BASE / "verification/legacy-scope-directories.json"
NATIVE_SNAPSHOT = ROOT / "02_analysis/draft/header-groups-20261106/native-snapshot.json"
ROLE_PATTERN = re.compile(r"\d\d_(concern|analysis|plan|requirement|method|evaluation|delivery|implementation|operations|ops)$")
ROLE_CODE = {
    "01_concern": "C", "02_analysis": "A", "03_plan": "P", "04_requirement": "R",
    "05_method": "M", "06_evaluation": "E", "07_delivery": "D",
    "09_operations": "O", "09_ops": "O",
}
EXCLUDED = {"archive", "archived", "_journal", "_projection", "000_CAPRMEDIO_framework", "goals_archive"}
ALLOWED_TAILS = {"draft", "backlog", "done", "canceled", "cancelled", "active"}
GROUPS = {
    "identity": ("atom_id", "ref_id"),
    "context": ("container", "role", "form", "label", "topics", "tier"),
    "relations": ("relations",),
    "state": ("status", "version", "updated_at"),
    "destination": ("carrier_destination",),
}
FIELD_GROUP = {field: group for group, fields in GROUPS.items() for field in fields}


class UniqueSafeLoader(yaml.SafeLoader):
    def construct_mapping(self, node: MappingNode, deep: bool = False) -> dict[Any, Any]:
        self.flatten_mapping(node)
        mapping: dict[Any, Any] = {}
        for key_node, value_node in node.value:
            key = self.construct_object(key_node, deep=deep)
            try:
                duplicate = key in mapping
            except TypeError as exc:
                raise yaml.constructor.ConstructorError(
                    "while constructing a mapping", node.start_mark,
                    f"unhashable key: {key!r}", key_node.start_mark,
                ) from exc
            if duplicate:
                raise yaml.constructor.ConstructorError(
                    "while constructing a mapping", node.start_mark,
                    f"duplicate key {key!r}", key_node.start_mark,
                )
            mapping[key] = self.construct_object(value_node, deep=deep)
        return mapping


UniqueSafeLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    UniqueSafeLoader.construct_mapping,
)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def select_sources() -> tuple[list[Path], list[Path], dict[str, str]]:
    """Use the root-owned, pin-refreshed native path set; do not rescan scope."""
    snapshot = json.loads(NATIVE_SNAPSHOT.read_text(encoding="utf-8"))
    rows = snapshot["carriers"]
    paths = [REPO / row["path"] for row in rows]
    pinned_hashes = {row["path"]: row["sha256"] for row in rows}
    symlinks = [path for path in paths if path.is_symlink()]
    return paths, symlinks, pinned_hashes


def parse_frontmatter(path: Path) -> tuple[dict[str, Any] | None, str | None]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n") or text.count("---") < 2:
        return None, "missing opening/closing YAML frontmatter fence"
    payload = text.split("---", 2)[1]
    try:
        value = yaml.load(payload, Loader=UniqueSafeLoader)
    except Exception as exc:  # census only; preserve exact source and report parser failure
        return None, f"{type(exc).__name__}: {exc}"
    if not isinstance(value, dict):
        return None, "frontmatter is not a mapping"
    return value, None


def main() -> None:
    old = json.loads(OLD_SNAPSHOT.read_text(encoding="utf-8"))
    old_paths = {row["path"]: row for row in old["carriers"]}
    paths, symlinks, pinned_hashes = select_sources()
    rows: list[dict[str, Any]] = []
    key_counts: collections.Counter[str] = collections.Counter()
    extra_counts: collections.Counter[str] = collections.Counter()
    duplicate_rows: list[dict[str, str]] = []
    parse_errors: list[dict[str, str]] = []
    pin_mismatches: list[dict[str, str]] = []
    empty_group_counts: collections.Counter[str] = collections.Counter()
    class_counts: collections.Counter[str] = collections.Counter()
    for path in paths:
        rel = str(path.relative_to(REPO))
        if not path.is_file():
            parse_errors.append({"path": rel, "sha256": "", "error": "pinned source is missing"})
            continue
        raw = path.read_bytes()
        metadata, error = parse_frontmatter(path)
        current_sha = sha(raw)
        if pinned_hashes.get(rel) != current_sha:
            pin_mismatches.append({"path": rel, "pinned_sha256": pinned_hashes.get(rel, ""), "current_sha256": current_sha})
        if error:
            parse_errors.append({"path": rel, "sha256": sha(raw), "error": error})
            duplicate = "duplicate key" in error.lower()
            if duplicate:
                duplicate_rows.append({"path": rel, "sha256": sha(raw), "error": error})
            rows.append({"path": rel, "sha256": sha(raw), "class": "Draft" if "/draft/" in rel else "Current", "parse": "error", "error": error})
            continue
        assert metadata is not None
        keys = list(metadata)
        key_counts.update(str(key) for key in keys)
        extra = sorted(str(key) for key in keys if key not in FIELD_GROUP)
        extra_counts.update(extra)
        group_fields = {group: [field for field in fields if field in metadata] for group, fields in GROUPS.items()}
        empty_groups = [group for group, fields in group_fields.items() if not fields]
        empty_group_counts.update(empty_groups)
        relparts = path.relative_to(ROOT).parts
        role_index = next((i for i, part in enumerate(relparts[:-1]) if ROLE_PATTERN.fullmatch(part)), None)
        is_draft = role_index is not None and any(part.lower() == "draft" for part in relparts[role_index + 1:-1])
        source_class = "Draft" if is_draft else "Current"
        class_counts.update([source_class])
        row = {
            "path": rel,
            "sha256": sha(raw),
            "class": source_class,
            "atom_id": metadata.get("atom_id"),
            "ref_id": metadata.get("ref_id"),
            "status": metadata.get("status"),
            "top_level_keys": [str(key) for key in keys],
            "mapped_group_fields": group_fields,
            "empty_groups_to_omit_if_no_other_decision": empty_groups,
            "unmapped_extra_keys_require_decision": extra,
            "grouping_candidate_ready": not extra,
        }
        rows.append(row)
    added = sorted(set(row["path"] for row in rows) - set(old_paths))
    removed = sorted(set(old_paths) - set(row["path"] for row in rows))
    by_path = {row["path"]: row for row in rows}
    common = set(by_path) & set(old_paths)
    hash_changed = sorted(path for path in common if old_paths[path]["sha256"] != by_path[path]["sha256"])
    report = {
        "status": "READ_ONLY_NATIVE_CURRENT_DRAFT_HEADER_GROUP_CENSUS",
        "scope": "Native Current and Draft carriers selected with the existing ordered-source-migration census boundary; archives/archived, 000/applicable copies, tests, journals, projections, and analysis packet descendants excluded.",
        "baseline": {
            "path": str(NATIVE_SNAPSHOT),
            "sha256": sha(NATIVE_SNAPSHOT.read_bytes()),
            "source_count": len(pinned_hashes),
            "previous_snapshot_path": str(OLD_SNAPSHOT),
            "previous_snapshot_sha256": sha(OLD_SNAPSHOT.read_bytes()),
            "previous_scope_count": len(old_paths),
            "legacy_scope_exception_source": str(LEGACY_ROOTS),
            "legacy_scope_exception_sha256": sha(LEGACY_ROOTS.read_bytes()),
        },
        "approved_groups": GROUPS,
        "counts": {
            "native_sources": len(rows),
            "classes": dict(class_counts),
            "top_level_keys": dict(key_counts),
            "unmapped_extra_keys": dict(extra_counts),
            "empty_groups": dict(empty_group_counts),
            "parse_errors": len(parse_errors),
            "duplicate_key_errors": len(duplicate_rows),
            "source_pin_mismatches": len(pin_mismatches),
            "symlinks_excluded": len(symlinks),
            "added_since_baseline": len(added),
            "removed_since_baseline": len(removed),
            "changed_hashes_on_common_paths": len(hash_changed),
            "grouping_candidate_ready_no_extra_keys": sum(bool(row.get("grouping_candidate_ready")) for row in rows),
            "held_for_extra_keys": sum(bool(row.get("unmapped_extra_keys_require_decision")) for row in rows),
        },
        "current_paths": [{"path": row["path"], "sha256": row["sha256"], "class": row["class"]} for row in rows],
        "added_paths": added,
        "removed_paths": removed,
        "changed_hash_paths": hash_changed,
        "parse_errors": parse_errors,
        "duplicate_key_errors": duplicate_rows,
        "source_pin_mismatches": pin_mismatches,
        "symlink_paths_excluded": [str(path) for path in symlinks],
        "records": rows,
        "limits": [
            "Grouping candidates describe the approved common mapping only; extra keys are not assigned to any group and must remain preserved pending an explicit decision.",
            "No YAML text or native source was rewritten. This census does not prove semantic admission, runtime compatibility, or source migration readiness.",
            "Empty groups are reported for omission review; Relations values remain preserved as-is, including an explicitly empty mapping.",
        ],
    }
    PACKET.mkdir(parents=True, exist_ok=True)
    (PACKET / "source-paths.json").write_text(json.dumps({"baseline_sha256": sha(OLD_SNAPSHOT.read_bytes()), "sources": report["current_paths"]}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (PACKET / "header-census.json").write_text(json.dumps(report, ensure_ascii=False, indent=2, default=str) + "\n", encoding="utf-8")
    print(json.dumps(report["counts"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
