"""Build the bounded batch-8 comparison receipt.

This helper only reads the captured snapshot and candidate evidence.  It may
create the one assigned JSON receipt when ``--persist`` is supplied; an
existing receipt must already be byte-identical.
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
import pathlib
import sys
from typing import Any


ROOT = pathlib.Path(__file__).resolve().parents[6]
BASE = ROOT / ".caprmedio_caprmedio/_projection/core-entity-review"
NODES = BASE / "nodes"
INPUT = NODES / "inputs/nodes.batch-8.input.json"
PRIOR_REVIEW = NODES / "nodes.batch-8.review.json"
DISPOSITIONS = NODES / "nodes.dispositions.json"
CANDIDATE = BASE / "presentation/operator.entity-graph.candidate.json"
BASELINE = BASE / "baseline.inventory.json"
OUTPUT = BASE / "consolidated/reviews/batch-8.review.json"
EXPECTED_CANDIDATE_SHA = "99e7710f5ef83df2b1f3ec1ef4142547655e63bef7415266c5521380da7fa99b"
EXPECTED_INPUT_SHA = "c7652bc1108b67b4fa9b9d037c78a9093ee2a78043f71bc244dec18033588b2b"
EXPECTED_BASELINE_SHA = "bc5d99e91fb7dd4dcb42e59ff33cc24cff1d0901c5904764394c769aaa0a9430"
EXPECTED_PRIOR_REVIEW_SHA = "1b9d751f95aa71486908b53b3d7f3f9825defae137be3d8792d45177587c48f8"
EXPECTED_BATCH_REVIEW_SHA = "ef376294fceedd369713f2c1b5aee0bb2b0a1ca657b4c7ec14705cbef5aa61ab"
CAPTURED_COMMIT = "a971d0e00c33c779f485fc8cad63194894d440fb"
ROOTS = {"Artifact", "Scope Unit", "Actor", "Relation", "Revision", "Carrier", "Execution"}

sys.path.insert(0, str(NODES / "support"))
from snapshot_sources import read_source, source_pins, verify_snapshot  # noqa: E402


ROLE_VIEW = {
    "Requirement": "R",
    "Method": "M",
    "Evaluation": "E",
    "Delivery": "D",
    "Operations": "O",
    "Concern": "C",
}

SYNTAX_RULES = [
    "$.entity_vs_syntax_rules[0]",
    "$.entity_vs_syntax_rules[1]",
    "$.entity_vs_syntax_rules[2]",
    "$.authority.complete_706_identity_remapping",
]
SUBJECT_RULES = [
    "$.content_direction",
    "$.terms_graph_boundary",
    "$.entity_vs_syntax_rules[0]",
]
RELATION_RULES = [
    "$.relation_type_model",
    "$.relation_type_model.endpoint_boundary",
    "$.graph_model",
]
EXECUTION_RULES = [
    "$.root_entities[6]",
    "$.execution_definition_policy",
    "$.m_e_root_question",
]
CARRIER_RULES = [
    "$.root_entities[5]",
    "$.carrier_delivery_model",
    "$.entity_identity_model.carrier_identity",
]
SCOPE_RULES = [
    "$.root_entities[1]",
    "$.entity_identity_model.scope_unit",
    "$.entity_identity_model.scope_unit_rename",
]
HISTORY_RULES = [
    "$.history_model",
    "$.atom_versioning",
    "$.review_backlog.deliberately_deferred",
]
PROJECTION_RULES = [
    "$.projection_member_model",
    "$.entity_representation_rules[1]",
    "$.authority",
]
DELIVERY_RULES = [
    "$.carrier_delivery_model",
    "$.entity_representation_rules[0]",
]


# These are display-only candidate comparisons.  No entry below admits a
# native root, edge, parser grammar, or migrated Subject.
POSITIVE: dict[str, dict[str, Any]] = {
    "Structural Coordinate": {
        "action": "syntax_context",
        "root": None,
        "path": None,
        "note": "The candidate has no Structural Coordinate root; preserve the captured locator as structural display context without inferring a subtype or edge from coordinate syntax.",
        "preserved": [
            "The defined Structural Coordinate remains a derived locator, not a new candidate root.",
            "Scope Unit ordering and Local Order qualification remain separate from candidate Entity identity.",
        ],
    },
    "Structural Entity": {
        "action": "syntax_context",
        "root": None,
        "path": None,
        "note": "The seven-root candidate does not make Structural Entity a new root; retain the captured term and its provenance without assigning it to Artifact or Scope Unit.",
        "preserved": [
            "Structural Entity remains distinct from its Carrier and from any binding metadata.",
            "The captured identity is not replaced by a heading-derived candidate subtype.",
        ],
    },
    "Structural Level": {
        "action": "syntax_context",
        "root": None,
        "path": None,
        "note": "Structural Level remains a captured structural qualifier; the candidate does not define it as a root or native edge.",
        "preserved": [
            "Structural level remains distinct from Scope Unit identity and Local Order.",
            "No hierarchy or endpoint is inferred from the label alone.",
        ],
    },
    "Structural Path": {
        "action": "syntax_context",
        "root": None,
        "path": None,
        "note": "Structural Path remains display/context syntax; the candidate's typed Relations remain canonical and no path string is promoted to a native edge.",
        "preserved": [
            "A captured structural path remains distinct from a Carrier filename or path.",
            "Path notation does not replace the original identity or source references.",
        ],
    },
    "Subject": {
        "action": "syntax_context",
        "root": None,
        "path": None,
        "note": "Subject remains a captured content and graph-input concept; the candidate adds no eighth Subject root and does not turn Subject notation into a native edge.",
        "preserved": [
            "Subject identity remains separate from its source Atom and from candidate display syntax.",
            "Substance and Substance Scope directions do not erase captured Subject meanings.",
        ],
    },
    "Subject Assignment": {
        "action": "syntax_context",
        "root": None,
        "path": None,
        "note": "Subject Assignment remains a method-level assignment context; the candidate does not introduce an Assignment root or infer a relation from the heading.",
        "preserved": [
            "Assignment remains distinct from the Subject it assigns and from a native Relation kind.",
            "The complete captured Main Content remains the evidence boundary.",
        ],
    },
    "Subject Expression": {
        "action": "syntax_context",
        "root": None,
        "path": None,
        "note": "Subject Expression remains canonical display syntax and validation context; /, :, and related notation do not create a native relation or subtype.",
        "preserved": [
            "Bearer and allowed-value qualification remain distinct from the expression string.",
            "Terms and their separate graph boundary remain preserved.",
        ],
    },
    "Subject Expression Evaluation": {
        "action": "syntax_context",
        "root": None,
        "path": None,
        "note": "The captured evaluation boundary is retained as a role-centred check context; the candidate does not add an Evaluation root and actual checks remain Executions.",
        "preserved": [
            "Invalid bearer, allowed-value, Term-resolution, and composite-expression cases remain qualified.",
            "Evaluation context is not collapsed into a Property or Relation identity.",
        ],
    },
    "Subject Expression Writing": {
        "action": "syntax_context",
        "root": None,
        "path": None,
        "note": "Subject Expression Writing remains method context for canonical references and qualification; no separate Method root or copied target Entity is inferred.",
        "preserved": [
            "Canonical reference writing remains distinct from the referenced bearer or allowed value.",
            "The notation remains non-authoritative candidate presentation.",
        ],
    },
    "Subject Path": {
        "action": "syntax_context",
        "root": None,
        "path": None,
        "note": "Subject Path remains a captured path/context identity; the candidate's relation endpoint rules do not make path nesting a native structural relation.",
        "preserved": [
            "Subject Path remains distinct from Structural Path and from Carrier storage paths.",
            "Original path references remain queryable without a replacement identity.",
        ],
    },
    "Subject Projection Derivation": {
        "action": "projection_view",
        "root": None,
        "path": None,
        "note": "The captured derivation rule maps to the candidate's Projection view boundary: derived instances keep source Atom IDs and Versions, while rebuild history belongs to the Projection set.",
        "preserved": [
            "A derived Atom remains separate from its source authority while retaining source ID and Version.",
            "Projection rebuild tracking does not increment the source Atom Version Number.",
        ],
    },
    "Subtree-owned Atoms": {
        "action": "syntax_context",
        "root": None,
        "path": None,
        "note": "Subtree ownership remains an applicability/ownership context around Scope Units; the candidate does not infer a new child Entity or native edge from the set label.",
        "preserved": [
            "Owning Scope Unit remains distinct from the owned Atom instances.",
            "A set of owned Atoms does not create a separate lifecycle root.",
        ],
    },
    "Subtree-targeting Atoms": {
        "action": "syntax_context",
        "root": None,
        "path": None,
        "note": "Subtree targeting remains targeting/query context; no Target Set root or native relation is inferred solely from the qualified label.",
        "preserved": [
            "Targeting meaning remains distinct from Scope Unit ownership.",
            "The targeted Atom identities and their constraints remain unchanged.",
        ],
    },
    "Targeting Atoms": {
        "action": "syntax_context",
        "root": None,
        "path": None,
        "note": "Targeting Atoms remains an operation/query context; the candidate does not promote the targeting set to a root or silently choose relation endpoints.",
        "preserved": [
            "Targeting remains distinct from owning or carrying an Atom.",
            "Existing target-selection queries remain separate from native Relation admission.",
        ],
    },
    "Term": {
        "action": "syntax_context",
        "root": None,
        "path": None,
        "note": "Term remains in the separate Terms graph; the candidate explicitly does not add Term as an eighth Entities-Graph root or admit a new cross-graph Relation.",
        "preserved": [
            "Term identity remains distinct from Subject Expression and from the Entities Graph roots.",
            "No cross-graph link is inferred from a term occurrence or slash path.",
        ],
    },
    "Terms Graph Construction Step": {
        "action": "operation_or_method",
        "root": None,
        "path": None,
        "note": "The captured construction step remains an Operation context in the separate Terms graph; it does not create a Method root or an Entities-Graph Term node.",
        "preserved": [
            "The construction step remains distinct from the resulting Terms graph and its Terms.",
            "Operation context does not imply an actual Execution or cross-graph Relation.",
        ],
    },
    "Type": {
        "action": "syntax_context",
        "root": None,
        "path": None,
        "note": "The broad captured Type identity is retained without collapsing qualified allowed-value domains; the Type/Kind equivalence applies only to the same Relation concept in its groups.",
        "preserved": [
            "General Type meaning remains distinct from Relation Type/Kind grouping.",
            "Qualified Status fields and allowed-value domains remain separate and constrained.",
        ],
    },
    "Unit": {
        "action": "inherit",
        "root": "Scope Unit",
        "path": "Scope Unit",
        "note": "The captured Unit shorthand inherits the candidate Scope Unit context; stable identity remains (project prefix)-SU-(number), with no folder rename or native migration.",
        "preserved": [
            "Scope Unit identity is the stable project-prefix SU number, not a changeable name or path.",
            "Project-root folder names remain outside the metadata naming rule.",
        ],
    },
    "Work Sequence Number": {
        "action": "syntax_context",
        "root": None,
        "path": None,
        "note": "The captured positive ordinal remains a sequence constraint for direct Plans; the candidate does not establish its owning root or dependent-field path, and it must not be assigned to Atom identity or Version Number.",
        "preserved": [
            "Work Sequence Number remains a Plan-ordering value, not an Atom ID or source Version.",
            "Positive ordering and uniqueness constraints remain distinct from lifecycle history.",
        ],
    },
    "Workflow": {
        "action": "operation_or_method",
        "root": None,
        "path": None,
        "note": "Workflow is retained as reusable Operation-definition context; the candidate keeps definitions distinct from actual Execution and does not add a separate Workflow or Method root.",
        "preserved": [
            "Reusable Workflow definitions remain distinct from Workflow Run instances.",
            "Repeatability is an Operator choice; no automatic O-Atom or repeatability rule is inferred.",
        ],
    },
    "Workflow Run": {
        "action": "retain",
        "root": "Execution",
        "path": "Execution.Workflow Run",
        "note": "Workflow Run maps to the candidate Execution root as an actual run; the reusable Workflow definition remains separate and Git history is not replaced by Journal body snapshots.",
        "preserved": [
            "Actual Workflow Run remains distinct from the reusable Workflow definition.",
            "An ad hoc Execution need not have an O Atom; repeatability remains an Operator decision.",
        ],
    },
    "Workflow/Carrier": {
        "action": "delivery_policy",
        "root": "Carrier",
        "path": "Carrier",
        "note": "The captured Workflow carrier layout is retained as a general Delivery policy under the separate Carrier root; Carrier ID remains separate from filename/path and no per-Property Carrier edge is inferred.",
        "preserved": [
            "Carrier remains a separate root and its identity is Carrier ID, not its storage filename or path.",
            "General D policy may cover multiple entities without a per-Property Carrier Relation Type or D Atom.",
        ],
    },
    "Workflow/Relation Kind": {
        "action": "retain",
        "root": "Relation",
        "path": "Relation.Relation Type",
        "note": "The captured Workflow control-flow kind is retained under the candidate Relation root; Relation Kind and Relation Type are one grouped concept with directed, endpoint-constrained connections and no new native admission.",
        "preserved": [
            "Relation Type and Relation Kind remain the same concept within the Workflow group.",
            "Directed endpoints and graph ownership remain constrained; the display heading is not a new edge.",
        ],
    },
    "Workflow/Relation Kind: On Result": {
        "action": "retain",
        "root": "Relation",
        "path": "Relation.Relation Type: On Result",
        "note": "The captured On Result condition is retained as a qualified Relation Type in the Workflow group; endpoint direction and the source Step Run result condition remain distinct without a new root.",
        "preserved": [
            "On Result remains a qualified relation-type condition, not a separate Type/Kind ontology.",
            "Source Step Run, target Step, direction, and endpoint constraints remain distinct.",
        ],
    },
}


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def load(path: pathlib.Path) -> tuple[dict[str, Any], bytes]:
    raw = path.read_bytes()
    return json.loads(raw), raw


def candidate_rules(identity: str, action: str) -> list[str]:
    if identity.startswith("Structural"):
        return list(SYNTAX_RULES)
    if identity.startswith("Subject"):
        return list(SUBJECT_RULES)
    if identity.startswith("Subtree") or identity == "Targeting Atoms":
        return [*SCOPE_RULES, *SYNTAX_RULES[:3]]
    if identity.startswith("Term") or identity.startswith("Terminology") or identity.startswith("Terms Graph"):
        return ["$.terms_graph_boundary", *SYNTAX_RULES[:2]]
    if identity.startswith("Workflow"):
        if action == "delivery_policy":
            return list(CARRIER_RULES)
        if "Relation Kind" in identity:
            return list(RELATION_RULES)
        return list(EXECUTION_RULES)
    if identity == "Unit" or identity.startswith("scope-") or identity == "project-containment graph":
        return list(SCOPE_RULES)
    if identity == "Work Sequence Number":
        return ["$.entity_vs_syntax_rules[0]", "$.m_e_root_question", "$.authority.complete_706_identity_remapping"]
    if identity == "Type" or identity == "Type-Qualified Status Validation":
        return ["$.relation_type_model", "$.content_direction", *SYNTAX_RULES[:2]]
    if identity in {"Uncertain Lineage Impact Disposition", "Update-Required Lineage Impact Disposition"}:
        return ["$.history_model", "$.content_direction", "$.entity_vs_syntax_rules[1]"]
    if identity == "Translation":
        return ["$.content_direction", "$.terms_graph_boundary", "$.m_e_root_question"]
    if identity == "Tool":
        return ["$.execution_definition_policy", "$.carrier_delivery_model", "$.graph_model"]
    if identity == "Target Set":
        return ["$.graph_model", "$.root_entities[1]", "$.entity_vs_syntax_rules[2]"]
    if identity == "applicability":
        return ["$.content_direction.scope_omission", "$.root_entities[1]", "$.authority"]
    if identity.startswith("Work Journal") or identity in {"lifecycle", "lifecycle-traceability", "runtime", "Verification"}:
        return list(HISTORY_RULES)
    if identity in {"artifact-catalog", "artifact-model", "atom-boundary", "authority", "classification", "extension-model", "external-boundary", "framework-boundary", "interaction", "language", "principles", "provenance", "relation validation", "relation-model", "requirement-topology", "semantics", "settings specification", "subject"}:
        return ["$.authority", "$.graph_model", *SYNTAX_RULES[:2]]
    if identity in {"TOML", "YAML"}:
        return list(DELIVERY_RULES)
    if identity in {"Subject Relation Kind", "Subject Relation Kind: DEPENDS_ON"}:
        return list(RELATION_RULES)
    return ["$.authority", "$.entity_vs_syntax_rules[0]", "$.review_backlog.authoring_and_implementation"]


def gap_note(identity: str) -> str:
    if identity.startswith("Structural Entity/"):
        return "The slash-qualified structural label may describe a relation, containment, or carrier qualifier, but the captured Main Content does not establish its exact candidate identity, direction, or endpoints."
    if identity == "Structural Parent Relation":
        return "The captured parent-relation occurrence does not establish the exact candidate Relation direction, graph ownership, or permitted endpoints."
    if identity == "Subject Relation Kind":
        return "The candidate groups Relation Type and Relation Kind, but the captured source does not establish the exact Subject relation group or its endpoint domain."
    if identity == "Subject Relation Kind: DEPENDS_ON":
        return "The captured source does not establish whether DEPENDS_ON is an allowed-value domain, its owning Property, or its value direction."
    if identity in {"TOML", "YAML"}:
        return "A format label alone does not establish a Carrier identity or a general D policy mapping."
    if identity == "Target Set":
        return "The captured source does not establish whether Target Set is a dependent field, a query view, or a Relation endpoint set."
    if identity == "Term/name":
        return "The qualified name label does not establish its owning Term field or a native property relation."
    if identity == "Terminology Projection Derivation":
        return "The candidate keeps the Terms graph separate and provides a Projection boundary, but the captured identity is not mapped to either without inventing a cross-graph edge."
    if identity == "Terms Graph":
        return "The candidate says Terms belong to a separate graph, but the exact graph identity and any allowed cross-graph binding are not established by the captured sources."
    if identity.startswith("Tool/Workflow Operations"):
        return "The qualified workflow-tool label does not establish a dependent field, reusable Operation definition, or actual Execution identity."
    if identity == "Tool":
        return "The captured Tool occurrences span delivery, evaluation, method, and operations; the candidate has no exact Tool root or replacement mapping."
    if identity == "Translation":
        return "The captured Translation occurrences span requirement, method, and evaluation contexts; no candidate root or cross-graph mapping is established."
    if identity in {"Type-Qualified Status Validation", "Uncertain Lineage Impact Disposition", "Update-Required Lineage Impact Disposition"}:
        return "The candidate preserves qualified Status and lineage distinctions, but the captured source does not establish the exact dependent field or validation identity."
    if identity == "Verification":
        return "The captured Verification meanings span several source roles; the candidate permits Execution checks but does not establish this exact identity's path."
    if identity == "Work Journal":
        return "The candidate says Journal records what happened while Git preserves Atom contents and versions, but the captured identity does not resolve a reusable definition, actual run, or durable record path."
    if identity.startswith("Work Journal/Event/Carrier"):
        return "The candidate keeps Carrier identity and general D policy separate from Journal records, but the captured identity does not establish the event serialization field or relation."
    if identity.startswith("Work Journal/Event/Type"):
        return "The candidate keeps Relation Type/Kind grouping and Journal records distinct, but the captured identity does not establish the event Type field or value domain."
    if identity == "Work Journal/Event":
        return "The captured event occurrences do not establish whether this is a Journal record, an Execution, or a durable event field."
    if identity.startswith("Work Journal/Projection Rebuild"):
        return "The candidate tracks Projection rebuilds as a whole and Journal records separately, but the captured identity does not establish the exact rebuild event or completion field."
    if identity == "Work Journal/Record":
        return "The candidate distinguishes a Journal record from the event itself, but the captured sources do not establish the record's exact dependent fields or relations."
    if identity in {"artifact-catalog", "artifact-model"}:
        return "The candidate selects Artifact as a root, but the captured source does not establish whether this identity is the root itself, a definition, or a derived catalog/view."
    if identity == "atom-boundary":
        return "The candidate defines Artifact/Atom as a dependent-entity boundary, but the captured sources do not establish a safe replacement for this qualified identity."
    if identity == "authority":
        return "The candidate separates source authority, Scope Unit ownership, and derived Projection views, but the captured source does not establish this label's exact owner or relation."
    if identity == "classification":
        return "The candidate preserves separate classification axes without multiplying types, but the captured source does not establish this identity's exact axis or dependent field."
    if identity in {"continuous-improvement", "development-flow", "extension-model", "external-boundary", "framework-boundary", "principles"}:
        return "The candidate has no dedicated root for this broad contextual label, and the captured source does not establish a dependent field, relation, or view mapping."
    if identity == "evaluation":
        return "The candidate treats Evaluation as a role-centred view and actual checks as Executions, but the captured source does not establish this identity's exact path."
    if identity == "interaction":
        return "The captured source does not resolve whether Interaction is an Actor, Relation, Execution, or content context."
    if identity == "language":
        return "The captured language occurrences may be content or delivery context, but the source does not establish a candidate root or D policy mapping."
    if identity == "lifecycle":
        return "The candidate defines lifecycle boundaries across roots, but the captured source does not establish a standalone Lifecycle identity."
    if identity == "lifecycle-traceability":
        return "The candidate separates active versions, archived history, Journal records, and Projection rebuilds, but the captured source does not establish this label's exact mapping."
    if identity == "project-containment graph":
        return "The candidate defines Scope Unit ownership and recursive nesting, but the captured graph label does not establish the exact Scope Unit or Relation identity."
    if identity == "provenance":
        return "The candidate has source links and rebuild provenance, but the captured source does not establish a standalone Provenance entity or field."
    if identity == "relation validation":
        return "The candidate constrains Relation endpoints, but the captured source does not establish a separate Relation Validation entity or operation."
    if identity == "relation-model":
        return "The candidate selects typed Relations with constrained endpoints, but the captured source does not establish this broad label's exact relation catalogue or ownership."
    if identity == "requirement-topology":
        return "The candidate keeps R content and Scope Unit topology distinct, but the captured source does not establish this label's exact topology view."
    if identity == "runtime":
        return "The candidate defers live or resumable Execution-state storage, but the captured source does not establish a runtime Entity mapping."
    if identity == "scope-topology":
        return "The candidate selects Scope Unit ownership, recursive nesting, and stable IDs, but the captured source does not establish this broad topology identity's exact path."
    if identity == "semantics":
        return "The candidate keeps semantics as content/context rather than a root, but the captured source does not establish a more specific mapping."
    if identity == "settings specification":
        return "The candidate separates settings boundaries from field-level D specifications, but the captured source does not establish an exact Carrier or dependent-field mapping."
    if identity == "subject":
        return "The lowercase label is not automatically the retained Subject identity; the candidate does not establish whether it is an alias, context, or distinct source term."
    return f"The captured source does not establish the exact candidate mapping for {identity!r}; no subtype, edge, or replacement identity is inferred."


def content_view(atom_ids: list[str], pins: dict[str, dict[str, Any]]) -> str:
    codes = {ROLE_VIEW.get(pins[atom_id]["content_role"]) for atom_id in atom_ids}
    codes.discard(None)
    if len(codes) == 1:
        return next(iter(codes))
    if len(codes) > 1:
        return "mixed"
    return "unclassified"


def validate_candidate_path(root: str | None, path: str | None) -> None:
    """Validate the candidate's compact display notation only.

    Slash is reserved for the candidate's explicit root narrowing (currently
    Artifact/Atom); dependent fields use dots and an allowed value follows a
    colon.  These paths never become native selectors or graph edges.
    """
    if root is None:
        assert path is None
        return
    assert root in ROOTS
    if path is None:
        return
    assert isinstance(path, str) and path.strip()
    if "/" in path:
        assert path.startswith("Artifact/Atom") and path.count("/") == 1, path
    else:
        assert path == root or path.startswith(f"{root}."), (root, path)
    if ":" in path:
        head, value = path.split(":", 1)
        assert "." in head and value.strip(), path


def verify_evidence(item: dict[str, Any]) -> None:
    pin = source_pins()[item["atom_id"]]
    for field in ("atom_revision", "carrier_path", "carrier_sha256"):
        assert item[field] == pin[field], (item["atom_id"], field)
    raw = read_source(item["atom_id"])
    assert sha(raw) == item["carrier_sha256"], item["atom_id"]
    lines = raw.decode().splitlines()
    start, end = item["start_line"], item["end_line"]
    assert isinstance(start, int) and isinstance(end, int) and 1 <= start <= end <= len(lines), item
    quote = "\n".join(lines[start - 1 : end])
    assert item["quote"] in (quote, quote + "\n"), item["atom_id"]
    assert sha(item["quote"].encode()) == item["text_sha256"], item["atom_id"]


def build() -> tuple[dict[str, Any], bytes]:
    input_data, input_raw = load(INPUT)
    candidate, candidate_raw = load(CANDIDATE)
    baseline, baseline_raw = load(BASELINE)
    dispositions, dispositions_raw = load(DISPOSITIONS)
    prior_review, prior_raw = load(PRIOR_REVIEW)

    assert sha(candidate_raw) == EXPECTED_CANDIDATE_SHA
    assert sha(input_raw) == EXPECTED_INPUT_SHA
    assert sha(baseline_raw) == EXPECTED_BASELINE_SHA
    assert sha(dispositions_raw) == EXPECTED_PRIOR_REVIEW_SHA
    assert sha(prior_raw) == EXPECTED_BATCH_REVIEW_SHA
    assert input_data["batch"] == 8 and input_data["source_task"] == "CA-P-1936"
    assert input_data["identity_count"] == 81
    assert baseline["inventory_sha256"] == "23394abaf6e9c18a585cf3146aedd0a80df166c9dd82be6e86ed7c3c56780bdc"

    snapshot = verify_snapshot()
    assert snapshot == {
        "source_context": "captured_snapshot",
        "git_commit": CAPTURED_COMMIT,
        "source_pins_checked": 951,
        "verification": "pass",
        "current_core_claimed": False,
    }

    pins = {item["atom_id"]: item for item in baseline["source_atoms"]}
    assert pins == source_pins()
    marks = {item["identity"]: item for item in dispositions["node_disposition_marks"]}
    old_rows = {item["identity"]: item for item in prior_review["nodes"]}
    input_nodes = input_data["nodes"]
    identities = [item["identity"] for item in input_nodes]
    assert len(identities) == 81 and len(set(identities)) == 81
    assert set(identities) == set(marks) & set(identities)
    assert set(POSITIVE) == {identity for identity in identities if marks[identity]["review_row"]["disposition"] == "retain"}
    assert set(identities) - set(POSITIVE) == {identity for identity in identities if marks[identity]["review_row"]["disposition"] == "question"}

    evidence_catalogue: dict[str, dict[str, Any]] = {}
    rows: list[dict[str, Any]] = []
    for item in input_nodes:
        identity = item["identity"]
        mark = marks[identity]
        old = mark["review_row"]
        assert old == old_rows[identity]
        refs = list(mark["scoped_refs"]["global_evidence_refs"])
        assert refs and all(ref in dispositions["evidence_catalogue"] for ref in refs)
        for ref in refs:
            evidence_catalogue[ref] = dispositions["evidence_catalogue"][ref]
            verify_evidence(evidence_catalogue[ref])
        checked = list(old["checked_source_atom_ids"])
        assert checked
        for atom_id in checked:
            assert atom_id in pins
            read_source(atom_id)
        view = content_view(checked, pins)
        rules = candidate_rules(identity, POSITIVE.get(identity, {}).get("action", "review_required"))
        for rule in rules:
            assert rule.startswith("$.")
            current: Any = candidate
            for component in rule[2:].split("."):
                if "[" in component:
                    name, index = component[:-1].split("[", 1)
                    current = current[name][int(index)]
                else:
                    current = current[component]
        if identity in POSITIVE:
            decision = POSITIVE[identity]
            confidence = old["confidence_percent"]
            assert confidence >= 90
            validate_candidate_path(decision["root"], decision["path"])
            row = {
                "identity": identity,
                "prior_disposition": old["disposition"],
                "action": decision["action"],
                "candidate_root": decision["root"],
                "candidate_path": decision["path"],
                "content_view": view,
                "confidence_percent": confidence,
                "reason": f"{old['reason']} Candidate comparison: {decision['note']}",
                "operator_rules": rules,
                "evidence_refs": refs,
                "checked_source_atom_ids": checked,
                "preserved_distinctions": decision["preserved"],
                "question": None,
            }
        else:
            note = gap_note(identity)
            row = {
                "identity": identity,
                "prior_disposition": old["disposition"],
                "action": "review_required",
                "candidate_root": None,
                "candidate_path": None,
                "content_view": view,
                "confidence_percent": 0,
                "reason": (
                    f"Captured snapshot review for {identity!r} checked {len(checked)} source Atom(s) "
                    f"against {', '.join(refs)} but did not establish a positive candidate mapping. "
                    f"Candidate comparison: {note} Keep the mapping pathless until targeted review "
                    "supplies positive meaning evidence; no native admission or replacement is made."
                ),
                "operator_rules": rules,
                "evidence_refs": refs,
                "checked_source_atom_ids": checked,
                "preserved_distinctions": [
                    f"The original identity {identity!r}, its captured source references, and qualified meaning remain unchanged.",
                    "Candidate rules remain separate from captured Core evidence; no native admission, subtype, edge, or replacement identity is made.",
                    note,
                ],
                "question": {
                    "kind": "source_gap",
                    "text": f"Review task only: captured Main Content for {identity!r} ({', '.join(refs)}) does not establish a positive candidate mapping. {note} Do not ask the Operator to choose a design until that meaning evidence is available.",
                },
            }
        rows.append(row)

    # The accepted catalogue also contains spans used by check-level meaning
    # notes but not repeated in a row's primary evidence_refs.  Carry every
    # batch-8 global key forward so the receipt remains closed over that
    # source-reviewed catalogue.
    for ref, item in dispositions["evidence_catalogue"].items():
        if ref.startswith("CA-P-1936/batch-8/"):
            evidence_catalogue[ref] = item
            verify_evidence(item)
    assert len(rows) == 81 and len({row["identity"] for row in rows}) == 81
    assert len(evidence_catalogue) == 78
    receipt = {
        "schema_version": 1,
        "batch": 8,
        "kind": "Captured nodes against Operator candidate",
        "non_authoritative": True,
        "native_admission": "not_performed",
        "source_migration": "not_performed",
        "captured_core_commit": CAPTURED_COMMIT,
        "candidate_sha256": EXPECTED_CANDIDATE_SHA,
        "input_sha256": EXPECTED_INPUT_SHA,
        "baseline_sha256": EXPECTED_BASELINE_SHA,
        "prior_review_sha256": EXPECTED_PRIOR_REVIEW_SHA,
        "review_method": (
            "Compared all 81 captured identities with the latest Operator candidate using the accepted "
            "batch-8 meanings and the global disposition evidence catalogue. Exact captured Main Content "
            "spans were rechecked through snapshot_sources.py against the pinned Git snapshot. Operator "
            "directions are display/proposal inputs only; this is not a fresh exhaustive audit of all 951 "
            "sources or an adoption/remapping operation."
        ),
        "nodes": rows,
    }
    raw = (json.dumps(receipt, ensure_ascii=False, indent=2) + "\n").encode()
    return receipt, raw


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--persist", action="store_true", help="create the assigned receipt if absent")
    parser.add_argument("--output", type=pathlib.Path, default=OUTPUT)
    args = parser.parse_args()
    receipt, raw = build()
    if args.persist:
        if args.output.exists():
            assert args.output.read_bytes() == raw, "existing receipt differs; refusing overwrite"
            state = "verified-existing"
        else:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_bytes(raw)
            state = "created"
    else:
        state = "checked-no-write"
    rows = receipt["nodes"]
    summary = {
        "identity_count": len(rows),
        "action_counts": dict(collections.Counter(row["action"] for row in rows)),
        "prior_disposition_counts": dict(collections.Counter(row["prior_disposition"] for row in rows)),
        "review_required_count": sum(row["action"] == "review_required" for row in rows),
        "evidence_span_count": len({ref for row in rows for ref in row["evidence_refs"]}),
        "captured_source_count": len({atom_id for row in rows for atom_id in row["checked_source_atom_ids"]}),
        "snapshot_verification": "pass",
    }
    print(json.dumps({"state": state, **summary}, sort_keys=True))


if __name__ == "__main__":
    main()
