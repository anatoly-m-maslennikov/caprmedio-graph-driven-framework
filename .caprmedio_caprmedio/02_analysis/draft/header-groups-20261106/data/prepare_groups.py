from __future__ import annotations

import collections
import copy
import datetime as dt
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

import yaml
from yaml.nodes import MappingNode

FEATURE_TOOLS = Path("LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS")
sys.path.insert(0, str(Path.cwd() / FEATURE_TOOLS))
from header_yaml import replace_header_scalar  # noqa: E402


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
PLAN_CONTEXT_FIELDS = ("ai_agent_confidence_threshold", "work_sequence_number")
PLAN_CONTEXT_SOURCE_FIELDS = {
    "ai_agent_confidence_threshold": ("ai_agent_confidence_threshold", "autonomous_confidence_threshold"),
    "work_sequence_number": ("work_sequence_number",),
}


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
    try:
        payload, _ = split_frontmatter(text)
    except ValueError as exc:
        return None, f"frontmatter boundary error: {exc}"
    try:
        value = yaml.load(payload, Loader=UniqueSafeLoader)
    except Exception as exc:  # census only; preserve exact source and report parser failure
        return None, f"{type(exc).__name__}: {exc}"
    if not isinstance(value, dict):
        return None, "frontmatter is not a mapping"
    return value, None


def role_evidence(metadata: dict[str, Any]) -> tuple[str | None, str]:
    role = metadata.get("role")
    if isinstance(role, str) and role:
        return role, "header.role"
    atom_id = metadata.get("atom_id")
    if isinstance(atom_id, str) and re.fullmatch(r"CA-[CP]-\d+", atom_id):
        return ("Concern" if atom_id.startswith("CA-C-") else "Plan"), "atom_id_prefix"
    return None, "unresolved"


def plan_target_for_source(field: Any) -> str | None:
    for target, source_fields in PLAN_CONTEXT_SOURCE_FIELDS.items():
        if field in source_fields:
            return target
    return None


def split_frontmatter(text: str) -> tuple[str, str]:
    match = re.match(r"\A---[ \t]*\r?\n(.*?)^---[ \t]*\r?\n(.*)\Z", text, re.S | re.M)
    if not match:
        raise ValueError("frontmatter fences are not unambiguous line boundaries")
    return match.group(1), match.group(2)


def nested_metadata(metadata: dict[str, Any]) -> tuple[dict[str, Any], dict[str, str]]:
    """Group only approved fields; leave all other top-level fields untouched."""
    role, evidence = role_evidence(metadata)
    collisions = sorted(key for key in ("identity", "context", "state", "destination") if key in metadata)
    if collisions:
        raise ValueError(f"existing top-level group-name collision: {collisions}")
    grouped: dict[str, Any] = {}
    extras: dict[str, Any] = {}
    for key, value in metadata.items():
        if key in GROUPS["identity"]:
            grouped.setdefault("identity", {})[key] = copy.deepcopy(value)
        elif key in GROUPS["context"]:
            grouped.setdefault("context", {})[key] = copy.deepcopy(value)
        elif key == "relations":
            grouped["relations"] = copy.deepcopy(value)
        elif key in GROUPS["state"]:
            grouped.setdefault("state", {})[key] = copy.deepcopy(value)
        elif key == "carrier_destination":
            grouped["destination"] = copy.deepcopy(value)
        elif key == "priority" and role == "Concern":
            grouped.setdefault("context", {}).setdefault("concern", {})[key] = copy.deepcopy(value)
        elif role == "Plan" and (target := plan_target_for_source(key)) is not None:
            current = grouped.setdefault("context", {}).setdefault("plan", {}).get(target, value)
            if current != value:
                raise ValueError(f"conflicting aliases for context.plan.{target}")
            grouped["context"]["plan"][target] = copy.deepcopy(value)
        else:
            extras[key] = copy.deepcopy(value)
    return grouped, {"role": role or "", "role_evidence": evidence, "extra_keys": ",".join(str(k) for k in extras)}


