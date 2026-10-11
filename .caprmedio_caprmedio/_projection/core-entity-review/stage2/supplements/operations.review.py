#!/usr/bin/env python3
"""Build and validate the bounded CA-P-2052 operations mapping supplement.

This is a one-off, derived report builder.  It deliberately reads the frozen
ledger and live pinned sources but never changes either authority surface.
"""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
STAGE2 = ROOT / ".caprmedio_caprmedio/_projection/core-entity-review/stage2"
LEDGER = STAGE2 / "current-subjects.mapping-ledger.json"
OWNERSHIP = STAGE2 / "current-subjects.research-ownership.json"
CANDIDATE = ROOT / ".caprmedio_caprmedio/_projection/core-entity-review/presentation/operator.entity-graph.candidate.json"
OPERATOR = STAGE2 / "operator.subject-decisions.2026-10-11.json"
SUPPLEMENT_CONTRACT = STAGE2 / "current-subjects.supplements.contract.md"
CURRENT_CONTRACT = STAGE2 / "current-subjects.contract.md"
REVIEW_CONTRACT = STAGE2 / "current-subjects.review.contract.md"
OUTPUT = Path(__file__).with_suffix(".json")
BASE_LEDGER_SHA256 = "4d094ce89390e31290ce6ae7248cde78701376085bbe3078e33a228055e2eb39"


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def pin(path: Path) -> dict[str, str]:
    return {"path": str(path.relative_to(ROOT)), "sha256": sha256_file(path)}


def content_span(source: Path, span: dict) -> dict:
    """Revalidate and return the frozen review's live Main Content span."""
    raw = source.read_bytes()
    lines = raw.splitlines(keepends=True)
    start, end = span["start_line"], span["end_line"]
    actual = sha256_bytes(b"".join(lines[start - 1 : end]))
    if actual != span["span_sha256"]:
        raise ValueError(f"stale Main Content span: {source}")
    return {
        "path": span["path"],
        "sha256": span["sha256"],
        "start_line": start,
        "end_line": end,
        "span_sha256": actual,
    }


ATOM_ACTION = {
    "value": "Atom/Action",
    "reason": (
        "Current Main Content uses Action as a reusable operational definition, "
        "not one actual execution. The confirmed Operation-definition policy and "
        "the explicit source definition support the Atom/Action subtype."
    ),
    "basis": [
        ("#/root_entities/0/narrower_entities/0", "Atom is the confirmed reusable governed definition bearer."),
        ("#/execution_definition_policy", "Repeatable Operations are definitions; actual executions remain distinct."),
    ],
    "distinctions": ["The reusable Action definition remains distinct from its actual Action Run."]
}
ATOM_STEP = {
    "value": "Atom/Step",
    "reason": (
        "Current Main Content identifies a reusable Step definition or Workflow node, "
        "rather than an actual Step Run. The confirmed definition/execution boundary "
        "supports Atom/Step."
    ),
    "basis": [
        ("#/root_entities/0/narrower_entities/0", "Atom is the confirmed reusable governed definition bearer."),
        ("#/execution_definition_policy", "Repeatable Operations are definitions; actual executions remain distinct."),
    ],
    "distinctions": ["The Step definition remains distinct from its Action binding and actual Step Run."]
}
ATOM_WORKFLOW = {
    "value": "Atom/Workflow",
    "reason": (
        "Current Main Content identifies a reusable Workflow graph or definition, not "
        "one actual Workflow Run. The confirmed definition/execution boundary supports "
        "Atom/Workflow."
    ),
    "basis": [
        ("#/root_entities/0/narrower_entities/0", "Atom is the confirmed reusable governed definition bearer."),
        ("#/execution_definition_policy", "Repeatable Operations are definitions; actual executions remain distinct."),
    ],
    "distinctions": ["The Workflow definition remains distinct from its actual Workflow Run and its contained Step bindings."]
}


