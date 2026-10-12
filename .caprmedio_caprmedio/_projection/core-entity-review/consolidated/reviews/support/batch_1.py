"""Create-only consolidated candidate review receipt for captured batch 1.

The receipt is derived from the accepted captured batch-1 rows and the global
disposition/evidence catalogue.  It verifies the quoted Main Content against
the Operator-selected Git snapshot and never reads current Core as evidence.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any


ROOT = Path.cwd().resolve()
REVIEW_DIR = ROOT / ".caprmedio_caprmedio/_projection/core-entity-review/consolidated/reviews"
OUTPUT = REVIEW_DIR / "batch-1.review.json"
INPUT = ROOT / ".caprmedio_caprmedio/_projection/core-entity-review/nodes/inputs/nodes.batch-1.input.json"
OLD_REVIEW = ROOT / ".caprmedio_caprmedio/_projection/core-entity-review/nodes/nodes.batch-1.review.json"
DISPOSITIONS = ROOT / ".caprmedio_caprmedio/_projection/core-entity-review/nodes/nodes.dispositions.json"
BASELINE = ROOT / ".caprmedio_caprmedio/_projection/core-entity-review/baseline.inventory.json"
CANDIDATE = ROOT / ".caprmedio_caprmedio/_projection/core-entity-review/presentation/operator.entity-graph.candidate.json"
SNAPSHOT_CONTEXT = ROOT / ".caprmedio_caprmedio/_projection/core-entity-review/nodes/snapshot.context.md"
NODE_CONTRACT = ROOT / ".caprmedio_caprmedio/_projection/core-entity-review/nodes/contract.md"
SCOPE_DECISION = ROOT / ".caprmedio_caprmedio/_projection/core-entity-review/nodes/scope.omission.decision.md"
SNAPSHOT_COMMIT = "a971d0e00c33c779f485fc8cad63194894d440fb"
EXPECTED_CANDIDATE_SHA256 = "99e7710f5ef83df2b1f3ec1ef4142547655e63bef7415266c5521380da7fa99b"
EXPECTED_BATCH = 1


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def canonical(value: Any) -> bytes:
    return json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False
    ).encode("utf-8")


def load_snapshot_reader():
    path = ROOT / ".caprmedio_caprmedio/_projection/core-entity-review/nodes/support/snapshot_sources.py"
    spec = importlib.util.spec_from_file_location("captured_snapshot_sources_batch_1", path)
    assert spec and spec.loader, path
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def evidence_line_check(item: dict[str, Any], reader: Any, pins: dict[str, Any]) -> None:
    atom_id = item["atom_id"]
    assert atom_id in pins, ("evidence-source-not-pinned", atom_id)
    pin = pins[atom_id]
    for field in ("atom_revision", "carrier_path", "carrier_sha256"):
        assert item[field] == pin[field], ("evidence-pin-mismatch", atom_id, field)
    raw = reader.read_source(atom_id)
    assert sha(raw) == pin["carrier_sha256"], ("captured-source-hash-mismatch", atom_id)
    lines = raw.decode("utf-8").splitlines()
    start, end = item["start_line"], item["end_line"]
    assert type(start) is int and type(end) is int and 1 <= start <= end <= len(lines)
    quoted = "\n".join(lines[start - 1 : end])
    assert item["quote"] in (quoted, quoted + "\n"), ("quote-span-mismatch", atom_id, start, end)
    assert item["text_sha256"] == sha(item["quote"].encode("utf-8")), ("quote-hash-mismatch", atom_id)
    headings = [line for line in lines[:start] if line.startswith(("# ", "## ", "### "))]
    assert headings and not headings[-1].startswith("# Summary"), ("non-content-evidence", atom_id, start)


def dedupe(values: list[str]) -> list[str]:
    return list(dict.fromkeys(values))


def rules_for(root: str | None, *, substance: bool = False, carrier: bool = False,
              history: bool = False, projection: bool = False, syntax: bool = False,
              actor: bool = False, execution: bool = False) -> list[str]:
    rules: list[str] = []
    if root == "Artifact":
        rules += ["root_entities[0]", "dependent_entities", "entity_identity_model.dependent_entity"]
    elif root == "Scope Unit":
        rules += ["root_entities[1]", "entity_identity_model.scope_unit"]
    elif root == "Actor":
        rules += ["root_entities[2]", "entity_identity_model.actor"]
    elif root == "Relation":
        rules += ["root_entities[3]", "graph_model", "relation_type_model"]
    elif root == "Revision":
        rules += ["root_entities[4]", "history_model"]
    elif root == "Carrier":
        rules += ["root_entities[5]", "entity_identity_model.carrier_identity", "carrier_delivery_model"]
    elif root == "Execution":
        rules += ["root_entities[6]", "execution_definition_policy"]
    if substance:
        rules.append("content_direction")
    if carrier and "carrier_delivery_model" not in rules:
        rules.append("carrier_delivery_model")
    if history:
        rules += ["history_model", "atom_versioning", "atom_lookup"]
    if projection:
        rules += ["entity_representation_rules", "projection_member_model"]
    if syntax:
        rules.append("entity_vs_syntax_rules")
    if actor and "entity_identity_model.actor" not in rules:
        rules.append("entity_identity_model.actor")
    if execution and "execution_definition_policy" not in rules:
        rules.append("execution_definition_policy")
    return dedupe(rules)


def classify(identity: str, old: dict[str, Any]) -> dict[str, Any]:
    """Return candidate-facing fields while retaining the old row's proof."""

    # The captured row is intentionally unresolved: the candidate direction
    # supplies a presentation name, but its single source does not establish
    # which Analysis model the old identity denotes.
    if identity == "Analysis":
        return {
            "action": "review_required",
            "candidate_root": None,
            "candidate_path": None,
            "content_view": "unclassified",
            "confidence_percent": old["confidence_percent"],
            "operator_rules": ["content_direction", "review_backlog.question_policy"],
            "candidate_note": "the candidate calls the Analysis role Question, but the captured source still lacks a positive model mapping",
            "preserved": [
                "Do not turn the candidate role label into retroactive Core evidence.",
                "Keep the captured Analysis identity and source gap visible for review.",
            ],
            "question": {
                "kind": "source_gap",
                "text": "Review task: CA-R-1611 distinguishes reverse-engineering results and proposed-versus-observed content but does not establish which candidate Analysis model this identity denotes; no candidate path is committed.",
            },
        }

    if identity == "Artifact":
        return {
            "action": "retain", "candidate_root": "Artifact", "candidate_path": "Artifact",
            "content_view": "mixed", "confidence_percent": old["confidence_percent"],
            "operator_rules": rules_for("Artifact"),
            "candidate_note": "the identity is the selected governed lifecycle root",
            "preserved": ["Artifact retains one lifecycle; named dependent Entities do not gain independent lifecycles."],
            "question": None,
        }
    if identity == "Actor":
        return {
            "action": "retain", "candidate_root": "Actor", "candidate_path": "Actor",
            "content_view": "R", "confidence_percent": old["confidence_percent"],
            "operator_rules": rules_for("Actor", actor=True),
            "candidate_note": "the identity is the selected Actor root",
            "preserved": ["Actor means who performs work; generic Actor Type is not one specific performer."],
            "question": None,
        }
    if identity == "AI Agent":
        return {
            "action": "rebase", "candidate_root": "Actor", "candidate_path": "Actor/AI Agent",
            "content_view": "R", "confidence_percent": old["confidence_percent"],
            "operator_rules": rules_for("Actor", actor=True),
            "candidate_note": "the candidate presents AI Agent as a bounded Actor Type rather than an eighth root",
            "preserved": ["AI Agent remains distinct as a qualified Actor Type with its captured authorization and confidence limits."],
            "question": None,
        }
    if identity == "AI Agent Delegation":
        return {
            "action": "review_required", "candidate_root": None, "candidate_path": None,
            "content_view": "R", "confidence_percent": 82,
            "operator_rules": ["content_direction", "review_backlog.question_policy"],
            "candidate_note": "the captured delegation is a structured authorization record, but the candidate selects no Delegation role or owner path",
            "preserved": [
                "Delegation keeps its Operator, Agent, action, scope, constraint, validity and revocation distinctions.",
                "Do not infer that every delegation is a dependent field of one Atom Claim; the candidate does not establish that bearer mapping.",
            ],
            "question": None,
        }
    if identity.startswith("AI Agent/"):
        return {
            "action": "inherit", "candidate_root": "Actor", "candidate_path": "Actor/AI Agent." + identity.split("/", 1)[1],
            "content_view": "R", "confidence_percent": old["confidence_percent"],
            "operator_rules": rules_for("Actor", actor=True),
            "candidate_note": "the qualified field remains attached to the AI Agent Actor Type and does not become a root",
            "preserved": ["Authorization and confidence are qualified Actor fields; they do not grant universal delegated authority."],
            "question": None,
        }
    if identity == "Action Run":
        return {
            "action": "rebase", "candidate_root": "Execution", "candidate_path": "Execution/Action Run",
            "content_view": "E", "confidence_percent": old["confidence_percent"],
            "operator_rules": rules_for("Execution", execution=True),
            "candidate_note": "the candidate reserves Action Run for one actual run under Execution",
            "preserved": ["Preview and definition states do not fabricate a successful actual Action Run."],
            "question": None,
        }
    if identity.startswith("Action"):
        tail = identity.replace("Action", "", 1).lstrip("/")
        path = "Artifact/Atom.Substance.Operation.Action" + (("." + tail.split(":", 1)[0].strip() + (":" + tail.split(":", 1)[1] if ":" in tail else "")) if tail else "")
        return {
            "action": "operation_or_method", "candidate_root": "Artifact", "candidate_path": path,
            "content_view": "O", "confidence_percent": old["confidence_percent"],
            "operator_rules": rules_for("Artifact", substance=True),
            "candidate_note": "the reusable Action definition is presented under the Operation role and remains distinct from an actual Execution",
            "preserved": ["Execution Kind and Agentic remain qualified operation-definition values, not new roots or actual runs."],
            "question": None,
        }
    if identity == "Active Atom Carrier Discovery":
        return {
            "action": "delivery_policy", "candidate_root": "Carrier", "candidate_path": "Carrier.Delivery Policy (Active Atom Carrier Discovery)",
            "content_view": "D", "confidence_percent": old["confidence_percent"],
            "operator_rules": rules_for("Carrier", carrier=True),
            "candidate_note": "the captured discovery constraint is presented as a general Carrier delivery policy",
            "preserved": ["Discovery remains scoped to selected Project-owned Markdown carriers with Active status."],
            "question": None,
        }
    if identity in {"Admit Methodology Expansion Mapping", "Apply Approved Source Corrections",
                    "Apply Structural Change", "Approved Change Reversal", "Approved Change Reversal Step",
                    "Assess Atom Update Identity", "Assess Lineage Impact", "Assess Prepared Result Conformance",
                    "Assess Source Conflicts", "Artifact Classification Resolution",
                    "Artifact query and fetch execution", "Artifact query and selected fetch",
                    "Atom Carrier Replacement", "Atom Carrier Validation", "Atom Content Authoring",
                    "Atom Claim Authoring", "Atom Claim Boundary Authoring", "Atom selection",
                    "Atom Tier Validation"}:
        if identity == "Atom selection":
            return {
                "action": "projection_view", "candidate_root": "Artifact", "candidate_path": "Artifact/Projection.Atom selection",
                "content_view": "P", "confidence_percent": old["confidence_percent"],
                "operator_rules": rules_for("Artifact", projection=True),
                "candidate_note": "the selected derived Atom sets are presented as a Projection view, while source Atoms remain authoritative",
                "preserved": ["Selection sets retain source Atom identity and do not become another authority."],
                "question": None,
            }
        if identity in {"Atom Carrier Validation", "Atom Tier Validation"}:
            content = "E"
        elif identity in {"Atom Claim Authoring", "Atom Claim Boundary Authoring"}:
            content = "M"
        else:
            content = "O"
        return {
            "action": "operation_or_method", "candidate_root": "Artifact",
            "candidate_path": "Artifact/Atom.Substance.Operation." + identity,
            "content_view": content, "confidence_percent": old["confidence_percent"],
            "operator_rules": rules_for("Artifact", substance=True, execution=content == "E"),
            "candidate_note": (
                "the captured authoring constraints remain a reusable Method view, distinct from any actual Execution"
                if content == "M" else
                "the captured reusable procedure/check is kept as an Operation definition or evaluation specification, not an actual Execution"
            ),
            "preserved": ["Definition, check specification and actual run remain separate; no new root is admitted."],
            "question": None,
        }
    if identity == "Atom":
        return {
            "action": "rebase", "candidate_root": "Artifact", "candidate_path": "Artifact/Atom",
            "content_view": "mixed", "confidence_percent": old["confidence_percent"],
            "operator_rules": rules_for("Artifact"),
            "candidate_note": "the candidate places Atom as a named dependent Entity inside Artifact",
            "preserved": ["Atom identity and captured smallest-governed meaning remain; its dependent fields do not gain separate lifecycles."],
            "question": None,
        }
    if identity == "Atom Collection" or identity.startswith("Atom Collection/"):
        tail = identity[len("Atom Collection"):].lstrip("/")
        if not tail:
            path = "Artifact/Atom Collection"
        elif ":" in tail:
            field, value = tail.split(":", 1)
            path = "Artifact/Atom Collection." + field.strip() + ":" + value
        else:
            path = "Artifact/Atom Collection." + tail.replace("/", ".")
        return {
            "action": "inherit", "candidate_root": "Artifact", "candidate_path": path,
            "content_view": "R", "confidence_percent": old["confidence_percent"],
            "operator_rules": rules_for("Artifact", syntax=True),
            "candidate_note": "the collection and its qualified fields remain dependent structural content rather than independent roots",
            "preserved": ["Collection grouping, direct containment and allowed-value domains remain distinct; grouping alone does not create another root."],
            "question": None,
        }
    if identity == "Atom Tier Validation/concrete cases":
        return {
            "action": "syntax_context", "candidate_root": None, "candidate_path": None,
            "content_view": "E", "confidence_percent": old["confidence_percent"],
            "operator_rules": rules_for(None, syntax=True),
            "candidate_note": "the captured concrete cases are contextual validation fixtures, not a candidate Entity",
            "preserved": ["Concrete validation fixtures remain traceable without being promoted to a native entity or taxonomy edge."],
            "question": None,
        }
    if identity.startswith("Atom Carrier/Filename"):
        tail = identity.split("/", 1)[1].replace("/", ".")
        return {
            "action": "delivery_policy", "candidate_root": "Carrier", "candidate_path": "Carrier/Atom Carrier." + tail,
            "content_view": "D", "confidence_percent": old["confidence_percent"],
            "operator_rules": rules_for("Carrier", carrier=True),
            "candidate_note": "filename rules are general Carrier representation policy, not Carrier identity or per-property graph edges",
            "preserved": ["Filename slug, token case and default-tier omission remain separate qualified serialization constraints."],
            "question": None,
        }
    if identity == "Atom Carrier":
        return {
            "action": "rebase", "candidate_root": "Carrier", "candidate_path": "Carrier/Atom Carrier",
            "content_view": "D", "confidence_percent": old["confidence_percent"],
            "operator_rules": rules_for("Carrier", carrier=True),
            "candidate_note": "the candidate keeps Carrier as a separate root and treats Atom Carrier as a qualified representation carrier",
            "preserved": ["Carrier identity is separate from filename/path and storage location."],
            "question": None,
        }
    if identity.startswith("Artifact/Carrier Placement"):
        tail = identity[len("Artifact/Carrier Placement"):].lstrip("/")
        path = "Carrier.Delivery Policy (Artifact Carrier Placement)"
        if tail:
            path += "." + tail.replace("/", ".")
        return {
            "action": "delivery_policy", "candidate_root": "Carrier", "candidate_path": path,
            "content_view": "D", "confidence_percent": old["confidence_percent"],
            "operator_rules": rules_for("Carrier", carrier=True),
            "candidate_note": "placement and status-subdirectory rules remain general Carrier delivery policy",
            "preserved": ["Placement conventions do not create a Directory Carrier for a status subdirectory."],
            "question": None,
        }
    if identity == "Artifact/Carrier":
        return {
            "action": "delivery_policy", "candidate_root": "Carrier", "candidate_path": "Carrier.Delivery Policy (Artifact Carrier)",
            "content_view": "D", "confidence_percent": old["confidence_percent"],
            "operator_rules": rules_for("Carrier", carrier=True),
            "candidate_note": "Artifact carrier forms are governed by general Carrier delivery policy, not a per-property Carrier edge",
            "preserved": ["File, Directory and Markdown Carrier distinctions remain qualified; no universal binding or cardinality is invented."],
            "question": None,
        }
    if identity.startswith("Artifact/Activity"):
        suffix = identity[len("Artifact/Activity"):]
        path = "Artifact.Activity" + suffix.replace("/", ".")
        return {
            "action": "inherit", "candidate_root": "Artifact", "candidate_path": path,
            "content_view": "D" if "Carrier Basename" in identity else "R", "confidence_percent": old["confidence_percent"],
            "operator_rules": rules_for("Artifact", carrier="Carrier Basename" in identity),
            "candidate_note": "Activity and its qualified status remain dependent Artifact fields; carrier basename is a delivery convention",
            "preserved": ["Activity status remains qualified by the applicable Status model and current Revision."],
            "question": None,
        }
    if identity in {"Artifact/Applicability", "Artifact/Authority", "Artifact/Currentness", "Artifact/Identity", "Artifact/Local Tier", "Artifact/Property", "Artifact/Property/Default", "Artifact/Type"}:
        path = identity.replace("/", ".")
        if identity == "Artifact/Property/Default":
            path = "Artifact.Property: Default"
        return {
            "action": "inherit", "candidate_root": "Artifact", "candidate_path": path,
            "content_view": "R", "confidence_percent": old["confidence_percent"],
            "operator_rules": rules_for("Artifact", history=identity in {"Artifact/Currentness", "Artifact/Identity"}),
            "candidate_note": "the identity is retained as a qualified dependent Artifact field under the candidate lifecycle",
            "preserved": ["Qualified meanings and allowed-value domains remain separate; a repeated field label is not treated as duplication."],
            "question": None,
        }
    if identity == "Atom Change Classification":
        return {
            "action": "inherit", "candidate_root": "Artifact", "candidate_path": "Artifact/Atom.Change Classification",
            "content_view": "R", "confidence_percent": old["confidence_percent"],
            "operator_rules": rules_for("Artifact", history=True),
            "candidate_note": "change classification is a dependent Atom field whose identity consequences remain qualified",
            "preserved": ["Change classification remains distinct from update identity checks and lineage impact assessments."],
            "question": None,
        }
    if identity.startswith("Atom Claim Projection"):
        return {
            "action": "projection_view", "candidate_root": "Artifact", "candidate_path": "Artifact/Atom.Substance.Claim.Projection",
            "content_view": "P", "confidence_percent": old["confidence_percent"],
            "operator_rules": rules_for("Artifact", substance=True, projection=True),
            "candidate_note": "the claim projection is a derived view retaining source identity and authority boundaries",
            "preserved": ["Projection copies retain source ID and version and do not become another authoritative source."],
            "question": None,
        }
    if identity.startswith("Atom/Carrier/"):
        tail = identity[len("Atom/Carrier/"):]
        if tail == "Canonical Address":
            return {
                "action": "delivery_policy", "candidate_root": "Carrier", "candidate_path": "Carrier.Delivery Policy (Atom Canonical Address)",
                "content_view": "D", "confidence_percent": old["confidence_percent"],
                "operator_rules": rules_for("Carrier", carrier=True),
                "candidate_note": "canonical address is a Carrier delivery convention and does not override the Atom identity",
                "preserved": ["Filename, matching-directory and placement representations remain qualified and must agree with canonical internal values."],
                "question": None,
            }
        if tail == "Current Scope Unit":
            return {
                "action": "inherit", "candidate_root": "Scope Unit", "candidate_path": "Scope Unit.Carrier ownership",
                "content_view": "R", "confidence_percent": old["confidence_percent"],
                "operator_rules": rules_for("Scope Unit"),
                "candidate_note": "the current owning Scope Unit is structural ownership metadata, not Substance applicability",
                "preserved": ["Scope Unit ownership remains distinct from Substance Scope applicability; no new Scope Unit is inferred."],
                "question": None,
            }
        if tail == "Current Scope Unit/Filename Token":
            return {
                "action": "delivery_policy", "candidate_root": "Carrier", "candidate_path": "Carrier.Delivery Policy (Atom Current Scope Unit Filename Token)",
                "content_view": "D", "confidence_percent": old["confidence_percent"],
                "operator_rules": rules_for("Carrier", carrier=True),
                "candidate_note": "the Scope Unit filename token is a Carrier serialization convention, not the Scope Unit identity",
                "preserved": ["Stable Scope Unit ID remains separate from its changeable label/name and Carrier filename token."],
                "question": None,
            }
        if tail == "Reconciliation":
            return {
                "action": "operation_or_method", "candidate_root": "Artifact", "candidate_path": "Artifact/Atom.Substance.Operation.Atom Carrier Reconciliation",
                "content_view": "O", "confidence_percent": old["confidence_percent"],
                "operator_rules": rules_for("Artifact", substance=True, carrier=True),
                "candidate_note": "reconciliation remains a reusable governed Operation over carried values and representations",
                "preserved": ["Reconciliation keeps before-state, address, Relation and history checks distinct."],
                "question": None,
            }
        if tail == "Validation":
            return {
                "action": "operation_or_method", "candidate_root": "Artifact", "candidate_path": "Artifact/Atom.Substance (Evaluation).Atom Carrier Validation",
                "content_view": "E", "confidence_percent": old["confidence_percent"],
                "operator_rules": rules_for("Artifact", substance=True, execution=True),
                "candidate_note": "validation is an evaluation specification over a Carrier binding, distinct from a run",
                "preserved": ["Validation preserves the one internal value-source and outward-representation consistency constraints."],
                "question": None,
            }
    if identity == "Atom/Carrier":
        return {
            "action": "rebase", "candidate_root": "Relation", "candidate_path": "Relation/IS_CARRIED_BY",
            "content_view": "R", "confidence_percent": old["confidence_percent"],
            "operator_rules": rules_for("Relation", carrier=True),
            "candidate_note": "the captured Entity-to-Carrier binding is presented as a typed Relation while Carrier remains a separate root",
            "preserved": ["Carrier remains a root Entity; this binding does not imply one Carrier edge for every dependent Property."],
            "question": None,
        }
    if identity == "Atom/Author":
        return {
            "action": "inherit", "candidate_root": "Artifact", "candidate_path": "Artifact/Atom.Author",
            "content_view": "R", "confidence_percent": old["confidence_percent"],
            "operator_rules": rules_for("Artifact", actor=True),
            "candidate_note": "Author remains a qualified dependent Atom field referring to an Actor",
            "preserved": ["Exactly-one-effective-Author obligation remains distinct from Actor root identity."],
            "question": None,
        }
    if identity.startswith("Atom/Content Role"):
        suffix = identity[len("Atom/Content Role"):]
        if suffix.startswith(": Analysis"):
            tail = suffix[len(": Analysis"):].lstrip("/")
            path = "Artifact/Atom.Substance (Question)" + (("." + tail.replace("/", ".").replace(": ", ": ")) if tail else "")
            content = "R"
            note = "the captured Analysis role is presented as the candidate Question role under Substance"
            preserved = ["Analysis is presented as Question; its qualified Status and Type domains remain distinct."]
            rules = rules_for("Artifact", substance=True)
            action = "rebase" if suffix == ": Analysis" else "inherit"
        elif suffix.startswith(": Concern"):
            tail = suffix[len(": Concern"):].lstrip("/")
            path = "Artifact/Atom.Substance (Issue)" + (("." + tail.replace("/", ".").replace(": ", ": ")) if tail else "")
            content = "R"
            note = "the captured Concern role is presented as the candidate Issue role under Substance"
            preserved = ["Concern is presented as Issue; its qualified Status and Type domains remain distinct."]
            rules = rules_for("Artifact", substance=True)
            action = "rebase" if suffix == ": Concern" else "inherit"
        elif suffix.startswith(": Delivery"):
            tail = suffix[len(": Delivery"):].lstrip("/")
            path = "Carrier.Delivery Policy (Delivery Content Role)" + (("." + tail.replace("/", ".")) if tail else "")
            content = "D"
            note = "the captured Delivery role is presented as general Carrier delivery policy, not a per-Property Carrier edge"
            preserved = ["Delivery policy remains general and reusable; no D Atom or Carrier Relation Type is created per Property."]
            rules = rules_for("Carrier", carrier=True)
            action = "delivery_policy" if suffix == ": Delivery" else "inherit"
        elif suffix.startswith(": Evaluation"):
            tail = suffix[len(": Evaluation"):].lstrip("/")
            path = "Artifact/Atom.Substance (Evaluation)" + (("." + tail.replace("/", ".")) if tail else "")
            content = "E"
            note = "the captured Evaluation role is presented as an M/E view over shared roots, distinct from actual Execution"
            preserved = ["Evaluation mechanism and realization remain distinct from an actual Execution." ]
            rules = rules_for("Artifact", substance=True, execution=True)
            action = "rebase" if suffix == ": Evaluation" else "inherit"
        elif suffix == "/Name":
            path = "Artifact/Atom.Content Role.Name"
            content = "R"
            note = "the role name remains a dependent Atom field"
            preserved = ["Canonical role names remain qualified content metadata, not new roots." ]
            rules = rules_for("Artifact")
            action = "inherit"
        else:
            path = "Artifact/Atom.Content Role"
            content = "R"
            note = "Content Role remains a named dependent Atom Property"
            preserved = ["Role values, statuses and types remain qualified dependent fields with separate allowed-value domains." ]
            rules = rules_for("Artifact", substance=True)
            action = "inherit"
        return {
            "action": action, "candidate_root": "Artifact" if path.startswith("Artifact/") else "Carrier",
            "candidate_path": path, "content_view": content, "confidence_percent": old["confidence_percent"],
            "operator_rules": rules, "candidate_note": note, "preserved": preserved,
            "question": None,
        }

    # Do not place an identity with no explicit candidate comparison under
    # Artifact merely because it is in this partition.  Keep the review task
    # unresolved, with no display path or lifecycle ownership asserted.
    return {
        "action": "review_required", "candidate_root": None, "candidate_path": None,
        "content_view": "unclassified", "confidence_percent": min(old["confidence_percent"], 89),
        "operator_rules": ["review_backlog.question_policy", "entity_vs_syntax_rules"],
        "candidate_note": "no explicit candidate mapping was authored for this identity",
        "preserved": ["Unknown mapping remains unresolved; no candidate root, subtype, dependent field or allowed-value path is inferred."],
        "question": {
            "kind": "source_gap",
            "text": f"Review task: no explicit candidate mapping is authored for {identity}; retain the captured identity and evidence without inferring lifecycle ownership.",
        },
    }


