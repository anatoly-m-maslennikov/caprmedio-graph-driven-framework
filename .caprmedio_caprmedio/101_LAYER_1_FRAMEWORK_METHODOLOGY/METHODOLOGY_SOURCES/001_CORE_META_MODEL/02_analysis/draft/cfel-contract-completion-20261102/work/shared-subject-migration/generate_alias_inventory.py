#!/usr/bin/env python3
"""Build a read-only inventory of source-backed Subject address aliases.

This report never edits Current or Draft source carriers.  It groups the
contract-graph baseline's unbound active Subjects by exact source text and
tests only aliases supported by the recorded migration packets.
"""

from __future__ import annotations

import collections
import hashlib
import json
import re
from pathlib import Path
from typing import Any


def find_repo() -> Path:
    for candidate in (Path.cwd(), *Path(__file__).resolve().parents):
        if (candidate / ".caprmedio_caprmedio").is_dir():
            return candidate
    raise RuntimeError("repository root not found")


REPO = find_repo()
ANALYSIS = (
    REPO
    / ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/02_analysis/draft/cfel-contract-completion-20261102"
)
MIGRATION = ANALYSIS.parent / "node-declaration-20261031/migration-20261101"
OUT = ANALYSIS / "work/shared-subject-migration"


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    return path.relative_to(REPO).as_posix()


def compact(value: str) -> str:
    """Normalize only operator-adjacent whitespace for address comparison."""

    value = re.sub(r"\s*:=\s*", ":=", value)
    value = re.sub(r"\s*:\s*", ":", value)
    return value.strip()


def id_sort(value: str) -> tuple[str, int, str]:
    match = re.match(r"^([A-Za-z]+)-?(\d+)$", value)
    if match:
        return match.group(1), int(match.group(2)), value
    return value, -1, value


def source_ids(rows: list[dict[str, Any]]) -> list[str]:
    return sorted({row["source"]["atom_id"] for row in rows}, key=id_sort)


def parse_ok(value: str, parser: Any) -> bool:
    try:
        parser(value, subject_profile="approved")
    except Exception:
        return False
    return True


def baseline_targets(baseline: dict[str, Any]) -> set[str]:
    targets: set[str] = set()
    for key in ("entities", "components", "relations"):
        targets.update(compact(item["target"]) for item in baseline[key])
    return targets


def owned_lane_ids() -> dict[str, set[str]]:
    result: dict[str, set[str]] = {
        "legacy-entities": set(),
        "relations": set(),
        "cfel-description": set(),
    }

    legacy_entities = load(ANALYSIS / "legacy-entities/legacy-entities-manifest.json")
    result["legacy-entities"].update(row["id"] for row in legacy_entities.get("rows", []))

    relation_manifest = load(ANALYSIS / "relations/coverage-manifest.json")
    for key in (
        "source_backed_declarations",
        "new_derived_declarations",
        "superseded_legacy_sources_retirement_candidates",
        "operator_reclassification_held",
    ):
        for row in relation_manifest.get(key, []):
            source_id = row.get("source_id")
            if source_id:
                result["relations"].add(source_id)

    cfel_manifest = load(ANALYSIS / "cfel-description/manifest.json")
    for row in cfel_manifest.get("source_pins", []):
        match = re.search(r"CA-[A-Z]+-\d+", str(row.get("source", "")))
        if match:
            result["cfel-description"].add(match.group(0))
    for item in cfel_manifest.get("owned_scope", []):
        match = re.search(r"CA-[A-Z]+-\d+", str(item))
        if match:
            result["cfel-description"].add(match.group(0))
    return result


def evidence(kind: str, ids: list[str], basis_file: str, detail: str) -> dict[str, Any]:
    return {
        "kind": kind,
        "basis_ids": sorted(set(ids), key=id_sort),
        "basis_file": basis_file,
        "detail": detail,
    }


