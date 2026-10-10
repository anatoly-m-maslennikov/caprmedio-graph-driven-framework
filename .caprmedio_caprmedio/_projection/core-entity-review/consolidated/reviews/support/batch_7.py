"""Build the batch-7 comparison receipt against the Operator candidate.

This helper is deliberately create-only: it reads the captured batch review,
the global accepted disposition ledger, and the candidate, then writes the
derived receipt only with ``--persist``.  It never changes Core or the input
reviews.
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
NODES = BASE / "nodes"
CONSOLIDATED = BASE / "consolidated"
INPUT = NODES / "inputs/nodes.batch-7.input.json"
OLD_REVIEW = NODES / "nodes.batch-7.review.json"
DISPOSITIONS = NODES / "nodes.dispositions.json"
BASELINE = BASE / "baseline.inventory.json"
CANDIDATE = BASE / "presentation/operator.entity-graph.candidate.json"
SNAPSHOT_HELPER = NODES / "support/snapshot_sources.py"
OUTPUT = CONSOLIDATED / "reviews/batch-7.review.json"

CAPTURED_COMMIT = "a971d0e00c33c779f485fc8cad63194894d440fb"
EXPECTED_CANDIDATE_SHA256 = (
    "99e7710f5ef83df2b1f3ec1ef4142547655e63bef7415266c5521380da7fa99b"
)
EXPECTED_INPUT_SHA256 = (
    "9a9188b17a1aca100515a3857e61a7499c07dd840d9672a5589e25739a1be1b6"
)
EXPECTED_BASELINE_SHA256 = (
    "bc5d99e91fb7dd4dcb42e59ff33cc24cff1d0901c5904764394c769aaa0a9430"
)
EXPECTED_OLD_REVIEW_SHA256 = (
    "190f91dccbf5e8009f2956e7c8b3cf52ca4e72b64129393b9c5a5f2b60ec28e3"
)
EXPECTED_DISPOSITIONS_SHA256 = (
    "1b9d751f95aa71486908b53b3d7f3f9825defae137be3d8792d45177587c48f8"
)


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def load(path: Path) -> Any:
    return json.loads(path.read_bytes())


def load_snapshot_module() -> Any:
    spec = importlib.util.spec_from_file_location("captured_snapshot_sources", SNAPSHOT_HELPER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SNAPSHOT_HELPER}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def evidence_refs_for(mark: dict[str, Any]) -> list[str]:
    refs = mark.get("scoped_refs", {}).get("global_evidence_refs")
    if refs is None:
        refs = mark.get("source_review", {}).get("evidence_refs", [])
    return list(refs)


def candidate_rules(root: str | None, action: str, identity: str) -> list[str]:
    if action == "syntax_context":
        return ["/terms_graph_boundary", "/entity_vs_syntax_rules"]
    if action == "review_required":
        if identity.startswith("Relation"):
            return ["/root_entities/3", "/relation_type_model", "/graph_model"]
        if identity.startswith("Scope"):
            return ["/root_entities/1", "/content_direction/scope_omission"]
        if "Carrier" in identity:
            return ["/root_entities/5", "/carrier_delivery_model"]
        return ["/root_entities/0", "/dependent_entities", "/content_direction"]
    if root == "Relation":
        return ["/root_entities/3", "/graph_model", "/relation_type_model"]
    if root == "Scope Unit":
        return [
            "/root_entities/1",
            "/entity_identity_model/scope_unit",
            "/entity_vs_syntax_rules",
        ]
    if root == "Carrier":
        return [
            "/root_entities/5",
            "/carrier_delivery_model",
            "/entity_identity_model/carrier_identity",
        ]
    if root == "Execution":
        return ["/root_entities/6", "/execution_definition_policy", "/m_e_root_question"]
    if action == "projection_view":
        return ["/projection_member_model", "/entity_representation_rules"]
    if identity in {"Runtime Journal", "Runtime Journal/Carrier"}:
        return ["/root_entities/0", "/history_model", "/carrier_delivery_model"]
    return [
        "/root_entities/0",
        "/dependent_entities",
        "/content_direction",
        "/execution_definition_policy",
    ]


def _operation_path(identity: str, role: str = "Operation") -> str:
    suffix = " ".join(identity.rsplit("/", 1)[-1].replace(":", " ").split())
    return f"Artifact/Atom.Substance.{role}.{suffix}"


def validate_candidate_path(path: str | None) -> None:
    """Keep review paths in the candidate's compact display notation.

    A slash is reserved for the one broader-to-narrower root step shown by
    the candidate (currently ``Artifact/Atom``).  Dependent fields use dots,
    and a colon is reserved for an explicit allowed value.  These are display
    checks only; no path is a native selector or relation.
    """
    if path is None:
        return
    if path.count("/") > 1:
        raise AssertionError(f"candidate display path has too many root slashes: {path}")
    if "/" in path and not path.startswith("Artifact/Atom"):
        raise AssertionError(f"candidate display path uses slash outside root narrowing: {path}")
    for forbidden in ("Substance/", "Relation/", "Scope Unit/", "Execution/"):
        if forbidden in path:
            raise AssertionError(f"candidate display path uses slash for a dependent field: {path}")
    if ":" in path:
        head = path.split(":", 1)[0]
        if "." not in head:
            raise AssertionError(f"candidate display path uses colon without a dependent field: {path}")


def map_identity(identity: str, old: dict[str, Any]) -> dict[str, Any]:
    """Return only a display proposal; no value here is a native mapping."""
    confidence = old["confidence_percent"]
    if confidence < 90:
        return {
            "action": "review_required",
            "candidate_root": None,
            "candidate_path": None,
            "content_view": "unclassified",
            "operator_rules": candidate_rules(None, "review_required", identity),
            "note": (
                "The checked source slice does not prove a candidate mapping; keep this as "
                "review work rather than asking the Operator to decide a source-proof gap."
            ),
        }

    if identity == "Root Term":
        return {
            "action": "syntax_context",
            "candidate_root": None,
            "candidate_path": None,
            "content_view": "unclassified",
            "operator_rules": candidate_rules(None, "syntax_context", identity),
            "note": (
                "Terms remain in their separate graph; Root Term is contextual graph syntax, "
                "not an eighth Entity root."
            ),
        }

    if identity in {"Relation", "Relation/authority", "Relation Kind", "Relation Kind/Metadata", "Relation Kind/registry compilation", "Rationale For Relation", "Related To Relation"}:
        if identity == "Relation Kind/registry compilation":
            return {
                "action": "projection_view",
                "candidate_root": "Relation",
                "candidate_path": "Relation.Kind.Registry Compilation",
                "content_view": "P",
                "operator_rules": candidate_rules("Relation", "projection_view", identity),
                "note": (
                    "The registry is a derived, non-authoritative compilation of Relation Kind "
                    "metadata; it is not a second Relation declaration."
                ),
            }
        return {
            "action": "retain",
            "candidate_root": "Relation",
            "candidate_path": {
                "Relation": "Relation",
                "Rationale For Relation": "Relation.Rationale For Relation",
                "Related To Relation": "Relation.Related To Relation",
                "Relation Kind": "Relation.Kind",
                "Relation Kind/Metadata": "Relation.Kind.Metadata",
                "Relation/authority": "Relation.Authority",
            }[identity],
            "content_view": {
                "Rationale For Relation": "R",
                "Related To Relation": "R",
                "Relation": "mixed",
                "Relation Kind": "mixed",
                "Relation Kind/Metadata": "mixed",
                "Relation/authority": "mixed",
            }[identity],
            "operator_rules": candidate_rules("Relation", "retain", identity),
            "note": (
                "Keep Relation facts, Relation Kinds, authority metadata, endpoints and "
                "derived provenance distinct; candidate comparison does not admit a native edge."
            ),
        }

    if identity in {"Relational Atom", "Relational Atom/Qualified Type"}:
        return {
            "action": "rebase" if identity == "Relational Atom" else "inherit",
            "candidate_root": "Artifact",
            "candidate_path": (
                "Artifact/Atom.Relational Atom"
                if identity == "Relational Atom"
                else "Artifact/Atom.Relational Atom.Qualified Type"
            ),
            "content_view": "mixed",
            "operator_rules": candidate_rules("Artifact", "rebase", identity),
            "note": (
                "Relational wording does not create a Relation root: the Atom, its qualified "
                "allowed values and its target conditions remain distinct."
            ),
        }

    if identity == "Relational Atom Classification Validation":
        return {
            "action": "operation_or_method",
            "candidate_root": "Artifact",
            "candidate_path": "Artifact/Atom.Substance.Evaluation.Relational Atom Classification Validation",
            "content_view": "E",
            "operator_rules": candidate_rules("Artifact", "operation_or_method", identity),
            "note": (
                "The captured classification check is an Evaluation specification; allowed "
                "qualified types and target conditions remain separate from Labels and from an "
                "actual Execution."
            ),
        }

    if identity == "Recurrence Protection":
        return {
            "action": "operation_or_method",
            "candidate_root": "Artifact",
            "candidate_path": "Artifact/Atom.Substance.Evaluation.Recurrence Protection",
            "content_view": "E",
            "operator_rules": candidate_rules("Artifact", "operation_or_method", identity),
            "note": (
                "The captured Evaluation meaning is a reusable check definition; it is not an "
                "actual Execution or a new root."
            ),
        }

    if identity in {
        "Runtime Journal",
        "Runtime Journal/Carrier",
    }:
        if identity == "Runtime Journal/Carrier":
            return {
                "action": "delivery_policy",
                "candidate_root": "Carrier",
                "candidate_path": "Carrier delivery policy for Runtime Journal",
                "content_view": "D",
                "operator_rules": candidate_rules("Carrier", "delivery_policy", identity),
                "note": (
                    "The D meaning is a general storage/delivery policy. It keeps Carrier ID "
                    "separate from filename/path and creates no per-Property Carrier edge."
                ),
            }
        return {
            "action": "delivery_policy",
            "candidate_root": "Artifact",
            "candidate_path": "Artifact/Atom.Journal",
            "content_view": "D",
            "operator_rules": candidate_rules("Artifact", "delivery_policy", identity),
            "note": (
                "Journal remains a record of changes and decisions; the captured D clause does "
                "not make a runtime directory or Carrier path canonical."
            ),
        }

    if identity == "Runtime State":
        return {
            "action": "retain",
            "candidate_root": "Execution",
            "candidate_path": "Execution.Runtime State",
            "content_view": "E",
            "operator_rules": candidate_rules("Execution", "retain", identity),
            "note": (
                "Runtime State is kept as an execution-state concern; it does not replace Git "
                "preservation of Atom contents or establish a new root."
            ),
        }

    if identity.startswith("Scope Expression"):
        if identity.endswith("Projection"):
            action = "projection_view"
            path = "Scope Unit.Scope Expression.Canonical Scope Signature.Projection"
            view = "P"
            note = (
                "The report is a non-authoritative Projection of a Scope Expression signature; "
                "it does not rewrite source scope or create a Relation."
            )
        elif identity.endswith("Canonical Scope Signature"):
            action = "projection_view"
            path = "Scope Unit.Scope Expression.Canonical Scope Signature"
            view = "P"
            note = (
                "The signature remains a derived comparison value, distinct from the source "
                "Scope Expression and its evaluation."
            )
        elif identity == "Scope Expression Evaluation":
            action = "operation_or_method"
            path = "Scope Unit.Scope Expression Evaluation"
            view = "M"
            note = (
                "Resolver/evaluation semantics remain a method view over Scope applicability, "
                "not a second Scope Unit."
            )
        else:
            action = "retain"
            path = "Scope Unit.Scope Expression"
            view = "mixed"
            note = (
                "The deterministic expression remains qualified applicability under a Scope "
                "Unit; its predicates and grouping are not inferred as Entity taxonomy."
            )
        return {
            "action": action,
            "candidate_root": "Scope Unit",
            "candidate_path": path,
            "content_view": view,
            "operator_rules": candidate_rules("Scope Unit", action, identity),
            "note": note,
        }

    if identity.startswith("Scope Unit"):
        suffix = identity[len("Scope Unit") :].lstrip("/")
        path = "Scope Unit" if not suffix else f"Scope Unit.{suffix}"
        if identity == "Scope Unit Graph":
            path = "Scope Unit.Graph"
            action, view = "projection_view", "P"
            note = (
                "The Scope Unit Graph is a derived view and does not replace authoritative "
                "Project Structure or declare native ancestry."
            )
        elif identity == "Scope Unit/Carrier":
            path = "Scope Unit carrier delivery policy"
            action, view = "delivery_policy", "D"
            note = (
                "Keep the Scope Unit-to-Carrier meaning distinct from concrete Carrier metadata; "
                "general D policies do not require per-Property Carrier edges."
            )
        else:
            action = "retain" if identity == "Scope Unit" else "inherit"
            view = {
                "Scope Unit": "mixed",
                "Scope Unit/Label": "mixed",
                "Scope Unit/Local Order": "mixed",
                "Scope Unit/Name": "mixed",
                "Scope Unit/Navigational Order Number": "R",
                "Scope Unit/Scope": "R",
                "Scope Unit/Structural Level": "mixed",
                "Scope Unit/Type": "mixed",
                "Scope Unit/Type: Ordered": "R",
                "Scope Unit/Type: Unordered": "R",
            }[identity]
            note = (
                "Scope Unit remains a root ownership boundary with stable `(project prefix)-SU-"
                "(number)` identity; its qualified property constraints and allowed values are "
                "retained without treating labels, folders or slash segments as new Entities."
            )
        return {
            "action": action,
            "candidate_root": "Scope Unit",
            "candidate_path": path,
            "content_view": view,
            "operator_rules": candidate_rules("Scope Unit", action, identity),
            "note": note,
        }

    if identity == "Scope Reference Validation":
        return {
            "action": "operation_or_method",
            "candidate_root": "Artifact",
            "candidate_path": "Artifact/Atom.Substance.Evaluation.Scope Reference Validation",
            "content_view": "E",
            "operator_rules": candidate_rules("Artifact", "operation_or_method", identity),
            "note": (
                "The captured fixture/acceptance meaning is an Evaluation specification; it "
                "does not transfer ownership or create Scope Unit ancestry."
            ),
        }

    if identity == "Scoped Operator-choice Applicability":
        return {
            "action": "rebase",
            "candidate_root": "Artifact",
            "candidate_path": "Artifact/Atom.Substance Scope",
            "content_view": "O",
            "operator_rules": [
                "/root_entities/0",
                "/content_direction/scope_omission",
                "/content_direction/details",
                "/entity_vs_syntax_rules",
            ],
            "note": (
                "Substance Scope is applicability, not ownership. Omission is valid only for the "
                "whole governed Subject and whole owning Scope Unit; role-required content stays."
            ),
        }

    if identity == "Single Source of Truth":
        return {
            "action": "retain",
            "candidate_root": "Artifact",
            "candidate_path": "Artifact/Atom.Single Source of Truth",
            "content_view": "mixed",
            "operator_rules": candidate_rules("Artifact", "retain", identity),
            "note": (
                "One representation per Entity instance and the projection authority boundary "
                "remain distinct from a duplicate source or a native Relation."
            ),
        }

    if identity == "Set-valued Property":
        path, action, view = "Artifact/Atom.Set-valued Property", "inherit", "M"
        note = "The set-valued property remains a dependent Entity with its membership domain preserved."
    elif identity == "Set-valued Property Membership Evaluation":
        path, action, view = (
            "Artifact/Atom.Substance.Evaluation.Set-valued Property Membership Evaluation",
            "operation_or_method",
            "M",
        )
        note = "Membership evaluation remains distinct from the set-valued Property and its allowed values."
    elif identity == "Spec Content Roles":
        path, action, view = "Artifact/Atom.Substance.Content Roles", "inherit", "mixed"
        note = (
            "Substance role labels remain qualified content views; optional general Details do not "
            "erase role/type-required content."
        )
    elif identity in {"Step Run", "Step Run/Invocation", "Step Run/Tool Call", "Step/Agentic Execution Context", "Session-State Envelope"}:
        if identity == "Step Run":
            path, action = "Execution.Step Run", "retain"
        elif identity == "Step Run/Invocation":
            path, action = "Execution.Step Run.Invocation", "inherit"
        elif identity == "Step Run/Tool Call":
            path, action = "Execution.Step Run.Tool Call", "inherit"
        elif identity == "Session-State Envelope":
            path, action = "Execution.Session-State Envelope", "inherit"
        else:
            path, action = "Execution.Step.Agentic Execution Context", "inherit"
        view = "E"
        note = (
            "An actual run/context is kept under Execution and remains distinct from its reusable "
            "Operation definition; no O Atom is required merely for an ad hoc Execution."
        )
    elif identity == "Replacement-Required Lineage Impact Disposition":
        path, action, view = (
            "Artifact/Atom.Substance.Claim.Replacement-Required Lineage Impact Disposition",
            "rebase",
            "C",
        )
        note = "The replacement/archival lineage distinction remains a Claim-level disposition, not a Revision or Execution root."
    elif identity == "Reconcile Navigation Numbers":
        path, action, view = _operation_path(identity), "operation_or_method", "O"
        note = "The bounded Action and its conformance/readiness conditions remain an Operation definition."
    elif identity == "Reconcile Unfinished Work":
        path, action, view = _operation_path(identity), "operation_or_method", "O"
        note = "Remaining-work reconciliation remains an Operation definition and does not authorize duplicate Plans or execution."
    elif identity == "Scripted Migration":
        path, action, view = _operation_path(identity), "operation_or_method", "O"
        note = "The migration occurrence retains its governed target-set and reviewable change-set constraints without extra mutation authority."
    elif identity == "Root Term":
        raise AssertionError("Root Term handled above")
    elif identity == "Runtime State":
        raise AssertionError("Runtime State handled above")
    elif identity == "Revert Changes Workflow":
        path, action, view = _operation_path(identity), "operation_or_method", "O"
        note = "The reusable Workflow definition remains separate from any actual Workflow Run."
    elif identity in {"Requirement Implementation", "Requirement Implementation Step", "Resolve Operator Priorities", "Resolve Project Initialization Inputs", "Repair RMED Review Batch", "Screen Short Names", "Select Priority-Governed Alternative", "Select RMED Review Batch", "Select Reconciliation Sources", "Source Reconciliation", "Source Reconciliation Assessment Step", "Source Reconciliation Correction Step", "Source Reconciliation Decision Step", "Source Reconciliation Proposal Step", "Source Reconciliation Publication Step", "Source Reconciliation Selection Step", "Step"}:
        path, action, view = _operation_path(identity), "operation_or_method", "O"
        note = "The captured reusable Action/Workflow/Step meaning maps to an Operation specification; any actual performance remains an Execution."
    elif identity in {"RMED Atom Review Workflow/coverage/Action: 118", "RMED Atom Review Workflow/coverage/Step: 119", "RMED Atom Review Workflow/coverage/Step: 120", "RMED Atom Review Workflow/coverage/Step: 121", "RMED Review Evaluation Step", "RMED Review Repair Step", "RMED Review Selection Step", "RMEDO Conflict Resolution"}:
        path, action = _operation_path(identity), "operation_or_method"
        view = "mixed" if identity == "RMEDO Conflict Resolution" else "O"
        note = "The numbered review workflow item remains a named dependent Operation specification; grouping does not create another root Entity."
    elif identity == "Rationale For Relation":
        raise AssertionError("Rationale For Relation handled above")
    else:
        raise AssertionError(f"no candidate mapping for {identity}")

    root = "Execution" if path == "Execution" or path.startswith("Execution.") else "Artifact"
    return {
        "action": action,
        "candidate_root": root,
        "candidate_path": path,
        "content_view": view,
        "operator_rules": candidate_rules(root, action, identity),
        "note": note,
    }


def verify_evidence(refs: list[str], catalogue: dict[str, Any], snapshot: Any) -> int:
    checked = 0
    for ref in refs:
        if ref not in catalogue:
            raise AssertionError(f"missing global evidence key: {ref}")
        item = catalogue[ref]
        pin = snapshot.source_pins()[item["atom_id"]]
        for field in ("atom_revision", "carrier_path", "carrier_sha256"):
            if item[field] != pin[field]:
                raise AssertionError(f"evidence pin mismatch ({field}): {ref}")
        raw = snapshot.read_source(item["atom_id"])
        lines = raw.decode().splitlines()
        start, end = item["start_line"], item["end_line"]
        if not (isinstance(start, int) and isinstance(end, int) and 1 <= start <= end <= len(lines)):
            raise AssertionError(f"invalid evidence span: {ref}")
        quote = "\n".join(lines[start - 1 : end])
        if item["quote"] not in (quote, quote + "\n"):
            raise AssertionError(f"captured Main Content quote mismatch: {ref}")
        if item["text_sha256"] != sha(item["quote"].encode()):
            raise AssertionError(f"evidence quote hash mismatch: {ref}")
        checked += 1
    return checked


def build() -> dict[str, Any]:
    input_raw = INPUT.read_bytes()
    old_raw = OLD_REVIEW.read_bytes()
    dispositions_raw = DISPOSITIONS.read_bytes()
    baseline_raw = BASELINE.read_bytes()
    candidate_raw = CANDIDATE.read_bytes()
    if sha(input_raw) != EXPECTED_INPUT_SHA256:
        raise AssertionError("batch-7 input changed")
    if sha(old_raw) != EXPECTED_OLD_REVIEW_SHA256:
        raise AssertionError("accepted batch-7 review changed")
    if sha(dispositions_raw) != EXPECTED_DISPOSITIONS_SHA256:
        raise AssertionError("global disposition ledger changed")
    if sha(baseline_raw) != EXPECTED_BASELINE_SHA256:
        raise AssertionError("captured baseline changed")
    if sha(candidate_raw) != EXPECTED_CANDIDATE_SHA256:
        raise AssertionError("Operator candidate changed from assigned pin")

    inp = json.loads(input_raw)
    old_review = json.loads(old_raw)
    dispositions = json.loads(dispositions_raw)
    candidate = json.loads(candidate_raw)
    if inp["batch"] != 7 or len(inp["nodes"]) != 80:
        raise AssertionError("unexpected batch-7 input coverage")
    if old_review["batch"] != 7 or len(old_review["nodes"]) != 80:
        raise AssertionError("unexpected old batch-7 coverage")
    if candidate["authority"]["adopted_core_model"] is not False:
        raise AssertionError("candidate unexpectedly claims Core adoption")

    marks = {mark["identity"]: mark for mark in dispositions["node_disposition_marks"]}
    old_rows = {row["identity"]: row for row in old_review["nodes"]}
    expected = {node["identity"] for node in inp["nodes"]}
    if set(old_rows) != expected or set(marks) & expected != expected:
        raise AssertionError("batch-7 identity coverage mismatch")

    snapshot = load_snapshot_module()
    snapshot_result = snapshot.verify_snapshot()
    if snapshot_result["verification"] != "pass" or snapshot_result["source_context"] != "captured_snapshot":
        raise AssertionError("captured snapshot verification failed")

    catalogue = dispositions["evidence_catalogue"]
    rows: list[dict[str, Any]] = []
    checked_spans = 0
    for identity in (node["identity"] for node in inp["nodes"]):
        old = old_rows[identity]
        mark = marks[identity]
        if mark["review_row"]["disposition"] != old["disposition"]:
            raise AssertionError(f"prior disposition mismatch: {identity}")
        mapping = map_identity(identity, old)
        validate_candidate_path(mapping["candidate_path"])
        refs = evidence_refs_for(mark)
        checked_spans += verify_evidence(refs, catalogue, snapshot)
        preserved = list((old.get("proposal") or {}).get("preserved_distinctions") or [])
        if old["reason"] not in preserved:
            preserved.append(old["reason"])
        preserved.append(mapping["note"])
        preserved = list(dict.fromkeys(preserved))
        if mapping["action"] == "review_required":
            question = {
                "kind": "source_gap",
                "text": (
                    "Review task (captured-evidence gap, not a new Operator design question): "
                    + (
                        old.get("question")
                        or "The checked captured Main Content does not establish a safe candidate mapping."
                    )
                    + " Keep the original identity and checked source IDs until qualifying Main Content is available."
                ),
            }
        else:
            question = None
        rows.append(
            {
                "identity": identity,
                "prior_disposition": old["disposition"],
                "action": mapping["action"],
                "candidate_root": mapping["candidate_root"],
                "candidate_path": mapping["candidate_path"],
                "content_view": mapping["content_view"],
                "confidence_percent": old["confidence_percent"],
                "reason": f"{old['reason']} Candidate comparison: {mapping['note']}",
                "operator_rules": mapping["operator_rules"],
                "evidence_refs": refs,
                "checked_source_atom_ids": old["checked_source_atom_ids"],
                "preserved_distinctions": preserved,
                "question": question,
            }
        )

    receipt = {
        "schema_version": 1,
        "batch": 7,
        "kind": "Captured nodes against Operator candidate",
        "non_authoritative": True,
        "native_admission": "not_performed",
        "source_migration": "not_performed",
        "captured_core_commit": CAPTURED_COMMIT,
        "candidate_sha256": EXPECTED_CANDIDATE_SHA256,
        "input_sha256": EXPECTED_INPUT_SHA256,
        "baseline_sha256": EXPECTED_BASELINE_SHA256,
        "prior_review_sha256": EXPECTED_DISPOSITIONS_SHA256,
        "review_method": (
            "Compared all 80 captured identities with the latest Operator candidate using the "
            "accepted batch-7 meanings and the global disposition evidence catalogue. Exact "
            "captured Main Content spans were rechecked through snapshot_sources.py against the "
            "pinned Git snapshot. Operator directions are display/proposal inputs only; this is "
            "not a fresh exhaustive audit of all 951 sources or an adoption/remapping operation."
        ),
        "nodes": rows,
    }
    return receipt


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--persist", action="store_true")
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    receipt = build()
    raw = json.dumps(receipt, ensure_ascii=False, indent=2).encode() + b"\n"
    checks = {
        "identity_count": len(receipt["nodes"]),
        "mapped_candidate_paths": sum(row["candidate_path"] is not None for row in receipt["nodes"]),
        "review_required": sum(row["action"] == "review_required" for row in receipt["nodes"]),
        "syntax_context": sum(row["action"] == "syntax_context" for row in receipt["nodes"]),
        "evidence_spans_rechecked": len({ref for row in receipt["nodes"] for ref in row["evidence_refs"]}),
        "captured_snapshot_verification": "pass",
        "native_admission": "not_performed",
        "source_migration": "not_performed",
    }
    if not args.persist:
        print(json.dumps(checks, ensure_ascii=False, sort_keys=True))
        return
    args.output.parent.mkdir(parents=True, exist_ok=True)
    if args.output.exists() and args.output.read_bytes() != raw:
        raise SystemExit(f"refusing to overwrite non-identical output: {args.output}")
    args.output.write_bytes(raw)
    print(json.dumps(checks, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
