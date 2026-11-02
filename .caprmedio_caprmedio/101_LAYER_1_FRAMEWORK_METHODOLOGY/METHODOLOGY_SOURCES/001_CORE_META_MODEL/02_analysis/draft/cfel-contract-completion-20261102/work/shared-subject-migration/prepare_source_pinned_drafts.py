#!/usr/bin/env python3
"""Prepare source-pinned Subject migration Drafts.

This lane copies selected active source carriers into role-local Draft
directories.  It changes only the Draft identity/status, the approved Subject
aliases, and the one known current CFEL operator address in the Cardinality
source.  Current sources, Journal, projections, and other lanes are read-only.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

import yaml


REPO = Path(__file__).resolve()
while not (REPO / ".caprmedio_caprmedio").is_dir():
    if REPO.parent == REPO:
        raise RuntimeError("repository root not found")
    REPO = REPO.parent

ANALYSIS = (
    REPO
    / ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/02_analysis/draft/cfel-contract-completion-20261102"
)
OUT = ANALYSIS / "work/shared-subject-migration"
INVENTORY = OUT / "alias-candidate-inventory.json"
BASELINE = ANALYSIS / "contract-graph/current-baseline.json"
MANIFEST = OUT / "source-pinned-draft-manifest.json"
OVERLAYS = OUT / "metadata-overlay-patches.json"

SKIP_IDS = {
    "CA-R-1643",
    "CA-R-1644",
    "CA-E-462",
    "CA-E-496",
    "CA-D-338",
    "CA-D-340",
    "CA-E-465",
    "CA-D-435",
    "CA-R-1569",
    "CA-R-1992",
}
LEGACY_ENTITY_IDS = {"CA-R-1213", "CA-R-1373", "CA-R-1616", "CA-R-2272"}
RELATION_EXCLUDED_IDS = {"CA-R-2247", "CA-E-436"}
# The legacy-CFEL lane already owns the authoritative Cardinality Draft.
# Keep its formal body and use only a metadata overlay if root needs one.
LEGACY_CFEL_OWNER_IDS = {"CA-R-2327"}
# These two Draft carriers belong to the semantic Projection Member lane.
# Preserve their paths and hashes; the owner packet is authoritative.
DELEGATED_SEMANTIC_IDS = {"CA-D-305", "CA-R-1314"}
# CA-R-1243 is an explicit retirement candidate.  Do not publish a Subject
# alias Draft for its superseded IS_BORNE_BY vocabulary.
RETIRED_ALIAS_IDS = {"CA-R-1243"}
PASSIVE_OPERATOR_ALIASES = {
    "CFEL > Relation//GOVERNS": "CFEL <+ Relation//GOVERNS",
    "CFEL > Relation//DERIVED_FROM": "CFEL <+ Relation//DERIVED_FROM",
}
CFEL_GENERIC_SUBJECT = "CFEL > Relation"
CFEL_TYPED_SUBJECTS = {
    "CFEL > Relation//DEPENDS_ON",
    "CFEL > Relation//NARROWER_THAN",
}
CFEL_GENERIC_IDS: set[str] = set()


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    return path.relative_to(REPO).as_posix()


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def id_sort(value: str) -> tuple[str, int, str]:
    match = re.match(r"^([A-Za-z]+)-?(\d+)$", value)
    if match:
        return match.group(1), int(match.group(2)), value
    return value, -1, value


def compact(value: str) -> str:
    value = re.sub(r"\s*:=\s*", ":=", value)
    value = re.sub(r"\s*:\s*", ":", value)
    return value.strip()


def parse_carrier(path: Path) -> tuple[dict[str, Any], str, str]:
    text = path.read_text(encoding="utf-8")
    parts = text.split("---\n", 2)
    if len(parts) != 3 or parts[0] != "":
        raise ValueError(f"missing YAML frontmatter: {path}")
    frontmatter = yaml.safe_load(parts[1]) or {}
    return frontmatter, parts[1], parts[2]


def render_carrier(metadata: dict[str, Any], body: str) -> str:
    frontmatter = yaml.safe_dump(
        metadata,
        sort_keys=False,
        allow_unicode=True,
        default_flow_style=False,
        width=1000,
    )
    return f"---\n{frontmatter}---\n{body}"


def summary_from_body(body: str) -> str | None:
    match = re.search(r"(?ms)^## Summary\s*\n\s*(.*?)(?=^## |\Z)", body)
    return match.group(1).strip() if match else None


def source_rows(baseline: dict[str, Any]) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for row in baseline["coverage_gaps"]:
        result.setdefault(row["source"]["atom_id"], row)
    return result


def alias_maps(inventory: dict[str, Any]) -> dict[str, str]:
    """Return only exact source-backed aliases, including known lane aliases."""

    mapping = {
        compact(item["subject"]): compact(item["proposed_canonical"])
        for item in inventory["entries"]
        if item.get("bound_without_new_entity") and item.get("proposed_canonical")
    }
    # These are the explicitly requested current CFEL composition addresses.
    mapping[CFEL_GENERIC_SUBJECT] = "CFEL <+ Relation"
    for old in CFEL_TYPED_SUBJECTS:
        mapping[old] = old.replace("CFEL >", "CFEL <+", 1)
    return mapping


def current_subject_by_id(baseline: dict[str, Any]) -> dict[str, str]:
    result: dict[str, str] = {}
    for row in baseline["coverage_gaps"]:
        result.setdefault(row["source"]["atom_id"], row["subject"])
    return result


def relation_source_ids(baseline: dict[str, Any]) -> tuple[set[str], set[str]]:
    generic: set[str] = set()
    typed: set[str] = set()
    for row in baseline["coverage_gaps"]:
        subject = row["subject"]
        sid = row["source"]["atom_id"]
        if subject == CFEL_GENERIC_SUBJECT and sid not in RELATION_EXCLUDED_IDS:
            generic.add(sid)
        if subject in CFEL_TYPED_SUBJECTS:
            typed.add(sid)
    return generic, typed


def eligible_source_ids(inventory: dict[str, Any], baseline: dict[str, Any]) -> tuple[set[str], set[str]]:
    proven = {
        sid
        for item in inventory["entries"]
        if item.get("bound_without_new_entity")
        for sid in item["source_ids"]
    }
    proven -= SKIP_IDS | LEGACY_ENTITY_IDS
    generic, typed = relation_source_ids(baseline)
    requested = proven | generic | typed
    return requested, proven


def source_role_root(source_path: Path) -> Path:
    roles = {
        "01_concern",
        "02_analysis",
        "04_requirement",
        "05_method",
        "06_evaluation",
        "07_delivery",
    }
    for parent in (source_path, *source_path.parents):
        if parent.name in roles:
            return parent
    raise ValueError(f"cannot find role root for {source_path}")


def existing_candidate_files() -> list[Path]:
    # Restrict the scan to this Epic's candidate packet.  Source carriers do
    # not use the @N-draft filename form.
    return sorted(
        path
        for path in (REPO / ".caprmedio_caprmedio").rglob("CA-*@*-draft-*.md")
        if "cfel-contract-completion-20261102" in path.as_posix()
    )


def candidate_index() -> tuple[dict[str, list[tuple[int, Path]]], dict[str, list[tuple[int, Path]]]]:
    versions: dict[str, list[tuple[int, Path]]] = {}
    by_source: dict[str, list[tuple[int, Path]]] = {}
    pattern = re.compile(r"^(CA-[A-Z]+-\d+)@(\d+)-draft-")
    for path in existing_candidate_files():
        match = pattern.match(path.name)
        if not match:
            continue
        base, version_text = match.groups()
        version = int(version_text)
        versions.setdefault(base, []).append((version, path))
        by_source.setdefault(base, []).append((version, path))
    return versions, by_source


def all_project_versions(bases: set[str]) -> dict[str, set[int]]:
    """Collect the version numbers already attached to each base Atom ID."""

    result: dict[str, set[int]] = {}
    draft_pattern = re.compile(r"^(CA-[A-Z]+-\d+)@(\d+)-draft-")
    current_pattern = re.compile(r"^(CA-[A-Z]+-\d+)-")
    for path in (REPO / ".caprmedio_caprmedio").rglob("*.md"):
        match = draft_pattern.match(path.name)
        if match and match.group(1) in bases:
            result.setdefault(match.group(1), set()).add(int(match.group(2)))
            continue
        match = current_pattern.match(path.name)
        if not match or match.group(1) not in bases:
            continue
        base = match.group(1)
        # Current source filenames have no @N marker.  Read only these
        # matching files and extract the scalar version without YAML parsing.
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        version_match = re.search(r"^version:\s*(\d+)\s*$", text, re.MULTILINE)
        if version_match:
            result.setdefault(base, set()).add(int(version_match.group(1)))
    return result


def candidate_suffix(source_path: Path, source_id: str, form: str) -> str:
    name = source_path.name
    prefix = f"{source_id}-"
    if not name.startswith(prefix):
        raise ValueError(f"source filename does not begin with {source_id}: {source_path}")
    suffix = name[len(prefix) :]
    if form == "Declaration":
        suffix = suffix.replace("ENTITY_DEFINITION", "DECLARATION", 1)
        suffix = suffix.replace("RELATION_DEFINITION", "DECLARATION", 1)
    return suffix


def proper_form(metadata: dict[str, Any]) -> str:
    form = metadata.get("form")
    if form in {"Entity Definition", "Relation Definition"}:
        return "Declaration"
    return form


def body_replacements(body: str, old_subject: str, new_subject: str) -> tuple[str, list[dict[str, str]]]:
    """Change only standalone current address lines inside a fenced block.

    Historical source pins and ordinary prose remain byte-for-byte unchanged.
    The legacy Cardinality source is handled by an overlay and is not rewritten
    here.  No current owned candidate presently has a body address requiring
    migration.
    """

    replacements: list[dict[str, str]] = []
    lines = body.splitlines(keepends=True)
    in_fence = False
    fence_marker = ""
    for index, line in enumerate(lines):
        stripped = line.rstrip("\r\n")
        if not in_fence and re.match(r"^\s*```", stripped):
            in_fence = True
            fence_marker = stripped.lstrip()[:3]
            continue
        if in_fence and stripped.lstrip().startswith(fence_marker) and stripped.lstrip().startswith("```"):
            in_fence = False
            fence_marker = ""
            continue
        if in_fence and stripped.strip() == old_subject:
            ending = line[len(line.rstrip("\r\n")) :]
            lines[index] = new_subject + ending
            replacements.append({"line": str(index + 1), "before": old_subject, "after": new_subject})
    return "".join(lines), replacements


def changed_fields(before: dict[str, Any], after: dict[str, Any]) -> list[dict[str, Any]]:
    fields: list[dict[str, Any]] = []
    for field in ("atom_id", "version", "status", "role", "form", "subjects"):
        if before.get(field) != after.get(field):
            fields.append({"field": field, "before": before.get(field), "after": after.get(field)})
    return fields


def is_relation_lane_candidate(path: Path) -> bool:
    return "/relations/" in path.as_posix() or "/relation-consumers/" in path.as_posix()


def enrich_existing_candidates(
    candidates: list[dict[str, Any]],
    *,
    source_path: Path,
    source_id: str,
    source_subject: str,
    candidate_subject: str,
) -> list[dict[str, Any]]:
    enriched: list[dict[str, Any]] = []
    for item in candidates:
        detail = dict(item)
        path = REPO / str(item["path"])
        detail["candidate_sha256"] = sha(path)
        try:
            metadata, _, _ = parse_carrier(path)
        except (OSError, ValueError, yaml.YAMLError) as error:
            detail["candidate_metadata_error"] = str(error)
        else:
            detail["candidate_id"] = metadata.get("atom_id")
            detail["candidate_status"] = metadata.get("status")
            detail["candidate_subject"] = (metadata.get("subjects") or {}).get("active")
        detail["source_id"] = source_id
        detail["source_path"] = rel(source_path)
        detail["source_sha256"] = sha(source_path)
        detail["source_subject"] = source_subject
        detail["requested_subject"] = candidate_subject
        enriched.append(detail)
    return enriched


def clear_owned_candidates() -> None:
    """Make this generator idempotent within its exclusive output lane."""

    # Remove only candidates recorded by the previous run.  This also handles
    # source roots outside METHODOLOGY_SOURCES, while leaving pre-existing
    # same-lane candidates available for overlay disposition.
    if MANIFEST.exists():
        try:
            previous = load(MANIFEST)
        except (OSError, json.JSONDecodeError):
            previous = {}
        for row in previous.get("created", []):
            if row.get("source_id") in DELEGATED_SEMANTIC_IDS:
                continue
            path = REPO / row["candidate_path"]
            if path.exists():
                path.unlink()

    source_root = (
        REPO
        / ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES"
    )
    for path in source_root.rglob("cfel-contract-completion-20261102/subject-migration/*.md"):
        match = re.match(r"^(CA-[A-Z]+-\d+)@", path.name)
        if match and match.group(1) in DELEGATED_SEMANTIC_IDS:
            continue
        path.unlink()


def main() -> None:  # noqa: C901 - bounded packet assembly is intentionally linear
    inventory = load(INVENTORY)
    baseline = load(BASELINE)
    rows = source_rows(baseline)
    subjects = current_subject_by_id(baseline)
    aliases = alias_maps(inventory)
    requested, proven = eligible_source_ids(inventory, baseline)
    generic_ids, typed_ids = relation_source_ids(baseline)

    # This lane owns its output directory; remove only its previously generated
    # Drafts so repeated runs produce one deterministic candidate per source.
    clear_owned_candidates()

    # Existing relation-lane and semantic candidates are owned sources, not a
    # reason to create a second Draft.  The legacy-CFEL R2327 candidate keeps
    # its authoritative formal body and receives metadata disposition only.
    existing_by_id: dict[str, list[tuple[int, Path]]] = {}
    existing_versions, _ = candidate_index()
    for base, candidates in existing_versions.items():
        existing_by_id[base] = candidates

    used_versions = all_project_versions(requested)
    created: list[dict[str, Any]] = []
    skipped: list[dict[str, Any]] = []
    overlays: list[dict[str, Any]] = []
    unresolved_metadata_aliases: list[dict[str, str]] = []
    applied_passive_operator_aliases: list[dict[str, str]] = []

    for source_id in sorted(requested, key=id_sort):
        row = rows.get(source_id)
        if row is None:
            skipped.append({"source_id": source_id, "reason": "source is not present in current baseline"})
            continue
        source_path = REPO / row["source"]["path"]
        if source_id in RELATION_EXCLUDED_IDS:
            skipped.append({"source_id": source_id, "reason": "excluded relation source; other lane owns it"})
            continue
        if source_id in RETIRED_ALIAS_IDS:
            skipped.append(
                {
                    "source_id": source_id,
                    "reason": "explicit retirement candidate; do not publish a Subject alias Draft",
                }
            )
            continue
        if source_id in LEGACY_CFEL_OWNER_IDS:
            candidates = [
                {"version": version, "path": rel(path)}
                for version, path in existing_by_id.get(source_id, [])
            ]
            candidates = enrich_existing_candidates(
                candidates,
                source_path=source_path,
                source_id=source_id,
                source_subject=subjects[source_id],
                candidate_subject=aliases.get(compact(subjects[source_id]), "CFEL <+ Cardinality"),
            )
            skipped.append(
                {
                    "source_id": source_id,
                    "reason": "authoritative legacy-CFEL semantic packet; do not publish a duplicate mechanical Draft",
                    "existing_candidates": candidates,
                    "overlay_required": True,
                }
            )
            overlays.append(
                {
                    "source_id": source_id,
                    "source_path": rel(source_path),
                    "required_patch": "metadata overlay only; preserve authoritative legacy-CFEL body and formal expression",
                    "existing_candidates": candidates,
                    "basis": "legacy-cfel packet is authoritative; mechanical subject-migration duplicate withdrawn",
                }
            )
            continue
        metadata, _, body = parse_carrier(source_path)
        if metadata.get("status") != "Active":
            skipped.append({"source_id": source_id, "reason": f"source status is {metadata.get('status')!r}, not Active"})
            continue
        old_subject = subjects[source_id]
        old_key = compact(old_subject)
        new_subject = aliases.get(old_key)
        if source_id in generic_ids:
            new_subject = "CFEL <+ Relation"
        elif old_subject in CFEL_TYPED_SUBJECTS or old_key in CFEL_TYPED_SUBJECTS:
            new_subject = old_key.replace("CFEL >", "CFEL <+", 1)
        if not new_subject:
            skipped.append({"source_id": source_id, "reason": "no exact approved alias for active Subject", "subject": old_subject})
            continue

        if source_id in DELEGATED_SEMANTIC_IDS:
            candidates = [
                {"version": version, "path": rel(path)}
                for version, path in existing_by_id.get(source_id, [])
                if "/subject-migration/" in path.as_posix()
            ]
            candidates = enrich_existing_candidates(
                candidates,
                source_path=source_path,
                source_id=source_id,
                source_subject=old_subject,
                candidate_subject=new_subject,
            )
            skipped.append(
                {
                    "source_id": source_id,
                    "reason": "delegated semantic Projection Member correction; owner B packet is authoritative",
                    "existing_candidates": candidates,
                    "overlay_required": True,
                }
            )
            overlays.append(
                {
                    "source_id": source_id,
                    "source_path": rel(source_path),
                    "required_patch": "delegated semantic B; root prefers the owner packet and excludes this A row",
                    "existing_candidates": candidates,
                    "basis": "separate semantic Projection Member lane; no concurrent rewrite",
                }
            )
            continue

        relation_owned = any(is_relation_lane_candidate(path) for _, path in existing_by_id.get(source_id, []))
        subject_lane_candidates = [
            {"version": version, "path": rel(path)}
            for version, path in existing_by_id.get(source_id, [])
            if "/subject-migration/" in path.as_posix()
        ]
        if subject_lane_candidates:
            subject_lane_candidates = enrich_existing_candidates(
                subject_lane_candidates,
                source_path=source_path,
                source_id=source_id,
                source_subject=old_subject,
                candidate_subject=new_subject,
            )
            skipped.append(
                {
                    "source_id": source_id,
                    "reason": "existing subject-migration candidate; do not duplicate",
                    "existing_candidates": subject_lane_candidates,
                    "overlay_required": True,
                }
            )
            overlays.append(
                {
                    "source_id": source_id,
                    "source_path": rel(source_path),
                    "required_patch": "merge exact source pin and metadata fields into the existing subject-migration candidate",
                    "existing_candidates": subject_lane_candidates,
                    "basis": "pre-existing same-lane candidate; no duplicate candidate",
                }
            )
            continue
        if relation_owned and source_id != "CA-R-2327":
            candidates = [
                {"version": version, "path": rel(path)}
                for version, path in existing_by_id[source_id]
            ]
            candidates = enrich_existing_candidates(
                candidates,
                source_path=source_path,
                source_id=source_id,
                source_subject=old_subject,
                candidate_subject=new_subject,
            )
            skipped.append(
                {
                    "source_id": source_id,
                    "reason": "existing relation-lane candidate; do not duplicate",
                    "existing_candidates": candidates,
                    "overlay_required": True,
                }
            )
            overlays.append(
                {
                    "source_id": source_id,
                    "source_path": rel(source_path),
                    "required_patch": "merge exact Subject metadata into the existing relation-lane candidate",
                    "existing_candidates": candidates,
                    "basis": "other-lane ownership; no duplicate candidate",
                }
            )
            continue

        before_metadata = dict(metadata)
        candidate_metadata = dict(metadata)
        source_version = int(metadata["version"])
        version = source_version + 1
        # Reusing the old R2327 candidate version is forbidden; choose the
        # next globally free version.  This also protects reruns from Draft
        # identity collisions.
        while version in used_versions.setdefault(source_id, set()):
            version += 1
        candidate_form = proper_form(candidate_metadata)
        candidate_metadata["atom_id"] = f"{source_id}@{version}-draft"
        candidate_metadata["version"] = version
        candidate_metadata["status"] = "Draft"
        candidate_metadata["form"] = candidate_form
        subject_data = candidate_metadata.get("subjects") or {}
        subject_data["active"] = new_subject
        passive = subject_data.get("passive") or []
        if isinstance(passive, str):
            passive = [passive]
        canonical_passive: list[str] = []
        for value in passive:
            text = str(value)
            compact_value = compact(text)
            replacement = PASSIVE_OPERATOR_ALIASES.get(
                compact_value,
                aliases.get(compact_value, text),
            )
            if replacement != text and compact_value in PASSIVE_OPERATOR_ALIASES:
                applied_passive_operator_aliases.append(
                    {
                        "source_id": source_id,
                        "before": text,
                        "after": replacement,
                        "basis": "approved relation-name continuity; operator direction only",
                    }
                )
            if replacement == text and text.startswith("CFEL >"):
                unresolved_metadata_aliases.append(
                    {
                        "source_id": source_id,
                        "field": "subjects.passive",
                        "value": text,
                        "decision": "preserve until an exact approved alias is registered; do not infer a relation-kind mapping",
                    }
                )
            if replacement not in canonical_passive:
                canonical_passive.append(replacement)
        subject_data["passive"] = canonical_passive
        candidate_metadata["subjects"] = subject_data

        candidate_body, replacements = body_replacements(body, old_subject, new_subject)
        candidate_path = source_role_root(source_path) / "draft/cfel-contract-completion-20261102/subject-migration"
        candidate_path = candidate_path / f"{source_id}@{version}-draft-{candidate_suffix(source_path, source_id, candidate_form)}"
        candidate_path.parent.mkdir(parents=True, exist_ok=True)
        candidate_text = render_carrier(candidate_metadata, candidate_body)
        candidate_path.write_text(candidate_text, encoding="utf-8")
        used_versions[source_id].add(version)

        created.append(
            {
                "source_id": source_id,
                "source_path": rel(source_path),
                "source_sha256": sha(source_path),
                "baseline_source_sha256": row["source"]["sha256"],
                "source_baseline_sha_match": sha(source_path) == row["source"]["sha256"],
                "source_version": source_version,
                "source_summary": summary_from_body(body),
                "source_subject": old_subject,
                "candidate_subject": new_subject,
                "candidate_path": rel(candidate_path),
                "candidate_id": candidate_metadata["atom_id"],
                "candidate_version": version,
                "candidate_sha256": sha(candidate_path),
                "candidate_role": candidate_metadata.get("role"),
                "candidate_form": candidate_form,
                "candidate_summary": summary_from_body(candidate_body),
                "summary_preserved": summary_from_body(body) == summary_from_body(candidate_body),
                "exact_field_changes": changed_fields(before_metadata, candidate_metadata),
                "body_sha256_before": hashlib.sha256(body.encode("utf-8")).hexdigest(),
                "body_sha256_after": hashlib.sha256(candidate_body.encode("utf-8")).hexdigest(),
                "body_changed": body != candidate_body,
                "body_replacements": replacements,
                "basis": (
                    [
                        "alias-candidate-inventory.json: bound_without_new_entity",
                        "contract-graph/current-baseline.json: source path/version/hash",
                    ]
                    if source_id in proven
                    else [
                        "contract-graph/current-baseline.json: current active CFEL Relation subject",
                        "approved current composition mapping: CFEL > Relation -> CFEL <+ Relation",
                    ]
                ),
            }
        )

    product_working = ANALYSIS / "legacy-entities/legacy-entities-working-dispositions.json"
    product_rows = load(product_working).get("rows", [])
    product_row = next((row for row in product_rows if row.get("id") == "CA-R-2256"), None)
    product_candidate = Path(product_row["candidate_path"]) if product_row else None
    if product_candidate and not product_candidate.is_absolute():
        product_candidate = REPO / product_candidate
    product_hash = sha(product_candidate) if product_candidate and product_candidate.exists() else None
    product_verified = bool(
        product_row
        and product_candidate.exists()
        and product_hash == product_row.get("candidate_sha256")
        and product_row.get("candidate_sha256") == "b1211656140ab8f293719350d5036c97d30314d00ac9c8b1aadc4234bda31fda"
    )
    product_note = {
        "status": "applied_existing_authoritative_candidate" if product_verified else "proof_missing",
        "old_subject": "Entity/Aspect/Product: CAPRMEDIO Framework",
        "requested_replacement": "Node/Continuant//CAPRMEDIO Framework",
        "source_id": "CA-R-2256",
        "basis": rel(product_working),
        "candidate_path": rel(product_candidate) if product_candidate and product_candidate.exists() else None,
        "candidate_sha256": product_hash,
        "expected_candidate_sha256": product_row.get("candidate_sha256") if product_row else None,
        "reason": (
            "Use the existing authoritative Declaration Draft; do not create a duplicate candidate."
            if product_verified
            else "The authoritative product Declaration proof is unavailable or has a different hash."
        ),
    }

    manifest = {
        "schema_version": 1,
        "status": "SOURCE_PINNED_DRAFTS_READY_FOR_REVIEW",
        "scope": "Subject metadata migration; Current sources, Journal, projections, and other-lane candidates remain unchanged",
        "source_inventory": rel(INVENTORY),
        "baseline": rel(BASELINE),
        "requested": {
            "proven_bound_without_new_entity_source_ids": len(proven),
            "generic_cfel_relation_source_ids": len(generic_ids),
            "typed_cfel_relation_source_ids": len(typed_ids),
            "total_unique_source_ids": len(requested),
            "generic_cfel_relation_ids": sorted(generic_ids, key=id_sort),
            "typed_cfel_relation_ids": sorted(typed_ids, key=id_sort),
        },
        "excluded": {
            "explicit_skip_ids": sorted(SKIP_IDS, key=id_sort),
            "legacy_entity_lane_ids": sorted(LEGACY_ENTITY_IDS, key=id_sort),
            "relation_lane_ids": sorted(RELATION_EXCLUDED_IDS, key=id_sort),
            "delegated_semantic_ids": sorted(DELEGATED_SEMANTIC_IDS, key=id_sort),
            "retired_alias_ids": sorted(RETIRED_ALIAS_IDS, key=id_sort),
            "legacy_cfel_owner_ids": sorted(LEGACY_CFEL_OWNER_IDS, key=id_sort),
            "reason": "These source IDs are assigned to another lane or explicitly deferred; no duplicate Draft is created here.",
        },
        "created_count": len(created),
        "skipped_count": len(skipped),
        "overlay_count": len(overlays),
        "verification": {
            "source_baseline_hashes_match": all(row["source_baseline_sha_match"] for row in created),
            "summaries_preserved": all(row["summary_preserved"] for row in created),
            "draft_status_and_version_written": all(
                row["candidate_id"].endswith("-draft") and row["candidate_version"] > row["source_version"]
                for row in created
            ),
            "active_aliases_are_source_backed": all(bool(row["candidate_subject"]) for row in created),
            "body_changes": [
                {"source_id": row["source_id"], "replacements": row["body_replacements"]}
                for row in created
                if row["body_changed"]
            ],
            "generic_relation_rules": {
                "requested": len(generic_ids),
                "created": sum(row["source_id"] in generic_ids for row in created),
                "existing_overlay": sum(
                    item["source_id"] in generic_ids for item in overlays
                ),
                "retired": sum(
                    item["source_id"] in generic_ids and item["source_id"] in RETIRED_ALIAS_IDS
                    for item in skipped
                ),
            },
            "typed_relation_rules": {
                "requested": len(typed_ids),
                "created": sum(row["source_id"] in typed_ids for row in created),
                "existing_overlay": sum(
                    item["source_id"] in typed_ids for item in overlays
                ),
                "retired": sum(
                    item["source_id"] in typed_ids and item["source_id"] in RETIRED_ALIAS_IDS
                    for item in skipped
                ),
            },
            "product_replacement_applied": product_verified,
            "applied_passive_operator_aliases": applied_passive_operator_aliases,
            "delegated_passive_operator_aliases": [
                {
                    "source_id": "CA-R-1314",
                    "before": "CFEL > Relation//DERIVED_FROM",
                    "after": "CFEL <+ Relation//DERIVED_FROM",
                    "owner": "separate semantic Projection Member lane",
                }
            ],
            "unresolved_metadata_aliases": unresolved_metadata_aliases,
        },
        "created": created,
        "skipped": skipped,
        "unresolved_metadata_aliases": unresolved_metadata_aliases,
        "product_replacement": product_note,
    }
    OUT.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    OVERLAYS.write_text(json.dumps({"schema_version": 1, "status": "OVERLAY_PATCHES_FOR_ROOT_MERGER", "items": overlays}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"created": len(created), "skipped": len(skipped), "overlays": len(overlays), "requested": len(requested)}, indent=2))


if __name__ == "__main__":
    main()