def mapping_inventory() -> dict[str, Any]:
    safe = load(MIGRATION / "subject-map-candidate.json")["safe_exact_path_candidates"]
    primary = load(MIGRATION / "primary-mapping-candidate.json")["rows"]
    properties = load(MIGRATION / "property-mapping-candidate.json")["rows"]
    retained = load(MIGRATION / "retained-concept-replacements.json")["replacements"]
    shared = load(MIGRATION / "shared-mapping-candidate.json")["rows"]
    legacy = load(ANALYSIS / "legacy-cfel/manifest.json")
    legacy_entities_working = load(
        ANALYSIS / "legacy-entities/legacy-entities-working-dispositions.json"
    )

    safe = sorted(safe, key=lambda row: len(compact(row["from"])), reverse=True)
    primary_by_target = {row["target"]: row for row in primary}
    property_by_target = {row["target"]: row for row in properties}
    composition = next(
        row
        for row in shared
        if row.get("summary") == "Define composition and its inverse"
    )
    return {
        "safe": safe,
        "primary": primary_by_target,
        "property": property_by_target,
        "retained": retained,
        "composition": composition,
        "legacy": legacy,
        "legacy_entities_working": legacy_entities_working,
    }


def transform_subject(subject: str, maps: dict[str, Any], *, allow_composition: bool = True) -> tuple[str | None, list[dict[str, Any]]]:  # noqa: C901
    """Return an evidence-backed candidate address, never an inferred entity."""

    text = compact(subject)
    evidence_rows: list[dict[str, Any]] = []

    # The product successor is already prepared by the legacy-entity lane.
    # Use its exact source-backed Draft and do not invent a new Product kind.
    if text == "Entity/Aspect/Product:CAPRMEDIO Framework":
        product_row = next(
            (
                row
                for row in maps["legacy_entities_working"].get("rows", [])
                if row.get("id") == "CA-R-2256"
            ),
            None,
        )
        if product_row:
            evidence_rows.append(
                evidence(
                    "legacy_product_successor",
                    ["CA-R-2256"],
                    rel(ANALYSIS / "legacy-entities/legacy-entities-working-dispositions.json"),
                    "Entity/Aspect/Product: CAPRMEDIO Framework -> Node/Continuant//CAPRMEDIO Framework; use the existing authoritative Declaration Draft (candidate hash b1211656140ab8f293719350d5036c97d30314d00ac9c8b1aadc4234bda31fda)",
                )
            )
            return "Node/Continuant//CAPRMEDIO Framework", evidence_rows

    # Exact CFEL language-element replacements are packet-backed.  Relation
    # instances remain inventory-only when their owner belongs to another lane.
    for row in maps["legacy"]["candidates"]:
        if text == compact(row["subject_before"]):
            evidence_rows.append(
                evidence(
                    "legacy_cfel_subject",
                    [row["id"]],
                    rel(ANALYSIS / "legacy-cfel/manifest.json"),
                    f"{row['subject_before']} -> {row['subject_after']}",
                )
            )
            return row["subject_after"], evidence_rows

    # Composition is the one permitted direction change.  Split endpoints,
    # transform each endpoint, and retain the cardinality token.
    if allow_composition:
        match = re.match(r"^(.*?)\s+>\{([^}]+)\}\s+(.*)$", text)
        if match:
            left, left_evidence = transform_subject(match.group(1), maps, allow_composition=False)
            right, right_evidence = transform_subject(match.group(3), maps, allow_composition=False)
            if left is not None and right is not None:
                evidence_rows.extend(left_evidence)
                evidence_rows.extend(right_evidence)
                composition = maps["composition"]
                ids = composition.get("current_candidate_ids", [])
                evidence_rows.append(
                    evidence(
                        "composition_operator",
                        ids,
                        rel(MIGRATION / "shared-mapping-candidate.json"),
                        "legacy HAS_PART spelling > -> current whole-to-part containment <+",
                    )
                )
                return f"{left} <+{{{match.group(2)}}} {right}", evidence_rows

    # Safe exact-path packet.  Prefix extension is retained as a candidate,
    # but the report marks it for review because the source packet explicitly
    # limits automatic application to exact paths.
    for row in maps["safe"]:
        old = compact(row["from"])
        if text == old:
            evidence_rows.append(
                evidence(
                    "safe_exact_path",
                    row.get("basis_ids", []),
                    rel(MIGRATION / "subject-map-candidate.json"),
                    f"exact path {row['from']} -> {row['to']}",
                )
            )
            text = row["to"]
            break
        if text.startswith(old + "/") or text.startswith(old + "."):
            evidence_rows.append(
                evidence(
                    "safe_prefix_extension",
                    row.get("basis_ids", []),
                    rel(MIGRATION / "subject-map-candidate.json"),
                    f"known prefix {row['from']} -> {row['to']}; suffix preserved for review",
                )
            )
            text = row["to"] + text[len(old) :]
            break

    # Retained concepts have an explicit old-definition -> Node mapping.  Do
    # not extend this mapping through arbitrary descendants: the retained
    # replacement is evidence for the named concept, not a blanket
    # Entity->Node rewrite.
    for row in maps["retained"]:
        old = f"Entity/Object/{row['concept']}"
        if text == old:
            new = f"Node/{row['concept']}"
            evidence_rows.append(
                evidence(
                    "retained_concept",
                    [row["old_definition"], row["new_declaration"]],
                    rel(MIGRATION / "retained-concept-replacements.json"),
                    f"retained {row['concept']} address {old} -> {new}",
                )
            )
            text = new
            break

    # The bare legacy property has an explicit high-confidence successor.
    # Qualified `Content Role:X` expressions are handled below as Subject
    # qualifiers and stay separate from this property-path rename.
    if text == "Atom/Content Role":
        row = maps["property"].get("Atom.Role", {})
        text = "Atom.Role"
        evidence_rows.append(
            evidence(
                "property_rename",
                row.get("sources", ["CA-R-2357"]),
                rel(MIGRATION / "property-mapping-candidate.json"),
                "Content Role -> Role",
            )
        )

    role_names = {
        "Concern",
        "Analysis",
        "Plan",
        "Requirement",
        "Method",
        "Evaluation",
        "Delivery",
        "Operations",
    }
    role_rows = {
        target.rsplit(" := ", 1)[-1].rstrip(")"): row
        for target, row in maps["primary"].items()
        if target.startswith("Atom/(.Role := ")
    }

    # Replace the whole parenthesized legacy qualifier.  A substring-only
    # replacement would produce `(.(` and an invalid Subject.
    def replace_parenthesized_role(match: re.Match[str]) -> str:
        role = match.group(1).strip()
        if role not in role_names:
            return match.group(0)
        row = role_rows.get(role)
        ids = [item["id"] for item in row.get("current_candidates", [])] if row else []
        evidence_rows.append(
            evidence(
                "role_qualification",
                ids,
                rel(MIGRATION / "primary-mapping-candidate.json"),
                f"parenthesized Content Role:{role} -> (.Role := {role})",
            )
        )
        return f"(.Role := {role})"

    text = re.sub(
        r"\(\.Content Role\s*:\s*([^()]+)\)",
        replace_parenthesized_role,
        text,
    )

    # These qualified Operations kinds have explicit current successors.
    # Other legacy Type values remain visible for review instead of being
    # guessed as Forms.
    for kind, target in (
        ("Action", "Atom/(.Role := Operations)/Action"),
        ("Workflow", "Atom/(.Role := Operations)/Workflow"),
        ("Step", "Atom/(.Role := Operations)/Step"),
        ("Substep", "Atom/(.Role := Operations)/Substep"),
    ):
        pattern = rf"\(\.Role := Operations\)/\(\.Type\s*:\s*{re.escape(kind)}\)"
        if re.search(pattern, text):
            row = maps["primary"].get(target)
            ids = [item["id"] for item in row.get("current_candidates", [])] if row else []
            text = re.sub(pattern, target.split("Atom/", 1)[1], text, count=1)
            evidence_rows.append(
                evidence(
                    "role_form_qualification",
                    ids,
                    rel(MIGRATION / "primary-mapping-candidate.json"),
                    f"Operations/{kind} -> {target}",
                )
            )
            break

    relation_definition_pattern = (
        r"\(\.Role := Requirement\)/\(\.Type\s*:\s*Relation Definition\)"
    )
    if re.search(relation_definition_pattern, text):
        row = maps["primary"].get(
            "Atom/(.Role := Requirement)/(.Form := Relation Definition)"
        )
        ids = [item["id"] for item in row.get("current_candidates", [])] if row else ["CA-R-2228"]
        text = re.sub(
            relation_definition_pattern,
            "(.Role := Requirement)/(.Form := Relation Definition)",
            text,
            count=1,
        )
        evidence_rows.append(
            evidence(
                "role_form_qualification",
                ids,
                rel(MIGRATION / "primary-mapping-candidate.json"),
                "Requirement/Relation Definition Form",
            )
        )

    # Explicit Operations kinds and the admitted Relation Definition Form.
    for role, kind, target in (
        ("Operations", "Action", "Atom/(.Role := Operations)/Action"),
        ("Operations", "Workflow", "Atom/(.Role := Operations)/Workflow"),
        ("Operations", "Step", "Atom/(.Role := Operations)/Step"),
        ("Operations", "Substep", "Atom/(.Role := Operations)/Substep"),
    ):
        pattern = rf"Content Role:?\s*{role}/Type:?\s*{kind}"
        if re.search(pattern, text):
            row = maps["primary"].get(target)
            ids = [item["id"] for item in row.get("current_candidates", [])] if row else []
            text = re.sub(pattern, target.split("Atom/", 1)[1], text, count=1)
            evidence_rows.append(
                evidence("role_form_qualification", ids, rel(MIGRATION / "primary-mapping-candidate.json"), f"{role}/{kind} -> {target}")
            )
            break

    if re.search(r"Content Role:?\s*Requirement/Type:?\s*Relation Definition", text):
        row = maps["primary"].get("Atom/(.Role := Requirement)/(.Form := Relation Definition)")
        ids = [item["id"] for item in row.get("current_candidates", [])] if row else ["CA-R-2228"]
        text = re.sub(
            r"Content Role:?\s*Requirement/Type:?\s*Relation Definition",
            "(.Role := Requirement)/(.Form := Relation Definition)",
            text,
            count=1,
        )
        evidence_rows.append(
            evidence("role_form_qualification", ids, rel(MIGRATION / "primary-mapping-candidate.json"), "Requirement/Relation Definition Form")
        )

    # General Content Role spelling is source-backed for the eight retained
    # roles.  Unadmitted Type values remain untouched.
    for role in role_names:
        pattern = rf"Content Role:?\s*{re.escape(role)}"
        if re.search(pattern, text):
            row = role_rows.get(role)
            ids = [item["id"] for item in row.get("current_candidates", [])] if row else []
            text = re.sub(pattern, f"(.Role := {role})", text, count=1)
            evidence_rows.append(
                evidence("role_qualification", ids, rel(MIGRATION / "primary-mapping-candidate.json"), f"Content Role:{role} -> .Role:{role}")
            )

    def replace_operations_type(match: re.Match[str]) -> str:
        kind = match.group(1)
        target = f"Atom/(.Role := Operations)/{kind}"
        row = maps["primary"].get(target)
        ids = [item["id"] for item in row.get("current_candidates", [])] if row else []
        evidence_rows.append(
            evidence(
                "role_form_qualification",
                ids,
                rel(MIGRATION / "primary-mapping-candidate.json"),
                f"Operations/{kind} -> {target}",
            )
        )
        return f"(.Role := Operations)/{kind}"

    # A legacy path can leave an unparenthesized Type after the Role has been
    # normalized.  Only the four explicitly mapped Operations kinds change.
    text = re.sub(
        r"\(\.Role := Operations\)/Type\s*:\s*(Action|Workflow|Step|Substep)",
        replace_operations_type,
        text,
    )
    # Unadmitted parenthesized qualifiers remain unchanged for review.

    # Explicit property migrations with source rows.  Framework Settings is
    # deliberately not mapped: the selected inventory defers it.
    if "Version Number" in text and "Atom" in text:
        text = text.replace("Version Number", "Version")
        row = maps["property"].get("Atom.Version", {})
        evidence_rows.append(evidence("property_rename", row.get("sources", ["CA-R-2363"]), rel(MIGRATION / "property-mapping-candidate.json"), "Version Number -> Version"))
    if "Autonomous Confidence Threshold" in text and "Plan" in text:
        text = text.replace("Autonomous Confidence Threshold", "AI Agent Confidence Threshold")
        row = maps["property"].get("Atom/(.Role := Plan).AI Agent Confidence Threshold", {})
        evidence_rows.append(evidence("property_rename", row.get("sources", ["CA-R-2381"]), rel(MIGRATION / "property-mapping-candidate.json"), "Autonomous Confidence Threshold -> AI Agent Confidence Threshold"))
    if "Project.Settings.Atom Prefix" in text:
        text = text.replace("Project.Settings.Atom Prefix", "Project.Settings.Prefix")
        row = maps["property"].get("Project.Settings.Prefix", {})
        evidence_rows.append(evidence("property_rename", row.get("sources", ["CA-R-2459"]), rel(MIGRATION / "property-mapping-candidate.json"), "latest Project.Settings.Prefix applies beyond Atoms"))
    if "Project Implementation" in text and "Package" in text:
        text = text.replace("Project Implementation", "Implementation")
        row = maps["primary"].get("Implementation", {})
        ids = [item["id"] for item in row.get("current_candidates", [])] or ["CA-R-2173"]
        evidence_rows.append(evidence("primary_rename", ids, rel(MIGRATION / "primary-mapping-candidate.json"), "Package/Project Implementation -> Package/Implementation"))

    # Type -> Form is source-backed for Projection only.  Atom.Form remains
    # ambiguous in the property packet and is not guessed here.
    if text.startswith("Projection/") and "/Type:" in text:
        value = text.split("/Type:", 1)[1].strip()
        text = f"Projection/(.Form := {value})"
        row = maps["property"].get("Projection.Form", {})
        evidence_rows.append(evidence("projection_form_qualification", row.get("sources", ["CA-R-2397"]), rel(MIGRATION / "property-mapping-candidate.json"), "Projection Type value -> qualified Projection Form"))
    elif text.startswith("Projection/") and text.endswith("/Type"):
        text = text.replace("/Type", ".Form", 1)
        row = maps["property"].get("Projection.Form", {})
        evidence_rows.append(evidence("property_rename", row.get("sources", ["CA-R-2397"]), rel(MIGRATION / "property-mapping-candidate.json"), "Projection Type property -> Projection.Form"))
    if text.startswith("Projection/(.Type:"):
        text = text.replace("(.Type:", "(.Form := ", 1)
        if not text.endswith(")"):
            text += ")"
        row = maps["property"].get("Projection.Form", {})
        evidence_rows.append(evidence("property_rename", row.get("sources", ["CA-R-2397"]), rel(MIGRATION / "property-mapping-candidate.json"), "Projection Type qualifier -> Form qualifier"))

    # Keep the ambiguous Local Order candidate visible, but do not treat it as
    # a proven binding.
    if "Navigational Order Number" in text:
        text = text.replace("Navigational Order Number", "Local Order")
        row = maps["property"].get("Scope Unit.Local Order", {})
        evidence_rows.append(evidence("ambiguous_property_rename", row.get("sources", ["CA-R-1763", "CA-R-978"]), rel(MIGRATION / "property-mapping-candidate.json"), "Navigational Order Number -> Local Order requires disposition"))

    return text if evidence_rows else None, evidence_rows