def dependent(value: str, reason: str, distinctions: list[str], *basis: tuple[str, str]) -> dict:
    return {
        "value": value,
        "reason": reason,
        "basis": [
            ("#/entity_identity_model/dependent_entity", "A confirmed dependent Entity is identified by owner selector plus field."),
            *basis,
        ],
        "distinctions": distinctions,
    }


RULES: dict[str, dict] = {
    "Action": ATOM_ACTION,
    "Step": ATOM_STEP,
    "Workflow": ATOM_WORKFLOW,
    "Action/Execution Kind": dependent(
        "Atom/Action.Execution Kind",
        "Current Main Content defines Execution Kind as a distinction of an Action's declared responsibility. It is retained as an Action-dependent field, not recast as an Execution or Action Run.",
        ["Programmatic and Agentic remain the source-defined Action Execution Kind domain.", "Execution Kind does not select an Agentic execution context."],
        ("#/execution_definition_policy", "The Action remains a reusable definition, distinct from actual execution."),
    ),
    "Action/Execution Kind: Agentic": dependent(
        "Atom/Action.Execution Kind: Agentic",
        "Current Main Content expressly defines Agentic as one Action Execution Kind. The dependent Action field and its allowed value are retained without treating an Agentic invocation as a new Action or Step.",
        ["Agentic remains an allowed Execution Kind of an Action.", "An Agentic Action remains distinct from the context selected for an invocation."],
        ("#/execution_definition_policy", "The Action remains a reusable definition, distinct from actual execution."),
    ),
    "Step/Agentic Execution Context": dependent(
        "Execution/Step Run.Agentic Execution Context",
        "Current Main Content expressly assigns Agentic Execution Context to the invocation and says the actual Step Run retains it. The mapped dependent field therefore belongs to an Execution Step Run, not to the reusable Step definition or Action identity.",
        ["Integrated and Isolated remain the source-defined context domain.", "Execution context remains distinct from Action Execution Kind and from Workflow classification."],
        ("#/root_entities/6", "Execution is the confirmed root for one actual Operation run."),
        ("#/root_entities/6/proposed_kinds/1", "Step Run is the confirmed actual-run kind."),
    ),
    "Workflow Run": {
        "value": "Execution/Workflow Run",
        "reason": "Current Main Content uses Workflow Run for one actual workflow execution. The candidate explicitly places Workflow Run under the distinct Execution root.",
        "basis": [
            ("#/root_entities/6", "Execution is the confirmed root for one actual Operation run."),
            ("#/root_entities/6/proposed_kinds/2", "Workflow Run is an explicit actual-run kind."),
        ],
        "distinctions": ["One actual Workflow Run remains distinct from its reusable Workflow definition."]
    },
    "Step Run/Invocation": dependent(
        "Execution/Step Run.Invocation",
        "Current Main Content treats an Invocation as an identifiable actual Step Run concern and distinguishes delivery from completion. The Invocation field is retained under the actual Step Run rather than collapsed to the Step definition.",
        ["Invocation delivery remains distinct from Step Run completion and recorded actual results."],
        ("#/root_entities/6", "Execution is the confirmed root for one actual Operation run."),
        ("#/root_entities/6/proposed_kinds/1", "Step Run is the confirmed actual-run kind."),
    ),
    "Step Run/Tool Call": dependent(
        "Execution/Step Run.Tool Call",
        "Current Main Content locates a Tool Call within a Step Run as execution detail and explicitly excludes it from becoming another Action or Step. The dependent field retains that actual-run qualification.",
        ["A Tool Call remains execution detail, not a new Action, Step, or Workflow node."],
        ("#/root_entities/6", "Execution is the confirmed root for one actual Operation run."),
        ("#/root_entities/6/proposed_kinds/1", "Step Run is the confirmed actual-run kind."),
    ),
    "Workflow/Relation Kind: On Result": {
        "value": "Relation.Type: On Result",
        "reason": "Current Main Content uses On Result as the typed transition relation in a Workflow graph. The candidate confirms Relation Type/Kind as one concept and preserves endpoint constraints, so the relation kind is not turned into a Workflow Property.",
        "basis": [
            ("#/relation_type_model", "Relation Type and Relation Kind are confirmed as one concept with endpoint constraints."),
        ],
        "distinctions": ["On Result remains a relation type for workflow transition routing.", "Workflow graph endpoint constraints remain explicit rather than becoming a Workflow Property."],
    },
    "Workflow/Carrier": dependent(
        "Atom/Workflow.Carrier",
        "Current Main Content describes Carrier binding for a reusable Workflow representation and separates it from Step and execution carriers. The source supports a Workflow-dependent binding while Carrier remains a separate root.",
        ["Carrier remains a separate root rather than a Workflow subtype.", "Workflow definition carrier separation remains distinct from Step and execution carriers."],
        ("#/root_entities/5", "Carrier is a confirmed separate root."),
        ("#/carrier_delivery_model/carrier_root_boundary", "Generic semantic Carrier links remain permitted without a per-Property registry."),
    ),
}