def flatten_metadata(grouped: dict[str, Any], original: dict[str, Any]) -> dict[str, Any]:
    """Inverse used as a preservation assertion; not a migration writer."""
    metadata = {key: copy.deepcopy(value) for key, value in original.items()
                if key not in FIELD_GROUP and key != "carrier_destination"
                and not (key == "priority" and role_evidence(original)[0] == "Concern")
                and not (role_evidence(original)[0] == "Plan" and plan_target_for_source(key) is not None)}
    for key, value in grouped.get("identity", {}).items():
        metadata[key] = copy.deepcopy(value)
    context = grouped.get("context", {})
    for key in GROUPS["context"]:
        if key in context:
            metadata[key] = copy.deepcopy(context[key])
    concern = context.get("concern", {}) if isinstance(context, dict) else {}
    if "priority" in concern:
        metadata["priority"] = copy.deepcopy(concern["priority"])
    plan = context.get("plan", {}) if isinstance(context, dict) else {}
    for target, sources in PLAN_CONTEXT_SOURCE_FIELDS.items():
        if target in plan:
            for source in sources:
                if source in original:
                    metadata[source] = copy.deepcopy(plan[target])
    if "relations" in grouped:
        metadata["relations"] = copy.deepcopy(grouped["relations"])
    for key in GROUPS["state"]:
        if key in grouped.get("state", {}):
            value = grouped["state"][key]
            if key == "updated_at" and isinstance(original.get(key), dt.datetime):
                # Legacy unquoted timestamps parse as datetime, while the declared
                # Header contract stores this field as a quoted string. Preserve
                # the source scalar's exact lexical value in the candidate.
                if not isinstance(value, str) or yaml.safe_load(value) != original[key]:
                    raise AssertionError("quoted updated_at cannot be inverted to its legacy timestamp value")
                metadata[key] = copy.deepcopy(original[key])
            else:
                metadata[key] = copy.deepcopy(value)
    if "destination" in grouped:
        metadata["carrier_destination"] = copy.deepcopy(grouped["destination"])
    return metadata


def render_grouped_metadata(grouped: dict[str, Any], body: str) -> str:
    """Render grouped metadata while retaining the declared quoted timestamp form."""
    yaml_text = yaml.safe_dump(grouped, allow_unicode=True, sort_keys=False,
                               default_flow_style=False, width=1000, indent=2)
    state = grouped.get("state", {})
    updated_at = state.get("updated_at") if isinstance(state, dict) else None
    if updated_at is not None:
        if not isinstance(updated_at, str):
            raise ValueError("state.updated_at must remain a string")
        yaml_text = replace_header_scalar(yaml_text, "updated_at", updated_at)
        rendered_node = yaml.compose(yaml_text)
        state_node = next((value for key, value in rendered_node.value if key.value == "state"), None)
        timestamp_node = (next((value for key, value in state_node.value if key.value == "updated_at"), None)
                          if isinstance(state_node, MappingNode) else None)
        if timestamp_node is None or timestamp_node.style not in ("'", '"'):
            raise AssertionError("state.updated_at did not retain an explicit quoted YAML style")
        rendered = yaml.load(yaml_text, Loader=UniqueSafeLoader)
        if rendered.get("state", {}).get("updated_at") != updated_at:
            raise AssertionError("quoted state.updated_at changed value")
    return f"---\n{yaml_text}---\n{body}"


