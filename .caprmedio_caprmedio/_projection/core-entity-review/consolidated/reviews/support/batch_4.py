"""Create-only batch-4 comparison of captured identities with the Operator candidate.

The batch review is derived from the accepted captured-snapshot rows and the
global evidence catalogue.  It does not read or modify current Core and does
not perform native admission or source migration.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any


ROOT = Path.cwd().resolve()
BASE = ROOT / ".caprmedio_caprmedio/_projection/core-entity-review"
NODES = BASE / "nodes"
CONSOLIDATED = BASE / "consolidated"
INPUT = NODES / "inputs/nodes.batch-4.input.json"
BASELINE = BASE / "baseline.inventory.json"
OLD_REVIEW = NODES / "nodes.batch-4.review.json"
DISPOSITIONS = NODES / "nodes.dispositions.json"
CANDIDATE = BASE / "presentation/operator.entity-graph.candidate.json"
OUTPUT = CONSOLIDATED / "reviews/batch-4.review.json"
SNAPSHOT_SOURCES = NODES / "support/snapshot_sources.py"

EXPECTED_CANDIDATE_SHA256 = "99e7710f5ef83df2b1f3ec1ef4142547655e63bef7415266c5521380da7fa99b"
EXPECTED_DISPOSITIONS_SHA256 = "1b9d751f95aa71486908b53b3d7f3f9825defae137be3d8792d45177587c48f8"
CAPTURED_COMMIT = "a971d0e00c33c779f485fc8cad63194894d440fb"
ROOT_ENTITIES = {
    "Artifact",
    "Scope Unit",
    "Actor",
    "Relation",
    "Revision",
    "Carrier",
    "Execution",
}
ALLOWED_ACTIONS = {
    "retain",
    "rebase",
    "inherit",
    "delivery_policy",
    "operation_or_method",
    "projection_view",
    "syntax_context",
    "drop_candidate",
    "review_required",
    "concrete_conflict",
}
ALLOWED_VIEWS = {"R", "M", "E", "D", "O", "P", "C", "A", "mixed", "unclassified"}

RELATION_IDENTITIES = {
    "Containment Relation Pair",
    "DEPENDS_ON",
    "DERIVED_FROM",
    "GOVERNS",
}
OPERATION_IDENTITIES = {
    "Corrective Method Acceptance",
    "Corrective Method Acceptance Step",
    "Entities Graph Construction Step",
    "Evaluate RMED Review Batch",
    "Evaluation Implementation",
    "Evaluation Implementation Step",
    "Evaluator Evidence Calibration",
    "Framework Instance Settings Validation",
    "Framework Instance Settings/parameter resolution",
    "Framework Instance Settings/parameter resolution validation",
}
CARRIER_ROOT_IDENTITIES = {
    "Directory Carrier",
    "File Carrier",
    "Framework-Owned Carrier",
}
CARRIER_POLICY_PREFIXES = (
    "Default Settings/Carrier",
    "Directory Carrier/",
    "Entity/Carrier",
    "File Carrier/",
    "Framework Instance Settings/Authoritative Carrier",
    "Framework Instance Settings/Carrier",
)


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def load_snapshot_module():
    spec = importlib.util.spec_from_file_location("batch4_snapshot_sources", SNAPSHOT_SOURCES)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SNAPSHOT_SOURCES}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def source_code(node: dict[str, Any]) -> str:
    ids = node.get("governing_source_atom_ids") or node.get("source_atom_ids")
    codes = {
        atom_id.split("-", 2)[1]
        for atom_id in ids
        if atom_id.startswith("CA-") and len(atom_id.split("-", 2)) == 3
    }
    return next(iter(codes)) if len(codes) == 1 else ("mixed" if codes else "unclassified")


def is_carrier_policy(identity: str) -> bool:
    return identity.endswith("/Carrier") or any(identity.startswith(prefix) for prefix in CARRIER_POLICY_PREFIXES)


def owner_field(identity: str) -> str:
    """Keep the captured owner and field visible while generalizing D policy."""
    parts = identity.split("/")
    if len(parts) == 1:
        return identity
    return f"{parts[0]}.{'.'.join(parts[1:])}"


def mapping(identity: str) -> dict[str, Any]:
    """Return only a display comparison; no value here is native admission."""
    if identity in RELATION_IDENTITIES:
        if identity == "Containment Relation Pair":
            path = "Relation/CONTAINS + Relation/IS_CONTAINED_BY"
        else:
            path = f"Relation/{identity}"
        return {
            "action": "retain",
            "candidate_root": "Relation",
            "candidate_path": path,
            "operator_rules": ["/root_entities/3", "/graph_model", "/relation_type_model"],
            "mapping_reason": "The captured identity is compared as a typed Relation; direction and endpoint meaning remain distinct, and the display path does not admit a native relation.",
            "distinctions": [
                "Typed relation direction, endpoints and qualified meaning remain distinct.",
                "Candidate display notation does not itself create or admit a native Relation.",
            ],
        }
    if identity in OPERATION_IDENTITIES:
        operation_label = identity.replace("/", ".")
        return {
            "action": "operation_or_method",
            "candidate_root": "Artifact",
            "candidate_path": f"Artifact/Atom.Substance.Operation.{operation_label}",
            "operator_rules": ["/root_entities/0", "/content_direction/role_labels/Operations", "/execution_definition_policy", "/root_entities/6"],
            "mapping_reason": "The captured identity is compared as an Operation or method definition under the Artifact content model; no actual run is inferred.",
            "distinctions": [
                "A reusable Operation or method definition remains distinct from an actual Execution; no Execution instance is inferred.",
                "Substance Scope expresses applicability to the whole governed Subject and owning Scope Unit, not ownership of either.",
            ],
        }
    if identity == "Extension":
        return {
            "action": "projection_view",
            "candidate_root": "Artifact",
            "candidate_path": "Artifact/Applicable Methodology/Extension",
            "operator_rules": ["/applicable_methodology", "/projection_member_model", "/entity_representation_rules"],
            "mapping_reason": "The captured Extension is compared within the derived Applicable Methodology view while preserving source authority and one-to-one projection provenance.",
            "distinctions": [
                "Extension source authority remains distinct from the derived Applicable Methodology Projection.",
                "One projected Atom maps to one source Atom with its source ID, version and relative source link; no second authority is created.",
            ],
        }
    if identity in CARRIER_ROOT_IDENTITIES:
        return {
            "action": "retain",
            "candidate_root": "Carrier",
            "candidate_path": f"Carrier/{identity}",
            "operator_rules": ["/root_entities/5", "/entity_identity_model/carrier_identity", "/carrier_delivery_model"],
            "mapping_reason": "The captured identity is retained as a Carrier kind under the separate Carrier root; its locator is not treated as its identity.",
            "distinctions": [
                "Carrier ID is separate from filename or full path; a path is a storage locator, not Carrier identity.",
                "Carrier remains a separate root Entity and is not reduced to a Property.",
            ],
        }
    if is_carrier_policy(identity):
        return {
            "action": "delivery_policy",
            "candidate_root": "Carrier",
            "candidate_path": "Carrier",
            "operator_rules": ["/root_entities/5", "/entity_identity_model/carrier_identity", "/carrier_delivery_model"],
            "mapping_reason": "The captured field or binding meaning is compared as a general Core D delivery policy; no per-Property Carrier registration is carried into the candidate display.",
            "distinctions": [
                "Carrier ID remains separate from filename or full path; the locator is not Carrier identity.",
                f"The captured owner and field remain distinct as {owner_field(identity)}; the general policy comparison does not erase that owner/field qualification.",
                "General Core D field mappings may cover multiple Entities; no per-property Carrier Relation Type, Carrier edge registry, or D Atom is inferred.",
            ],
        }
    if identity == "Dependent Entity":
        return {
            "action": "inherit",
            "candidate_root": "Artifact",
            "candidate_path": "Artifact.Dependent Entity",
            "operator_rules": ["/root_entities/0", "/dependent_entities", "/entity_vs_syntax_rules"],
            "mapping_reason": "The captured dependent-entity meaning is displayed inside the Artifact model and inherits the owning Artifact lifecycle; it does not receive an independent lifecycle or Carrier.",
            "distinctions": [
                "Inheritance applies common Artifact obligations, not another Entity's concrete Carrier.",
                "The dependent Entity keeps its immediate bearer requirement and does not become a separate root.",
            ],
        }
    if identity == "Entity":
        return {
            "action": "syntax_context",
            "candidate_root": None,
            "candidate_path": None,
            "operator_rules": ["/root_entities", "/entity_vs_syntax_rules"],
            "mapping_reason": "The captured generic Entity identity is retained as contextual vocabulary; the seven candidate roots are Entity kinds and Entity itself is not asserted to be Artifact-contained.",
            "distinctions": [
                "The seven-root candidate boundary is preserved; generic Entity vocabulary does not add another root or Artifact ownership.",
                "A heading, alias or display grouping is not itself a new Entity or native relation.",
            ],
        }
    if identity == "Current-scope Atom":
        return {
            "action": "retain",
            "candidate_root": "Artifact",
            "candidate_path": "Artifact/Atom",
            "operator_rules": ["/root_entities/0", "/entity_identity_model/scope_unit", "/entity_vs_syntax_rules"],
            "mapping_reason": "The captured qualification is retained on the candidate Atom kind; Current-scope Atom is not asserted to be a separate dependent Entity or Carrier identity.",
            "distinctions": [
                "Scope Unit identity remains stable as (project prefix)-SU-(number); current-scope qualification is not a Carrier path or ownership rewrite.",
                "Current-scope Atom is an Atom kind; the qualifier does not create another dependent Entity or a new root.",
            ],
        }
    if identity == "Entity/Identity":
        return {
            "action": "syntax_context",
            "candidate_root": None,
            "candidate_path": None,
            "operator_rules": ["/root_entities", "/entity_vs_syntax_rules", "/entity_identity_model/dependent_entity"],
            "mapping_reason": "The captured Entity identity vocabulary is retained without asserting that Entity or its identity field is an Artifact-contained dependent Entity.",
            "distinctions": [
                "Entity vocabulary is contextual here; the seven candidate roots remain the only asserted root Entity kinds.",
                "Changing Carrier format or extension does not establish an Entity identity change; that distinction remains captured without a native property path.",
            ],
        }
    if identity == "Default Settings":
        return {
            "action": "retain",
            "candidate_root": "Artifact",
            "candidate_path": "Artifact (Default Settings)",
            "operator_rules": ["/root_entities/0", "/entity_representation_rules", "/carrier_delivery_model"],
            "mapping_reason": "Captured Main Content identifies Default Settings as an Artifact; the comparison retains that exact kind without asserting an unsupported narrower or dependent path.",
            "distinctions": [
                "Default Settings remains a distinct Artifact identity containing reusable baseline values, not Project initialization inputs or explicit selections.",
                "Its Carrier and field conventions remain general D policy comparisons; the Artifact identity is not replaced by a storage path.",
            ],
        }
    if identity == "Framework Instance Settings":
        return {
            "action": "retain",
            "candidate_root": "Artifact",
            "candidate_path": "Artifact (Framework Instance Settings)",
            "operator_rules": ["/root_entities/0", "/entity_representation_rules", "/carrier_delivery_model"],
            "mapping_reason": "Captured Main Content identifies Framework Instance Settings as an authoritative Artifact; the comparison retains that kind without asserting an unsupported narrower or dependent path.",
            "distinctions": [
                "Framework Instance Settings remains an authoritative Artifact for explicit instance choices, distinct from Project initialization inputs and Project Structure.",
                "Its Carrier and field conventions remain general D policy comparisons; the Artifact identity is not replaced by a storage path.",
            ],
        }
    if identity.startswith("Framework Instance Settings/"):
        field_path = identity.replace("/", ".")
        return {
            "action": "retain",
            "candidate_root": "Artifact",
            "candidate_path": f"Artifact ({field_path})",
            "operator_rules": ["/root_entities/0", "/dependent_entities", "/entity_vs_syntax_rules", "/content_direction/details"],
            "mapping_reason": "The captured settings field is compared with dot notation as a dependent field of the named Framework Instance Settings Artifact; slash hierarchy is not treated as narrower-than here.",
            "distinctions": [
                f"The owner and field remain distinct as {field_path}; dot notation indicates bearer-to-property presentation, not a new root or subtype admission.",
                "Qualified allowed values and field-specific constraints remain preserved; no separate lifecycle or per-property Carrier registration is inferred.",
            ],
        }
    raise AssertionError(f"no explicit candidate comparison mapping for positive identity: {identity}")


def verify_evidence(item: dict[str, Any], snapshot: Any) -> None:
    pins = snapshot.source_pins()
    atom_id = item["atom_id"]
    pin = pins[atom_id]
    for field in ("atom_revision", "carrier_path", "carrier_sha256"):
        if item[field] != pin[field]:
            raise AssertionError((item["evidence_ref"], field))
    raw = snapshot.read_source(atom_id)
    if sha(raw) != pin["carrier_sha256"]:
        raise AssertionError((item["evidence_ref"], "captured source hash"))
    lines = raw.decode().splitlines()
    start, end = item["start_line"], item["end_line"]
    if not (isinstance(start, int) and isinstance(end, int) and 1 <= start <= end <= len(lines)):
        raise AssertionError((item["evidence_ref"], "line span"))
    quote = "\n".join(lines[start - 1 : end])
    if item["quote"] not in (quote, quote + "\n"):
        raise AssertionError((item["evidence_ref"], "quote"))
    if item["text_sha256"] != sha(item["quote"].encode()):
        raise AssertionError((item["evidence_ref"], "quote hash"))
    frontmatter_end = next(i for i, line in enumerate(lines[1:], 2) if line == "---")
    if start <= frontmatter_end:
        raise AssertionError((item["evidence_ref"], "frontmatter evidence"))
    headings = [line for line in lines[:start] if line.startswith(("# ", "## ", "### "))]
    if not headings or headings[-1].startswith("# Summary"):
        raise AssertionError((item["evidence_ref"], "non-substantive evidence"))


def make_row(node: dict[str, Any], old: dict[str, Any], global_catalogue: dict[str, Any]) -> dict[str, Any]:
    identity = node["identity"]
    old_refs = list(old.get("evidence_refs", []))
    global_refs = [f"CA-P-1932/batch-4/{ref}" for ref in old_refs]
    for ref in global_refs:
        if ref not in global_catalogue:
            raise AssertionError((identity, ref, "missing global evidence"))
    if old["confidence_percent"] < 90 or old["disposition"] == "question":
        return {
            "identity": identity,
            "prior_disposition": old["disposition"],
            "action": "review_required",
            "candidate_root": None,
            "candidate_path": None,
            "content_view": "unclassified",
            "confidence_percent": old["confidence_percent"],
            "reason": f"{old['reason']} Latest candidate rules were checked for a seven-root comparison, but the missing captured definition leaves this identity in review backlog; no mapping is committed.",
            "operator_rules": [],
            "evidence_refs": global_refs,
            "checked_source_atom_ids": old["checked_source_atom_ids"],
            "preserved_distinctions": [
                identity,
                "Original identity is preserved; missing source evidence is not treated as deletion, duplication, or permission to invent a root kind.",
            ],
            "question": {
                "kind": "source_gap",
                "text": f"{old['question']} This is a captured-evidence gap, not a new Operator design question; provide a qualifying Main Content assertion before assigning a candidate mapping.",
            },
        }
    plan = mapping(identity)
    reason = f"{old['reason']} Candidate comparison: {plan['mapping_reason']}"
    distinctions = [identity, *plan["distinctions"]]
    if identity.startswith("Directory Carrier"):
        distinctions.append("Scope Unit naming retains the permanent (project prefix)-SU-(number) prefix; Label and Name are changeable suffixes and project-root folders remain unchanged.")
    if identity.startswith("Framework Instance Settings") and "/parameter resolution" in identity:
        distinctions.append("Parameter resolution remains per-parameter: explicit values win, valid false/0/empty values stay explicit, and inherited defaults are not copied back as authored selections.")
    if identity.endswith("reporting mode: silent") or identity.endswith("reporting mode: verbose"):
        distinctions.append("The reporting-mode allowed domain remains qualified as silent or verbose; reporting mode changes presentation only, not authorization or safety behavior.")
    return {
        "identity": identity,
        "prior_disposition": old["disposition"],
        "action": plan["action"],
        "candidate_root": plan["candidate_root"],
        "candidate_path": plan["candidate_path"],
        "content_view": source_code(node),
        "confidence_percent": old["confidence_percent"],
        "reason": reason,
        "operator_rules": plan["operator_rules"],
        "evidence_refs": global_refs,
        "checked_source_atom_ids": old["checked_source_atom_ids"],
        "preserved_distinctions": distinctions,
        "question": None,
    }


def build() -> dict[str, Any]:
    if ROOT.name != "caprmedio-graph-driven-framework":
        raise RuntimeError(f"unexpected execution cwd: {ROOT}")
    input_raw = INPUT.read_bytes()
    baseline_raw = BASELINE.read_bytes()
    old_review_raw = OLD_REVIEW.read_bytes()
    dispositions_raw = DISPOSITIONS.read_bytes()
    candidate_raw = CANDIDATE.read_bytes()
    if sha(candidate_raw) != EXPECTED_CANDIDATE_SHA256:
        raise AssertionError("latest Operator candidate SHA mismatch")
    if sha(dispositions_raw) != EXPECTED_DISPOSITIONS_SHA256:
        raise AssertionError("accepted dispositions packet SHA mismatch")
    packet = json.loads(input_raw)
    baseline = json.loads(baseline_raw)
    candidate = json.loads(candidate_raw)
    dispositions = json.loads(dispositions_raw)
    old_review = json.loads(old_review_raw)
    if packet["batch"] != 4 or packet["identity_count"] != 81:
        raise AssertionError("unexpected batch-4 packet")
    if old_review["batch"] != 4 or old_review["source_task"] != packet["source_task"]:
        raise AssertionError("old review binding mismatch")
    if old_review["input_file_sha256"] != sha(input_raw) or old_review["partition_sha256"] != packet["partition_sha256"]:
        raise AssertionError("old review input binding mismatch")
    if baseline["inventory_sha256"] != packet["baseline"]["inventory_sha256"]:
        raise AssertionError("baseline inventory binding mismatch")
    all_marks = {mark["identity"]: mark for mark in dispositions["node_disposition_marks"]}
    input_by_identity = {node["identity"]: node for node in packet["nodes"]}
    old_by_identity = {row["identity"]: row for row in old_review["nodes"]}
    mark_by_identity = {identity: all_marks[identity] for identity in input_by_identity}
    if set(input_by_identity) != set(mark_by_identity) or set(input_by_identity) != set(old_by_identity):
        raise AssertionError("batch-4 identity coverage mismatch")
    global_catalogue = dispositions["evidence_catalogue"]
    if not isinstance(global_catalogue, dict):
        raise AssertionError("global evidence catalogue must be a mapping")
    snapshot = load_snapshot_module()
    for ref, item in global_catalogue.items():
        if ref.startswith("CA-P-1932/batch-4/"):
            verify_evidence(item, snapshot)
    for node in packet["nodes"]:
        old = mark_by_identity[node["identity"]]["review_row"]
        if old != old_by_identity[node["identity"]]:
            raise AssertionError((node["identity"], "accepted row mismatch"))
    rows = [make_row(node, mark_by_identity[node["identity"]]["review_row"], global_catalogue) for node in packet["nodes"]]
    if len(rows) != 81 or len({row["identity"] for row in rows}) != 81:
        raise AssertionError("exact batch-4 output coverage required")
    for row in rows:
        if row["action"] not in ALLOWED_ACTIONS:
            raise AssertionError((row["identity"], row["action"]))
        if row["candidate_root"] is not None and row["candidate_root"] not in ROOT_ENTITIES:
            raise AssertionError((row["identity"], row["candidate_root"]))
        if row["content_view"] not in ALLOWED_VIEWS:
            raise AssertionError((row["identity"], row["content_view"]))
        if row["confidence_percent"] < 90 and row["candidate_path"] is not None:
            raise AssertionError((row["identity"], "low-confidence mapping"))
        if row["action"] in {"review_required", "concrete_conflict"} and row["candidate_path"] is not None:
            raise AssertionError((row["identity"], "unresolved mapping"))
        if row["candidate_path"] is not None and row["candidate_root"] is None:
            raise AssertionError((row["identity"], "path without root"))
    return {
        "schema_version": 1,
        "batch": 4,
        "kind": "Captured nodes against Operator candidate",
        "non_authoritative": True,
        "native_admission": "not_performed",
        "source_migration": "not_performed",
        "captured_core_commit": CAPTURED_COMMIT,
        "candidate_sha256": sha(candidate_raw),
        "input_sha256": sha(input_raw),
        "baseline_sha256": sha(baseline_raw),
        "prior_review_sha256": sha(dispositions_raw),
        "review_method": "Compared the accepted batch-4 row meanings from nodes.dispositions.json with the latest Operator candidate; reused only its global evidence keys and verified their quoted Main Content spans through nodes/support/snapshot_sources.py at the captured snapshot. This is a bounded batch review, not a fresh exhaustive audit of all 951 source pins; no live Core refresh, native admission, or source migration was performed.",
        "nodes": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.write and args.check:
        raise SystemExit("choose --write or --check")
    if args.write:
        result = build()
        raw = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
        if OUTPUT.exists():
            if OUTPUT.read_text() != raw:
                raise RuntimeError(f"create-only output exists with different bytes: {OUTPUT}")
        else:
            OUTPUT.parent.mkdir(parents=True, exist_ok=True)
            OUTPUT.write_text(raw)
        print(json.dumps({"output": str(OUTPUT), "sha256": sha(raw.encode()), "identities": len(result["nodes"])}, sort_keys=True))
        return
    if args.check:
        expected = build()
        if not OUTPUT.exists():
            raise FileNotFoundError(OUTPUT)
        actual = json.loads(OUTPUT.read_text())
        if actual != expected:
            raise AssertionError("consolidated batch-4 output differs from deterministic rebuild")
        print(json.dumps({"output": str(OUTPUT), "sha256": sha(OUTPUT.read_bytes()), "identities": len(actual["nodes"]), "verification": "pass"}, sort_keys=True))
        return
    parser.error("use --write or --check")


if __name__ == "__main__":
    main()