def check_display_operators(identity: str, path: str | None) -> None:
    """Reject slash-flattened dependent fields in candidate display paths."""

    if path is None:
        return
    # A single slash introduces the root's explicit subtype.  All further
    # qualification is dependent-field (.) or allowed-value (:) notation.
    assert path.count("/") <= 1, (identity, "multiple-subtype-separators", path)
    forbidden_dependent_slashes = (
        "/Substance/", "/Operation/", "/Question", "/Issue", "/Evaluation",
        "/Content Role", "/Change Classification", "/Author", "/Applicability",
        "/Authority", "/Currentness", "/Identity", "/Local Tier", "/Property",
        "/Type", "/Status", "/Filename", "/Projection/", "/Current Scope Unit",
    )
    assert not any(token in path for token in forbidden_dependent_slashes), (identity, path)
    allowed_value_identities = {
        "Action/Execution Kind: Agentic",
        "Artifact/Activity: Active",
        "Artifact/Activity: Active/Carrier Basename",
        "Artifact/Activity: Inactive",
        "Atom Collection/Type: Ad Hoc",
        "Atom/Content Role: Analysis/Type: Analysis Report",
        "Atom/Content Role: Analysis/Type: Rationale",
        "Artifact/Property/Default",
    }
    if identity in allowed_value_identities:
        assert ":" in path, (identity, "missing-allowed-value-operator", path)
    dependent_identities = {
        "AI Agent/Confidence", "AI Agent/authorization", "Artifact/Activity",
        "Artifact/Activity: Active", "Artifact/Activity: Active/Carrier Basename",
        "Artifact/Activity: Inactive", "Artifact/Applicability", "Artifact/Authority",
        "Artifact/Currentness", "Artifact/Identity", "Artifact/Local Tier",
        "Artifact/Property", "Artifact/Property/Default", "Artifact/Type",
        "Atom/Author", "Atom/Carrier/Current Scope Unit", "Atom Change Classification",
        "Atom Collection/Direct Containment", "Atom Collection/Local Tier",
        "Atom Collection/Type", "Atom Collection/Type: Ad Hoc",
        "Atom/Content Role", "Atom/Content Role/Name",
        "Atom/Content Role: Analysis/Status", "Atom/Content Role: Analysis/Type",
        "Atom/Content Role: Analysis/Type: Analysis Report",
        "Atom/Content Role: Analysis/Type: Rationale",
        "Atom/Content Role: Concern/Status", "Atom/Content Role: Concern/Type",
        "Atom/Content Role: Delivery/Status",
    }
    if identity in dependent_identities:
        assert "." in path, (identity, "missing-dependent-operator", path)


