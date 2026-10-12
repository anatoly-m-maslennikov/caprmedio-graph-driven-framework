"""Emit the CA-P-1947 snapshot-only node review; it never writes files."""
import hashlib
import json
import sys
from pathlib import Path


ROOT = Path.cwd()
NODES = ROOT / ".caprmedio_caprmedio/_projection/core-entity-review/nodes"
sys.path.insert(0, str(NODES / "support"))
from snapshot_sources import COMMIT, read_source, source_pins, verify_snapshot


INPUT = NODES / "inputs/slices/CA-P-1947.input.json"
SCOPE_DECISION = NODES / "scope.omission.decision.md"
pins = source_pins()
catalogue = {}


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def evidence(atom_id, start_line, end_line):
    key = f"{atom_id}-{start_line}-{end_line}"
    if key not in catalogue:
        lines = read_source(atom_id).decode().splitlines()
        quote = "\n".join(lines[start_line - 1 : end_line])
        pin = pins[atom_id]
        catalogue[key] = {
            "evidence_ref": key,
            "atom_id": atom_id,
            "atom_revision": pin["atom_revision"],
            "carrier_path": pin["carrier_path"],
            "carrier_sha256": pin["carrier_sha256"],
            "start_line": start_line,
            "end_line": end_line,
            "quote": quote,
            "text_sha256": sha(quote.encode()),
        }
    return key


E = {
    "replacement": evidence("CA-R-1035", 29, 29),
    "implementation": evidence("CA-O-019", 35, 40),
    "implementation_step": evidence("CA-O-093", 35, 41),
    "operator_priorities": evidence("CA-O-022", 28, 35),
    "initialization": evidence("CA-O-052", 36, 42),
    "revert": evidence("CA-O-130", 25, 36),
    "root_term": evidence("CA-R-1347", 30, 30),
    "runtime_journal": evidence("CA-D-559", 27, 27),
    "runtime_state": evidence("CA-E-522", 55, 60),
    "runtime_state_carrier": evidence("CA-D-341", 30, 30),
    "scope_context": evidence("CA-E-207", 42, 49),
    "scope_expression": evidence("CA-R-999", 28, 28),
    "scope_evaluation": evidence("CA-M-121", 25, 34),
    "scope_signature": evidence("CA-R-1361", 32, 32),
    "scope_projection": evidence("CA-D-347", 31, 31),
}


def checks(identity, refs, messages):
    return {
        name: {"finding": finding, "reason": reason, "evidence_refs": refs}
        for name, finding, reason in messages
    }


def retain(identity, confidence, reason, refs, checked, messages, preserves):
    return {
        "identity": identity,
        "disposition": "retain",
        "confidence_percent": confidence,
        "reason": reason,
        "checks": checks(identity, refs, messages),
        "evidence_refs": refs,
        "checked_source_atom_ids": checked,
        "proposal": {
            "action": "retain",
            "preserves": preserves,
            "effects": {
                "relations": "no change proposed",
                "constraints": "no change proposed",
                "historical_references": "no change proposed",
                "queries": "no change proposed",
            },
        },
        "question": None,
    }


def question(identity, confidence, reason, refs, checked, messages, prompt):
    return {
        "identity": identity,
        "disposition": "question",
        "confidence_percent": confidence,
        "reason": reason,
        "checks": checks(identity, refs, messages),
        "evidence_refs": refs,
        "checked_source_atom_ids": checked,
        "proposal": None,
        "question": prompt,
    }


def five(dup, red, empty, distinct, general):
    return [
        ("duplicates", "no-duplicate-proof", dup),
        ("redundancy", "separate-contribution", red),
        ("empty_definition", "meaningful-captured-content", empty),
        ("distinct_meaning", "identity-specific-boundary", distinct),
        ("generalization", "no-safe-generalization", general),
    ]