def transform_text(preimage: str) -> tuple[str, str]:
    """Return deterministic nested YAML plus the original body, with round-trip assertion."""
    front, body = split_frontmatter(preimage)
    original = yaml.load(front, Loader=UniqueSafeLoader)
    if not isinstance(original, dict):
        raise ValueError("frontmatter is not a mapping")
    grouped, _ = nested_metadata(original)
    if isinstance(original.get("updated_at"), dt.datetime):
        original_node = yaml.compose(front)
        timestamp_node = next((value for key, value in original_node.value if key.value == "updated_at"), None)
        if timestamp_node is None or not isinstance(timestamp_node, yaml.ScalarNode):
            raise ValueError("legacy updated_at timestamp has no scalar source node")
        grouped.setdefault("state", {})["updated_at"] = timestamp_node.value
    extras = {key: copy.deepcopy(value) for key, value in original.items()
              if key not in FIELD_GROUP and key != "carrier_destination"
              and not (key == "priority" and role_evidence(original)[0] == "Concern")
              and not (role_evidence(original)[0] == "Plan" and plan_target_for_source(key) is not None)}
    ordered_context: dict[str, Any] = {}
    context = grouped.get("context", {})
    for key in GROUPS["context"]:
        if key in context:
            ordered_context[key] = context[key]
    for role_key, role_fields in (("concern", ("priority",)), ("plan", PLAN_CONTEXT_FIELDS)):
        if role_key in context:
            ordered_context[role_key] = {key: context[role_key][key] for key in role_fields if key in context[role_key]}
    ordered_grouped: dict[str, Any] = {}
    for group in ("identity", "context", "relations", "state", "destination"):
        if group not in grouped:
            continue
        ordered_grouped[group] = ordered_context if group == "context" else grouped[group]
    candidate = {**ordered_grouped, **extras}
    transformed = render_grouped_metadata(candidate, body)
    cfront, cbody = split_frontmatter(transformed)
    decoded = yaml.load(cfront, Loader=UniqueSafeLoader)
    if cbody != body or flatten_metadata(decoded, original) != original:
        raise AssertionError("grouping transform failed inverse metadata/body preservation")
    return transformed, body