UNRESOLVED = {
    "CCE/Role Profile: Operations": "Current Main Content names an Operations-specific CCE Role Profile, but the candidate has no confirmed CCE profile field or Type domain preserving that qualification.",
    "Tool/Workflow Operations/Atom Lifecycle/Request Parameters": "Current Main Content retains a compound Tool, Workflow Operations, Atom Lifecycle, and Request Parameters boundary. The candidate does not establish one owner-qualified dependent identity preserving every component.",
    "Work Journal/Action": "Current Main Content binds an Action to the Work Journal and terminal event routing. The candidate does not establish an owner-qualified identity preserving the Work Journal qualification rather than flattening it to Action.",
}


def rule_for(old_value: str) -> dict | None:
    if old_value in RULES:
        return RULES[old_value]
    if old_value in UNRESOLVED:
        return None
    if old_value.endswith(" Workflow"):
        return {
            **ATOM_WORKFLOW,
            "reason": "Current Main Content defines the named item as a reusable Workflow graph. Its source Atom identity retains the specific name and bindings; the candidate target is the reusable Atom/Workflow category, not an Execution.",
            "distinctions": ["The named Workflow's source identity and graph bindings remain distinct from an actual Workflow Run."],
        }
    if old_value.endswith(" Step") or "/Step:" in old_value:
        return {
            **ATOM_STEP,
            "reason": "Current Main Content defines the named item as a reusable Workflow Step/node. The source Atom identity retains the node's specific name and workflow binding; the candidate target is Atom/Step, not an actual Step Run.",
            "distinctions": ["The named Step's source identity and workflow binding remain distinct from an Action and actual Step Run."],
        }
    raise ValueError(f"unclassified operations value: {old_value!r}")


