"""Build the bounded batch-3 comparison against the latest candidate."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path.cwd()
BASE = ROOT / ".caprmedio_caprmedio/_projection/core-entity-review"
NODES = BASE / "nodes"
INPUT = NODES / "inputs/nodes.batch-3.input.json"
PRIOR = NODES / "nodes.batch-3.review.json"
DISPOSITIONS = NODES / "nodes.dispositions.json"
CANDIDATE = BASE / "presentation/operator.entity-graph.candidate.json"
INVENTORY = BASE / "baseline.inventory.json"
OUT = BASE / "consolidated/reviews/batch-3.review.json"
SNAPSHOT_PATH = NODES / "support/snapshot_sources.py"
SNAPSHOT_COMMIT = "a971d0e00c33c779f485fc8cad63194894d440fb"
EXPECTED_CANDIDATE_SHA = "99e7710f5ef83df2b1f3ec1ef4142547655e63bef7415266c5521380da7fa99b"
EXPECTED_GLOBAL_DISPOSITIONS_SHA = "1b9d751f95aa71486908b53b3d7f3f9825defae137be3d8792d45177587c48f8"

# Candidate presentation operators: `/` is broader-to-narrower display,
# `.` qualifies a bearer/dependent Entity, and `:` is an allowed value.  The
# original captured identity remains a separate receipt field.
CCE_ROLE_PROFILE_SUFFIXES = {
    "CCE/Role Profile": ".Role Profile",
    "CCE/Role Profile/validation": ".Role Profile.validation",
    "CCE/Role Profile/resolution": ".Role Profile.resolution",
    "CCE/Role Profile: Delivery": ".Role Profile: Delivery",
    "CCE/Role Profile: Evaluation": ".Role Profile: Evaluation",
    "CCE/Role Profile: Method": ".Role Profile: Method",
    "CCE/Role Profile: Operations": ".Role Profile: Operations",
    "CCE/Role Profile: Plan": ".Role Profile: Plan",
    "CCE/Role Profile: Requirement": ".Role Profile: Requirement",
}
CCE_ROLE_PROFILE_VALUE_IDENTITIES = {
    identity for identity in CCE_ROLE_PROFILE_SUFFIXES if ":" in identity
}
RELATION_SUBTYPE_IDENTITIES = {"BEARS", "CARRIES", "Concern About Relation"}
QUALIFIED_DOT_PATHS = {
    "CCE/Role Profile/resolution": "Artifact/Atom.Substance.Claim.CCE.Role Profile.resolution",
    "Confidence Threshold/resolution": "Artifact/Atom.Confidence Threshold.resolution",
    "Confidence Threshold/source": "Artifact/Atom.Confidence Threshold.source",
    "Confidence Threshold/resolution validation": "Artifact/Atom.Substance.Operation.Confidence Threshold.resolution validation",
}
NO_GENERIC_OWNER_NOTE = (
    "No candidate owner is inferred from a generic label; keep this identity "
    "unresolved until an explicit candidate owner is established."
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_snapshot():
    spec = importlib.util.spec_from_file_location("batch3_snapshot_sources", SNAPSHOT_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load captured snapshot reader")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def unresolved(identity: str, old: dict) -> dict | None:
    if identity not in {"Atom/Status", "Atom/Type", "Authority", "CORE_META_MODEL", "Concern"}:
        return None
    base_text = old.get("question") or (
        f"Which captured-snapshot Main Content statement defines or supplies a meaningful "
        f"constraint for {identity}?"
    )
    text = (
        f"{base_text} This is a captured-evidence gap, not a new Operator design question; "
        "keep the mapping unresolved until qualifying Main Content is available."
    )
    return {
        "action": "review_required",
        "candidate_root": None,
        "candidate_path": None,
        "content_view": "unclassified",
        "question": {"kind": "source_gap", "text": text},
        "mapping_note": (
            "The latest candidate supplies a broad boundary but the assigned captured "
            "sources do not establish this exact identity's meaning; keep it unresolved."
        ),
    }


def no_generic_owner(identity: str) -> dict:
    return {
        "action": "review_required",
        "candidate_root": None,
        "candidate_path": None,
        "content_view": "unclassified",
        "question": {
            "kind": "technical_followup",
            "text": (
                f"The latest candidate does not give {identity} an explicit owner; "
                "choose a bounded display owner only after semantic review, and do not "
                "infer one from the label."
            ),
        },
        "mapping_note": NO_GENERIC_OWNER_NOTE,
    }


def mapping(identity: str, old: dict) -> dict:
    pending = unresolved(identity, old)
    if pending:
        return pending

    if identity == "Atom/Property/Carrier":
        return {
            "action": "delivery_policy",
            "candidate_root": "Carrier",
            "candidate_path": "Carrier.Delivery Policy (Atom Property storage)",
            "content_view": "D",
            "mapping_note": (
                "Keep the qualified property-location obligation under general Carrier "
                "delivery policy; do not create a per-property Carrier edge or D Atom."
            ),
        }
    if identity == "Atom/Scope/Filename Token":
        return {
            "action": "delivery_policy",
            "candidate_root": "Scope Unit",
            "candidate_path": "Scope Unit.Reference Token",
            "content_view": "D",
            "mapping_note": "Keep the serialized Scope Unit token as a delivery convention; it does not replace the stable Scope Unit ID or make name/path the identity.",
        }
    if identity == "Atom/Subjects/Frontmatter":
        return {
            "action": "delivery_policy",
            "candidate_root": "Carrier",
            "candidate_path": "Carrier.Delivery Policy (Subjects frontmatter)",
            "content_view": "D",
            "mapping_note": "Keep frontmatter placement as a general representation policy, distinct from the Subject identity and without a per-Property Carrier edge.",
        }
    if identity.startswith("Atom/"):
        leaf = identity.removeprefix("Atom/").replace("/", ".")
        view = "D" if any(x in identity for x in ("Frontmatter", "Filename", "Carrier")) else "R"
        if any(x in identity for x in ("Status", "Threshold", "Validation")):
            view = "E"
        return {
            "action": "inherit",
            "candidate_root": "Artifact",
            "candidate_path": f"Artifact/Atom.{leaf}",
            "content_view": view,
            "mapping_note": (
                "Treat this as a named dependent Entity of Artifact/Atom with the shared "
                "Artifact lifecycle; the display path does not admit a native edge."
            ),
        }
    if identity in {"BEARS", "CARRIES", "Concern About Relation"}:
        return {
            "action": "projection_view" if identity == "BEARS" else "retain",
            "candidate_root": "Relation",
            "candidate_path": f"Relation/{identity}",
            "content_view": "P" if identity == "BEARS" else "R",
            "mapping_note": (
                "Preserve the typed Relation meaning and endpoint direction; BEARS remains "
                "a derived inverse view and CARRIES remains distinct from Carrier and binding metadata."
            ),
        }
    if identity == "Carrier":
        return {
            "action": "retain",
            "candidate_root": "Carrier",
            "candidate_path": "Carrier",
            "content_view": "D",
            "mapping_note": "Retain Carrier as a separate root Entity; its filename and path remain storage locations, not identity.",
        }
    if identity == "Carrier-Only Recoding" or identity.startswith("Carrier/"):
        leaf = identity.removeprefix("Carrier-").removeprefix("Carrier/").replace("/", ".")
        return {
            "action": "delivery_policy",
            "candidate_root": "Carrier",
            "candidate_path": f"Carrier.{leaf}",
            "content_view": "D",
            "mapping_note": "Keep the qualified Carrier representation/storage rule under general D policy; do not treat filename or path as Carrier identity or create a per-Property edge.",
        }
    if identity in {"CAPRMEDIO Graph", "CAPRMEDIO Graph/Connectivity"}:
        return {
            "action": "projection_view",
            "candidate_root": "Artifact" if identity == "CAPRMEDIO Graph" else "Relation",
            "candidate_path": (
                "Artifact/Projection.CAPRMEDIO Graph"
                if identity == "CAPRMEDIO Graph"
                else "Relation.Graph Connectivity"
            ),
            "content_view": "P",
            "mapping_note": (
                "Keep the graph as a derived, source-traceable view; connectivity preserves "
                "endpoint, direction and source identity without becoming a new native relation kind."
            ),
        }
    if identity == "CAPRMEDIO Framework Instance":
        return {
            "action": "rebase",
            "candidate_root": "Artifact",
            "candidate_path": "Artifact",
            "content_view": "R",
            "mapping_note": (
                "The candidate's governed lifecycle unit is Artifact; retain the Framework Instance "
                "boundary without treating Actor participation or a carrier as the instance itself."
            ),
        }
    if identity == "CAPRMEDIO Framework Identity":
        return {
            "action": "rebase",
            "candidate_root": "Artifact",
            "candidate_path": "Artifact.Framework Identity",
            "content_view": "R",
            "mapping_note": "Retain the Framework naming constraint as an Artifact-level identity property, separate from its instance and carrier.",
        }
    if identity == "CAPRMEDIO Framework Instance/Carrier Root":
        return {
            "action": "delivery_policy",
            "candidate_root": "Carrier",
            "candidate_path": "Carrier.Framework Instance Root",
            "content_view": "D",
            "mapping_note": "Retain the placement constraint as a general Carrier delivery policy, separate from Framework Instance identity.",
        }
    if identity in {"CAPRMEDIO Metamodel", "CAPRMEDIO Metamodel/Fractality"}:
        return {
            "action": "rebase" if identity == "CAPRMEDIO Metamodel" else "inherit",
            "candidate_root": "Scope Unit",
            "candidate_path": "Scope Unit.Metamodel" + (".Fractality" if "/" in identity else ""),
            "content_view": "R",
            "mapping_note": "Preserve recursive Scope Unit governance without promoting a display qualification into a new root or universal subtype.",
        }
    if identity == "Author":
        return {
            "action": "rebase",
            "candidate_root": "Actor",
            "candidate_path": "Actor.Author",
            "content_view": "R",
            "mapping_note": "Keep authorship obligations distinct from a generic Actor identity and from a native relation admission.",
        }
    if identity in {"Authority Mode", "Autonomous Confidence Threshold"}:
        return {
            "action": "inherit",
            "candidate_root": "Artifact",
            "candidate_path": f"Artifact/Atom.{identity}",
            "content_view": "E",
            "mapping_note": "Keep the qualified decision/threshold field as a named dependent Entity under the owning Artifact lifecycle.",
        }
    if identity in {"Authorize Structural Change", "Canonical Scope Signature Derivation", "Canonical Signature Derivation", "Cardinality Constraint Authoring", "Configuration Selection and Precedence"}:
        root = "Scope Unit" if identity == "Configuration Selection and Precedence" else "Artifact"
        prefix = "Scope Unit" if root == "Scope Unit" else "Artifact/Atom.Substance.Operation"
        return {
            "action": "operation_or_method",
            "candidate_root": root,
            "candidate_path": f"{prefix}.{identity}",
            "content_view": "M",
            "mapping_note": "Keep the reusable method/policy definition separate from any actual Execution; no automatic repeatability rule is inferred.",
        }
    if identity in {"Canonical Scope Signature Derivation Validation", "Canonical Signature Derivation Validation", "Condition Expression", "Confidence Threshold/resolution validation", "Claim Value Set Consolidation Candidate Evaluation", "Claim Value Set Validation", "Compatible Lineage Impact Disposition"}:
        return {
            "action": "operation_or_method",
            "candidate_root": "Artifact",
            "candidate_path": f"Artifact/Atom.Substance.Operation.{identity.replace('/', '.')}",
            "content_view": "E",
            "mapping_note": "Keep the bounded checking/evaluation definition distinct from any actual Execution and preserve its qualified rejection constraints.",
        }
    if identity in {"Build Entities Graph", "Build Terms Graph", "Check Atoms", "Check Atoms Step", "Construct Entities Graph Projection", "Construct Terms Graph Projection"}:
        return {
            "action": "operation_or_method",
            "candidate_root": "Artifact",
            "candidate_path": f"Artifact/Atom.Substance.Operation.{identity}",
            "content_view": "O",
            "mapping_note": "Preserve the reusable Operation/Workflow or Step definition separately from its actual Execution, Projection result and Journal record.",
        }
    if identity in {"CCE", "CCE Method", "CCE Operator", "CCE Operator Expression", "CCE Operator Expression Normalization", "CCE Operator Registry", "CCE/Role Profile", "CCE/Role Profile: Delivery", "CCE/Role Profile: Method", "CCE/Role Profile: Plan", "CCE/Role Profile: Requirement"}:
        base = "Artifact/Atom.Substance.Claim.CCE"
        suffix = CCE_ROLE_PROFILE_SUFFIXES.get(identity)
        if suffix is None:
            return {
                "action": "operation_or_method",
                "candidate_root": "Artifact",
                "candidate_path": f"Artifact/Atom.Substance.Claim.{identity}",
                "content_view": "M",
                "mapping_note": "Retain the CCE authoring language/profile boundary as a reusable Method definition under the role-specific Substance headings.",
            }
        return {
            "action": "operation_or_method",
            "candidate_root": "Artifact",
            "candidate_path": f"{base}{suffix}" if suffix else base,
            "content_view": "M",
            "mapping_note": "Retain the CCE authoring language/profile boundary as a reusable Method definition under the role-specific Substance headings.",
        }
    if identity in {"CCE Claim and Projection Validation", "CCE Condition Expression Evaluation", "CCE/Role Profile/resolution", "CCE/Role Profile/validation", "CCE/Role Profile: Evaluation"}:
        base = "Artifact/Atom.Substance.Claim.CCE"
        suffix = CCE_ROLE_PROFILE_SUFFIXES.get(identity)
        return {
            "action": "operation_or_method",
            "candidate_root": "Artifact",
            "candidate_path": (
                f"{base}{suffix}" if suffix is not None else f"Artifact/Atom.Substance.Claim.{identity}"
            ),
            "content_view": "E",
            "mapping_note": "Retain the CCE validation/evaluation boundary as an Execution-capable method definition, not as a new root.",
        }
    if identity in {"CCE/Role Profile: Operations"}:
        base = "Artifact/Atom.Substance.Operation.CCE"
        return {
            "action": "operation_or_method",
            "candidate_root": "Artifact",
            "candidate_path": f"{base}{CCE_ROLE_PROFILE_SUFFIXES[identity]}",
            "content_view": "O",
            "mapping_note": "Keep the Operations role profile distinct from an actual Operation Execution and from the shared Substance umbrella.",
        }
    if identity in {"Cardinality Constraint", "Claim Value Set", "Composite Claim", "Child Composition"}:
        return {
            "action": "inherit",
            "candidate_root": "Artifact",
            "candidate_path": f"Artifact/Atom.Substance.Claim.{identity}",
            "content_view": "R",
            "mapping_note": "Keep the qualified Claim/property constraint under the shared Artifact/Atom lifecycle, including its exact cardinality or allowed-value domain.",
        }
    if identity in {"Claim Value Set Authoring"}:
        return {
            "action": "operation_or_method",
            "candidate_root": "Artifact",
            "candidate_path": "Artifact/Atom.Substance.Claim.Value Set Authoring",
            "content_view": "M",
            "mapping_note": "Preserve one-Property finite allowed-value authoring as a reusable method, without turning values into separate roots.",
        }
    if identity == "Change Content Roles":
        return {
            "action": "syntax_context",
            "candidate_root": None,
            "candidate_path": None,
            "content_view": "mixed",
            "mapping_note": "Treat CAPO as role-grouping context for Substance headings, not as another Entity or lifecycle root.",
        }
    if identity == "CAPRMEDIO Expansion":
        return {
            "action": "syntax_context",
            "candidate_root": None,
            "candidate_path": None,
            "content_view": "mixed",
            "mapping_note": "Preserve the ordered role expansion as Substance heading context rather than a new subtype or root.",
        }
    if identity in {"Condition Expression", "Confidence Threshold", "Confidence Threshold/resolution", "Confidence Threshold/source"}:
        return {
            "action": "inherit",
            "candidate_root": "Artifact",
            "candidate_path": f"Artifact/Atom.{identity.replace('/', '.')}",
            "content_view": "E",
            "mapping_note": "Keep the threshold/condition and its qualified source or resolution rules as named dependent constraints.",
        }
    if identity in {"Concern About Relation"}:
        return {
            "action": "retain",
            "candidate_root": "Relation",
            "candidate_path": "Relation/Concern About Relation",
            "content_view": "R",
            "mapping_note": "Retain the declared Concern-owned direction to the affected Observation/entity; no inverse or independent lifecycle is inferred.",
        }
    if identity in {"Consumer", "Consumer/Goal"}:
        return {
            "action": "rebase" if identity == "Consumer" else "inherit",
            "candidate_root": "Actor",
            "candidate_path": "Actor.Consumer" + (".Goal" if "/" in identity else ""),
            "content_view": "R",
            "mapping_note": "Keep the consumer-side Actor boundary and its Goal qualification distinct from the demanded Atom and any Execution.",
        }
    if identity in {"CAPRMEDIO Graph/Connectivity"}:
        return {
            "action": "projection_view",
            "candidate_root": "Relation",
            "candidate_path": "Relation.Graph Connectivity",
            "content_view": "P",
            "mapping_note": "Keep source-qualified graph connectivity as a derived view over typed endpoints, not a new primitive relation kind.",
        }

    # Do not manufacture an owner from a lexical label. An unhandled identity
    # is safer as bounded review work than as an invented Artifact dependent.
    return no_generic_owner(identity)


def check_display_notation(rows: list[dict]) -> None:
    """Reject paths that confuse subtype, dependent, and allowed-value syntax."""

    for row in rows:
        identity = row["identity"]
        path = row["candidate_path"]
        if NO_GENERIC_OWNER_NOTE in row["reason"]:
            assert row["action"] == "review_required", (identity, row)
            assert row["candidate_root"] is None and row["candidate_path"] is None, (identity, row)
        if path is None:
            assert row["candidate_root"] is None, (identity, row)
            continue
        assert "@" not in path, (identity, path)
        assert not path.startswith("Artifact/Atom/"), (identity, path)
        assert not path.startswith("Artifact/Projection/"), (identity, path)
        assert not path.startswith("Carrier/"), (identity, path)
        if identity in RELATION_SUBTYPE_IDENTITIES:
            assert path == f"Relation/{identity}", (identity, path)
        if identity in CCE_ROLE_PROFILE_SUFFIXES:
            base = (
                "Artifact/Atom.Substance.Operation.CCE"
                if identity == "CCE/Role Profile: Operations"
                else "Artifact/Atom.Substance.Claim.CCE"
            )
            expected = f"{base}{CCE_ROLE_PROFILE_SUFFIXES[identity]}"
            assert path == expected, (identity, path, expected)
            if identity not in CCE_ROLE_PROFILE_VALUE_IDENTITIES:
                assert ":" not in path, (identity, path)
        if identity in QUALIFIED_DOT_PATHS:
            assert path == QUALIFIED_DOT_PATHS[identity], (identity, path)
            assert "/" not in path.removeprefix("Artifact/"), (identity, path)
        if ":" in path:
            assert identity in CCE_ROLE_PROFILE_VALUE_IDENTITIES, (identity, path)
            assert ".Role Profile: " in path, (identity, path)


def rules_for(item: dict, resolved: dict) -> list[str]:
    rules = []
    root = resolved["candidate_root"]
    if root == "Artifact":
        rules += ["root_entities[0]", "dependent_entities", "entity_identity_model.dependent_entity"]
    elif root == "Scope Unit":
        rules += ["root_entities[1]", "entity_identity_model.scope_unit"]
    elif root == "Actor":
        rules += ["root_entities[2]", "entity_identity_model.actor"]
    elif root == "Relation":
        rules += ["root_entities[3]", "graph_model", "relation_type_model"]
    elif root == "Revision":
        rules += ["root_entities[4]", "snapshot_and_history_rules", "history_model"]
    elif root == "Carrier":
        rules += ["root_entities[5]", "carrier_delivery_model", "entity_identity_model.carrier_identity"]
    elif root == "Execution":
        rules += ["root_entities[6]", "execution_definition_policy"]
    action = resolved["action"]
    if action == "delivery_policy":
        rules += ["carrier_delivery_model", "entity_representation_rules"]
    if action == "operation_or_method":
        rules += ["execution_definition_policy", "m_e_root_question", "content_direction"]
    if action == "projection_view":
        rules += ["projection_member_model", "applicable_methodology", "entity_representation_rules"]
    if action == "syntax_context":
        rules += ["entity_vs_syntax_rules", "content_direction"]
    if item["identity"] == "Author":
        rules += ["entity_identity_model.actor"]
    if any(k in item["identity"] for k in ("Version", "Revision", "Status", "Updated At", "Journal")):
        rules += ["atom_versioning", "atom_lookup", "history_model"]
    return list(dict.fromkeys(rules))


def preserved(item: dict, resolved: dict, old: dict) -> list[str]:
    values = list((old.get("proposal") or {}).get("preserved_distinctions") or [])
    identity = item["identity"]
    values.append("Original captured identity, qualifiers, allowed-value domains and constraints remain preserved; candidate_path is display-only.")
    if resolved["action"] == "delivery_policy":
        values.append("Carrier identity remains distinct from filename/path, carried Entity and binding metadata; no per-Property Carrier edge or D Atom is introduced.")
    if resolved["action"] == "operation_or_method":
        values.append("Reusable definition/method meaning remains distinct from an actual Execution; repeatability remains an Operator decision.")
    if resolved["action"] == "projection_view":
        values.append("Derived view membership and source authority remain distinct; source IDs, versions and provenance are not rewritten here.")
    if resolved["action"] == "syntax_context":
        values.append("Heading/grouping/alias context does not create an Entity or native Relation.")
    if identity in {"Claim Value Set", "Claim Value Set Authoring", "Claim Value Set Consolidation Candidate Evaluation", "Claim Value Set Validation"}:
        values.append("The finite unordered allowed-value domain remains tied to one Property and governed as one qualified set.")
    if identity in {"Atom/Status", "Atom/Type", "Authority", "CORE_META_MODEL", "Concern"}:
        values.append("No absence of checked meaning is treated as emptiness or permission to drop the identity.")
    return list(dict.fromkeys(values))


def mapping_reason(old_reason: str, resolved: dict) -> str:
    return f"{old_reason} Latest candidate comparison: {resolved['mapping_note']}"


def main() -> None:
    candidate_sha = sha(CANDIDATE)
    assert candidate_sha == EXPECTED_CANDIDATE_SHA, candidate_sha
    input_data = load(INPUT)
    prior_data = load(PRIOR)
    dispositions = load(DISPOSITIONS)
    candidate = load(CANDIDATE)
    assert candidate["status"] == "Candidate"
    assert input_data["batch"] == 3 and input_data["identity_count"] == 80
    assert len(input_data["nodes"]) == 80

    prior_by_identity = {row["identity"]: row for row in prior_data["nodes"]}
    accepted_by_identity = {
        row["identity"]: row["review_row"]
        for row in dispositions["node_disposition_marks"]
        if row["identity"] in prior_by_identity
    }
    assert set(prior_by_identity) == {row["identity"] for row in input_data["nodes"]}
    assert len(accepted_by_identity) == 80

    old_catalogue = prior_data["evidence_catalogue"]
    global_catalogue = dispositions["evidence_catalogue"]
    used_refs: set[str] = set()
    rows = []
    for item in input_data["nodes"]:
        identity = item["identity"]
        old = prior_by_identity[identity]
        resolved = mapping(identity, old)
        resolved.setdefault("question", None)
        global_refs = []
        for local_ref in old.get("evidence_refs", []):
            assert local_ref in old_catalogue, (identity, local_ref)
            global_ref = local_ref if local_ref.startswith("CA-P-1931/batch-3/") else f"CA-P-1931/batch-3/{local_ref}"
            assert global_ref in global_catalogue, (identity, global_ref)
            global_refs.append(global_ref)
            used_refs.add(global_ref)
        prior_disposition = accepted_by_identity[identity]["disposition"]
        if prior_disposition != old["disposition"]:
            raise AssertionError((identity, prior_disposition, old["disposition"]))
        rows.append({
            "identity": identity,
            "prior_disposition": prior_disposition,
            "action": resolved["action"],
            "candidate_root": resolved["candidate_root"],
            "candidate_path": resolved["candidate_path"],
            "content_view": resolved["content_view"],
            "confidence_percent": old["confidence_percent"],
            "reason": mapping_reason(old["reason"], resolved),
            "operator_rules": rules_for(item, resolved),
            "evidence_refs": global_refs,
            "checked_source_atom_ids": old.get("checked_source_atom_ids", []),
            "preserved_distinctions": preserved(item, resolved, old),
            "question": resolved["question"],
        })

    check_display_notation(rows)
    snapshot = load_snapshot()
    snapshot_result = snapshot.verify_snapshot()
    assert snapshot_result["git_commit"] == SNAPSHOT_COMMIT
    assert snapshot_result["verification"] == "pass"
    selected_catalogue = {}
    for ref in sorted(global_catalogue):
        if not ref.startswith("CA-P-1931/batch-3/"):
            continue
        value = copy.deepcopy(global_catalogue[ref])
        value["evidence_ref"] = ref
        raw = snapshot.read_source(value["atom_id"])
        text_lines = raw.decode("utf-8").splitlines()
        quote = "\n".join(text_lines[value["start_line"] - 1:value["end_line"]])
        assert quote == value["quote"], ref
        assert hashlib.sha256(quote.encode("utf-8")).hexdigest() == value["text_sha256"], ref
        frontmatter_end = next(i for i, line in enumerate(text_lines[1:], 2) if line == "---")
        assert value["start_line"] > frontmatter_end, ref
        headings = [line for line in text_lines[:value["start_line"]] if line.startswith(("# ", "## ", "### "))]
        assert headings and not headings[-1].startswith("# Summary"), ref
        if ref in used_refs:
            selected_catalogue[ref] = value

    baseline_sha = sha(INVENTORY)
    input_sha = sha(INPUT)
    global_dispositions_sha = sha(DISPOSITIONS)
    assert global_dispositions_sha == EXPECTED_GLOBAL_DISPOSITIONS_SHA, global_dispositions_sha
    output = {
        "schema_version": 1,
        "batch": 3,
        "kind": "Captured nodes against Operator candidate",
        "non_authoritative": True,
        "native_admission": "not_performed",
        "source_migration": "not_performed",
        "captured_core_commit": SNAPSHOT_COMMIT,
        "candidate_sha256": candidate_sha,
        "input_sha256": input_sha,
        "baseline_sha256": baseline_sha,
        "prior_review_sha256": global_dispositions_sha,
        "review_method": (
            "Compared each assigned identity with its accepted prior reviewed meaning, then "
            "checked the pertinent captured-snapshot Main Content evidence and exact quote spans "
            "through nodes/support/snapshot_sources.py. Applied only the latest Operator-authored "
            "candidate rules; no fresh exhaustive audit of all 951 source pins, no Core read, "
            "native admission or source migration was performed."
        ),
        "nodes": rows,
    }
    assert len(rows) == 80
    assert [row["identity"] for row in rows] == [item["identity"] for item in input_data["nodes"]]
    assert len({row["identity"] for row in rows}) == 80
    for row in rows:
        if row["action"] in {"review_required", "concrete_conflict", "syntax_context"}:
            assert row["candidate_root"] is None and row["candidate_path"] is None
        if row["action"] not in {"review_required", "syntax_context"}:
            assert row["candidate_root"] in {"Artifact", "Scope Unit", "Actor", "Relation", "Revision", "Carrier", "Execution"}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    encoded = json.dumps(output, ensure_ascii=False, indent=2) + "\n"
    if OUT.exists() and OUT.read_text(encoding="utf-8") != encoded:
        raise RuntimeError(f"refusing to overwrite non-identical output: {OUT}")
    OUT.write_text(encoded, encoding="utf-8")
    print(json.dumps({
        "output": str(OUT),
        "identities": len(rows),
        "evidence_refs": len(selected_catalogue),
        "actions": {action: sum(row["action"] == action for row in rows) for action in sorted({row["action"] for row in rows})},
        "snapshot": snapshot_result,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