rows_by_identity = {
    "Replacement-Required Lineage Impact Disposition": retain(
        "Replacement-Required Lineage Impact Disposition", 99,
        "Captured Claim defines replacement_required as successor plus archival before traversal of every affected descendant.",
        [E["replacement"]], ["CA-R-1035"], five(
            "The successor-and-archival disposition is not shown equivalent to another lineage disposition.",
            "It controls descendant traversal after a required replacement, so is not a redundant status label.",
            "CA-R-1035 gives a direct captured definition rather than a mere occurrence.",
            "It differs from compatible lineage handling because it requires a successor and archival before continuation.",
            "Generalizing to a generic impact status would lose the successor, archival, and traversal boundary.",
        ), "the exact replacement-required lineage gate"),
    "Requirement Implementation": retain(
        "Requirement Implementation", 99,
        "Captured Operation defines the Agentic Action that realizes selected Plan-item Requirements after tests are prepared within Delivery boundaries.",
        [E["implementation"]], ["CA-O-019"], five(
            "The Action is not evidenced as duplicate of its Workflow Step; the Step separately binds this Action.",
            "It performs selected ready work and reports implemented or blocked results, a contribution not supplied by a Plan item.",
            "CA-O-019 directly defines inputs, work boundary, test order, and return conditions.",
            "It is a reusable Agentic Action, not proof of a completed Evaluation or actual execution record.",
            "Generalizing to implementation would lose selected-Plan, test-first, and Delivery-boundary constraints.",
        ), "the reusable Action and its bounded implementation safeguards"),
    "Requirement Implementation Step": retain(
        "Requirement Implementation Step", 99,
        "Captured Operation defines the Workflow node invoking exactly one CA-O-019 Action in Isolated context with retained execution evidence.",
        [E["implementation_step"]], ["CA-O-093"], five(
            "The Step is not duplicate of CA-O-019 because it binds Action execution in a Workflow context.",
            "It supplies workflow bindings and result pass-through rather than repeating implementation behavior.",
            "CA-O-093 directly defines the node, its inputs, context, and evidence retention.",
            "It is a reusable Step definition, distinct from an actual Step Run or the invoked Action.",
            "Generalizing to implementation would lose isolated-context and unchanged-result constraints.",
        ), "the Step/Action/actual-run distinction"),
    "Resolve Operator Priorities": retain(
        "Resolve Operator Priorities", 99,
        "Captured legacy Action body directly defines the Action that turns applicable Operator input into the effective priority model for an identified Scope and Project stage.",
        [E["operator_priorities"]], ["CA-O-022"], five(
            "No captured evidence shows this Action duplicates a priority model; it turns input into that model for one identified context.",
            "It contributes context identification, model/parameter/criteria resolution, activation, and unresolved handling rather than merely naming priorities.",
            "CA-O-022's descriptive H1 is followed by a captured body definition and bounded Action behavior; no Summary heading is used as evidence.",
            "The reusable Action is distinct from the effective priority model, an individual alternative selection, and an actual Action Run.",
            "Generalizing to priorities would lose Operator-input, Scope-and-stage, activation, and unresolved-result boundaries.",
        ), "the reusable Action and its contextual priority-resolution boundary"),
    "Resolve Project Initialization Inputs": retain(
        "Resolve Project Initialization Inputs", 99,
        "Captured Operation defines the reusable Action resolving authoritative Project and Framework Instance initialization inputs before Project Structure interpretation.",
        [E["initialization"]], ["CA-O-052"], five(
            "It is not duplicate of Settings Artifacts: it resolves their inputs without defining their representation.",
            "It establishes ordered resolution before structural interpretation and refuses cross-Project substitution.",
            "CA-O-052 gives direct captured Action meaning and boundaries.",
            "The Action differs from a Projection and from Project Structure authority.",
            "Generalizing to settings resolution would lose the pre-structure and no-existing-Atom/Implementation boundaries.",
        ), "the reusable pre-structure initialization-resolution Action"),
    "Revert Changes Workflow": retain(
        "Revert Changes Workflow", 99,
        "Captured Operation defines the reusable single-node Workflow graph and its terminal outcomes.",
        [E["revert"]], ["CA-O-130"], five(
            "The Workflow is not a duplicate of its CA-O-132 node because it owns graph entry and terminal-outcome mapping.",
            "Its graph-level terminal semantics are not supplied by a generic revert Action or Run.",
            "CA-O-130 directly defines the graph, lack of retries, and outcome mapping.",
            "It is a reusable Workflow definition, not an actual revert execution or Journal result.",
            "Generalizing to revert loses no-retry and terminal-outcome distinctions.",
        ), "the reusable Workflow/Step/Run separation and terminal mapping"),
    "Root Term": retain(
        "Root Term", 99,
        "Captured Claim defines Root Term by zero direct NARROWER_THAN parents in the Terms Graph.",
        [E["root_term"]], ["CA-R-1347", "CA-R-1353"], five(
            "No duplicate proof exists with Term; Root Term has the zero-direct-parent predicate.",
            "The predicate identifies a graph-boundary role rather than a redundant generic Term label.",
            "CA-R-1347 provides an exact captured definition.",
            "It differs from Term through direct-parent cardinality in the Terms Graph.",
            "Generalizing to Term loses the root/topology predicate.",
        ), "the Terms Graph root predicate"),
    "Runtime Journal": retain(
        "Runtime Journal", 91,
        "Captured Claim imposes a meaningful delivery boundary for runtime technical and business Journals without making their Carrier location canonical.",
        [E["runtime_journal"]], ["CA-D-559"], five(
            "The source does not prove equivalence to the shared Project Work Journal or another Journal identity.",
            "The delivery-location permission is a distinct operational constraint rather than a duplicate carrier rule.",
            "CA-D-559 supplies a concrete captured Journal delivery rule, not an empty label.",
            "Runtime Journal remains distinct from a Carrier: the Claim permits delivery to several governed sinks.",
            "Generalizing to Journal would lose its runtime technical/business and non-directory location boundary.",
        ), "the runtime-Journal delivery boundary and Journal/Carrier distinction"),
    "Runtime Journal/Carrier": retain(
        "Runtime Journal/Carrier", 93,
        "Captured Claim states the Carriers that may deliver runtime technical and business Journals and rejects a fixed journal/runtime-directory requirement.",
        [E["runtime_journal"]], ["CA-D-559"], five(
            "No equivalence is shown with the Journal itself; the clause expressly distinguishes Journal delivery from its Carriers.",
            "The allowed governed-sink choices contribute a carrier boundary not present in Runtime Journal alone.",
            "CA-D-559 gives a concrete carrier rule for runtime Journals.",
            "Carrier denotes delivery location/sink, not canonical Journal authority or Journal identity.",
            "Generalizing to Carrier would lose the runtime-Journal-specific delivery permission.",
        ), "the Journal/Carrier binding distinction and allowed delivery locations"),
    "Runtime State": retain(
        "Runtime State", 90,
        "Captured Evaluation gives Runtime State a meaningful storage-boundary role: treating it as canonical truth fails readiness.",
        [E["runtime_state"]], ["CA-E-522", "CA-E-523"], five(
            "No captured source proves Runtime State duplicates a Journal or scratch identity.",
            "The explicit prohibition against canonical-truth classification is a separate boundary contribution.",
            "CA-E-522 supplies a concrete failure condition involving Runtime State.",
            "Runtime State is distinguished from canonical Journal history by the fail condition.",
            "Generalizing to storage would lose the non-canonical-truth boundary.",
        ), "the non-canonical Runtime State versus durable Journal-history boundary"),
    "Runtime State Carrier": question(
        "Runtime State Carrier", 78,
        "Captured CA-D-341 requires persistent Framework/Project Carriers to remain outside Runtime State, but does not define a Runtime State Carrier identity or its binding.",
        [E["runtime_state_carrier"]], ["CA-D-341"], five(
            "No duplicate proof with persistent Carrier or Runtime State follows from the outside-Runtime-State rule.",
            "The rule protects persistent authority/history; it does not establish a separate Runtime State Carrier contribution.",
            "The captured clause has meaning but not a definition of this qualified identity.",
            "Persistent carriers are explicitly outside Runtime State, so they cannot silently define a Runtime State Carrier.",
            "Generalization or consolidation would risk inventing a carrier binding absent from the captured source.",
        ), "What captured Core Claim defines `Runtime State Carrier` itself, including whether it is a carrier of ephemeral state or a prohibited persistent-carrier classification?"),
    "Scope": question(
        "Scope", 78,
        "The listed captured candidates use affected Scope as context but do not define this exact generic Scope identity; the later omission direction is candidate-only and is not Core evidence.",
        [E["scope_context"]], ["CA-E-207", "CA-O-022", "CA-R-1487"], five(
            "No captured Claim/Operation source proves Scope is duplicate of Scope Unit, Claim Target Scope Unit, or applicability restriction.",
            "Priority-selection clauses require an affected Scope context but do not establish a standalone Scope entity definition.",
            "CA-E-207 supplies an evaluation condition, not a direct Scope definition.",
            "The source use must not collapse ownership, target, structural parentage, and applicability into one identity.",
            "Generalization would erase precisely those unresolved Scope distinctions.",
        ), "Which captured Core Claim defines this generic `Scope` identity and distinguishes it from Scope Unit ownership, Claim Target Scope Unit, and applicability Scope?"),
    "Scope Expression": retain(
        "Scope Expression", 99,
        "Captured Claim defines one deterministic expression identifying Governed Entities by references, IDs, grouping, registered operators, and predicates.",
        [E["scope_expression"]], ["CA-R-999", "CA-M-121", "CA-R-1271"], five(
            "No duplicate proof with a Canonical Scope Signature: the signature is a derived comparison value.",
            "The expression contributes deterministic governed-entity selection rather than merely recording a result.",
            "CA-R-999 gives an exact captured definition.",
            "Expression evaluation and signature derivation are separate operations/artifacts from the source expression.",
            "Generalizing to Scope loses grammar, determinism, and entity-selection semantics.",
        ), "the deterministic source expression distinct from evaluation and derived signatures"),
    "Scope Expression Evaluation": retain(
        "Scope Expression Evaluation", 99,
        "Captured Claim defines ordered Resolver semantics for identities, entity-kind selectors, operators, predicates, and parentheses.",
        [E["scope_evaluation"]], ["CA-M-121"], five(
            "It is not duplicate of Scope Expression because it specifies how the expression is resolved.",
            "The ordered set semantics add a distinct evaluation contribution.",
            "CA-M-121 directly defines required evaluation behavior.",
            "Evaluation is distinct from a derived Canonical Scope Signature and from the expression occurrence.",
            "Generalizing to expression would lose union/intersection/exclusion/predicate evaluation semantics.",
        ), "the Resolver's deterministic evaluation semantics"),
    "Scope Expression/Canonical Scope Signature": retain(
        "Scope Expression/Canonical Scope Signature", 99,
        "Captured Claim defines the Canonical Scope Signature as a derived non-authoritative comparison value for one parenthesized Scope Expression occurrence.",
        [E["scope_signature"]], ["CA-R-1361", "CA-E-407", "CA-M-241"], five(
            "It is not duplicate of its source Scope Expression because it is a derived comparison value.",
            "The comparison role is separate from evaluation and source authoring.",
            "CA-R-1361 directly names and defines this derived value.",
            "The non-authoritative signature must not establish Claim equivalence or authority.",
            "Generalizing to Scope Expression loses derivation and non-authority constraints.",
        ), "the source-expression versus derived non-authoritative comparison-value distinction"),
    "Scope Expression/Canonical Scope Signature/Projection": retain(
        "Scope Expression/Canonical Scope Signature/Projection", 99,
        "Captured Claim requires one non-authoritative JSON report with exact source frontier and diagnostics, while prohibiting source rewrite, Claim equivalence, and dependency creation.",
        [E["scope_projection"]], ["CA-D-347"], five(
            "The Projection is not duplicate of the signature value; it is its delivery/report representation.",
            "It contributes source/revision/digest/frontier and exclusion diagnostics.",
            "CA-D-347 directly defines the required delivery form.",
            "The report remains non-authoritative and distinct from an Atom Carrier or dependency relation.",
            "Generalizing to Projection loses its exact signature-report and non-equivalence boundaries.",
        ), "the signature value versus its non-authoritative evidence-bearing Projection"),
}


def main():
    inp = json.loads(INPUT.read_bytes())
    snapshot = verify_snapshot()
    assert sha(SCOPE_DECISION.read_bytes()) == inp["scope_omission_pin"]["sha256"]
    rows = [rows_by_identity[n["identity"]] for n in inp["nodes"]]
    out = {
        "source_task": inp["source_task"],
        "batch": inp["batch"],
        "baseline_inventory_sha256": inp["baseline"]["inventory_sha256"],
        "input_file_sha256": sha(INPUT.read_bytes()),
        "partition_sha256": inp["partition_sha256"],
        "non_authoritative": True,
        "semantic_admission": "not_performed",
        "source_migration": "not_performed",
        "snapshot_context": snapshot,
        "operator_direction": {
            "path": inp["scope_omission_pin"]["path"],
            "sha256": inp["scope_omission_pin"]["sha256"],
            "status": "candidate_input_only_not_captured_core_evidence",
            "summary": "Absent explicit Substance Scope defaults only to whole governed Subject in whole owning Scope Unit; neither restriction permits omission.",
        },
        "evidence_catalogue": catalogue,
        "nodes": rows,
    }
    print(json.dumps(out, ensure_ascii=False, indent=2) + "\n", end="")


if __name__ == "__main__":
    main()