def build() -> dict[str, Any]:
    candidate_raw = CANDIDATE.read_bytes()
    assert sha(candidate_raw) == EXPECTED_CANDIDATE_SHA256, "candidate SHA changed"
    input_raw = INPUT.read_bytes()
    input_data = json.loads(input_raw)
    assert input_data["batch"] == EXPECTED_BATCH and input_data["identity_count"] == 80
    baseline_raw = BASELINE.read_bytes()
    assert sha(baseline_raw) == input_data["baseline"]["sha256"]
    old_raw = OLD_REVIEW.read_bytes()
    old_review = json.loads(old_raw)
    dispositions_raw = DISPOSITIONS.read_bytes()
    assert sha(dispositions_raw) == "1b9d751f95aa71486908b53b3d7f3f9825defae137be3d8792d45177587c48f8"
    dispositions = json.loads(dispositions_raw)
    marks = {
        mark["identity"]: mark
        for mark in dispositions["node_disposition_marks"]
        if mark.get("scoped_refs", {}).get("batch") == EXPECTED_BATCH
    }
    input_nodes = {node["identity"]: node for node in input_data["nodes"]}
    old_nodes = {node["identity"]: node for node in old_review["nodes"]}
    assert set(input_nodes) == set(old_nodes) == set(marks) and len(input_nodes) == 80

    reader = load_snapshot_reader()
    snapshot_result = reader.verify_snapshot()
    assert snapshot_result["verification"] == "pass"
    baseline = json.loads(baseline_raw)
    pins = {source["atom_id"]: source for source in baseline["source_atoms"]}
    catalogue = dispositions["evidence_catalogue"]
    nodes: list[dict[str, Any]] = []

    for identity in input_nodes:
        mark = marks[identity]
        old = mark["review_row"]
        old_file_row = old_nodes[identity]
        # Keep the old reviewed meaning/proof aligned with the global mark.
        for field in ("disposition", "confidence_percent", "reason", "checked_source_atom_ids"):
            assert old[field] == old_file_row[field], (identity, field)
        global_refs = mark["scoped_refs"]["global_evidence_refs"]
        for ref in global_refs:
            assert ref in catalogue, (identity, "missing-global-evidence", ref)
            evidence_line_check(catalogue[ref], reader, pins)
        for atom_id in old["checked_source_atom_ids"]:
            assert atom_id in pins, (identity, "checked-source-not-pinned", atom_id)
            checked_raw = reader.read_source(atom_id)
            assert sha(checked_raw) == pins[atom_id]["carrier_sha256"], (
                identity, "checked-source-hash-mismatch", atom_id
            )
        candidate = classify(identity, old)
        check_display_operators(identity, candidate["candidate_path"])
        # Batch 1 has no captured or candidate basis for the legacy A/C view
        # labels; structural identities use R, while M/E/D/O/P are explicit
        # method/check/storage/operation/projection distinctions.
        assert candidate["content_view"] not in {"A", "C"}, (identity, candidate["content_view"])
        confidence = candidate["confidence_percent"]
        if confidence < 90:
            assert candidate["action"] in {"review_required", "concrete_conflict"}
            assert candidate["candidate_path"] is None
        else:
            assert candidate["action"] in {
                "retain", "rebase", "inherit", "delivery_policy", "operation_or_method",
                "projection_view", "syntax_context", "drop_candidate", "review_required", "concrete_conflict",
            }
        old_proposal = old.get("proposal") or {}
        if candidate["action"] == "delivery_policy":
            candidate["operator_rules"] = dedupe(candidate["operator_rules"] + ["entity_representation_rules"])
        if candidate["action"] == "operation_or_method":
            candidate["operator_rules"] = dedupe(candidate["operator_rules"] + [
                "execution_definition_policy", "m_e_root_question"
            ])
        preserved = dedupe([
            "Original captured identity, qualifiers, allowed-value domains and constraints remain preserved; candidate_path is display-only."
        ] + list(old_proposal.get("preserved_distinctions", [])) + candidate["preserved"])
        row = {
            "identity": identity,
            "prior_disposition": old["disposition"],
            "action": candidate["action"],
            "candidate_root": candidate["candidate_root"],
            "candidate_path": candidate["candidate_path"],
            "content_view": candidate["content_view"],
            "confidence_percent": confidence,
            "reason": old["reason"] + " Candidate comparison: " + candidate["candidate_note"] + ".",
            "operator_rules": candidate["operator_rules"],
            "evidence_refs": global_refs,
            "checked_source_atom_ids": old["checked_source_atom_ids"],
            "preserved_distinctions": preserved,
            "question": candidate["question"],
        }
        nodes.append(row)

    assert len(nodes) == 80 and len({node["identity"] for node in nodes}) == 80
    return {
        "schema_version": 1,
        "batch": EXPECTED_BATCH,
        "kind": "Captured nodes against Operator candidate",
        "non_authoritative": True,
        "native_admission": "not_performed",
        "source_migration": "not_performed",
        "captured_core_commit": SNAPSHOT_COMMIT,
        "candidate_sha256": EXPECTED_CANDIDATE_SHA256,
        "input_sha256": sha(input_raw),
        "baseline_sha256": sha(baseline_raw),
        "prior_review_sha256": sha(dispositions_raw),
        "review_method": (
            "Reused the accepted batch-1 reviewed meanings and exact global evidence catalogue from "
            "nodes.dispositions.json; compared each identity with the latest Operator candidate; "
            "verified every quoted evidence span against captured Main Content through "
            "nodes/support/snapshot_sources.py and the captured Git snapshot. This is not a fresh "
            "exhaustive audit of all 951 source pins or all source candidates."
        ),
        "nodes": nodes,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--persist", action="store_true", help="create the receipt if absent")
    args = parser.parse_args()
    receipt = build()
    raw = json.dumps(receipt, ensure_ascii=False, sort_keys=True, indent=2).encode("utf-8") + b"\n"
    if args.persist:
        REVIEW_DIR.mkdir(parents=True, exist_ok=True)
        if OUTPUT.exists():
            assert OUTPUT.read_bytes() == raw, ("refuse-overwrite", str(OUTPUT))
        else:
            with OUTPUT.open("xb") as handle:
                handle.write(raw)
    print(json.dumps({"outcome": "persisted" if args.persist else "dry_run", "batch": 1,
                      "identities": len(receipt["nodes"]), "bytes": len(raw),
                      "output": str(OUTPUT.relative_to(ROOT))}, sort_keys=True))


if __name__ == "__main__":
    main()