def family(subject: str) -> str:
    if subject.startswith("CFEL") or "CFEL >" in subject:
        return "legacy_cfel_syntax"
    if re.search(r"\s>\{", subject):
        return "legacy_composition"
    if "Content Role" in subject or "/Type" in subject or "(.Type" in subject:
        return "role_form_qualification"
    if subject.startswith("Entity/"):
        return "legacy_entity_path"
    if "//" in subject:
        return "instance_or_named_scope"
    if subject.startswith("Atom/") or subject.startswith("Atom.") or subject.startswith("(Node"):
        return "current_root_unbound"
    return "other_semantic_review"


def binding(canonical: str | None, targets: set[str]) -> tuple[str | None, bool]:
    if canonical is None:
        return None, False
    key = compact(canonical)
    if key in targets:
        return "exact_target", True
    # A value condition addresses an existing Property; it does not create a
    # new node.  This handles `Projection.Form: X` and `Atom.Status: Draft`.
    if ":" in key and ":=" not in key and not key.startswith("CFEL"):
        base = key.split(":", 1)[0]
        if base in targets:
            return "allowed_value_on_existing_property", True
    return None, False


def main() -> None:
    from subject_notation import parse_subject_expression

    baseline_path = ANALYSIS / "contract-graph/current-baseline.json"
    baseline = load(baseline_path)
    groups: dict[str, list[dict[str, Any]]] = collections.defaultdict(list)
    for row in baseline["coverage_gaps"]:
        groups[row["subject"]].append(row)
    maps = mapping_inventory()
    targets = baseline_targets(baseline)
    lane_ids = owned_lane_ids()
    entries: list[dict[str, Any]] = []

    for subject in sorted(groups):
        rows = groups[subject]
        canonical, evidence_rows = transform_subject(subject, maps)
        original_valid = parse_ok(subject, parse_subject_expression)
        proposed_valid = parse_ok(canonical, parse_subject_expression) if canonical else None
        binding_kind, bound = binding(canonical, targets)
        if any(item["kind"] == "projection_form_qualification" for item in evidence_rows):
            binding_kind, bound = "allowed_value_on_existing_property", True
        ids = source_ids(rows)
        owned = {
            lane: sorted(set(ids) & values, key=id_sort)
            for lane, values in lane_ids.items()
            if set(ids) & values
        }
        mapping_kinds = {item["kind"] for item in evidence_rows}
        ambiguous = "ambiguous_property_rename" in mapping_kinds
        prefix_extension = "safe_prefix_extension" in mapping_kinds
        confidence = "none"
        if evidence_rows:
            confidence = "low" if ambiguous else "medium" if prefix_extension else "high"
        if bound and ambiguous:
            bound = False
            binding_kind = None
        status = (
            "bound_without_new_entity"
            if bound
            else "candidate_requires_review"
            if evidence_rows
            else "no_source_backed_alias"
        )
        entries.append(
            {
                "subject": subject,
                "count": len(rows),
                "source_ids": ids,
                "proposed_canonical": canonical,
                "confidence": confidence,
                "mapping_status": status,
                "binding_kind": binding_kind,
                "bound_without_new_entity": bound,
                "structurally_valid_parse": original_valid,
                "proposed_structurally_valid_parse": proposed_valid,
                "semantic_family": family(subject),
                "owned_by_other_lane": owned,
                "future_mutation_allowed": False,
                "evidence": evidence_rows,
                "reason": (
                    "A source-backed address candidate exists; adoption requires parent review."
                    if evidence_rows
                    else "No exact source-backed alias was found; preserve the subject for semantic review."
                ),
            }
        )

    rows_total = sum(item["count"] for item in entries)
    summary: dict[str, Any] = {
        "unbound_rows": rows_total,
        "unique_subjects": len(entries),
        "original_structurally_valid_rows": sum(item["count"] for item in entries if item["structurally_valid_parse"]),
        "original_structurally_invalid_rows": sum(item["count"] for item in entries if not item["structurally_valid_parse"]),
        "proposed_alias_rows": sum(item["count"] for item in entries if item["proposed_canonical"]),
        "proposed_alias_subjects": sum(1 for item in entries if item["proposed_canonical"]),
        "bound_without_new_entity_rows": sum(item["count"] for item in entries if item["bound_without_new_entity"]),
        "bound_without_new_entity_subjects": sum(1 for item in entries if item["bound_without_new_entity"]),
        "unresolved_rows": sum(item["count"] for item in entries if not item["bound_without_new_entity"]),
        "unresolved_subjects": sum(1 for item in entries if not item["bound_without_new_entity"]),
        "source_ids_owned_by_other_lane": sum(
            sum(len(ids) for ids in item["owned_by_other_lane"].values())
            for item in entries
        ),
    }
    summary["source_ids_owned_by_other_lane_by_lane"] = {
        lane: sum(
            len(item["owned_by_other_lane"].get(lane, []))
            for item in entries
        )
        for lane in lane_ids
    }
    family_counts: dict[str, dict[str, int]] = {}
    for item in entries:
        group = family_counts.setdefault(item["semantic_family"], {"rows": 0, "unique_subjects": 0})
        group["rows"] += item["count"]
        group["unique_subjects"] += 1

    report = {
        "schema_version": 1,
        "status": "READ_ONLY_ALIAS_CANDIDATE_INVENTORY",
        "scope": "Current-baseline unbound active Subjects only; no source or Current/Draft mutation",
        "source_baseline": {
            "path": rel(baseline_path),
            "sha256": hashlib.sha256(baseline_path.read_bytes()).hexdigest(),
            "coverage_gap_rows": len(baseline["coverage_gaps"]),
            "coverage_gap_unique_subjects": len(groups),
        },
        "mapping_basis": {
            "primary": rel(MIGRATION / "primary-mapping-candidate.json"),
            "properties": rel(MIGRATION / "property-mapping-candidate.json"),
            "safe_subject_paths": rel(MIGRATION / "subject-map-candidate.json"),
            "retained_concepts": rel(MIGRATION / "retained-concept-replacements.json"),
            "selected_inventory": rel(MIGRATION.parent / "declaration-expansion/selected-node-inventory.json"),
            "cfel_legacy_subjects": rel(ANALYSIS / "legacy-cfel/manifest.json"),
            "legacy_product_successor": rel(ANALYSIS / "legacy-entities/legacy-entities-working-dispositions.json"),
            "composition_mapping": rel(MIGRATION / "shared-mapping-candidate.json"),
            "rule": "Only source-backed address changes are proposed; Entity->Node, arbitrary >->/, and Subtype->Instance are never inferred.",
        },
        "summary": summary,
        "remaining_semantic_families": family_counts,
        "entries": entries,
    }
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "alias-candidate-inventory.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"summary": summary, "remaining_semantic_families": family_counts}, indent=2))


if __name__ == "__main__":
    main()