def main() -> None:
    if sha256_file(LEDGER) != BASE_LEDGER_SHA256:
        raise ValueError("baseline ledger pin is stale")
    ledger = json.loads(LEDGER.read_text())
    ownership = json.loads(OWNERSHIP.read_text())
    task = next(row for row in ownership["research_tasks"] if row["group"] == "operations")
    values = set(task["old_values"])
    rows = sorted(
        (row for row in ledger["occurrences"] if row["decision"] == "unresolved" and row["old_value"] in values),
        key=lambda row: row["occurrence_id"],
    )
    identifiers = [row["occurrence_id"] for row in rows]
    identifiers_sha = sha256_bytes(json.dumps(identifiers, separators=(",", ":")).encode())
    if len(rows) != task["occurrences"] or identifiers_sha != task["occurrence_ids_sha256"]:
        raise ValueError("operations research ownership selection is stale")
    if len({row["source_path"] for row in rows}) != task["sources"]:
        raise ValueError("operations source coverage differs from ownership")

    reviewed = []
    for baseline in rows:
        source = ROOT / baseline["source_path"]
        if sha256_file(source) != baseline["source_sha256"]:
            raise ValueError(f"current source pin is stale: {source}")
        span = content_span(source, baseline["evidence"][0])
        old = baseline["old_value"]
        rule = rule_for(old)
        base = {
            "occurrence_id": baseline["occurrence_id"],
            "source_path": baseline["source_path"],
            "source_atom_id": baseline["source_atom_id"],
            "source_version": baseline["source_version"],
            "source_sha256": baseline["source_sha256"],
            "field": baseline["field"],
            "index": baseline["index"],
            "old_value": old,
            "quarantined": baseline["quarantined"],
            "originating_batch_id": baseline["batch_id"],
            "originating_task_id": baseline["task_id"],
            "originating_review_path": baseline["originating_review_path"],
            "originating_review_sha256": baseline["originating_review_sha256"],
            "baseline_decision": baseline["decision"],
            "baseline_proposed_value": baseline["proposed_value"],
            "baseline_confidence": baseline["confidence"],
            "baseline_reason": baseline["reason"],
            "evidence": [{**span, "reason": f"Current Main Content for {baseline['source_atom_id']} establishes the reviewed meaning of {old!r}."}],
            "question": None,
            "executable": False,
        }
        if rule is None:
            reviewed.append({
                **base,
                "decision": "unresolved",
                "proposed_value": None,
                "confidence": 0.5,
                "reason": UNRESOLVED[old],
                "candidate_basis": [],
                "preserved_distinctions": ["The complete source qualification remains explicit; no replacement identity is invented."],
            })
        else:
            reviewed.append({
                **base,
                "decision": "proposed",
                "proposed_value": rule["value"],
                "confidence": 0.95,
                "reason": rule["reason"],
                "candidate_basis": [{"pointer": pointer, "reason": reason} for pointer, reason in rule["basis"]],
                "preserved_distinctions": rule["distinctions"],
            })

    sources = sorted({row["source_path"] for row in reviewed})
    report = {
        "schema_version": 1,
        "task_id": "CA-P-2052",
        "non_authoritative": True,
        "source_migration": "not_performed",
        "native_admission": "not_performed",
        "base_ledger": {"path": str(LEDGER.relative_to(ROOT)), "sha256": BASE_LEDGER_SHA256},
        "research_ownership": {"path": str(OWNERSHIP.relative_to(ROOT)), "group": "operations", "occurrence_ids_sha256": identifiers_sha},
        "evidence_pins": [pin(CANDIDATE), pin(OPERATOR), pin(SUPPLEMENT_CONTRACT), pin(CURRENT_CONTRACT), pin(REVIEW_CONTRACT)],
        "coverage": {"occurrences": len(reviewed), "sources": len(sources), "old_values": len(values), "occurrence_ids_sha256": identifiers_sha},
        "source_pins": [
            {
                "path": source,
                "sha256": next(row["source_sha256"] for row in reviewed if row["source_path"] == source),
            }
            for source in sources
        ],
        "occurrences": reviewed,
    }
    verify(report, task)
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"output": str(OUTPUT.relative_to(ROOT)), "sha256": sha256_file(OUTPUT), "decisions": Counter(row["decision"] for row in reviewed), "coverage": report["coverage"]}, default=dict, sort_keys=True))


def verify(report: dict, task: dict) -> None:
    rows = report["occurrences"]
    assert report["coverage"]["occurrences"] == task["occurrences"] == len(rows)
    assert report["coverage"]["sources"] == task["sources"] == len(report["source_pins"])
    assert report["coverage"]["old_values"] == len(task["old_values"])
    assert report["coverage"]["occurrence_ids_sha256"] == task["occurrence_ids_sha256"]
    assert len({row["occurrence_id"] for row in rows}) == len(rows)
    for row in rows:
        assert row["baseline_decision"] == "unresolved" and row["baseline_proposed_value"] is None
        assert row["executable"] is False and row["evidence"]
        if row["decision"] == "proposed":
            assert row["proposed_value"] and row["confidence"] >= 0.90 and row["candidate_basis"]
        else:
            assert row["decision"] == "unresolved" and row["proposed_value"] is None and row["confidence"] < 0.90 and not row["candidate_basis"]


if __name__ == "__main__":
    main()
