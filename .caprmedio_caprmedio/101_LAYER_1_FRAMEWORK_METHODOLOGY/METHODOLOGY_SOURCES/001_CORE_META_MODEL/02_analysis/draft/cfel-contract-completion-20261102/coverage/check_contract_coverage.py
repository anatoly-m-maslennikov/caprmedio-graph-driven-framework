#!/usr/bin/env python3
"""Check the source-bound CFEL/entity contract coverage.

This is a bounded evidence checker, not a CFEL parser.  It checks:

* the pinned Current source frontier;
* the selected 90 Node Declarations;
* retained CFEL, Carrier and Term root sources;
* every Current Relation Definition candidate;
* raw labelled CFEL blocks, every fenced Claim block (including legacy and
  unrecognized blocks), prose Claim sections and relation-token usage;
* a later generated contract graph, when supplied.

Relation names are not inferred from arbitrary operators, literals, predicates
or wildcards.  A relation is modelled only when it is named by a Relation
Definition candidate.  Direct and derived permissions remain independent;
inverse bounds are never inferred.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve()
for candidate in ROOT.parents:
    if (candidate / ".git").exists():
        REPO_ROOT = candidate
        break
else:  # pragma: no cover - only applies to a copied standalone script
    REPO_ROOT = Path.cwd()

ANALYSIS_ROOT = (
    REPO_ROOT
    / ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/"
    "METHODOLOGY_SOURCES/001_CORE_META_MODEL/02_analysis/draft/"
    "cfel-contract-completion-20261102"
)
FRONTIER_DEFAULT = (
    REPO_ROOT
    / ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/"
    "METHODOLOGY_SOURCES/001_CORE_META_MODEL/02_analysis/draft/"
    "node-declaration-20261031/migration-20261101/current-source-frontier.json"
)
DIAGNOSTICS_DEFAULT = FRONTIER_DEFAULT.parent / "current-graph-diagnostics.json"
INVENTORY_DEFAULT = (
    REPO_ROOT
    / ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/"
    "METHODOLOGY_SOURCES/001_CORE_META_MODEL/02_analysis/draft/"
    "node-declaration-20261031/declaration-expansion/selected-node-inventory.json"
)

RELATION_NAME_RE = re.compile(r"\bRelation//([A-Za-z_][A-Za-z0-9_]*)")
DOUBLE_RELATION_RE = re.compile(r"\(\(\s*([A-Za-z_][A-Za-z0-9_]*)\s*\)\)")
FENCE_RE = re.compile(r"^(?P<indent>\s*)(?P<fence>`{3,}|~{3,})\s*(?P<info>[^\s]*)?.*$")
HEADING_RE = re.compile(r"^##(?!#)\s+(.+?)\s*$")
CLAIM_RE = re.compile(r"^##\s+Claim\s*$", re.IGNORECASE)

# These are syntax/predicate words, never relation declarations.  The set is
# deliberately conservative: unknown names remain review candidates.
CFEL_PREDICATES = frozenset(
    {
        "ALL",
        "AND",
        "ANY",
        "AS",
        "COUNT",
        "DISTINCT",
        "ELSE",
        "EMPTY",
        "EXISTS",
        "FALSE",
        "FORALL",
        "IF",
        "IN",
        "IS",
        "MAX",
        "MIN",
        "NOT",
        "NULL",
        "OR",
        "SUM",
        "THEN",
        "TRUE",
        "WHERE",
        "WITH",
    }
)
CFEL_RELATION_PLACEHOLDERS = frozenset({"R", "RELATION", "RELATION_TOKEN", "RELATION_TYPE"})
CFEL_OPERATOR_RE = re.compile(
    r"(?P<operator>\+>|<\+|\|<|>|<|>>|<<|::|:=|==|=|:|;|\*\*|\*)"
)

RELATION_MANIFEST = ANALYSIS_ROOT / "relations/coverage-manifest.json"
DERIVED_CANDIDATES = ANALYSIS_ROOT / "relations/derived-declaration-candidates.json"
SOURCE_CANDIDATES = ANALYSIS_ROOT / "relations/source-definition-candidates.json"
LEGACY_CFEL_MANIFEST = ANALYSIS_ROOT / "legacy-cfel/manifest.json"

# These are the path aliases explicitly recorded by the current parser.  They
# are evidence of existing notation, not a license to invent a short symbol
# for a named Relation that has none.
PUBLIC_PATH_ALIASES = {
    "/": "NARROWER_THAN",
    "//": "INSTANCE_OF",
    ".": "IS_PROPERTY_OF",
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_path(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def rel_path(path: Path) -> str:
    resolved = path.resolve()
    try:
        return resolved.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return resolved.as_posix()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def relation_support_manifests() -> tuple[dict[str, Any], list[dict[str, Any]], list[dict[str, Any]]]:
    """Load optional relation-lane evidence without making it authoritative.

    The live frontier remains the source of the Current candidate set.  These
    packets only add explicit notation/inverse/derived-link evidence and draft
    provenance to the coverage report.
    """

    manifest = load_json(RELATION_MANIFEST) if RELATION_MANIFEST.exists() else {}
    source = load_json(SOURCE_CANDIDATES) if SOURCE_CANDIDATES.exists() else []
    derived = load_json(DERIVED_CANDIDATES) if DERIVED_CANDIDATES.exists() else []
    if not isinstance(source, list):
        source = []
    if not isinstance(derived, list):
        derived = []
    return manifest if isinstance(manifest, dict) else {}, source, derived


def confirmed_inverse_pairs(manifest: dict[str, Any]) -> dict[str, str]:
    """Return both directions of explicitly confirmed endpoint reversals."""

    values = manifest.get("inverse_names_explicitly_covered", {})
    if not isinstance(values, dict):
        return {}
    pairs: dict[str, str] = {}
    for left, right in values.items():
        if isinstance(left, str) and isinstance(right, str) and left and right:
            pairs[left] = right
            pairs[right] = left
    return pairs


def frontier_rows(frontier_path: Path) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    data = load_json(frontier_path)
    raw_rows = data.get("operations", [])
    if isinstance(raw_rows, dict):
        rows = list(raw_rows.values())
    else:
        rows = list(raw_rows)
    rows.sort(key=lambda row: row.get("destination_path", ""))
    return data, rows


def frontmatter(text: str) -> dict[str, Any]:
    """Extract the small metadata subset needed by this evidence check."""

    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        return {}
    result: dict[str, Any] = {}
    in_subjects = False
    subjects: dict[str, Any] = {}
    list_key: str | None = None
    for line in lines[1:end]:
        if not line.strip():
            continue
        if line.startswith("subjects:"):
            in_subjects = True
            list_key = None
            continue
        if in_subjects and line and not line.startswith(" "):
            in_subjects = False
            list_key = None
        if in_subjects:
            match = re.match(r"^\s+(active|passive|governs|depends_on):\s*(.*)$", line)
            if match:
                key, value = match.groups()
                if value:
                    subjects[key] = value.strip().strip('"')
                    list_key = None
                else:
                    subjects[key] = []
                    list_key = key
                continue
            item = re.match(r"^\s+-\s+(.*)$", line)
            if item and list_key:
                value = item.group(1).strip().strip('"')
                assert isinstance(subjects[list_key], list)
                subjects[list_key].append(value)
            continue
        match = re.match(r"^(atom_id|version|status|role|form|current_scope_unit|updated_at):\s*(.*)$", line)
        if match:
            key, value = match.groups()
            result[key] = value.strip().strip('"')
    result["subjects"] = subjects
    return result


def active_subject(meta: dict[str, Any]) -> str:
    value = meta.get("subjects", {}).get("active", "")
    return value if isinstance(value, str) else ""


def source_record(row: dict[str, Any], path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    meta = frontmatter(text)
    return {
        "id": row.get("base_id") or meta.get("atom_id"),
        "version": row.get("version") or int(meta.get("version", 0)),
        "status": row.get("status") or meta.get("status"),
        "path": rel_path(path),
        "sha256": row.get("sha256") or sha256_bytes(text.encode()),
        "actual_sha256": sha256_path(path),
        "sha256_matches_frontier": row.get("sha256") == sha256_path(path),
        "role": meta.get("role", ""),
        "form": meta.get("form", ""),
        "active_subject": active_subject(meta),
        "text": text,
    }


def source_key(record: dict[str, Any]) -> str:
    return f"{record.get('id')}@{record.get('version')}"


def source_pin(record: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": record.get("id"),
        "version": record.get("version"),
        "status": record.get("status"),
        "path": record.get("path"),
        "sha256": record.get("sha256"),
    }


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def labelled_cfel_blocks(text: str) -> list[dict[str, Any]]:
    lines = text.splitlines()
    blocks: list[dict[str, Any]] = []
    index = 0
    while index < len(lines):
        match = FENCE_RE.match(lines[index])
        info = (match.group("info") or "") if match else ""
        if not match or not info.lower().startswith("cfel"):
            index += 1
            continue
        fence = match.group("fence")
        start = index
        index += 1
        content: list[str] = []
        while index < len(lines):
            close = FENCE_RE.match(lines[index])
            if close and close.group("fence")[0] == fence[0] and len(close.group("fence")) >= len(fence):
                break
            content.append(lines[index])
            index += 1
        end = min(index, len(lines) - 1)
        raw = "\n".join(content)
        blocks.append(
            {
                "line_start": start + 1,
                "line_end": end + 1,
                "label": info,
                "raw_sha256": sha256_bytes(raw.encode()),
                "text": raw,
            }
        )
        index += 1
    return blocks


def claim_section(text: str) -> tuple[int | None, list[str]]:
    lines = text.splitlines()
    start: int | None = None
    for i, line in enumerate(lines):
        if CLAIM_RE.match(line):
            start = i
            break
    if start is None:
        return None, []
    end = len(lines)
    for i in range(start + 1, len(lines)):
        if HEADING_RE.match(lines[i]):
            end = i
            break
    return start + 1, lines[start + 1 : end]


def claim_fenced_blocks(text: str) -> list[dict[str, Any]]:
    """Capture every fenced block in Claim, including legacy labels.

    A block is retained even when its contents are not recognizable CFEL.  The
    checker is evidence-oriented: an unrecognized clause is a review gap, not
    an invitation to silently drop source material.
    """

    lines = text.splitlines()
    claim_start, _ = claim_section(text)
    if claim_start is None:
        return []
    start = claim_start
    end = len(lines)
    for i in range(start, len(lines)):
        if HEADING_RE.match(lines[i]):
            end = i
            break
    blocks: list[dict[str, Any]] = []
    index = start
    while index < end:
        match = FENCE_RE.match(lines[index])
        if not match:
            index += 1
            continue
        fence = match.group("fence")
        info = match.group("info") or ""
        opening = index
        index += 1
        content: list[str] = []
        while index < end:
            close = FENCE_RE.match(lines[index])
            if close and close.group("fence")[0] == fence[0] and len(close.group("fence")) >= len(fence):
                break
            content.append(lines[index])
            index += 1
        closing = min(index, len(lines) - 1)
        raw = "\n".join(content)
        formal_like = bool(
            DOUBLE_RELATION_RE.search(raw)
            or RELATION_NAME_RE.search(raw)
            or re.search(r"(?:\+>|<\+|\|<|::|:=|==|>>|<<)", raw)
            or re.search(r"\[[^\]]+\]\s*\{[^}]*\}", raw)
            or re.search(r"\b[A-Za-z][A-Za-z0-9 _-]*[/.][A-Za-z]", raw)
        )
        label_is_cfel = info.lower().startswith("cfel")
        blocks.append(
            {
                "line_start": opening + 1,
                "line_end": closing + 1,
                "label": info,
                "label_is_cfel": label_is_cfel,
                "legacy_unlabelled": not label_is_cfel,
                "formal_like": formal_like,
                "recognition_status": "recognized_pattern" if formal_like else "unrecognized",
                "raw_sha256": sha256_bytes(raw.encode()),
                "text": raw,
            }
        )
        index += 1
    return blocks


def prose_from_claim(lines: Iterable[str]) -> str:
    result: list[str] = []
    in_fence = False
    fence_char = ""
    for line in lines:
        match = FENCE_RE.match(line)
        if match:
            if not in_fence:
                in_fence = True
                fence_char = match.group("fence")[0]
            elif match.group("fence")[0] == fence_char:
                in_fence = False
            continue
        if in_fence:
            continue
        if line.strip().startswith("###"):
            continue
        if line.strip():
            result.append(line.strip())
    return "\n".join(result).strip()


def relation_names_from_text(text: str) -> set[str]:
    return set(RELATION_NAME_RE.findall(text)) | set(DOUBLE_RELATION_RE.findall(text))


def relation_occurrences(text: str) -> list[dict[str, Any]]:
    occurrences: list[dict[str, Any]] = []
    for match in DOUBLE_RELATION_RE.finditer(text):
        token = match.group(1)
        occurrences.append(
            {
                "token": token,
                "line": line_number(text, match.start()),
                "syntax": "double_parenthesized",
                "raw": match.group(0),
            }
        )
    for match in RELATION_NAME_RE.finditer(text):
        token = match.group(1)
        occurrences.append(
            {
                "token": token,
                "line": line_number(text, match.start()),
                "syntax": "relation_address",
                "raw": match.group(0),
            }
        )
    return occurrences


def selected_nodes(inventory_path: Path, frontier_by_path: dict[str, dict[str, Any]]) -> dict[str, Any]:
    data = load_json(inventory_path)
    primary = list(data.get("primary_declarations", []))
    properties = list(data.get("property_declarations", []))
    records: list[dict[str, Any]] = []
    for kind, values in (("Primary Node", primary), ("Property", properties)):
        for item in values:
            path = item["path"]
            frontier = frontier_by_path.get(path)
            actual = REPO_ROOT / path
            record = {
                "kind": kind,
                "subject": item["subject"],
                "id": item["id"],
                "version": item["version"],
                "status": item["status"],
                "path": path,
                "sha256": sha256_path(actual) if actual.exists() else None,
                "frontier_sha256": frontier.get("sha256") if frontier else None,
                "frontier_version": frontier.get("version") if frontier else None,
                "frontier_status": frontier.get("status") if frontier else None,
                "in_frontier": frontier is not None,
                "frontier_pin_matches": bool(
                    frontier
                    and frontier.get("version") == item["version"]
                    and frontier.get("status") == item["status"]
                    and frontier.get("sha256") == (sha256_path(actual) if actual.exists() else None)
                ),
            }
            records.append(record)
    return {
        "inventory_path": rel_path(inventory_path),
        "inventory_sha256": sha256_path(inventory_path),
        "status": data.get("status"),
        "primary_count": len(primary),
        "property_count": len(properties),
        "expected_count": len(records),
        "records": records,
        "missing_from_frontier": [r["subject"] for r in records if not r["in_frontier"]],
        "pin_mismatches": [r["subject"] for r in records if not r["frontier_pin_matches"]],
    }


def retained_roots(records: list[dict[str, Any]]) -> dict[str, Any]:
    branches = {"CFEL": [], "Carrier": [], "Term": []}
    for record in records:
        subject = record["active_subject"]
        if subject in branches:
            branches[subject].append(source_pin(record) | {"active_subject": subject})
    return {
        "branches": branches,
        "expected_root_count": sum(len(values) for values in branches.values()),
        "missing_roots": [key for key, values in branches.items() if not values],
    }


def relation_candidates(records: list[dict[str, Any]]) -> dict[str, Any]:
    relation_manifest, source_support, derived_support = relation_support_manifests()
    support_by_id = {item.get("source_id"): item for item in source_support if item.get("source_id")}
    derived_by_id = {item.get("source_id"): item for item in derived_support if item.get("source_id")}
    inverse_pairs = confirmed_inverse_pairs(relation_manifest)
    candidates: list[dict[str, Any]] = []
    for record in records:
        if record["form"] != "Relation Definition":
            continue
        # The active Subject owns the candidate relation.  Names mentioned in
        # its Claim (for example an inverse or a pair) are tracked separately;
        # they do not silently become additional authored declarations.
        names = sorted(set(RELATION_NAME_RE.findall(record["active_subject"])))
        referenced_names = sorted(relation_names_from_text(record["active_subject"] + "\n" + record["text"]))
        name = names[0] if names else ""
        support = support_by_id.get(record.get("id"), {})
        derived = derived_by_id.get(record.get("id"), {})
        support_kind = support.get("derivation") or derived.get("derivation")
        relation_is_derived = support_kind == "Derived" or bool(
            re.search(r"\bDerivation\s*==\s*Derived\b", record["text"])
        )
        short_notation_present = any(
            re.search(rf"\(\(\s*{re.escape(candidate)}\s*\)\)\s*==\s*\S", record["text"])
            for candidate in names
        )
        notation_kind = support.get("notation_kind") or derived.get("notation_kind")
        notation_binding = support.get("notation_binding") or derived.get("notation_binding")
        short_notation_required = bool(
            notation_kind == "short notation alias" or notation_binding
        )
        inverse_required = name in inverse_pairs
        inverse_present = any(
            re.search(
                rf"\(\(\s*{re.escape(candidate)}\s*\)\)\s*\(\(\s*HAS_INVERSE\s*\)\)\s*\(\(\s*[A-Za-z_][A-Za-z0-9_]*\s*\)\)",
                record["text"],
            )
            or re.search(
                rf"\(\(\s*[A-Za-z_][A-Za-z0-9_]*\s*\)\)\s*\(\(\s*HAS_INVERSE\s*\)\)\s*\(\(\s*{re.escape(candidate)}\s*\)\)",
                record["text"],
            )
            for candidate in names
        )
        candidates.append(
            {
                **source_pin(record),
                "active_subject": record["active_subject"],
                "relation_names": names,
                "referenced_relation_names": referenced_names,
                "relation_name": name,
                "semantics_present": bool(section_text(record["text"], "Semantics")),
                "short_notation_present": short_notation_present,
                "short_notation_required": short_notation_required,
                "short_notation": support.get("notation") or derived.get("notation"),
                "notation_kind": notation_kind,
                "derivation_present": any(
                    re.search(
                        rf"\(\(\s*{re.escape(candidate)}\s*\)\)\s*>\|\s*Derivation\s*==\s*(Direct|Derived)",
                        record["text"],
                    )
                    for candidate in names
                ),
                "derivation_classification": support.get("derivation_classification")
                or derived.get("derivation_classification"),
                "relation_is_derived": relation_is_derived,
                "derived_relation_source": support.get("derived_from_relation")
                or derived.get("derived_from_relation"),
                "derived_relation_link_present": bool(
                    re.search(
                        rf"\(\(\s*{re.escape(name)}\s*\)\)\s*\(\(\s*IS_DERIVED_RELATION_OF\s*\)\)",
                        record["text"],
                    )
                ),
                "inverse_present": inverse_present,
                "inverse_required": inverse_required,
                "inverse_counterpart": inverse_pairs.get(name),
                "relation_candidate_kind": support.get("kind") or derived.get("kind") or "Current",
                "support_source": {
                    key: support.get(key)
                    for key in (
                        "source_id", "source_version", "source_path", "source_sha256",
                        "draft_id", "draft_path", "draft_sha256", "kind", "review",
                    )
                    if key in support
                },
                "support_derived": {
                    key: derived.get(key)
                    for key in (
                        "source_id", "source_version", "source_path", "source_sha256",
                        "draft_id", "draft_path", "draft_sha256", "derived_from_relation",
                        "derivation_link", "review",
                    )
                    if key in derived
                },
                "policy": {
                    "short_notation_is_not_invented": True,
                    "inverse_is_required_only_for_confirmed_pair": inverse_required,
                    "inverse_cardinality_is_not_inferred": True,
                    "formal_derivation_relation": "IS_DERIVED_RELATION_OF",
                    "unrecognized_clauses_are_retained": True,
                },
            }
        )
    relation_names = sorted({name for item in candidates for name in item["relation_names"]})
    referenced_relation_names = sorted({name for item in candidates for name in item["referenced_relation_names"]})
    return {
        "candidate_count": len(candidates),
        "named_candidate_count": sum(bool(item["relation_names"]) for item in candidates),
        "records": candidates,
        "relation_names": relation_names,
        "referenced_relation_names": referenced_relation_names,
        "template_requirements": {
            "semantics": "Semantics section for each named Relation",
            "short_notation": "((REL)) == shortnotation only when an existing alias is admitted; otherwise use the full Relation name",
            "derivation": "((REL)) >| Derivation == Direct|Derived",
            "derived_relation": "((DERIVED_REL)) ((IS_DERIVED_RELATION_OF)) ((SOURCE_REL)) for each Derived Relation",
            "inverse": "((REL)) ((HAS_INVERSE)) ((COUNTERPART)) only for a confirmed endpoint-reversing pair",
            "direct_and_derived_permissions_are_independent": True,
            "inverse_bounds_are_inferred": False,
            "inverse_permission_is_not_automatic": True,
            "unrecognized_clauses_are_retained": True,
        },
        "missing_template_counts": {
            "semantics": sum(not item["semantics_present"] for item in candidates if item["relation_names"]),
            "short_notation": sum(
                item["short_notation_required"] and not item["short_notation_present"]
                for item in candidates
                if item["relation_names"]
            ),
            "derivation": sum(
                not item["derivation_present"] for item in candidates if item["relation_names"]
            ),
            "derived_relation": sum(
                item["relation_is_derived"] and not item["derived_relation_link_present"]
                for item in candidates
                if item["relation_names"]
            ),
            "inverse": sum(
                item["inverse_required"] and not item["inverse_present"]
                for item in candidates
                if item["relation_names"]
            ),
        },
        "confirmed_inverse_pairs": inverse_pairs,
        "public_path_aliases": PUBLIC_PATH_ALIASES,
        "public_path_alias_policy": "Existing parser mappings are evidence only; derived same-glyph mappings are flagged for canonical review.",
    }


def section_text(text: str, title: str) -> str:
    lines = text.splitlines()
    target = re.compile(rf"^##\s+{re.escape(title)}\s*$", re.IGNORECASE)
    start = next((i for i, line in enumerate(lines) if target.match(line)), None)
    if start is None:
        return ""
    end = next((i for i in range(start + 1, len(lines)) if HEADING_RE.match(lines[i])), len(lines))
    return "\n".join(lines[start + 1 : end]).strip()


def claim_evidence(records: list[dict[str, Any]]) -> dict[str, Any]:
    blocks: list[dict[str, Any]] = []
    claim_blocks: list[dict[str, Any]] = []
    legacy_claim_blocks: list[dict[str, Any]] = []
    unrecognized_claim_blocks: list[dict[str, Any]] = []
    prose: list[dict[str, Any]] = []
    formal_only = 0
    no_claim = 0
    for record in records:
        claim_line, claim_lines = claim_section(record["text"])
        source = source_pin(record)
        if claim_line is None:
            no_claim += 1
        raw_blocks = labelled_cfel_blocks(record["text"])
        for block in raw_blocks:
            blocks.append(source | {"active_subject": record["active_subject"], **block})
        for block in claim_fenced_blocks(record["text"]):
            enriched = source | {"active_subject": record["active_subject"], **block}
            claim_blocks.append(enriched)
            if block["legacy_unlabelled"]:
                legacy_claim_blocks.append(enriched)
            if block["recognition_status"] == "unrecognized":
                unrecognized_claim_blocks.append(enriched)
        claim_prose = prose_from_claim(claim_lines)
        if claim_prose:
            prose.append(
                source
                | {
                    "active_subject": record["active_subject"],
                    "claim_line": claim_line,
                    "has_cfel_block": bool(raw_blocks),
                    "has_claim_fenced_block": bool(claim_fenced_blocks(record["text"])),
                    "claim_sha256": sha256_bytes(claim_prose.encode()),
                    "claim_length": len(claim_prose),
                    "claim_preview": claim_prose[:1000],
                }
            )
        elif claim_fenced_blocks(record["text"]):
            formal_only += 1
    return {
        "raw_cfel_block_count": len(blocks),
        "raw_cfel_source_count": len({item["path"] for item in blocks}),
        "raw_cfel_blocks": blocks,
        "claim_fenced_block_count": len(claim_blocks),
        "claim_fenced_source_count": len({item["path"] for item in claim_blocks}),
        "claim_fenced_blocks": claim_blocks,
        "legacy_unlabelled_formal_claim_block_count": len(legacy_claim_blocks),
        "legacy_unlabelled_formal_claim_blocks": legacy_claim_blocks,
        "unrecognized_claim_block_count": len(unrecognized_claim_blocks),
        "unrecognized_claim_blocks": unrecognized_claim_blocks,
        "prose_claim_count": len(prose),
        "prose_claims": prose,
        "formal_only_claim_count": formal_only,
        "sources_without_claim_heading": no_claim,
    }


def relation_usage(records: list[dict[str, Any]], defined_names: set[str]) -> dict[str, Any]:
    occurrences: list[dict[str, Any]] = []
    for record in records:
        for occurrence in relation_occurrences(record["text"]):
            token = occurrence["token"]
            if token in defined_names:
                classification = "modeled_relation"
            elif token in CFEL_PREDICATES:
                classification = "predicate_or_function"
            elif token in CFEL_RELATION_PLACEHOLDERS:
                classification = "relation_placeholder"
            else:
                classification = "unknown_relation_candidate"
            occurrences.append(source_pin(record) | occurrence | {"classification": classification})
    modeled = sorted({item["token"] for item in occurrences if item["classification"] == "modeled_relation"})
    unknown = sorted({item["token"] for item in occurrences if item["classification"] == "unknown_relation_candidate"})
    predicates = sorted({item["token"] for item in occurrences if item["classification"] == "predicate_or_function"})
    placeholders = sorted({item["token"] for item in occurrences if item["classification"] == "relation_placeholder"})
    literal_markers: list[dict[str, Any]] = []
    wildcard_markers: list[dict[str, Any]] = []
    for record in records:
        for i, line in enumerate(record["text"].splitlines(), start=1):
            for match in re.finditer(r"(?<![=!<>]):(?!=)|(?<![=!<>])=(?!=)", line):
                literal_markers.append(source_pin(record) | {"line": i, "marker": match.group(0)})
            for match in re.finditer(r"\*{1,2}", line):
                wildcard_markers.append(source_pin(record) | {"line": i, "marker": match.group(0)})
    return {
        "occurrence_count": len(occurrences),
        "occurrences": occurrences,
        "modeled_relation_names_used": modeled,
        "unknown_relation_candidates": unknown,
        "predicate_or_function_tokens": predicates,
        "relation_placeholder_tokens": placeholders,
        "literal_binding_marker_count": len(literal_markers),
        "literal_binding_markers": literal_markers[:100],
        "wildcard_marker_count": len(wildcard_markers),
        "wildcard_markers": wildcard_markers[:100],
        "classification_policy": {
            "modeled_relation": "Relation Definition candidate name only",
            "predicate_or_function": "reserved CFEL predicate/function token",
            "relation_placeholder": "generic relation placeholder, not an authored Relation",
            "unknown_relation_candidate": "double-parenthesized or Relation// token without a current definition",
            "literal_binding": "colon/equality marker outside relation token; not a Relation",
            "wildcard": "* or ** selector; not a Relation",
        },
    }


def draft_contract_evidence(candidate: dict[str, Any], relation_name: str) -> dict[str, Any]:
    draft_path_value = candidate.get("draft_path")
    if not isinstance(draft_path_value, str) or not draft_path_value:
        return {
            "draft_exists": False,
            "draft_path": draft_path_value,
            "draft_sha256_actual": None,
            "draft_sha256_matches_packet": None,
            "draft_active_subject": None,
            "draft_formal_claim_block_count": 0,
            "draft_legacy_unlabelled_formal_claim_block_count": 0,
            "draft_unrecognized_claim_block_count": 0,
            "draft_semantics_present": False,
            "draft_derivation_classification_present": False,
            "draft_derived_relation_link_present": False,
            "draft_inverse_binding_present": False,
            "draft_short_notation_binding_present": False,
        }
    path = REPO_ROOT / draft_path_value
    if not path.exists():
        return {
            "draft_exists": False,
            "draft_path": draft_path_value,
            "draft_sha256_actual": None,
            "draft_sha256_matches_packet": None,
            "draft_active_subject": None,
            "draft_formal_claim_block_count": 0,
            "draft_legacy_unlabelled_formal_claim_block_count": 0,
            "draft_unrecognized_claim_block_count": 0,
            "draft_semantics_present": False,
            "draft_derivation_classification_present": False,
            "draft_derived_relation_link_present": False,
            "draft_inverse_binding_present": False,
            "draft_short_notation_binding_present": False,
        }
    text = path.read_text(encoding="utf-8")
    meta = frontmatter(text)
    blocks = claim_fenced_blocks(text)
    derivation = bool(
        re.search(
            rf"\(\(\s*{re.escape(relation_name)}\s*\)\)\s*>\|\s*Derivation\s*==\s*(Direct|Derived)",
            text,
        )
    )
    derived_link = bool(
        re.search(
            rf"\(\(\s*{re.escape(relation_name)}\s*\)\)\s*\(\(\s*IS_DERIVED_RELATION_OF\s*\)\)",
            text,
        )
    )
    inverse = bool(
        re.search(
            rf"\(\(\s*{re.escape(relation_name)}\s*\)\)\s*\(\(\s*HAS_INVERSE\s*\)\)",
            text,
        )
        or re.search(
            rf"\(\(\s*[A-Za-z_][A-Za-z0-9_]*\s*\)\)\s*\(\(\s*HAS_INVERSE\s*\)\)\s*\(\(\s*{re.escape(relation_name)}\s*\)\)",
            text,
        )
    )
    notation = bool(
        re.search(rf"\(\(\s*{re.escape(relation_name)}\s*\)\)\s*==\s*\S", text)
    )
    packet_sha = candidate.get("draft_sha256")
    actual_sha = sha256_path(path)
    return {
        "draft_exists": True,
        "draft_path": draft_path_value,
        "draft_sha256_actual": actual_sha,
        "draft_sha256_packet": packet_sha,
        "draft_sha256_matches_packet": bool(packet_sha and packet_sha == actual_sha),
        "draft_active_subject": active_subject(meta),
        "draft_formal_claim_block_count": sum(block["formal_like"] for block in blocks),
        "draft_legacy_unlabelled_formal_claim_block_count": sum(
            block["legacy_unlabelled"] for block in blocks
        ),
        "draft_unrecognized_claim_block_count": sum(
            block["recognition_status"] == "unrecognized" for block in blocks
        ),
        "draft_semantics_present": bool(section_text(text, "Semantics")),
        "draft_derivation_classification_present": derivation,
        "draft_derived_relation_link_present": derived_link,
        "draft_inverse_binding_present": inverse,
        "draft_short_notation_binding_present": notation,
    }


def candidate_clause_coverage(
    records: list[dict[str, Any]],
    relations: dict[str, Any],
    claims: dict[str, Any],
) -> dict[str, Any]:
    """Build a source-to-draft matrix without interpreting CFEL semantics."""

    current_by_id = {record.get("id"): record for record in records}
    relation_manifest, source_support, derived_support = relation_support_manifests()
    source_support_by_id = {item.get("source_id"): item for item in source_support}
    claim_by_path: dict[str, dict[str, int]] = {}
    for block in claims["claim_fenced_blocks"]:
        counts = claim_by_path.setdefault(
            block["path"],
            {"all": 0, "legacy_formal": 0, "unrecognized": 0},
        )
        counts["all"] += 1
        counts["legacy_formal"] += int(block["legacy_unlabelled"])
        counts["unrecognized"] += int(block["recognition_status"] == "unrecognized")

    rows: list[dict[str, Any]] = []

    def append_relation_row(
        candidate: dict[str, Any],
        *,
        candidate_class: str,
        source_manifest: dict[str, Any] | None = None,
        derived_manifest: dict[str, Any] | None = None,
    ) -> None:
        if source_manifest is None and derived_manifest is None:
            source_manifest = source_support_by_id.get(candidate.get("id"))
        relation_name = candidate.get("relation_name") or (
            (source_manifest or {}).get("relation")
            or (derived_manifest or {}).get("relation")
            or ""
        )
        support = source_manifest or derived_manifest or {}
        source_record = current_by_id.get(support.get("source_id"))
        source_path = source_record.get("path") if source_record else candidate.get("path")
        source_claim = claim_by_path.get(source_path or "", {"all": 0, "legacy_formal": 0, "unrecognized": 0})
        draft = draft_contract_evidence(support, relation_name)
        derived_flag = candidate_class == "new_derived" or support.get("derivation") == "Derived"
        inverse_required = relation_name in relations.get("confirmed_inverse_pairs", {})
        gaps: list[str] = []
        if not candidate.get("semantics_present", False) and not support.get("semantics_present", False):
            gaps.append("current_semantics")
        if not draft["draft_exists"]:
            gaps.append("draft_missing")
        if not draft["draft_semantics_present"]:
            gaps.append("draft_semantics")
        if not draft["draft_derivation_classification_present"]:
            gaps.append("draft_derivation_classification")
        if derived_flag and not draft["draft_derived_relation_link_present"]:
            gaps.append("draft_is_derived_relation_of")
        if inverse_required and not draft["draft_inverse_binding_present"]:
            gaps.append("draft_confirmed_inverse")
        notation_required = bool(
            support.get("notation_kind") == "short notation alias" or support.get("notation_binding")
        )
        if notation_required and not draft["draft_short_notation_binding_present"]:
            gaps.append("draft_existing_notation_binding")
        rows.append(
            {
                "candidate_class": candidate_class,
                "relation": relation_name,
                "relation_kind": support.get("kind") or candidate.get("relation_candidate_kind"),
                "source": source_pin(source_record) if source_record else {
                    "id": support.get("source_id"),
                    "version": support.get("source_version"),
                    "status": None,
                    "path": support.get("source_path"),
                    "sha256": support.get("source_sha256"),
                },
                "source_clause_present": bool(source_record),
                "source_claim_fenced_block_count": source_claim["all"],
                "source_legacy_unlabelled_formal_claim_block_count": source_claim["legacy_formal"],
                "source_unrecognized_claim_block_count": source_claim["unrecognized"],
                "source_formal_claim_present": bool(source_claim["all"]),
                "source_semantics_present": bool(
                    (source_manifest or {}).get("semantics_present")
                    or (derived_manifest or {}).get("semantics_present")
                    or candidate.get("semantics_present")
                ),
                "source_sha256_expected": support.get("source_sha256")
                or (source_record or {}).get("sha256"),
                "draft": {
                    "id": support.get("draft_id"),
                    **draft,
                },
                "existing_short_notation": support.get("notation")
                if notation_required
                else None,
                "short_notation_required": notation_required,
                "confirmed_inverse_required": inverse_required,
                "confirmed_inverse": relations.get("confirmed_inverse_pairs", {}).get(relation_name),
                "derived_relation": derived_flag,
                "derived_from_relation": support.get("derived_from_relation"),
                "unrecognized_clause_policy": "retain and review",
                "gaps": gaps,
                "status": "gap" if gaps else "covered",
            }
        )

    for candidate in relations["records"]:
        append_relation_row(candidate, candidate_class="current_relation")

    relation_by_id = {item.get("id"): item for item in relations["records"]}
    for item in derived_support:
        owner = relation_by_id.get(item.get("source_id"), {})
        owner = dict(owner)
        owner["relation_name"] = item.get("relation")
        owner["relation_candidate_kind"] = "derived"
        owner["semantics_present"] = bool(item.get("semantics_present"))
        append_relation_row(owner, candidate_class="new_derived", derived_manifest=item)

    legacy_manifest = load_json(LEGACY_CFEL_MANIFEST) if LEGACY_CFEL_MANIFEST.exists() else {}
    legacy_rows: list[dict[str, Any]] = []
    if isinstance(legacy_manifest, dict) and isinstance(legacy_manifest.get("candidates"), list):
        for item in legacy_manifest["candidates"]:
            source_record = current_by_id.get(item.get("id"))
            source_path = source_record.get("path") if source_record else None
            source_claim = claim_by_path.get(source_path or "", {"all": 0, "legacy_formal": 0, "unrecognized": 0})
            draft_path = item.get("candidate_path")
            draft_text = ""
            draft_exists = False
            draft_actual_sha = None
            draft_claim_blocks: list[dict[str, Any]] = []
            if isinstance(draft_path, str):
                draft_file = REPO_ROOT / draft_path
                if not draft_file.exists():
                    draft_file = ANALYSIS_ROOT / "legacy-cfel" / draft_path
                draft_exists = draft_file.exists()
                if draft_exists:
                    draft_text = draft_file.read_text(encoding="utf-8")
                    draft_actual_sha = sha256_path(draft_file)
                    draft_claim_blocks = claim_fenced_blocks(draft_text)
            gaps = []
            if not draft_exists:
                gaps.append("draft_missing")
            if draft_exists and not section_text(draft_text, "Semantics"):
                gaps.append("draft_semantics")
            legacy_rows.append(
                {
                    "candidate_class": "legacy_cfel",
                    "source": source_pin(source_record)
                    if source_record
                    else {
                        "id": item.get("id"),
                        "version": item.get("current_version"),
                        "status": "Current",
                        "path": None,
                        "sha256": item.get("source_sha256"),
                    },
                    "relation": None,
                    "subject_before": item.get("subject_before"),
                    "subject_after": item.get("subject_after"),
                    "source_clause_present": bool(source_record),
                    "source_claim_fenced_block_count": source_claim["all"],
                    "source_legacy_unlabelled_formal_claim_block_count": source_claim["legacy_formal"],
                    "source_unrecognized_claim_block_count": source_claim["unrecognized"],
                    "draft": {
                        "id": item.get("candidate"),
                        "path": draft_path,
                        "path_actual": rel_path(draft_file) if draft_exists else None,
                        "exists": draft_exists,
                        "sha256_actual": draft_actual_sha,
                        "sha256_expected": None,
                        "formal_claim_block_count": sum(block["formal_like"] for block in draft_claim_blocks),
                        "legacy_unlabelled_formal_claim_block_count": sum(
                            block["legacy_unlabelled"] for block in draft_claim_blocks
                        ),
                        "unrecognized_claim_block_count": sum(
                            block["recognition_status"] == "unrecognized" for block in draft_claim_blocks
                        ),
                    },
                    "gaps": gaps,
                    "status": "gap" if gaps else "covered",
                    "unrecognized_clause_policy": "retain and review",
                }
            )

    rows.extend(legacy_rows)
    return {
        "schema_version": 1,
        "source_candidate_count": len(source_support),
        "derived_candidate_count": len(derived_support),
        "current_relation_candidate_count": len(relations["records"]),
        "legacy_cfel_candidate_count": len(legacy_rows),
        "row_count": len(rows),
        "rows": rows,
        "summary": {
            "covered": sum(row["status"] == "covered" for row in rows),
            "gaps": sum(row["status"] == "gap" for row in rows),
            "source_legacy_unlabelled_formal_claim_blocks": sum(
                row.get("source_legacy_unlabelled_formal_claim_block_count", 0) for row in rows
            ),
            "source_unrecognized_claim_blocks": sum(
                row.get("source_unrecognized_claim_block_count", 0) for row in rows
            ),
        },
        "policy": {
            "relation_declarations": "Relation/Declaration candidates are source-backed; derived declarations retain explicit source and derivation-link evidence.",
            "short_notation": "Only an existing admitted alias is checked; no symbol is invented for a full named Relation.",
            "inverse": "HAS_INVERSE is checked only for confirmed endpoint-reversing pairs; inverse permission/cardinality is not inferred.",
            "derived": "Every Derived candidate requires IS_DERIVED_RELATION_OF in its formal declaration.",
            "legacy_formal_claims": "Unlabelled and unrecognized Claim fences remain matrix rows and gaps.",
        },
    }


def diagnostics_evidence() -> dict[str, Any]:
    expected = {"total": 31, "cfel": 16, "legacy_entity": 14, "event_record": 1}
    current_count = None
    if DIAGNOSTICS_DEFAULT.exists():
        data = load_json(DIAGNOSTICS_DEFAULT)
        current_count = len(data.get("diagnostics", []))
    legacy_path = ANALYSIS_ROOT / "legacy-entities/legacy-entities-manifest.json"
    legacy = load_json(legacy_path) if legacy_path.exists() else None
    observed = {
        "cfel": None,
        "legacy_entity": (legacy or {}).get("counts", {}).get("diagnostic_sources"),
        "event_record": 1 if (legacy or {}).get("event_record") else None,
    }
    cfel_candidates: list[str] = []
    # The retained CFEL packet publishes candidate rows rather than a
    # ``counts`` object.  Count its candidates directly and keep the manifest
    # pin in the evidence.
    if LEGACY_CFEL_MANIFEST.exists():
        try:
            manifest = load_json(LEGACY_CFEL_MANIFEST)
            candidates = manifest.get("candidates") if isinstance(manifest, dict) else None
            if isinstance(candidates, list):
                observed["cfel"] = len(candidates)
                cfel_candidates.append(rel_path(LEGACY_CFEL_MANIFEST))
        except (OSError, json.JSONDecodeError):
            pass
    for path in sorted((ANALYSIS_ROOT / "legacy-cfel").glob("*.json")) if (ANALYSIS_ROOT / "legacy-cfel").exists() else []:
        if path == LEGACY_CFEL_MANIFEST:
            continue
        try:
            value = load_json(path)
        except (OSError, json.JSONDecodeError):
            continue
        counts = value.get("counts", {}) if isinstance(value, dict) else {}
        for key in ("diagnostic_sources", "diagnostics", "count", "rows"):
            if key in counts and isinstance(counts[key], int):
                observed["cfel"] = counts[key]
                cfel_candidates.append(rel_path(path))
                break
    available = all(value is not None for value in observed.values())
    total = sum(value for value in observed.values() if value is not None)
    return {
        "expected": expected,
        "observed": observed,
        "observed_total": total,
        "status": "verified" if available and observed == {"cfel": 16, "legacy_entity": 14, "event_record": 1} else "pending_cfel_manifest",
        "current_graph_diagnostics_count": current_count,
        "source": {
            "legacy_entities_manifest": rel_path(legacy_path) if legacy_path.exists() else None,
            "cfel_manifest_candidates": cfel_candidates,
        },
        "note": "The expected 31 tree issues are separate from the current graph diagnostic count.",
    }


def graph_items(data: Any, keys: tuple[str, ...]) -> list[Any]:
    if not isinstance(data, dict):
        return []
    for key in keys:
        value = data.get(key)
        if isinstance(value, list):
            return value
        if isinstance(value, dict):
            return list(value.values())
    return []


def graph_subject(item: Any) -> str:
    if isinstance(item, str):
        return item
    if not isinstance(item, dict):
        return ""
    for key in ("subject", "entity", "node", "name", "path"):
        value = item.get(key)
        if isinstance(value, str):
            return value
    return ""


def flatten_strings(value: Any) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        result: list[str] = []
        for item in value:
            result.extend(flatten_strings(item))
        return result
    if isinstance(value, dict):
        result = []
        for item in value.values():
            result.extend(flatten_strings(item))
        return result
    return []


def graph_source_strings(item: Any) -> list[str]:
    if not isinstance(item, dict):
        return []
    values: list[str] = []
    for key in (
        "source",
        "sources",
        "source_clause",
        "source_clauses",
        "evidence",
        "provenance",
        "source_id",
        "source_ids",
        "source_path",
        "source_paths",
    ):
        if key in item:
            values.extend(flatten_strings(item[key]))
    return values


def source_clause_matches(item: Any, expected: dict[str, Any]) -> bool:
    haystack = "\n".join(graph_source_strings(item))
    if not haystack:
        return False
    return any(
        needle and needle in haystack
        for needle in (source_key(expected), expected.get("id", ""), expected.get("path", ""), expected.get("sha256", ""))
    )


def graph_relation_names(item: Any) -> set[str]:
    values: list[str] = []
    if isinstance(item, dict):
        for key in ("subject", "name", "relation", "relation_name", "counterpart", "inverse"):
            if key in item:
                values.extend(flatten_strings(item[key]))
    else:
        values.extend(flatten_strings(item))
    return set().union(*(relation_names_from_text(value) for value in values))


def graph_relation_field_names(item: Any) -> set[str]:
    """Read explicit relation-name fields without treating arbitrary strings as Relations."""

    if not isinstance(item, dict):
        return set()
    values: list[str] = []
    for key in (
        "relation",
        "relation_name",
        "relation_names",
        "counterpart",
        "inverse",
        "source_relation",
        "derived_from",
        "is_derived_relation_of",
    ):
        if key in item:
            values.extend(flatten_strings(item[key]))
    result: set[str] = set()
    for value in values:
        result.update(relation_names_from_text(value))
        if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", value) and value.upper() not in CFEL_PREDICATES:
            result.add(value)
    return result


def graph_has_named_link(item: Any, relation_name: str, link_name: str) -> bool:
    if not isinstance(item, dict):
        return False
    haystack = "\n".join(flatten_strings(item))
    return bool(
        re.search(rf"\b{re.escape(link_name)}\b", haystack)
        and re.search(rf"\b{re.escape(relation_name)}\b", haystack)
    )


def graph_field_present(item: Any, keys: tuple[str, ...]) -> bool:
    if not isinstance(item, dict):
        return False
    return any(key in item and bool(item[key]) for key in keys)


def check_graph(graph_path: Path, nodes: dict[str, Any], roots: dict[str, Any], relations: dict[str, Any]) -> dict[str, Any]:
    data = load_json(graph_path)
    entities = graph_items(data, ("entities", "nodes", "contracts", "entity_contracts"))
    relation_items = graph_items(data, ("relation_declarations", "relations", "relation_contracts"))
    by_subject: dict[str, list[Any]] = {}
    for item in entities:
        by_subject.setdefault(graph_subject(item), []).append(item)
    expected_entities = list(nodes["records"])
    for branch_records in roots["branches"].values():
        expected_entities.extend(branch_records)
    missing_entities = []
    missing_sources = []
    for expected in expected_entities:
        subject = expected.get("subject") or expected.get("active_subject")
        candidates = by_subject.get(subject, [])
        if not candidates:
            missing_entities.append(subject)
            continue
        if not any(source_clause_matches(item, expected) for item in candidates):
            missing_sources.append(subject)
    missing_relations = []
    relation_template_errors = []
    known_relation_names = set(relations["relation_names"]) | set(relations["referenced_relation_names"])
    confirmed_inverse = relations.get("confirmed_inverse_pairs", {})
    known_relation_names.update(confirmed_inverse.keys())
    _, _, derived_candidates = relation_support_manifests()
    for item in derived_candidates:
        for key in ("relation", "inverse", "derived_from_relation"):
            value = item.get(key)
            if isinstance(value, str):
                known_relation_names.add(value)
    unrecognized_relation_clauses: list[dict[str, Any]] = []
    for index, item in enumerate(relation_items):
        names = graph_relation_field_names(item)
        unknown = sorted(name for name in names if name not in known_relation_names)
        if unknown:
            unrecognized_relation_clauses.append(
                {
                    "index": index,
                    "names": unknown,
                    "item": item,
                    "reason": "Graph relation clause has no source-backed or candidate Relation name; retained for review.",
                }
            )
    for expected in relations["records"]:
        names = set(expected["relation_names"])
        matching = [item for item in relation_items if source_clause_matches(item, expected)]
        if not matching:
            matching = [item for item in relation_items if names.intersection(graph_relation_names(item))]
        if not matching:
            matching = [item for item in entities if names.intersection(graph_relation_names(item))]
        if not matching or not any(source_clause_matches(item, expected) for item in matching):
            missing_relations.append(source_key(expected))
            continue
        candidate = next((item for item in matching if source_clause_matches(item, expected)), matching[0])
        missing_fields = []
        if not graph_field_present(candidate, ("semantics", "meaning", "semantics_text")):
            missing_fields.append("semantics")
        if expected["short_notation_required"] and not graph_field_present(candidate, ("short_notation", "notation")):
            missing_fields.append("short_notation")
        if not graph_field_present(candidate, ("derivation", "derivation_classification")):
            missing_fields.append("derivation")
        if expected["relation_is_derived"] and not (
            graph_field_present(candidate, ("is_derived_relation_of", "derived_from", "derivation_link"))
            or graph_has_named_link(candidate, expected["relation_name"], "IS_DERIVED_RELATION_OF")
        ):
            missing_fields.append("is_derived_relation_of")
        if expected["inverse_required"] and not graph_field_present(candidate, ("inverse", "has_inverse", "counterpart")):
            missing_fields.append("inverse")
        direct_present = graph_field_present(candidate, ("direct", "direct_permissions", "direct_relation"))
        derived_present = graph_field_present(candidate, ("derived", "derived_permissions", "derived_relation"))
        if direct_present != derived_present:
            missing_fields.append("independent_direct_and_derived_permissions")
        if missing_fields:
            relation_template_errors.append({"source": source_key(expected), "missing": missing_fields})
    errors = []
    errors.extend({"kind": "missing_entity", "subject": value} for value in missing_entities)
    errors.extend({"kind": "missing_entity_source_clause", "subject": value} for value in missing_sources)
    errors.extend({"kind": "missing_relation_declaration", "source": value} for value in missing_relations)
    errors.extend({"kind": "relation_template_incomplete", **value} for value in relation_template_errors)
    errors.extend(
        {"kind": "unrecognized_relation_clause", **value}
        for value in unrecognized_relation_clauses
    )
    return {
        "graph_path": rel_path(graph_path),
        "entity_item_count": len(entities),
        "relation_item_count": len(relation_items),
        "expected_entity_count": len(expected_entities),
        "expected_relation_candidate_count": relations["candidate_count"],
        "relation_template_errors": relation_template_errors,
        "unrecognized_relation_clauses": unrecognized_relation_clauses,
        "errors": errors,
        "status": "pass" if not errors else "fail",
        "policy": {
            "no_inverse_permission_or_cardinality_inferred": True,
            "short_notation_optional_without_existing_alias": True,
            "derived_link": "IS_DERIVED_RELATION_OF",
            "inverse_permission": "HAS_INVERSE only for confirmed endpoint-reversing pairs",
            "unrecognized_clauses_retained": True,
        },
    }


def build_baseline(frontier_path: Path, inventory_path: Path, graph_path: Path | None) -> dict[str, Any]:
    frontier, rows = frontier_rows(frontier_path)
    frontier_by_path = {row["destination_path"]: row for row in rows}
    records: list[dict[str, Any]] = []
    for row in rows:
        path = REPO_ROOT / row["destination_path"]
        if path.exists():
            records.append(source_record(row, path))
    source_mismatches = [source_pin(record) for record in records if not record["sha256_matches_frontier"]]
    nodes = selected_nodes(inventory_path, frontier_by_path)
    roots = retained_roots(records)
    relations = relation_candidates(records)
    claims = claim_evidence(records)
    usage = relation_usage(records, set(relations["relation_names"]))
    clause_matrix = candidate_clause_coverage(records, relations, claims)
    result: dict[str, Any] = {
        "schema_version": 1,
        "status": "baseline_evidence",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "frontier": {
            "path": rel_path(frontier_path),
            "sha256": sha256_path(frontier_path),
            "source_count_declared": frontier.get("source_count"),
            "source_count_loaded": len(records),
            "status": frontier.get("status"),
        },
        "source_integrity": {
            "checked": len(records),
            "sha256_mismatches": source_mismatches,
            "status": "pass" if not source_mismatches and len(records) == frontier.get("source_count") else "fail",
        },
        "node_declarations": nodes,
        "retained_non_node_roots": roots,
        "relation_definition_candidates": relations,
        "claim_evidence": claims,
        "relation_usage": usage,
        "diagnostics": diagnostics_evidence(),
        "policy": {
            "source_pins": "Every expected record carries ID, Version, path and SHA-256.",
            "relation_definition_template": "Semantics; ((REL)) >| Derivation == Direct|Derived; existing short notation only when admitted; ((DERIVED_REL)) ((IS_DERIVED_RELATION_OF)) ((SOURCE_REL)) for Derived Relations; ((REL)) ((HAS_INVERSE)) ((COUNTERPART)) only for confirmed endpoint-reversing pairs.",
            "relation_permission": "Direct and derived permissions are checked independently.",
            "inverse_bounds": "Never inferred; inverse permission is not automatic.",
            "graph_relation_category": "Graph Relations and other CFEL operators are distinct.",
            "public_path_aliases": PUBLIC_PATH_ALIASES,
            "public_path_alias_policy": "Existing parser mappings are / -> NARROWER_THAN, // -> INSTANCE_OF and . -> IS_PROPERTY_OF; traversal can use the opposite authored edge. Candidate canonical mapping changes remain review items.",
            "legacy_formal_claims": "Every fenced Claim block, including unlabelled and unrecognized blocks, remains evidence.",
            "scope": "Coverage only; no general CFEL semantic validation.",
        },
    }
    result["candidate_clause_coverage"] = clause_matrix
    if graph_path:
        result["graph_check"] = check_graph(graph_path, nodes, roots, relations)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--frontier", type=Path, default=FRONTIER_DEFAULT)
    parser.add_argument("--inventory", type=Path, default=INVENTORY_DEFAULT)
    parser.add_argument("--graph", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--strict-diagnostics", action="store_true")
    args = parser.parse_args()
    result = build_baseline(args.frontier, args.inventory, args.graph)
    if args.strict_diagnostics and result["diagnostics"]["status"] != "verified":
        print(json.dumps(result["diagnostics"], indent=2), file=sys.stderr)
        return 2
    if args.graph and result.get("graph_check", {}).get("status") == "fail":
        if args.output:
            args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(result["graph_check"], indent=2), file=sys.stderr)
        return 1
    payload = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload, encoding="utf-8")
        matrix_path = args.output.parent / "candidate-clause-matrix.json"
        matrix_path.write_text(
            json.dumps(result["candidate_clause_coverage"], indent=2) + "\n",
            encoding="utf-8",
        )
    else:
        print(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