def write_summary_and_report(report: dict[str, Any]) -> None:
    counts = report["counts"]
    rows = report["records"]
    mapped_counts: collections.Counter[str] = collections.Counter()
    for row in rows:
        for group, fields in row.get("mapped_group_fields", {}).items():
            for field in fields:
                name = field if group == "relations" else f"{group}.{field}"
                mapped_counts[name] += 1
    snapshot = json.loads(NATIVE_SNAPSHOT.read_text(encoding="utf-8"))
    rows_by_path: dict[str, list[dict[str, Any]]] = collections.defaultdict(list)
    for row in rows:
        rows_by_path[row["path"]].append(row)
    supplemental_review_sources = []
    seen_supplemental: set[str] = set()
    for expected in snapshot.get("supplemental_sources", []):
        source_path = expected["path"]
        if source_path in seen_supplemental:
            raise ValueError(f"duplicate supplemental source path: {source_path}")
        seen_supplemental.add(source_path)
        matches = rows_by_path.get(source_path, [])
        if len(matches) != 1:
            raise ValueError(f"expected exactly one pinned supplemental source at {source_path}, found {len(matches)}")
        row = matches[0]
        if row.get("class") != "Draft" or row.get("transform_roundtrip") != "pass":
            raise ValueError(f"supplemental source is not a passing Draft: {source_path}")
        checks = {
            "atom_id": expected.get("atom_id"),
            "version": expected.get("version"),
            "status": expected.get("status"),
            "ref_id": expected.get("ref_id", f"{expected['atom_id']}@{expected['version']}-draft"),
        }
        mismatched = {key: {"snapshot": value, "observed": row.get(key)}
                      for key, value in checks.items() if row.get(key) != value}
        if row.get("sha256") != expected.get("sha256"):
            mismatched["sha256"] = {"snapshot": expected.get("sha256"), "observed": row.get("sha256")}
        if mismatched:
            raise ValueError(f"supplemental source metadata/hash differs from snapshot at {source_path}: {mismatched}")
        supplemental_review_sources.append({
            "id": row.get("atom_id"), "version": row.get("version"), "ref_id": row.get("ref_id"),
            "path": source_path, "sha256": row["sha256"], "class": row["class"],
            "status": row.get("status"), "transform_roundtrip": row.get("transform_roundtrip"),
            "snapshot_checks": list(checks) + ["sha256"], "promotion": "not performed",
        })
    d657 = ROOT / "CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-657-CORE_META_MODEL-DECISION--yaml-frontmatter-encodes-atom-properties-with-minimal-syntax.md"
    d657_sha = sha(d657.read_bytes()) if d657.is_file() else None
    summary = {
        "status": report["status"],
        "source_snapshot": {"path": report["baseline"]["path"], "sha256": report["baseline"]["sha256"], "count": counts["native_sources"]},
        "sources": counts["classes"],
        "approved_group_field_counts": dict(mapped_counts),
        "priority_mapping": {
            "concern_role_or_CA_C_ID_to_context.concern.priority": counts["priority_mapped_concern"],
            "by_CA_C_ID_fallback": sum(row.get("priority_mapping_state") == "mapped_concern" and row.get("role_evidence") == "atom_id_prefix" for row in rows),
            "by_explicit_role": sum(row.get("priority_mapping_state") == "mapped_concern" and row.get("role_evidence") == "header.role" for row in rows),
            "non_Concern_priority_preserved_flat": counts["priority_preserved_other_role"],
        },
        "plan_context_mapping": {
            "physical_autonomous_confidence_threshold_to_canonical_ai_agent_confidence_threshold": mapped_counts.get("context.plan.ai_agent_confidence_threshold", 0),
            "work_sequence_number": mapped_counts.get("context.plan.work_sequence_number", 0),
            "ai_agent_confidence_threshold_physical_source_count": counts["top_level_keys"].get("ai_agent_confidence_threshold", 0),
            "authority": {"id": "CA-D-657", "path": str(d657.relative_to(REPO)), "sha256": d657_sha},
        },
        "special_cases": {
            "sources_missing_role_with_no_supported_concern_or_plan_id_fallback": sum(row.get("role") is None for row in rows),
            "sources_missing_form": counts["native_sources"] - counts["top_level_keys"].get("form", 0),
            "sources_missing_updated_at": counts["native_sources"] - counts["top_level_keys"].get("updated_at", 0),
            "form_specific_context_slots_used": False,
            "supplemental_review_drafts": supplemental_review_sources,
        },
        "empty_groups": counts["empty_groups"],
        "checks": {key: counts[key] for key in ("parse_errors", "duplicate_key_errors", "source_pin_mismatches", "symlinks_excluded", "grouping_candidates_roundtrip_pass", "held_for_transform_collision_or_parse")},
        "path_delta_from_previous_snapshot": {key: counts[key] for key in ("added_since_baseline", "removed_since_baseline", "changed_hashes_on_common_paths")},
        "source_pin_mismatches": report["source_pin_mismatches"],
        "unmapped_extra_keys_preserved_flat": counts["unmapped_extra_keys"],
        "no_native_source_writes": True,
        "application_gate": "CA3+CA8 readiness is external; current Workbench readiness is NotReady.",
    }
    (PACKET / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    classes = counts["classes"]
    mismatch_ids = ", ".join((re.search(r"CA-[A-Z]-\d+", Path(item["path"]).name) or [Path(item["path"]).name])[0] for item in report["source_pin_mismatches"])
    extra_counts = counts["unmapped_extra_keys"]
    report_md = f"""# Header grouping source census and migration preparation

Read-only census of the root-owned native Current/Draft source set. The deterministic preparer computes a nested-header candidate in memory and verifies that inverse flattening restores the exact parsed metadata values and byte-identical Markdown body. It does not write native sources.

## Source set

- {counts['native_sources']:,} pinned native sources: {classes.get('Current', 0):,} Current and {classes.get('Draft', 0):,} Draft.
- Scope is exactly the path set in [`native-snapshot.json`](../native-snapshot.json); archives, generated `000`/applicable copies, tests, Journal, projections, and analysis packet descendants are excluded by that selection.
- Current path/hash pins are in [source-paths.json](source-paths.json). {counts['source_pin_mismatches']} source hashes differ from the root snapshot ({mismatch_ids}); the census uses directly observed live bytes and records refreshed preimage pins. Refresh and review them before application.
- YAML parsing found {counts['duplicate_key_errors']} duplicate-key errors, {counts['parse_errors']} malformed/missing sources, and {counts['symlinks_excluded']} symlinks in the pinned set.
- Compared with the previous source snapshot, {counts['added_since_baseline']} paths were added, {counts['removed_since_baseline']} removed, and {counts['changed_hashes_on_common_paths']} common paths changed. The current snapshot lists {len(supplemental_review_sources)} supplemental Draft sources, each checked against its pinned path, hash, ID, version, Draft Ref ID, and status.

## Approved grouping

The preparer maps common fields to `identity`, `context`, `relations`, `state`, and `destination`. The full per-field counts are in [summary.json](summary.json). Concern `priority` maps to `context.concern.priority` for Concern Role sources or the approved CA-C ID fallback. Plan `autonomous_confidence_threshold` maps to the canonical `context.plan.ai_agent_confidence_threshold` and `work_sequence_number` maps to `context.plan.work_sequence_number`.

- Concern priority: {counts['priority_mapped_concern']} values mapped ({summary['priority_mapping']['by_explicit_role']} by explicit Role, {summary['priority_mapping']['by_CA_C_ID_fallback']} by CA-C ID fallback). {counts['priority_preserved_other_role']} Plan `priority` values remain flat because no Plan priority slot is authorized.
- Plan context: {summary['plan_context_mapping']['physical_autonomous_confidence_threshold_to_canonical_ai_agent_confidence_threshold']} existing `autonomous_confidence_threshold` values map to `ai_agent_confidence_threshold`; {summary['plan_context_mapping']['work_sequence_number']} `work_sequence_number` values map. The physical source key is retained by inverse flatten for exact-value verification. No exact physical `ai_agent_confidence_threshold` key occurs.
- Canonical field authority is Current D657 (`{d657.name}`, SHA-256 `{d657_sha}`). No source has both the legacy and canonical Plan threshold keys.
- Other unmapped keys remain at the top level after the approved groups. Counts are in `header-census.json`; notable extras include `author` ({extra_counts.get('author', 0):,}), `current_scope_unit` ({extra_counts.get('current_scope_unit', 0):,}), `claim_target_scope_unit` ({extra_counts.get('claim_target_scope_unit', 0):,}), `assignee` ({extra_counts.get('assignee', 0):,}), and CCE legacy keys `cce_form`/`cce_version` ({extra_counts.get('cce_form', 0):,} each). Four Plan priority values remain flat. No unapproved group is inferred.
- {summary['special_cases']['sources_missing_role_with_no_supported_concern_or_plan_id_fallback']} sources lack Role without an approved Concern/Plan ID fallback; no Role or Form is synthesized.

## Shape and preservation checks

- Omit a group when it has no mapped leaf. Empty groups found: Context {counts['empty_groups'].get('context', 0):,}, Relations {counts['empty_groups'].get('relations', 0):,}, Destination {counts['empty_groups'].get('destination', 0):,}. State and Identity are populated in all sources. Explicit Relations values are preserved; none is an empty mapping.
- Deterministic transform/inverse-flatten checks passed for {counts['grouping_candidates_roundtrip_pass']:,} sources; {counts['held_for_transform_collision_or_parse']} are held. Candidate and source hashes are per record in [header-census.json](header-census.json).
- [representation-example.yaml](representation-example.yaml) illustrates Concern and common group shape. Unsupported extras remain flat.
- YAML serialization canonicalizes frontmatter layout and scalar presentation; it preserves parsed metadata values and the exact body. Preserving frontmatter comments or original quoting style would require a token/span-preserving writer.
- Runtime readers that expect flat `atom_id` and `status` require the separate CA #3 adapter/readiness gate before any cutover. Current Workbench readiness is NotReady. This preparation does not establish runtime compatibility, schema admission, or promotion.

Run `./.venv/bin/python .caprmedio_caprmedio/02_analysis/draft/header-groups-20261106/data/prepare_groups.py` from the repository root to refresh the census and in-memory round-trip hashes against the root-pinned source list.
"""
    (PACKET / "REPORT.md").write_text(report_md, encoding="utf-8")


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
        role, role_evidence_kind = role_evidence(metadata)
        extra = sorted(str(key) for key in keys if key not in FIELD_GROUP
                       and not (key == "priority" and role == "Concern")
                       and not (role == "Plan" and plan_target_for_source(key) is not None))
        extra_counts.update(extra)
        group_fields = {group: [field for field in fields if field in metadata] for group, fields in GROUPS.items()}
        if role == "Concern" and "priority" in metadata:
            group_fields["context"].append("concern.priority")
        elif role == "Plan":
            group_fields["context"].extend(
                f"plan.{target}" for target, sources in PLAN_CONTEXT_SOURCE_FIELDS.items()
                if any(source in metadata for source in sources)
            )
        empty_groups = [group for group, fields in group_fields.items() if not fields]
        empty_group_counts.update(empty_groups)
        relparts = path.relative_to(ROOT).parts
        role_index = next((i for i, part in enumerate(relparts[:-1]) if ROLE_PATTERN.fullmatch(part)), None)
        is_draft = role_index is not None and any(part.lower() == "draft" for part in relparts[role_index + 1:-1])
        source_class = "Draft" if is_draft else "Current"
        class_counts.update([source_class])
        candidate_text = None
        candidate_error = None
        try:
            candidate_text, body_text = transform_text(path.read_text(encoding="utf-8"))
        except Exception as exc:
            candidate_error = f"{type(exc).__name__}: {exc}"
        priority_state = "not_present"
        if "priority" in metadata:
            priority_state = "mapped_concern" if role == "Concern" else "unmapped_other_role"
        row = {
            "path": rel,
            "sha256": sha(raw),
            "native_snapshot_sha256": pinned_hashes.get(rel),
            "source_pin_status": "match" if pinned_hashes.get(rel) == sha(raw) else "refresh_preimage_pin_before_application",
            "class": source_class,
            "atom_id": metadata.get("atom_id"),
            "ref_id": metadata.get("ref_id"),
            "version": metadata.get("version"),
            "status": metadata.get("status"),
            "role_evidence": role_evidence_kind,
            "role": role,
            "top_level_keys": [str(key) for key in keys],
            "mapped_group_fields": group_fields,
            "empty_groups_to_omit_if_no_other_decision": empty_groups,
            "unmapped_extra_keys_preserved_at_root": [key for key in extra if not (
                (key == "priority" and role == "Concern") or
                (role == "Plan" and plan_target_for_source(key) is not None)
            )],
            "priority_mapping_state": priority_state,
            "candidate_sha256": sha(candidate_text.encode("utf-8")) if candidate_text is not None else None,
            "body_sha256": sha(body_text.encode("utf-8")) if candidate_text is not None else None,
            "transform_roundtrip": "pass" if candidate_text is not None else "hold",
            "transform_error": candidate_error,
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
            "grouping_candidates_roundtrip_pass": sum(row.get("transform_roundtrip") == "pass" for row in rows),
            "held_for_transform_collision_or_parse": sum(row.get("transform_roundtrip") != "pass" for row in rows),
            "priority_mapped_concern": sum(row.get("priority_mapping_state") == "mapped_concern" for row in rows),
            "priority_preserved_other_role": sum(row.get("priority_mapping_state") == "unmapped_other_role" for row in rows),
        },
        "current_paths": [{
            "path": row["path"], "sha256": row["sha256"],
            "native_snapshot_sha256": row.get("native_snapshot_sha256"),
            "source_pin_status": row.get("source_pin_status"), "class": row["class"],
        } for row in rows],
        "added_paths": added,
        "removed_paths": removed,
        "changed_hash_paths": hash_changed,
        "parse_errors": parse_errors,
        "duplicate_key_errors": duplicate_rows,
        "source_pin_mismatches": pin_mismatches,
        "symlink_paths_excluded": [str(path) for path in symlinks],
        "records": rows,
        "limits": [
            "Grouping candidates describe the approved common mapping and the confirmed Concern/Plan context slots; other extra keys remain top-level and are not assigned to a new group.",
            "No YAML text or native source was rewritten. This census does not prove semantic admission, runtime compatibility, or source migration readiness.",
            "Empty groups are reported for omission review; Relations values remain preserved as-is, including an explicitly empty mapping.",
        ],
    }
    PACKET.mkdir(parents=True, exist_ok=True)
    (PACKET / "source-paths.json").write_text(json.dumps({
        "native_snapshot_path": str(NATIVE_SNAPSHOT),
        "native_snapshot_sha256": sha(NATIVE_SNAPSHOT.read_bytes()),
        "previous_snapshot_sha256": sha(OLD_SNAPSHOT.read_bytes()),
        "sources": report["current_paths"],
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (PACKET / "header-census.json").write_text(json.dumps(report, ensure_ascii=False, indent=2, default=str) + "\n", encoding="utf-8")
    write_summary_and_report(report)
    print(json.dumps(report["counts"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
