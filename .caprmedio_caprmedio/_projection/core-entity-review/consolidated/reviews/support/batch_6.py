"""Build and verify the bounded consolidated review receipt for batch 6.

The receipt is derived from the captured batch-6 review and the accepted
global evidence catalogue.  It is intentionally create-only: use --persist
to create the JSON, and an existing byte-different receipt is an error.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[6]
BASE = ROOT / ".caprmedio_caprmedio/_projection/core-entity-review"
INPUT = BASE / "nodes/inputs/nodes.batch-6.input.json"
PRIOR = BASE / "nodes/nodes.batch-6.review.json"
DISPOSITIONS = BASE / "nodes/nodes.dispositions.json"
CANDIDATE = BASE / "presentation/operator.entity-graph.candidate.json"
BASELINE = BASE / "baseline.inventory.json"
OUTPUT = BASE / "consolidated/reviews/batch-6.review.json"
SNAPSHOT_READER = BASE / "nodes/support/snapshot_sources.py"

CAPTURED_COMMIT = "a971d0e00c33c779f485fc8cad63194894d440fb"
EXPECTED_CANDIDATE_SHA256 = (
    "99e7710f5ef83df2b1f3ec1ef4142547655e63bef7415266c5521380da7fa99b"
)
EXPECTED_INPUT_SHA256 = (
    "6ffc7e45c5c647e5c299b98761c74db7f9aca3ed76c80a4d7f32cde9df74e71c"
)
EXPECTED_BASELINE_SHA256 = (
    "bc5d99e91fb7dd4dcb42e59ff33cc24cff1d0901c5904764394c769aaa0a9430"
)
EXPECTED_BATCH_REVIEW_SHA256 = (
    "66b0bcbebb8d66cb569eb7258817ceba597de509898f966f51e72d49d7075114"
)
EXPECTED_GLOBAL_DISPOSITIONS_SHA256 = (
    "1b9d751f95aa71486908b53b3d7f3f9825defae137be3d8792d45177587c48f8"
)


def sha256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes())


def load_snapshot_reader() -> Any:
    spec = importlib.util.spec_from_file_location("batch6_snapshot_sources", SNAPSHOT_READER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SNAPSHOT_READER}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def verify_evidence(evidence_catalogue: dict[str, Any], refs: list[str], reader: Any) -> None:
    for ref in refs:
        if ref not in evidence_catalogue:
            raise AssertionError(f"missing global evidence reference: {ref}")
        item = evidence_catalogue[ref]
        raw = reader.read_source(item["atom_id"])
        lines = raw.decode("utf-8").splitlines()
        start = item["start_line"]
        end = item["end_line"]
        quote = "\n".join(lines[start - 1 : end])
        if quote != item["quote"]:
            raise AssertionError(f"captured quote mismatch: {ref}")
        if sha256(quote.encode("utf-8")) != item["text_sha256"]:
            raise AssertionError(f"captured quote hash mismatch: {ref}")


ROOT_RULES = {
    "Artifact": "root_entities[0]",
    "Scope Unit": "root_entities[1]",
    "Actor": "root_entities[2]",
    "Relation": "root_entities[3]",
    "Revision": "root_entities[4]",
    "Carrier": "root_entities[5]",
    "Execution": "root_entities[6]",
}

NOTES = {
    "artifact": (
        "The seven-root comparison keeps this as an Artifact or dependent-Entity "
        "display path; the path is not a native edge, Subject migration, or new root."
    ),
    "artifact_property": (
        "The dependent-Entity rule selects the owner plus field; it does not create "
        "an independent lifecycle or a per-Property Carrier relation."
    ),
    "priority": (
        "Keep Priority as a qualified Atom field in the structural view. Its captured "
        "High/Medium/Low domain is Concern-specific; it is not a storage policy, "
        "universal Status, or an inferred Issue bearer."
    ),
    "actor": (
        "The evidenced performer concept maps to Actor; a generic Actor Type stays "
        "distinct from a specific performer, authorization record, or execution."
    ),
    "carrier": (
        "Carrier is a separate root identified by Carrier ID; physical filename and "
        "path remain storage locations, not Carrier identity."
    ),
    "delivery": (
        "Use the general D storage/field policy. No per-Property Carrier Relation, "
        "D Atom, or filename/path identity is introduced."
    ),
    "execution": (
        "The actual occurrence maps to Execution and remains distinct from its "
        "reusable Operation definition and any Journal record. Git preserves every "
        "Atom version; the current Active version and archived history remain distinct."
    ),
    "operation": (
        "Keep the reusable Operation definition distinct from an actual Execution "
        "and its record; role-centred views do not add a root or native kind."
    ),
    "projection": (
        "Keep this as a derived Projection view with source traceability and whole-set "
        "rebuild semantics; a rebuild does not invent a source Atom version, and the "
        "Projection is not another authority or an independent root."
    ),
    "relation": (
        "Preserve the qualified relation or ordering meaning without admitting a new "
        "native relation kind from a label or display path alone."
    ),
    "scope": (
        "Scope Unit ownership and stable identity remain distinct from Atom content, "
        "applicability Scope and Carrier storage."
    ),
    "syntax": (
        "Treat this as contextual, value-domain or applicability syntax; no hidden "
        "native edge, subtype, or independent Entity is admitted."
    ),
    "generic": (
        "Generic Entity vocabulary has no selected candidate root or owner/field in "
        "the latest candidate. Keep it in review; do not place it under Artifact. "
        "Atom remains an Artifact subtype, not a dependent Property."
    ),
}


def spec(
    action: str,
    root: str,
    path: str,
    view: str,
    rules: list[str],
    note: str,
) -> dict[str, Any]:
    normalized_rules = [normalize_rule(rule) for rule in [ROOT_RULES[root], *rules]]
    return {
        "action": action,
        "candidate_root": root,
        "candidate_path": path,
        "content_view": view,
        "operator_rules": normalized_rules,
        "candidate_note": NOTES[note],
    }


def null_spec(
    action: str,
    view: str,
    rules: list[str],
    note: str,
) -> dict[str, Any]:
    return {
        "action": action,
        "candidate_root": None,
        "candidate_path": None,
        "content_view": view,
        "operator_rules": [normalize_rule(rule) for rule in rules],
        "candidate_note": NOTES[note],
    }


def normalize_rule(rule: str) -> str:
    """Use JSON-pointer-like candidate paths in the receipt."""
    if rule.startswith("/"):
        return rule
    if rule.startswith("root_entities[") and rule.endswith("]"):
        return f"/root_entities/{rule[len('root_entities['):-1]}"
    return "/" + rule.replace(".", "/")


def high_specs() -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}

    operation_names = {
        "Obtain Source Correction Decision",
        "Persist Atom Replacement",
        "Prepare Structural Change",
        "Project Settings Validation",
        "Project Structure Maintenance",
        "Project Structure Maintenance Application Step",
        "Project Structure Maintenance Authorization Step",
        "Project Structure Maintenance Candidate Assessment Step",
        "Project Structure Maintenance Preparation Step",
        "Project Structure Maintenance Result Assessment Step",
        "Project Structure Maintenance Selection Step",
        "Propose Source Corrections",
        "Publish Reconciled Projection",
        "RMED Atom Review Workflow",
        "RMED Atom Review Workflow/coverage/Action",
    }
    for identity in operation_names:
        out[identity] = spec(
            "operation_or_method",
            "Artifact",
            f"Artifact/Atom.Substance.Operation.{identity.replace('/', '.')}",
            "O",
            [
                "dependent_entities",
                "content_direction.role_labels.Operations",
                "execution_definition_policy",
            ],
            "operation",
        )
    out["Project Settings Validation"]["candidate_path"] = (
        "Artifact/Atom.Substance.Operation.Project Settings Validation"
    )
    out["Project Settings Validation"]["content_view"] = "E"

    projection_names = {
        "Optional Projection",
        "Optional Projection/Activation",
        "Plan Graph",
        "Project Scope Unit Graph Projection",
        "Projection",
        "Projection/Authority",
        "Projection/Type",
        "Projection/Type: Artifact Change Log",
        "Projection/Type: Atom Subjects Graph",
        "Projection/Type: Catalog",
        "Projection/Type: Entities Graph",
        "Projection/Type: Extended Entities Graph",
        "Projection/Type: Hub",
        "Projection/Type: Implementation Overview",
        "Projection/Type: Map",
        "Projection/Type: Process Log",
        "Projection/Type: Reconciled Projection",
        "Projection/Type: Terms Graph",
    }
    for identity in projection_names:
        if identity == "Projection":
            path = "Artifact/Projection"
        elif identity.startswith("Projection/"):
            path = f"Artifact/Projection.{identity.removeprefix('Projection/').replace('/', '.')}"
        else:
            path = f"Artifact/Projection.{identity.replace('/', '.')}"
        out[identity] = spec(
            "projection_view",
            "Artifact",
            path,
            "P",
            [
                "dependent_entities",
                "projection_member_model",
                "entity_representation_rules",
            ],
            "projection",
        )

    carrier_names = {
        "Project Settings/Atom Prefix/Carrier",
        "Project Settings/Authoritative Carrier",
        "Project Settings/Authoritative Carrier/Content",
        "Project Settings/Authoritative Carrier/Filename",
        "Project-Owned Carrier",
        "Project-Owned Carrier Root",
        "Project-Owned Markdown Atom Carrier/Filename",
        "Project/Operator Registry/Carrier",
        "Projection/Carrier Root",
        "Proof Carrier",
        "Proof Carrier/Dependency Frontier",
    }
    for identity in carrier_names:
        out[identity] = spec(
            "delivery_policy",
            "Carrier",
            f"Carrier.Delivery Policy ({identity.replace('/', ' ')})",
            "D",
            ["entity_identity_model.carrier_identity", "carrier_delivery_model"],
            "carrier",
        )

    delivery_artifact_names = {
        "Obsolete Project Name": "Artifact/Project Settings.Obsolete Project Name",
        "Project Name": "Artifact/Project Settings.Project Name",
        "Project Settings/Atom Prefix": "Artifact/Project Settings.Atom Prefix",
        "Project Settings/Identifier": "Artifact/Project Settings.Identifier",
        "Project Atom ID": "Artifact/Atom.Project Atom ID",
        "Priority": "Artifact/Atom.Priority",
        "Projection/Carrier/Updated At": "Artifact/Projection.Updated At",
    }
    for identity, path in delivery_artifact_names.items():
        rules = ["dependent_entities", "carrier_delivery_model"]
        if identity == "Priority":
            rules = ["dependent_entities", "entity_vs_syntax_rules", "content_direction.role_labels.Concern"]
        elif identity == "Project Atom ID":
            rules.append("entity_identity_model.dependent_entity")
        content_view = "R" if identity == "Priority" else "D"
        out[identity] = spec(
            "delivery_policy" if identity.startswith("Project Settings/") or identity == "Projection/Carrier/Updated At" else "rebase",
            "Artifact",
            path,
            content_view,
            rules,
            "priority" if identity == "Priority" else ("delivery" if identity.startswith("Project Settings/") or identity == "Projection/Carrier/Updated At" else "artifact_property"),
        )

    out["Operator"] = spec(
        "retain",
        "Actor",
        "Actor/Operator",
        "C",
        ["entity_identity_model.actor", "m_e_root_question"],
        "actor",
    )

    scope_names = {
        "Project",
        "Previous Unit",
        "Owned Atoms",
        "Project Boundary Position",
        "Project/Principle universe",
        "Project/priority model application",
    }
    for identity in scope_names:
        if identity == "Project":
            action = "retain"
            view = "C"
        elif identity == "Owned Atoms":
            action = "projection_view"
            view = "P"
        else:
            action = "syntax_context"
            view = "unclassified"
        if identity == "Project":
            out[identity] = spec(
                action,
                "Scope Unit",
                "Scope Unit/Project",
                view,
                ["entity_identity_model.scope_unit", "entity_vs_syntax_rules"],
                "scope",
            )
        elif identity == "Owned Atoms":
            out[identity] = spec(
                action,
                "Scope Unit",
                "Scope Unit.Owned Atoms",
                view,
                ["entity_identity_model.scope_unit", "entity_vs_syntax_rules"],
                "scope",
            )
        else:
            out[identity] = null_spec(
                action,
                view,
                ["entity_identity_model.scope_unit", "entity_vs_syntax_rules"],
                "syntax",
            )

    out["Project Configuration"] = spec(
        "retain",
        "Artifact",
        "Artifact/Project Configuration",
        "R",
        ["dependent_entities", "content_direction"],
        "artifact",
    )
    out["Project Settings"] = spec(
        "retain",
        "Artifact",
        "Artifact/Project Settings",
        "R",
        ["dependent_entities", "content_direction"],
        "artifact",
    )
    out["Project Structure"] = spec(
        "retain",
        "Artifact",
        "Artifact/Project Structure",
        "R",
        ["dependent_entities", "content_direction"],
        "artifact",
    )
    out["Project/Operator Registry"] = spec(
        "retain",
        "Artifact",
        "Artifact/Operator Registry",
        "R",
        ["dependent_entities", "entity_identity_model.actor"],
        "artifact",
    )

    out["Primary Entity"] = null_spec(
        "review_required",
        "unclassified",
        ["dependent_entities", "entity_vs_syntax_rules", "review_backlog.question_policy"],
        "generic",
    )
    out["Property"] = null_spec(
        "review_required",
        "unclassified",
        ["dependent_entities", "entity_identity_model.dependent_entity", "review_backlog.question_policy"],
        "generic",
    )

    out["Producer Result/Flow Direction"] = spec(
        "retain",
        "Relation",
        "Relation/Producer Result.Flow Direction",
        "R",
        ["relation_type_model", "entity_vs_syntax_rules"],
        "relation",
    )
    for identity in {"Project/graph dimensions", "Project/normative authority graph"}:
        out[identity] = null_spec(
            "syntax_context",
            "R",
            ["relation_type_model", "entity_vs_syntax_rules"],
            "syntax",
        )

    out["Project/minimum model"] = null_spec(
        "syntax_context",
        "M",
        ["content_direction", "m_e_root_question", "execution_definition_policy"],
        "syntax",
    )
    out["Projection Rebuild"] = spec(
        "rebase",
        "Execution",
        "Execution/Projection Rebuild",
        "E",
        ["execution_definition_policy", "projection_member_model"],
        "execution",
    )

    expected = {
        input_node["identity"]
        for input_node in json.loads(INPUT.read_text(encoding="utf-8"))["nodes"]
        if input_node["identity"] not in LOW_CONFIDENCE
    }
    actual = set(out)
    if actual != expected:
        raise AssertionError(
            f"high-confidence mapping mismatch; missing={sorted(expected - actual)}, "
            f"extra={sorted(actual - expected)}"
        )
    return out


LOW_CONFIDENCE = {
    "Producer",
    "Producer Result",
    "Producer/Result",
    "Producer/Scope Unit",
    "Project Settings/Project identity",
    "Project Settings/Project identity/Carrier",
    "Project-Owned Markdown Atom Carrier",
    "Project/Scope Unit",
    "Project/lexicographic selection",
    "Projection/Carrier",
    "Provenance",
    "RMED Atom Review Workflow/coverage",
}


LOW_RULES = {
    "Producer": ["content_direction", "entity_vs_syntax_rules", "review_backlog.question_policy"],
    "Producer Result": ["content_direction", "entity_vs_syntax_rules", "review_backlog.question_policy"],
    "Producer/Result": ["content_direction", "entity_vs_syntax_rules", "review_backlog.question_policy"],
    "Producer/Scope Unit": ["entity_identity_model.scope_unit", "entity_vs_syntax_rules", "review_backlog.question_policy"],
    "Project Settings/Project identity": ["entity_identity_model.scope_unit", "dependent_entities", "review_backlog.question_policy"],
    "Project Settings/Project identity/Carrier": ["entity_identity_model.carrier_identity", "carrier_delivery_model", "review_backlog.question_policy"],
    "Project-Owned Markdown Atom Carrier": ["entity_identity_model.carrier_identity", "carrier_delivery_model", "review_backlog.question_policy"],
    "Project/Scope Unit": ["entity_identity_model.scope_unit", "entity_vs_syntax_rules", "review_backlog.question_policy"],
    "Project/lexicographic selection": ["entity_vs_syntax_rules", "review_backlog.question_policy"],
    "Projection/Carrier": ["entity_identity_model.carrier_identity", "carrier_delivery_model", "review_backlog.question_policy"],
    "Provenance": ["entity_identity_model", "history_model", "review_backlog.question_policy"],
    "RMED Atom Review Workflow/coverage": ["m_e_root_question", "execution_definition_policy", "review_backlog.question_policy"],
}


def low_question(identity: str, checked: list[str]) -> dict[str, str]:
    checked_text = ", ".join(checked)
    messages = {
        "Producer": "The checked Main Content names qualified Producer target/result roles but does not define a standalone Producer identity.",
        "Producer Result": "The checked Main Content defines producer-result flow direction but not the bare Producer Result identity.",
        "Producer/Result": "The checked Main Content constrains one producer result but leaves its qualified identity unresolved.",
        "Producer/Scope Unit": "The checked Main Content supplies a filename token/target qualifier, not a positive Producer Scope Unit identity.",
        "Project Settings/Project identity": "The checked source does not settle whether this contextual identity is an Artifact field, Scope Unit identity, or syntax-only qualifier.",
        "Project Settings/Project identity/Carrier": "The checked source does not settle the carrier binding; filename/path must not be used as Carrier identity.",
        "Project-Owned Markdown Atom Carrier": "The checked source names a project-owned carrier context but does not positively settle its independent Carrier identity.",
        "Project/Scope Unit": "The checked source does not positively settle whether this slash form is a Scope Unit identity or contextual ownership syntax.",
        "Project/lexicographic selection": "The checked source preserves a selection rule but does not establish an independent Entity or native relation.",
        "Projection/Carrier": "The checked source identifies a carrier context but does not establish a concrete Carrier ID or binding rule.",
        "Provenance": "The checked source says provenance does not establish authority, applicability, or currentness, but does not define Provenance identity.",
        "RMED Atom Review Workflow/coverage": "The checked sources define stage-bound coverage gates, not an independent coverage Entity or Property.",
    }
    return {
        "kind": "source_gap",
        "text": f"{messages[identity]} Checked captured sources: {checked_text}. Keep this as review work; no candidate path is committed.",
    }


def generic_question(identity: str, checked: list[str]) -> dict[str, str]:
    checked_text = ", ".join(checked)
    return {
        "kind": "source_gap",
        "text": (
            f"The captured meaning for {identity} is preserved, but the latest candidate "
            "does not select a root or an owner/field expression for this generic Entity "
            f"vocabulary. Checked captured sources: {checked_text}. Keep this as review "
            "work; do not manufacture Artifact ownership or a candidate path."
        ),
    }


def validate_display_paths(nodes: list[dict[str, Any]]) -> None:
    """Reject untyped broad paths before a receipt can be persisted."""
    generic = {"Primary Entity", "Property"}
    for row in nodes:
        identity = row["identity"]
        path = row["candidate_path"]
        root = row["candidate_root"]
        if identity in generic:
            if root is not None or path is not None:
                raise AssertionError(f"generic Entity vocabulary got a candidate path: {identity}")
            continue
        if path is None:
            if root is not None:
                raise AssertionError(f"candidate root without path: {identity}")
            continue
        if path.startswith("Carrier/"):
            raise AssertionError(f"Carrier path uses an untyped slash: {identity}")
        if path.startswith("Artifact/Atom/"):
            raise AssertionError(f"Atom dependent field uses subtype slash: {identity}")
        if path.startswith("Artifact/Projection/"):
            raise AssertionError(f"Projection dependent field uses subtype slash: {identity}")
        if path.startswith("Artifact/Project Settings/"):
            raise AssertionError(f"Project Settings field uses subtype slash: {identity}")
        if path.startswith("Artifact/Project/"):
            raise AssertionError(f"Project is incorrectly nested under Artifact: {identity}")
        if "Substance (" in path:
            raise AssertionError(f"role-centred Substance path uses legacy root syntax: {identity}")
        if row["action"] == "delivery_policy" and root == "Carrier":
            if not path.startswith("Carrier.Delivery Policy ("):
                raise AssertionError(f"concrete Carrier path escaped general D policy: {identity}")
        if row["action"] == "operation_or_method" and root == "Artifact":
            if ".Substance.Operation." not in path:
                raise AssertionError(f"operation path is not role-centred: {identity}")
        if identity.startswith("Projection/Type:"):
            if ".Type: " not in path:
                raise AssertionError(f"Projection Type value is not colon-qualified: {identity}")
        if identity == "Producer Result/Flow Direction":
            if path != "Relation/Producer Result.Flow Direction":
                raise AssertionError("Producer Result field lost subtype/dependent operators")
        if identity == "Priority":
            if path != "Artifact/Atom.Priority" or row["content_view"] != "R":
                raise AssertionError("Priority must remain a qualified structural Atom field")


def build() -> dict[str, Any]:
    raw_input = INPUT.read_bytes()
    raw_prior = PRIOR.read_bytes()
    raw_baseline = BASELINE.read_bytes()
    raw_candidate = CANDIDATE.read_bytes()
    if sha256(raw_input) != EXPECTED_INPUT_SHA256:
        raise AssertionError("batch-6 input changed")
    if sha256(raw_prior) != EXPECTED_BATCH_REVIEW_SHA256:
        raise AssertionError("accepted batch-6 review changed")
    if sha256(raw_baseline) != EXPECTED_BASELINE_SHA256:
        raise AssertionError("captured baseline changed")
    raw_dispositions = DISPOSITIONS.read_bytes()
    if sha256(raw_dispositions) != EXPECTED_GLOBAL_DISPOSITIONS_SHA256:
        raise AssertionError("global dispositions changed")
    candidate_sha = sha256(raw_candidate)
    if candidate_sha != EXPECTED_CANDIDATE_SHA256:
        raise AssertionError(f"candidate SHA mismatch: {candidate_sha}")

    source_input = json.loads(raw_input)
    prior = json.loads(raw_prior)
    dispositions = json.loads(raw_dispositions)
    candidate = json.loads(raw_candidate)
    if candidate.get("status") != "Candidate":
        raise AssertionError("candidate status changed")
    if candidate.get("authority", {}).get("native_relation_admission") != "not performed":
        raise AssertionError("candidate native admission boundary changed")
    if candidate.get("authority", {}).get("adopted_core_model") is not False:
        raise AssertionError("candidate unexpectedly claims Core adoption")
    if source_input.get("batch") != 6 or len(source_input.get("nodes", [])) != 81:
        raise AssertionError("unexpected batch-6 input coverage")
    if prior.get("batch") != 6 or len(prior.get("nodes", [])) != 81:
        raise AssertionError("unexpected accepted batch-6 review coverage")
    expected_identities = {node["identity"] for node in source_input["nodes"]}
    if {node["identity"] for node in prior["nodes"]} != expected_identities:
        raise AssertionError("prior review identities do not match batch-6 input")

    marks = {
        mark["identity"]: mark
        for mark in dispositions["node_disposition_marks"]
        if mark.get("scoped_refs", {}).get("batch") == 6
    }
    if len(marks) != 81:
        raise AssertionError(f"expected 81 accepted batch-6 marks, got {len(marks)}")
    evidence_catalogue = dispositions["evidence_catalogue"]
    reader = load_snapshot_reader()
    snapshot_result = reader.verify_snapshot()
    if snapshot_result["verification"] != "pass" or snapshot_result["source_context"] != "captured_snapshot":
        raise AssertionError("captured snapshot verification failed")
    all_refs = [
        ref
        for mark in marks.values()
        for ref in mark["scoped_refs"]["global_evidence_refs"]
    ]
    verify_evidence(evidence_catalogue, sorted(set(all_refs)), reader)

    specs = high_specs()
    nodes = []
    input_identities = []
    for input_node in source_input["nodes"]:
        identity = input_node["identity"]
        input_identities.append(identity)
        mark = marks.get(identity)
        if mark is None:
            raise AssertionError(f"missing accepted disposition mark: {identity}")
        review_row = mark["review_row"]
        refs = mark["scoped_refs"]["global_evidence_refs"]
        checked = review_row["checked_source_atom_ids"]
        prior_proposal = review_row.get("proposal") or {}
        preserved = list(prior_proposal.get("preserved_distinctions", []))
        prior_reason = review_row["reason"]
        common = {
            "identity": identity,
            "prior_disposition": review_row["disposition"],
            "confidence_percent": review_row["confidence_percent"],
            "reason": prior_reason,
            "evidence_refs": refs,
            "checked_source_atom_ids": checked,
            "preserved_distinctions": preserved,
        }
        if identity in LOW_CONFIDENCE:
            if review_row["confidence_percent"] >= 90:
                raise AssertionError(f"low-confidence row unexpectedly >=90: {identity}")
            common.update(
                {
                    "action": "review_required",
                    "candidate_root": None,
                    "candidate_path": None,
                    "content_view": "unclassified",
                    "operator_rules": [normalize_rule(rule) for rule in LOW_RULES[identity]],
                    "question": low_question(identity, checked),
                }
            )
            common["preserved_distinctions"] = preserved or [prior_reason]
        else:
            mapping = specs[identity]
            question = (
                generic_question(identity, checked)
                if mapping["action"] == "review_required"
                else None
            )
            common.update(
                {
                    "action": mapping["action"],
                    "candidate_root": mapping["candidate_root"],
                    "candidate_path": mapping["candidate_path"],
                    "content_view": mapping["content_view"],
                    "operator_rules": mapping["operator_rules"],
                    "question": question,
                    "reason": f"{prior_reason} {mapping['candidate_note']}",
                }
            )
            if mapping["candidate_note"] not in preserved:
                preserved.append(mapping["candidate_note"])
            common["preserved_distinctions"] = preserved or [mapping["candidate_note"]]
        nodes.append(common)

    if len(nodes) != 81 or len(set(input_identities)) != 81:
        raise AssertionError("batch-6 input identities are not unique")
    if {row["identity"] for row in nodes} != set(input_identities):
        raise AssertionError("receipt identities do not exactly cover batch-6 input")
    validate_display_paths(nodes)
    for row in nodes:
        verify_evidence(evidence_catalogue, row["evidence_refs"], reader)
        if row["confidence_percent"] < 90:
            if row["action"] not in {"review_required", "concrete_conflict"}:
                raise AssertionError(f"low-confidence action is mapped: {row['identity']}")
            if row["candidate_path"] is not None:
                raise AssertionError(f"low-confidence path is committed: {row['identity']}")

    return {
        "schema_version": 1,
        "batch": 6,
        "kind": "Captured nodes against Operator candidate",
        "non_authoritative": True,
        "native_admission": "not_performed",
        "source_migration": "not_performed",
        "captured_core_commit": CAPTURED_COMMIT,
        "candidate_sha256": candidate_sha,
        "input_sha256": file_sha256(INPUT),
        "baseline_sha256": file_sha256(BASELINE),
        "prior_review_sha256": file_sha256(DISPOSITIONS),
        "review_method": (
            "Reused each row's source-reviewed meaning and global evidence references "
            "from nodes.dispositions.json, verified every referenced Main Content quote "
            "span through nodes/support/snapshot_sources.py at the captured commit, and "
            "compared those meanings with the latest Operator-authored candidate rules. "
            "This is not a fresh exhaustive audit of all 951 source pins and does not use "
            "current Core as replacement evidence."
        ),
        "nodes": nodes,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--persist", action="store_true")
    args = parser.parse_args()
    receipt = build()
    encoded = (json.dumps(receipt, indent=2, ensure_ascii=False) + "\n").encode("utf-8")
    if OUTPUT.exists():
        existing = OUTPUT.read_bytes()
        if existing != encoded:
            raise SystemExit(f"refusing to overwrite non-identical receipt: {OUTPUT}")
        print(json.dumps({"output": str(OUTPUT), "bytes": len(encoded), "identical": True}))
        return
    if not args.persist:
        print(json.dumps({"output": str(OUTPUT), "bytes": len(encoded), "would_create": True}))
        return
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(encoded)
    print(json.dumps({"output": str(OUTPUT), "bytes": len(encoded), "created": True}))


if __name__ == "__main__":
    main()
