"""Create/check the bounded Batch 2 consolidated candidate review.

The script reads the accepted global disposition ledger only as historical
evidence.  It validates every carried evidence quote against the selected
captured snapshot before producing the derived review.  It never reads current
Core, changes a pin, or makes a native admission.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[6]
REVIEW_ROOT = ROOT / ".caprmedio_caprmedio/_projection/core-entity-review"
NODES = REVIEW_ROOT / "nodes"
INPUT = NODES / "inputs/nodes.batch-2.input.json"
CANDIDATE = REVIEW_ROOT / "presentation/operator.entity-graph.candidate.json"
BASELINE = REVIEW_ROOT / "baseline.inventory.json"
LEDGER = NODES / "nodes.dispositions.json"
OUTPUT = REVIEW_ROOT / "consolidated/reviews/batch-2.review.json"
EXPECTED_CANDIDATE_SHA256 = "99e7710f5ef83df2b1f3ec1ef4142547655e63bef7415266c5521380da7fa99b"

sys.path.insert(0, str(NODES / "support"))
from snapshot_sources import COMMIT, read_source  # noqa: E402


def sha256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def source_text_for_evidence(item: dict[str, Any]) -> None:
    """Verify the exact global quote is captured Main Content, byte-for-byte."""

    raw = read_source(item["atom_id"])
    if sha256(raw) != item["carrier_sha256"]:
        raise AssertionError(f"captured carrier pin changed: {item['atom_id']}")
    lines = raw.decode("utf-8").splitlines()
    start, end = item["start_line"], item["end_line"]
    if not (1 <= start <= end <= len(lines)):
        raise AssertionError(f"invalid evidence span: {item['atom_id']}")
    exact = "\n".join(lines[start - 1 : end])
    if exact != item["quote"] or sha256(exact.encode("utf-8")) != item["text_sha256"]:
        raise AssertionError(f"captured quote mismatch: {item['atom_id']}:{start}-{end}")
    # Quotes used for meaning may not be frontmatter-only evidence.
    if lines and lines[0].strip() == "---":
        frontmatter_end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
        if frontmatter_end is None or start <= frontmatter_end + 1:
            raise AssertionError(f"non-Main-Content evidence: {item['atom_id']}:{start}-{end}")


def inherited(identity: str, root: str, path: str, view: str, rules: list[str], preserved: list[str], reason: str) -> dict[str, Any]:
    return {
        "action": "inherit",
        "candidate_root": root,
        "candidate_path": path,
        "content_view": view,
        "confidence_percent": 93,
        "reason": reason,
        "operator_rules": rules,
        "preserved_distinctions": preserved,
        "question": None,
    }


def rebase(identity: str, root: str, path: str, view: str, rules: list[str], preserved: list[str], reason: str, *, action: str = "rebase", confidence: int = 92) -> dict[str, Any]:
    return {
        "action": action,
        "candidate_root": root,
        "candidate_path": path,
        "content_view": view,
        "confidence_percent": confidence,
        "reason": reason,
        "operator_rules": rules,
        "preserved_distinctions": preserved,
        "question": None,
    }


def unresolved(identity: str, view: str, rules: list[str], preserved: list[str], reason: str, *, confidence: int = 82) -> dict[str, Any]:
    """A source/candidate gap is review work, not an Operator question."""

    return {
        "action": "review_required",
        "candidate_root": None,
        "candidate_path": None,
        "content_view": view,
        "confidence_percent": confidence,
        "reason": reason,
        "operator_rules": rules,
        "preserved_distinctions": preserved,
        "question": None,
    }


def syntax(identity: str, view: str, rules: list[str], preserved: list[str], reason: str) -> dict[str, Any]:
    return {
        "action": "syntax_context",
        "candidate_root": None,
        "candidate_path": None,
        "content_view": view,
        "confidence_percent": 94,
        "reason": reason,
        "operator_rules": rules,
        "preserved_distinctions": preserved,
        "question": None,
    }


def delivery(identity: str, preserved: list[str], reason: str) -> dict[str, Any]:
    return {
        "action": "delivery_policy",
        "candidate_root": "Carrier",
        "candidate_path": "Carrier (general Core D policy; storage field/path is not Carrier ID)",
        "content_view": "D",
        "confidence_percent": 94,
        "reason": reason,
        "operator_rules": [
            "carrier_delivery_model.decision",
            "carrier_delivery_model.carrier_root_boundary",
            "entity_identity_model.carrier_identity",
        ],
        "preserved_distinctions": preserved + [
            "General delivery policy does not inherit or create an actual Carrier for another Entity.",
            "Filename and path remain storage location, not Carrier identity.",
        ],
        "question": None,
    }


def candidate_mapping(identity: str) -> dict[str, Any]:
    """Map only meanings fixed by the candidate; leave the rest uncommitted."""

    prefix = "Atom/Content Role: "
    plan_prefix = prefix + "Plan"
    operation_prefix = prefix + "Operations"
    method_prefix = prefix + "Method"
    evaluation_prefix = prefix + "Evaluation"
    requirement_prefix = prefix + "Requirement"

    if identity == "Atom/Property":
        return inherited(
            identity, "Artifact", "Artifact/Atom.Property", "A",
            ["dependent_entities.property_node_vs_relation", "dependent_entities.compact_examples"],
            ["Property remains a named dependent Entity, connected by property-of rather than promoted to a root."],
            "The candidate expressly retains Property as a dependent Entity node inside an Artifact; this display mapping does not admit a native edge.",
        )
    if identity == "Atom/Governed Subject":
        return rebase(
            identity, "Artifact", "Artifact/Atom.Substance Scope (applicability, not ownership)", "C",
            ["content_direction.scope_omission"],
            ["A Subject restriction and owning Scope Unit remain distinct.", "Omitted Scope resolves only to whole Subject plus whole owning Scope Unit."],
            "The candidate settles Scope as applicability rather than ownership; the existing governed-Subject distinction remains explicit when restricted.",
        )
    if identity == "Atom/Identifier":
        return inherited(
            identity, "Artifact", "Artifact/Atom (atom_id owner selector)", "A",
            ["entity_identity_model.dependent_entity"],
            ["The complete dependent ID includes its owner selector and field; it is not merely a display address."],
            "The candidate fixes Atom selection by atom_id and keeps dependent identity qualified by its owner.",
        )
    if identity == "Atom/Identity":
        return inherited(
            identity, "Artifact", "Artifact/Atom (atom_id identity)", "A",
            ["entity_identity_model.dependent_entity", "atom_lookup.maximum_active_originals_per_atom_id"],
            ["At most one Active original exists per Atom ID; projections remain separate instances."],
            "The candidate confirms Atom identity and preserves the separate Projection-instance boundary.",
        )
    if identity == "Atom/Identifier/Project Prefix":
        return unresolved(
            identity, "A", ["entity_identity_model.scope_unit", "entity_identity_model.scope_unit_rename"],
            ["Scope Unit ID format is stable, but the old Atom-qualified Project Prefix is not silently made a Scope Unit field."],
            "The candidate confirms a Scope Unit prefix format, not a semantic mapping for this Atom-qualified identifier component; preserve it pending authoring review.",
        )
    if identity == "Atom/Identity/collision repair":
        return unresolved(
            identity, "A", ["entity_identity_model.unconfirmed_details"],
            ["No collision-repair lifecycle or replacement policy is inferred from stable identity."],
            "The candidate confirms identity boundaries but does not establish this historical collision-repair procedure as a candidate Entity or policy.",
        )
    if identity.startswith("Atom/Local Tier") or identity == "Atom/Global Tier":
        return unresolved(
            identity, "A", ["review_backlog.authoring_and_implementation"],
            ["The captured qualified tier and allowed-value distinctions remain separate; no tier collapse is proposed."],
            "The candidate names no Local/Global Tier model or allowed-value domain, so a candidate path would overstate the available direction.",
        )
    if identity == "Atom/Direct Relation":
        return unresolved(
            identity, "C", ["graph_model", "relation_type_model.endpoint_boundary", "review_backlog.question_policy"],
            ["Typed Relation endpoint constraints remain required; generic Direct Relation is not inferred from a label."],
            "The candidate confirms typed Relations but does not make the captured generic Direct Relation heading a settled Relation kind; this is review work, not a new Operator question.",
        )
    if identity == "Atom/Direct Relation Serialization":
        return syntax(
            identity, "C", ["entity_vs_syntax_rules"],
            ["A serialization form is distinct from the Relation it may describe."],
            "The candidate expressly separates syntax and compact notation from Entity identity; no native relation is proposed from this serialization label.",
        )
    if identity == "Atom/Frontmatter":
        return delivery(
            identity, ["Frontmatter remains carrier/serialization context, not an independent root Entity."],
            "The candidate assigns storage and field conventions to general D policies and preserves Carrier as the separate root.",
        )

    # Field-oriented historic paths retain their qualified domain while sharing
    # the candidate's one named dependent Status Entity; this is not status
    # inheritance between different Artifacts or old versions.
    if "/Status" in identity:
        suffix = identity.split("/Status", 1)[1] or ""
        return inherited(
            identity, "Artifact", f"Artifact/Atom.Status{suffix} (qualified domain retained)", "mixed",
            ["dependent_entities.compact_examples", "atom_versioning.trigger", "atom_versioning.version_transition"],
            ["Qualified Status fields and allowed-value domains do not collapse merely because their labels repeat.", "An older archived version does not transfer archived Status to the current version."],
            "The candidate confirms Status as a named dependent Entity and requires version increments for Status-only changes; the captured qualified domain remains distinct.",
        )
    if "Carrier" in identity or "Filename" in identity or "filename" in identity or identity.endswith("/Frontmatter"):
        return delivery(
            identity, ["The qualified field/filename/placement meaning remains distinct from the Carrier root and Carrier ID."],
            "The candidate puts these delivery details under reusable Core D policy rather than per-Property Carrier edges or D Atoms.",
        )

    if identity == operation_prefix:
        return rebase(
            identity, "Artifact", "Artifact/Atom.Substance (Operations role; repeatable Operation definition)", "O",
            ["content_direction.role_labels.Operations", "execution_definition_policy.o_atom_role"],
            ["A repeatable Operation definition differs from one actual Execution.", "Ad hoc Executions need no O Atom."],
            "The candidate maps Operations content to a repeatable Operation definition while keeping actual runs at the Execution root; the path does not use allowed-value notation.",
            action="operation_or_method", confidence=95,
        )
    if identity.startswith(operation_prefix):
        tail = identity[len(operation_prefix):]
        if tail == "/Type: Actor":
            return rebase(
                identity, "Actor", "Actor (Operation participant type)", "O",
                ["root_entities[2]", "execution_definition_policy.o_atom_role"],
                ["Actor means who performs work; it is not an Operation's Carrier or actual Execution."],
                "The candidate gives Actor a root meaning and keeps repeatable Operation definitions distinct from actual runs.",
            )
        if tail in {"/Type: Action", "/Type: Step", "/Type: Workflow"}:
            kind = tail.rsplit(": ", 1)[1]
            return rebase(
                identity, "Artifact", f"Artifact/Atom.Substance (Operations role; repeatable {kind} definition)", "O",
                ["content_direction.role_labels.Operations", "execution_definition_policy", "root_entities[6].proposed_kinds"],
                [f"The {kind} definition is not its {kind} Run Execution.", "The Operator, not an automatic rule, decides repeatability."],
                "The candidate retains repeatable Operation definitions in Atom content and reserves Execution for actual runs.",
                action="operation_or_method", confidence=94,
            )
        if tail == "/Type":
            return rebase(
                identity, "Artifact", "Artifact/Atom.Substance (Operations role; qualified operation type)", "O",
                ["content_direction.role_labels.Operations", "execution_definition_policy"],
                ["Operation type remains qualified and does not become an eighth root."],
                "The candidate's Operation direction supports a qualified repeatable-definition display, without admitting a native subtype.",
                action="operation_or_method", confidence=91,
            )
        return rebase(
            identity, "Artifact", "Artifact/Atom.Substance (Operations role)", "O",
            ["content_direction.role_labels.Operations", "execution_definition_policy"],
            ["Operation definition and actual Execution remain distinct."],
            "The candidate provides the Operation content role and leaves exact native field grammar unadopted.",
            action="operation_or_method", confidence=91,
        )

    if identity == method_prefix:
        return rebase(
            identity, "Artifact", "Artifact/Atom (M view specification)", "M",
            ["m_e_root_question.decision"],
            ["Method is a view over shared roots, not an additional root."],
            "The candidate resolves Method as an M view whose specifications are Atoms, with actual performances represented as Executions.",
            action="operation_or_method", confidence=94,
        )
    if identity.startswith(method_prefix):
        return rebase(
            identity, "Artifact", "Artifact/Atom (M view qualified content)", "M",
            ["m_e_root_question.decision", "dependent_entities"],
            ["The qualified Method field remains distinct from a separate Method root."],
            "The candidate places Method specifications in Atoms and does not create a Method root.",
            action="operation_or_method", confidence=91,
        )
    if identity == evaluation_prefix:
        return rebase(
            identity, "Artifact", "Artifact/Atom (E view specification)", "E",
            ["m_e_root_question.decision"],
            ["Evaluation is a view over shared roots; an actual check is an Execution."],
            "The candidate resolves Evaluation as an E view rather than an added root.",
            action="operation_or_method", confidence=94,
        )
    if identity.startswith(evaluation_prefix):
        return unresolved(
            identity, "E", ["m_e_root_question.decision", "entity_vs_syntax_rules"],
            ["Evaluation view status/type/tier qualifiers remain distinct and are not inferred from the shared label."],
            "The candidate settles the E-view boundary but not this exact qualified field/allowed-value mapping; retain it for authoring review without an Operator escalation.",
        )

    if identity == plan_prefix:
        return rebase(
            identity, "Artifact", "Artifact/Atom.Substance (Plan role; Objective content)", "P",
            ["content_direction.role_labels.Plan", "content_direction.details"],
            ["Plan role content is Objective; general Details optionality does not erase required Plan content."],
            "The candidate explicitly associates Plan with Objective content while preserving role/type-required material; this display path does not misuse allowed-value notation.",
            confidence=95,
        )
    if identity.startswith(plan_prefix):
        tail = identity[len(plan_prefix):]
        if tail in {"/Backlog", "/Type: Plan/Backlog"}:
            return inherited(
                identity, "Artifact", "Artifact/Atom.Status: Backlog (Plan-qualified domain)", "P",
                ["snapshot_and_history_rules[2]", "atom_lookup.default_view"],
                ["Plan Backlog remains future work outside current Plan Scope, not a Version Label.", "The qualified Plan Backlog domain remains separate from other Status uses."],
                "The candidate retains Backlog among non-archived status containers; the captured Plan Backlog meaning is preserved as a qualified Status domain, not folded into Version labels.",
            )
        if tail == "/Type: Plan":
            return rebase(
                identity, "Artifact", "Artifact/Atom (Plan Atom kind; Content Role Plan and Type Plan)", "P",
                ["dependent_entities", "content_direction.role_labels.Plan"],
                ["Plan Atom kind requires both Content Role Plan and Type Plan.", "Type Plan remains distinct from an Atom.Plan dependent field."],
                "Captured CA-R-1574 defines a Plan Atom by Content Role Plan plus Type Plan; the candidate keeps dependent fields inside the Atom without inventing an Atom.Plan field.",
                confidence=90,
            )
        if tail == "/Current Scope":
            return rebase(
                identity, "Scope Unit", "Scope Unit (Plan applicability/ownership qualifier; not an inferred owner)", "P",
                ["content_direction.scope_omission", "root_entities[1]"],
                ["Substance Scope is applicability rather than ownership; a restriction stays explicit."],
                "The candidate preserves Scope Unit and Scope applicability boundaries without converting plan scope into automatic ownership.",
            )
        if tail in {"/Direct Work Decomposition", "/Type: Plan/Decomposition", "/Type: Plan/Recursive Decomposition"}:
            return rebase(
                identity, "Relation", "Relation (Plan decomposition; exact native Type remains unadmitted)", "P",
                ["graph_model", "relation_type_model.endpoint_boundary"],
                ["Decomposition semantics and exact endpoint constraints remain explicit; no lexical relation kind is silently admitted."],
                "The candidate retains typed Relations while leaving the exact native decomposition catalogue to later authoring review.",
            )
        if tail == "/Type":
            return syntax(
                identity, "P", ["entity_vs_syntax_rules", "dependent_entities"],
                ["The qualified Plan Type leaves retain their meanings; the parent heading is not independently promoted."],
                "The candidate says contextual grouping does not itself create an Entity; no source gap is escalated as an Operator conflict.",
            )
        if tail in {"/Type: Plan/Definition of Done", "/Type: Plan/Details"}:
            field = "Definition of Done" if tail.endswith("Definition of Done") else "Details"
            return rebase(
                identity, "Artifact", f"Artifact/Atom.Substance (Plan role; Objective content; {field})", "P",
                ["content_direction.role_labels.Plan", "content_direction.details"],
                ["Optional general Details does not erase role/type-required Definition of Done or analysis results."],
                "The candidate preserves required Plan content despite the general Details optionality rule.",
            )
        if tail == "/Type: Plan/Assignee":
            return rebase(
                identity, "Actor", "Actor (Plan assignee)", "P",
                ["root_entities[2]", "entity_identity_model.actor"],
                ["An Actor Type can be generic or named; assignee is not a Carrier."],
                "The candidate has a distinct Actor root for who performs work.",
            )
        if tail in {"/Type: Plan/Autonomous Confidence Threshold", "/Type: Plan/Blocking", "/Type: Plan/Subtype", "/Type: Plan/Work Sequence Number", "/Identity", "/Type: Plan/Identifier", "/Type: Plan/Label"}:
            field = tail.rsplit("/", 1)[-1]
            return rebase(
                identity, "Artifact", f"Artifact/Atom.{field} (Plan-qualified dependent field)", "P",
                ["dependent_entities", "content_direction.role_labels.Plan"],
                ["The Plan-qualified field remains distinct; it has no independent lifecycle."],
                "The candidate keeps named dependent fields inside the Artifact and preserves the Plan Objective role.",
            )
        return rebase(
            identity, "Artifact", "Artifact/Atom.Substance (Plan role; Objective content; qualified field)", "P",
            ["content_direction.role_labels.Plan", "dependent_entities"],
            ["Plan qualification and allowed-value constraints remain distinct from generic labels."],
            "The candidate maps Plan content to Objective while retaining named dependent Entities and their qualified meanings.",
        )

    if identity == requirement_prefix:
        return unresolved(
            identity, "R", ["content_direction.role_labels", "review_backlog.question_policy"],
            ["Requirement, Demand, and Goal meanings remain distinct; none is silently relabelled as a settled candidate role."],
            "The candidate's role-label table does not select a one-to-one Requirement mapping, so this positive captured meaning remains uncommitted review work.",
        )
    if identity.startswith(requirement_prefix):
        if "/Filename" in identity or "/filename" in identity:
            return delivery(
                identity, ["Requirement filename/token meaning remains carrier context, not a semantic Requirement collapse."],
                "The candidate applies general D delivery policies without turning a filename token into Carrier identity.",
            )
        if identity.endswith("/Type: Goal/Reference"):
            return delivery(
                identity, ["An external Project Goal reference without an Atom ID uses its complete current Carrier filename stem.", "That reference convention does not make the filename stem the Goal's or Carrier's identity."],
                "Captured CA-D-342 is a carrier-reference convention. The candidate retains general delivery policy and separates filename/path from Carrier identity.",
            )
        if "/Type: Goal" in identity:
            return rebase(
                identity, "Artifact", "Artifact/Atom.Substance (RMED Claim; Goal-qualified Requirement)", "R",
                ["content_direction.umbrella", "content_direction.role_labels.RMED"],
                ["Goal is a Relational Atom with Content Role Requirement and Type Goal.", "A parent Scope Unit owns child-targeted Goal Atoms without transferring ownership.", "Goal stays distinct from Demand; no type hierarchy is admitted."],
                "Captured CA-R-925 and CA-R-1775 preserve Goal as a Requirement-qualified RMED Claim, not Plan Objective content; the path is prose rather than allowed-value notation.",
                confidence=92,
            )
        return unresolved(
            identity, "R", ["content_direction.role_labels", "review_backlog.question_policy"],
            ["Qualified Demand/Requirement fields and allowed values remain distinct."],
            "The candidate does not select this Requirement/Demand-qualified role mapping; leave it as review work rather than inventing a new Operator question.",
        )

    if identity == "Atom/Content Role: Implementation":
        return unresolved(
            identity, "mixed", ["content_direction.role_labels", "review_backlog.question_policy"],
            ["Implementation is not conflated with Operation, Method, or actual Execution."],
            "The candidate supplies no settled Implementation role label, so a candidate root/path would be speculative.",
        )
    return unresolved(
        identity, "unclassified", ["review_backlog.question_policy"],
        ["The original qualified identity and captured meaning remain preserved."],
        "No candidate mapping is asserted without a settled Operator direction and verified captured meaning.",
    )


def prior_rows(ledger: dict[str, Any]) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for mark in ledger["node_disposition_marks"]:
        identity = mark["identity"]
        if identity in result:
            raise AssertionError(f"duplicate identity in accepted ledger: {identity}")
        result[identity] = mark
    return result


def build() -> dict[str, Any]:
    candidate_raw = CANDIDATE.read_bytes()
    if sha256(candidate_raw) != EXPECTED_CANDIDATE_SHA256:
        raise AssertionError("candidate snapshot hash differs from the assigned input")
    input_raw = INPUT.read_bytes()
    baseline_raw = BASELINE.read_bytes()
    ledger_raw = LEDGER.read_bytes()
    batch = load(INPUT)
    baseline = load(BASELINE)
    ledger = load(LEDGER)
    if batch["batch"] != 2 or len(batch["nodes"]) != 81 or batch["identity_count"] != 81:
        raise AssertionError("expected the 81-identity batch 2 input")
    if sha256(baseline_raw) != batch["baseline"]["sha256"]:
        raise AssertionError("baseline snapshot does not match the input pin")
    accepted = prior_rows(ledger)
    catalogue = ledger["evidence_catalogue"]
    result_nodes: list[dict[str, Any]] = []
    used_refs: set[str] = set()
    for input_node in batch["nodes"]:
        identity = input_node["identity"]
        previous = accepted.get(identity)
        if previous is None:
            raise AssertionError(f"input identity absent from accepted ledger: {identity}")
        old = previous["review_row"]
        refs = previous["scoped_refs"]["global_evidence_refs"]
        if not refs:
            raise AssertionError(f"no accepted evidence refs: {identity}")
        checked_ids: list[str] = []
        for ref in refs:
            evidence = catalogue.get(ref)
            if evidence is None:
                raise AssertionError(f"missing exact global evidence ref: {ref}")
            source_text_for_evidence(evidence)
            used_refs.add(ref)
            if evidence["atom_id"] not in checked_ids:
                checked_ids.append(evidence["atom_id"])
        mapping = candidate_mapping(identity)
        # Contract rule: uncommitted mappings never acquire a display path.
        if mapping["confidence_percent"] < 90:
            if mapping["candidate_path"] is not None or mapping["action"] not in {"review_required", "concrete_conflict"}:
                raise AssertionError(f"low-confidence mapping must remain unresolved: {identity}")
        result_nodes.append(
            {
                "identity": identity,
                "prior_disposition": old["disposition"],
                "action": mapping["action"],
                "candidate_root": mapping["candidate_root"],
                "candidate_path": mapping["candidate_path"],
                "content_view": mapping["content_view"],
                "confidence_percent": mapping["confidence_percent"],
                "reason": mapping["reason"],
                "operator_rules": mapping["operator_rules"],
                "evidence_refs": refs,
                "checked_source_atom_ids": checked_ids,
                "preserved_distinctions": mapping["preserved_distinctions"],
                "question": mapping["question"],
            }
        )
    identities = [row["identity"] for row in result_nodes]
    if len(identities) != 81 or len(set(identities)) != 81:
        raise AssertionError("review must cover each input identity exactly once")
    return {
        "schema_version": 1,
        "batch": 2,
        "kind": "Captured nodes against Operator candidate",
        "non_authoritative": True,
        "native_admission": "not_performed",
        "source_migration": "not_performed",
        "captured_core_commit": COMMIT,
        "candidate_sha256": sha256(candidate_raw),
        "input_sha256": sha256(input_raw),
        "baseline_sha256": sha256(baseline_raw),
        "prior_review_sha256": sha256(ledger_raw),
        "review_method": "Compared all 81 assigned captured identities with the latest Operator candidate; reused the accepted ledger's exact global evidence references only after verifying each referenced captured Main Content quote and span through snapshot_sources.py. This is a bounded captured-snapshot comparison, not a fresh audit of all source candidates or a native admission.",
        "nodes": result_nodes,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--persist", action="store_true", help="create the byte-stable review if absent")
    args = parser.parse_args()
    payload = json.dumps(build(), ensure_ascii=False, indent=2) + "\n"
    expected = payload.encode("utf-8")
    if OUTPUT.exists():
        actual = OUTPUT.read_bytes()
        if actual != expected:
            raise SystemExit("existing output differs; refusing to overwrite")
        print(json.dumps({"output": str(OUTPUT), "status": "byte_identical", "nodes": 81}, sort_keys=True))
        return
    if not args.persist:
        print(json.dumps({"output": str(OUTPUT), "status": "checked_not_written", "nodes": 81}, sort_keys=True))
        return
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(expected)
    print(json.dumps({"output": str(OUTPUT), "status": "created", "nodes": 81}, sort_keys=True))


if __name__ == "__main__":
    main()
