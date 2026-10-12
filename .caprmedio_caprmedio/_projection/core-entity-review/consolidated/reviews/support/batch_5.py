"""Build the bounded batch-5 consolidated candidate review receipt.

The script is deliberately create-only.  It reuses the accepted batch-5
meanings and global evidence catalogue, verifies the quoted captured Main
Content through ``snapshot_sources.py``, and writes only the lane-owned
receipt when ``--persist`` is supplied.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[6]
PROJECTION = ROOT / ".caprmedio_caprmedio/_projection/core-entity-review"
INPUT = PROJECTION / "nodes/inputs/nodes.batch-5.input.json"
CANDIDATE = PROJECTION / "presentation/operator.entity-graph.candidate.json"
BASELINE = PROJECTION / "baseline.inventory.json"
PRIOR_REVIEW = PROJECTION / "nodes/nodes.batch-5.review.json"
DISPOSITIONS = PROJECTION / "nodes/nodes.dispositions.json"
OUTPUT = Path(__file__).resolve().parents[1] / "batch-5.review.json"
CAPTURED_COMMIT = "a971d0e00c33c779f485fc8cad63194894d440fb"
EXPECTED_CANDIDATE_SHA256 = (
    "99e7710f5ef83df2b1f3ec1ef4142547655e63bef7415266c5521380da7fa99b"
)


def sha256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _spec(
    action: str,
    root: str | None,
    path: str | None,
    rules: list[str],
    note: str,
) -> dict[str, Any]:
    return {
        "action": action,
        "candidate_root": root,
        "candidate_path": path,
        "operator_rules": rules,
        "note": note,
    }


def _group(
    target: dict[str, dict[str, Any]],
    names: list[str],
    action: str,
    root: str | None,
    path_prefix: str | None,
    rules: list[str],
    note: str,
) -> None:
    for name in names:
        if path_prefix is None:
            path = None
        elif path_prefix.endswith((".", ":")):
            path = f"{path_prefix}{name}"
        else:
            path = f"{path_prefix}/{name}"
        target[name] = _spec(action, root, path, rules, note)


def mapping() -> dict[str, dict[str, Any]]:
    """Return explicit display mappings; none of these are native admission."""

    result: dict[str, dict[str, Any]] = {}
    artifact_rules = [
        "authority.operator_confirmed_root_list",
        "root_entities[0]",
        "dependent_entities",
        "entity_identity_model.dependent_entity",
    ]
    operation_rules = [
        "authority.operator_confirmed_root_list",
        "m_e_root_question",
        "execution_definition_policy",
        "dependent_entities",
    ]
    carrier_rules = [
        "authority.operator_confirmed_root_list",
        "root_entities[5]",
        "carrier_delivery_model",
        "entity_representation_rules",
    ]
    relation_rules = [
        "authority.operator_confirmed_root_list",
        "graph_model",
        "relation_type_model",
    ]
    projection_rules = [
        "authority.operator_confirmed_root_list",
        "projection_member_model",
        "entity_vs_syntax_rules",
    ]
    syntax_rules = [
        "entity_vs_syntax_rules",
        "terms_graph_boundary",
    ]

    _group(
        result,
        ["General Artifact Graph", "Graph of Graphs"],
        "projection_view",
        None,
        None,
        projection_rules,
        "Keep this graph description as a derived display view; it does not create a new root or native edge.",
    )
    _group(
        result,
        ["General Term", "Governed Term", "Governed Term Rendering"],
        "syntax_context",
        None,
        None,
        syntax_rules,
        "Terms and their rendering remain a separate terminology/syntax context, not an eighth Entity root or an admitted cross-graph relation.",
    )
    _group(
        result,
        ["Generated-Only Provenance Validation"],
        "retain",
        None,
        None,
        artifact_rules,
        "Retain the bounded provenance-validation identity in the Evaluation view; its owner/root remains unspecified and a generated projection is not an authority.",
    )
    _group(
        result,
        ["Generator"],
        "operation_or_method",
        None,
        None,
        operation_rules,
        "Keep the Generator as a reusable construction definition in the M view; it is not an Actor root and not an actual Execution.",
    )
    _group(
        result,
        ["Global Tier", "Local Tier", "Local Order", "Label"],
        "retain",
        "Artifact",
        "Artifact/Atom.",
        artifact_rules,
        "Preserve the qualified field/value meaning and owner-specific use as a dependent field; no independent lifecycle or blanket inheritance is implied.",
    )
    _group(
        result,
        ["Goal"],
        "review_required",
        None,
        None,
        [
            "authority.operator_confirmed_root_list",
            "entity_identity_model.dependent_entity",
            "content_direction",
        ],
        "The sole exact evidence observes Active Goal visibility alongside an undeclared candidate; observation is not declaration, so no candidate owner or path is assigned. Do not conflate this captured identity with Requirement Type Goal (the RMED Claim reviewed in batch 2); no Substance Objective mapping is established, and ':' remains allowed-value notation rather than a role label.",
    )
    _group(
        result,
        ["Governance Origin", "Governed Entity"],
        "retain",
        None,
        None,
        artifact_rules,
        "Preserve each captured governance/selection meaning without assigning an unproved owner/root; a display grouping does not authorize a new subtype.",
    )
    _group(
        result,
        ["Hub", "Hub Atom"],
        "projection_view",
        None,
        None,
        projection_rules,
        "Keep the Hub or Hub Atom as navigation/projection context; headings, aliases, and derived descriptions do not create an independent Entity.",
    )
    _group(
        result,
        ["Hub/Carrier", "Hub/Carrier/Navigation Entry"],
        "delivery_policy",
        "Carrier",
        "Carrier/Hub",
        carrier_rules,
        "Preserve durable Hub navigation as a general Carrier policy and its stable-folder boundary; do not enumerate Atom Carriers or Runtime State as new entities.",
    )
    _group(
        result,
        ["IS_ALLOWED_VALUE_OF"],
        "retain",
        "Relation",
        "Relation",
        relation_rules,
        "Retain the directed allowed-value relation and each qualified value domain; repeated labels do not collapse distinct owner/value meanings.",
    )
    _group(
        result,
        ["IS_BORNE_BY"],
        "retain",
        "Relation",
        "Relation",
        relation_rules + ["carrier_delivery_model"],
        "Retain the directed bearer-to-Carrier relation as a typed relation; its derived inverse presentation is not a new primitive or root.",
    )
    _group(
        result,
        ["IS_CARRIED_BY"],
        "retain",
        "Relation",
        "Relation",
        relation_rules + ["carrier_delivery_model"],
        "Retain the generic carried-by meaning and endpoint constraints, while using general D policies instead of per-Property Carrier relation instances.",
    )
    _group(
        result,
        ["Implementation"],
        "operation_or_method",
        None,
        None,
        operation_rules,
        "Preserve observed Implementation facts separately from refactoring decisions in the M/O view; this is not an Execution root.",
    )
    _group(
        result,
        ["Implementation Binding"],
        "retain",
        "Relation",
        "Relation",
        relation_rules + ["history_model"],
        "Retain the owner-specific evaluation-to-realization binding and its revision/Journaling constraints without inventing endpoint or lifecycle changes.",
    )
    _group(
        result,
        [
            "Implementation Evaluation",
            "Implementation Evaluation Step",
            "Implementation Failure Diagnosis",
            "Implementation Failure Diagnosis Step",
            "Implementation Preparation",
            "Implementation Preparation Step",
            "Implementation Repair",
            "Implementation Repair Step",
            "Implementation Retry Control",
            "Implementation Retry Control Step",
            "Implementation Retry Limit",
            "Implementation Retry Limit/resolution",
            "Implementation Retry Limit/source",
            "Implementation Workflow",
            "Legacy Evidence and Provisional RMED Preparation",
            "Method Learning Workflow",
            "Method Lesson Drafting",
            "Method Lesson Drafting Step",
            "Migrate Atom CCE Representation",
            "Normative Atom Prose Authoring",
        ],
        "operation_or_method",
        None,
        None,
        operation_rules,
        "Keep this reusable definition, check, preparation, repair, workflow or policy in the shared M/E/O view; actual performances/checks would be separate Executions, and no new M/E root is added.",
    )
    _group(
        result,
        ["Implementation Folder"],
        "delivery_policy",
        "Carrier",
        "Carrier",
        carrier_rules,
        "Treat the folder binding as a general delivery/storage policy that selects a layout; it is not a new folder-derived Entity root.",
    )
    _group(
        result,
        ["Implementation Of Relation", "Implementation Relation", "Implementation Relation Pair"],
        "retain",
        "Relation",
        "Relation",
        relation_rules + ["history_model"],
        "Retain the captured typed relation/pair meaning and declared direction; an inverse-derived pair does not become a second primitive relation kind.",
    )
    _group(
        result,
        ["Implementation Retry Limit/Carrier"],
        "delivery_policy",
        "Carrier",
        "Carrier/Implementation Retry Limit.",
        carrier_rules,
        "Keep the selected retry-limit storage binding as a general D policy on its owning Carrier; the field is not a separate Carrier identity.",
    )
    _group(
        result,
        ["Implementation/Derivation and Actual-State Authority"],
        "projection_view",
        None,
        None,
        projection_rules + ["entity_representation_rules"],
        "Preserve the boundary between derived Implementation views and native actual-state truth; the display is non-authoritative and does not replace the source identity.",
    )
    _group(
        result,
        ["Journal"],
        "retain",
        None,
        None,
        artifact_rules + ["history_model", "applicable_methodology.decision_journal"],
        "Retain Journal as a history/decision record without inventing an owner/root; records register changes and outcomes while Git preserves Atom contents and versions.",
    )
    _group(
        result,
        ["Journal Event query"],
        "operation_or_method",
        None,
        None,
        operation_rules + ["history_model.journal_role"],
        "Treat the query as an operation definition over Journal records, not as the event itself or a new Execution instance.",
    )
    _group(
        result,
        ["Journal/Carrier", "Journal/Carrier Root"],
        "delivery_policy",
        "Carrier",
        "Carrier/Journal.",
        carrier_rules + ["history_model"],
        "Preserve append-only Journal storage and its project-root placement as general D policies; a Carrier path is storage location, not Carrier identity.",
    )
    _group(
        result,
        ["Journal/Record"],
        "retain",
        None,
        None,
        artifact_rules + ["history_model"],
        "Keep the ordered Journal Record distinct from the event or Execution it may record; append-only and historical references remain qualified.",
    )
    _group(
        result,
        ["Lineage Impact Analysis"],
        "retain",
        "Artifact",
        None,
        artifact_rules + ["content_direction", "snapshot_and_history_rules"],
        "Map the analysis to the candidate Substance Question role while retaining revision change, provenance, impact radius and fixed-point distinctions.",
    )
    _group(
        result,
        ["Lineage Impact Analysis Content"],
        "retain",
        "Artifact",
        None,
        artifact_rules + ["content_direction"],
        "Preserve the required analysis content fields and their exact Revision references as dependent content, not as a new root.",
    )
    _group(
        result,
        ["Markdown"],
        "delivery_policy",
        "Carrier",
        "Carrier/Markdown",
        carrier_rules,
        "Retain Markdown as a file-carrier delivery policy covering validity, legibility and navigation; it does not create per-field Carrier edges.",
    )
    _group(
        result,
        ["Markdown Atom Carrier"],
        "delivery_policy",
        "Carrier",
        "Carrier/Markdown Atom Carrier",
        carrier_rules,
        "Map the Markdown Atom Carrier to the Carrier root and preserve its one-representation boundary, without treating its path as identity.",
    )
    _group(
        result,
        ["Markdown Atom Carrier Validation"],
        "operation_or_method",
        None,
        None,
        operation_rules + ["carrier_delivery_model"],
        "Keep validation as an Evaluation/check definition; actual checks are Executions and the authoritative Carrier requirements remain qualified.",
    )
    _group(
        result,
        ["Markdown Atom Carrier/Main Content"],
        "delivery_policy",
        "Carrier",
        "Carrier/Markdown Atom Carrier.",
        carrier_rules + ["content_direction"],
        "Preserve Main Content as the body carried after frontmatter, including its role-specific property constraints; the slash display is not a native edge.",
    )
    _group(
        result,
        [
            "Markdown Atom Carrier/Main Content/CCE Operator",
            "Markdown Atom Carrier/Main Content/Paragraph",
        ],
        "syntax_context",
        None,
        None,
        syntax_rules,
        "Retain the captured rendering/paragraph rule as syntax context; nested headings and formatting do not create new Entity types.",
    )
    _group(
        result,
        [
            "Markdown Atom Carrier/Structure",
            "Markdown Atom Carrier/YAML Frontmatter",
            "Markdown Atom Carrier/YAML Frontmatter/Default",
            "Markdown Atom Carrier/YAML Frontmatter/Scalar",
        ],
        "delivery_policy",
        "Carrier",
        "Carrier/Markdown Atom Carrier.",
        carrier_rules,
        "Keep structure and frontmatter constraints as general Carrier policies; controlled values, defaults and prose domains remain qualified rather than becoming per-Property Carrier nodes.",
    )
    _group(
        result,
        ["Materialized Representation"],
        "delivery_policy",
        "Carrier",
        "Carrier",
        carrier_rules + ["snapshot_and_history_rules"],
        "Preserve the materialized representation's canonical-source Revision binding and deterministic regeneration/reconciliation rule as Carrier policy.",
    )
    _group(
        result,
        ["Materialized Representation/Carrier"],
        "delivery_policy",
        "Carrier",
        "Carrier/Materialized Representation.",
        carrier_rules + ["snapshot_and_history_rules"],
        "Preserve the materialized representation's canonical-source Revision binding and deterministic regeneration/reconciliation rule as Carrier policy.",
    )
    _group(
        result,
        ["Method For Relation"],
        "retain",
        "Relation",
        "Relation",
        relation_rules,
        "Retain the directed method-for relation and its owner/Requirement endpoint meanings; display nesting does not change its permitted endpoints.",
    )
    _group(
        result,
        ["Methodology"],
        "operation_or_method",
        None,
        None,
        operation_rules + ["applicable_methodology"],
        "Keep Methodology as a reusable execution-rule definition; its projected Applicable Methodology view and source collection remain distinct.",
    )
    _group(
        result,
        ["Methodology Source"],
        "projection_view",
        None,
        None,
        projection_rules + ["applicable_methodology"],
        "Keep Methodology Source as a source/projection context distinct from the compiled Applicable Methodology and its projected members.",
    )
    _group(
        result,
        ["Methodology Source/Carrier"],
        "delivery_policy",
        "Carrier",
        "Carrier/Methodology Source.",
        carrier_rules + ["applicable_methodology"],
        "Preserve the original source Carrier binding and source-fidelity requirement; a projected copy keeps source ID and Version without a new identity.",
    )
    _group(
        result,
        ["Methodology Source/Expansion Boundary", "Methodology Source/expansion mapping"],
        "projection_view",
        None,
        None,
        projection_rules + ["applicable_methodology"],
        "Retain explicit source/target/scope mapping and the no-Core-mutation boundary as projection context, not as a new native relation or subtype.",
    )
    _group(
        result,
        ["NARROWER_THAN"],
        "retain",
        "Relation",
        "Relation",
        relation_rules,
        "Retain the typed narrower-than relation with its own direction and endpoint constraints; compact slash hierarchy is only presentation.",
    )
    _group(
        result,
        ["Navigation Projection Derivation", "Navigational Order Number"],
        "projection_view",
        None,
        None,
        projection_rules,
        "Keep navigation derivation and order as non-authoritative Projection context derived from authoritative complete content; no navigation field becomes a new Entity root.",
    )
    _group(
        result,
        ["New Archived Revision Markdown Carrier Binding"],
        "delivery_policy",
        "Carrier",
        "Carrier/Archived Revision Markdown Carrier Binding",
        carrier_rules + ["snapshot_and_history_rules", "history_model"],
        "Preserve the one-Carrier archived placement rule and its Revision/history distinction; it does not make a Carrier path the Carrier identity.",
    )
    _group(
        result,
        ["Nonnegative Integer Literal"],
        "syntax_context",
        None,
        None,
        syntax_rules,
        "Retain the qualified numeric literal grammar as syntax context; a literal is not an Entity or an allowed-value domain by repetition alone.",
    )
    _group(
        result,
        ["Normative Authority Relation Pair"],
        "retain",
        "Relation",
        "Relation",
        relation_rules,
        "Retain the declared upstream relation and inverse-derived downstream view as one qualified pair, without adding a second primitive relation kind.",
    )

    # Nested source labels are not copied literally into candidate paths.  Use
    # only the candidate's slash/dot/colon display notation where the owner is
    # explicit; leave all other owners unresolved rather than inventing one.
    result["Lineage Impact Analysis"]["candidate_path"] = (
        "Artifact/Atom.Substance:Question"
    )
    result["Lineage Impact Analysis Content"]["candidate_path"] = (
        "Artifact/Atom.Substance:Question.Content"
    )
    result["Hub/Carrier"]["candidate_path"] = "Carrier/Hub"
    result["Hub/Carrier/Navigation Entry"]["candidate_path"] = (
        "Carrier/Hub.Navigation Entry"
    )
    result["Implementation Retry Limit/Carrier"]["candidate_path"] = (
        "Carrier/Implementation Retry Limit.Carrier"
    )
    result["Journal/Carrier"]["candidate_path"] = "Carrier/Journal.Carrier"
    result["Journal/Carrier Root"]["candidate_path"] = "Carrier/Journal.Root"
    result["Markdown Atom Carrier/Main Content"]["candidate_path"] = (
        "Carrier/Markdown Atom Carrier.Main Content"
    )
    result["Markdown"]["candidate_path"] = "Carrier/Markdown"
    result["Markdown Atom Carrier"]["candidate_path"] = (
        "Carrier/Markdown Atom Carrier"
    )
    result["Markdown Atom Carrier/Structure"]["candidate_path"] = (
        "Carrier/Markdown Atom Carrier.Structure"
    )
    result["Markdown Atom Carrier/YAML Frontmatter"]["candidate_path"] = (
        "Carrier/Markdown Atom Carrier.YAML Frontmatter"
    )
    result["Markdown Atom Carrier/YAML Frontmatter/Default"]["candidate_path"] = (
        "Carrier/Markdown Atom Carrier.YAML Frontmatter.Default"
    )
    result["Markdown Atom Carrier/YAML Frontmatter/Scalar"]["candidate_path"] = (
        "Carrier/Markdown Atom Carrier.YAML Frontmatter.Scalar"
    )
    result["Materialized Representation/Carrier"]["candidate_path"] = (
        "Carrier/Materialized Representation.Carrier"
    )
    result["Methodology Source/Carrier"]["candidate_path"] = (
        "Carrier/Methodology Source.Carrier"
    )
    result["New Archived Revision Markdown Carrier Binding"]["candidate_path"] = (
        "Carrier/New Archived Revision Markdown Carrier Binding"
    )

    return result


def _role_view(atom_ids: list[str]) -> str:
    roles: set[str] = set()
    for atom_id in atom_ids:
        match = re.match(r"CA-([RDMEO])-", atom_id)
        if match:
            roles.add(match.group(1))
        elif atom_id.startswith("CAPRMEDIO-GOV-EVAL-"):
            roles.add("E")
    if not roles:
        return "unclassified"
    if len(roles) == 1:
        return next(iter(roles))
    return "mixed"


def _verify_used_evidence(
    dispositions: dict[str, Any],
    refs: set[str],
    snapshot_sources: Any,
) -> None:
    catalogue = dispositions["evidence_catalogue"]
    for ref in sorted(refs):
        if ref not in catalogue:
            raise AssertionError(f"evidence ref is not global: {ref}")
        entry = catalogue[ref]
        quote = entry["quote"]
        if sha256(quote.encode("utf-8")) != entry["text_sha256"]:
            raise AssertionError(f"evidence text hash mismatch: {ref}")
        raw = snapshot_sources.read_source(entry["atom_id"])
        lines = raw.decode("utf-8").splitlines()
        actual = "\n".join(lines[entry["start_line"] - 1 : entry["end_line"]])
        if actual != quote:
            raise AssertionError(f"captured quote mismatch: {ref}")


def build() -> tuple[dict[str, Any], dict[str, int]]:
    candidate_raw = CANDIDATE.read_bytes()
    candidate_sha = sha256(candidate_raw)
    if candidate_sha != EXPECTED_CANDIDATE_SHA256:
        raise AssertionError(
            f"candidate SHA changed: expected {EXPECTED_CANDIDATE_SHA256}, got {candidate_sha}"
        )

    # Import the required read-only captured-source helper only after all paths
    # are resolved.  It reads Git history and does not copy or mutate sources.
    import importlib.util

    helper_path = PROJECTION / "nodes/support/snapshot_sources.py"
    spec = importlib.util.spec_from_file_location("snapshot_sources", helper_path)
    if spec is None or spec.loader is None:
        raise AssertionError(f"cannot load {helper_path}")
    snapshot_sources = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(snapshot_sources)
    snapshot_result = snapshot_sources.verify_snapshot()
    if snapshot_result["git_commit"] != CAPTURED_COMMIT:
        raise AssertionError("captured commit changed")

    input_data = read_json(INPUT)
    prior_data = read_json(PRIOR_REVIEW)
    dispositions = read_json(DISPOSITIONS)
    candidate = json.loads(candidate_raw)
    del candidate  # The hash and operator paths are the relevant inputs here.

    input_nodes = input_data["nodes"]
    prior_nodes = {node["identity"]: node for node in prior_data["nodes"]}
    marks = {
        mark["identity"]: mark
        for mark in dispositions["node_disposition_marks"]
        if mark["scoped_refs"]["batch"] == 5
    }
    specs = mapping()
    identities = [node["identity"] for node in input_nodes]
    if len(identities) != 80 or len(set(identities)) != 80:
        raise AssertionError("batch-5 input identity coverage changed")
    if set(identities) != set(prior_nodes) or set(identities) != set(marks):
        raise AssertionError("batch-5 input/prior/disposition identities differ")
    if set(identities) != set(specs):
        missing = sorted(set(identities) - set(specs))
        extra = sorted(set(specs) - set(identities))
        raise AssertionError(f"mapping coverage mismatch; missing={missing}, extra={extra}")

    refs = {
        ref
        for mark in marks.values()
        for ref in mark["scoped_refs"]["global_evidence_refs"]
    }
    _verify_used_evidence(dispositions, refs, snapshot_sources)

    nodes: list[dict[str, Any]] = []
    for source_node in input_nodes:
        identity = source_node["identity"]
        mark = marks[identity]
        prior = prior_nodes[identity]
        review_row = mark["review_row"]
        candidate_spec = specs[identity]
        checked = list(mark["source_review"]["checked_source_atom_ids"])
        old_proposal = prior.get("proposal") or {}
        meanings = list(old_proposal.get("preserved_distinctions") or [])
        if not meanings:
            meanings = [
                f"Captured Main Content supports the bounded original identity {identity!r}; no same-referent replacement was proved."
            ]
        meanings.append(candidate_spec["note"])
        old_reason = review_row.get("reason", "")
        reason = (
            f"{identity}: {candidate_spec['note']} "
            f"The accepted captured-snapshot review checked {', '.join(checked)} "
            f"and retained its prior bounded meaning: {old_reason}"
        )
        confidence = min(int(review_row["confidence_percent"]), 95)
        if candidate_spec["action"] in {"review_required", "concrete_conflict"}:
            confidence = min(confidence, 89)
        nodes.append(
            {
                "identity": identity,
                "prior_disposition": review_row["disposition"],
                "action": candidate_spec["action"],
                "candidate_root": candidate_spec["candidate_root"],
                "candidate_path": candidate_spec["candidate_path"],
                "content_view": _role_view(checked),
                "confidence_percent": confidence,
                "reason": reason,
                "operator_rules": candidate_spec["operator_rules"],
                "evidence_refs": mark["scoped_refs"]["global_evidence_refs"],
                "checked_source_atom_ids": checked,
                "preserved_distinctions": meanings,
                "question": None,
            }
        )

    action_counts = Counter(node["action"] for node in nodes)
    root_counts = Counter(node["candidate_root"] or "context/unresolved" for node in nodes)
    receipt = {
        "schema_version": 1,
        "source_task": input_data["source_task"],
        "batch": input_data["batch"],
        "kind": "Captured nodes against Operator candidate",
        "non_authoritative": True,
        "native_admission": "not_performed",
        "source_migration": "not_performed",
        "captured_core_commit": CAPTURED_COMMIT,
        "candidate_sha256": candidate_sha,
        "input_sha256": sha256(INPUT.read_bytes()),
        "baseline_sha256": sha256(BASELINE.read_bytes()),
        # This field names the accepted global disposition ledger used for
        # prior meanings/evidence, not the superseded per-batch receipt.
        "prior_review_sha256": sha256(DISPOSITIONS.read_bytes()),
        "review_method": (
            "Compared each captured batch-5 identity with the latest Operator-authored candidate "
            "using the accepted prior meanings and global evidence keys from nodes.dispositions.json. "
            "Quoted Main Content was rechecked through snapshot_sources.py against the captured Git "
            "snapshot; this is not a fresh exhaustive audit of all 951 source pins or all source "
            "candidates. Display paths are proposals only: no Core admission, source migration, "
            "pin refresh, or native relation rewrite was performed."
        ),
        "nodes": nodes,
    }
    return receipt, {
        "nodes": len(nodes),
        "evidence_refs": len(refs),
        "source_atoms": len(
            {
                dispositions["evidence_catalogue"][ref]["atom_id"]
                for ref in refs
            }
        ),
        "actions": dict(sorted(action_counts.items())),
        "roots": dict(sorted(root_counts.items())),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--persist", action="store_true")
    args = parser.parse_args()
    receipt, counts = build()
    encoded = (json.dumps(receipt, indent=2, ensure_ascii=False) + "\n").encode("utf-8")
    if args.persist:
        if OUTPUT.exists():
            if OUTPUT.read_bytes() != encoded:
                raise SystemExit(f"refusing to overwrite non-identical output: {OUTPUT}")
            status = "byte-identical-existing"
        else:
            OUTPUT.write_bytes(encoded)
            status = "created"
    else:
        status = "dry-run"
    print(json.dumps({"status": status, "output": str(OUTPUT), **counts}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
