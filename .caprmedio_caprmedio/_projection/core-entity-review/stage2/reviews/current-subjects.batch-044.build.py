import hashlib
import json
from pathlib import Path


BASE = Path(".")
INPUT = ".caprmedio_caprmedio/_projection/core-entity-review/stage2/inputs/current-subjects.batch-044.json"
INVENTORY = ".caprmedio_caprmedio/_projection/core-entity-review/stage2/current-subjects.inventory.json"
CANDIDATE = ".caprmedio_caprmedio/_projection/core-entity-review/presentation/operator.entity-graph.candidate.json"
CONSOLIDATED = ".caprmedio_caprmedio/_projection/core-entity-review/consolidated/nodes.review.json"
CONTRACT = ".caprmedio_caprmedio/_projection/core-entity-review/stage2/current-subjects.contract.md"
REVIEW_CONTRACT = ".caprmedio_caprmedio/_projection/core-entity-review/stage2/current-subjects.review.contract.md"


def digest(path):
    return hashlib.sha256((BASE / path).read_bytes()).hexdigest()


def body_span(path):
    raw = (BASE / path).read_bytes()
    lines = raw.splitlines(keepends=True)
    delimiters = [i for i, line in enumerate(lines) if line.rstrip(b"\r\n") == b"---"]
    assert len(delimiters) >= 2, path
    start = delimiters[1] + 2
    value = b"".join(lines[start - 1 :])
    return {
        "path": path,
        "sha256": hashlib.sha256(raw).hexdigest(),
        "start_line": start,
        "end_line": len(lines),
        "span_sha256": hashlib.sha256(value).hexdigest(),
        "reason": "The complete current Main Content after frontmatter was read before this review.",
    }


OPERATION_LINES = {
    "CA-O-155": (38, 48),
    "CA-O-156": (35, 45),
    "CA-O-157": (38, 48),
    "CA-O-080": (33, 45),
    "CA-O-087": (56, 95),
    "CA-O-088": (30, 33),
    "CA-O-004": (28, 28),
    "CA-O-005": (31, 42),
    "CA-O-006": (35, 44),
    "CA-O-007": (31, 38),
    "CA-O-008": (36, 44),
}


SOURCE_FACT = {
    "CA-O-155": "the Step is the decide node of Applicable Methodology Compilation, invokes Obtain Source Correction Decision, and binds a Workflow Run, Operator approval, and a canonical Journal reference",
    "CA-O-156": "the Step is the correct node of Applicable Methodology Compilation, invokes Apply Approved Source Corrections, and binds its approved correction, Workflow Run, and owning-source change workflow",
    "CA-O-157": "the Step is the publish node of Applicable Methodology Compilation, invokes Publish Reconciled Projection, and preserves selected Atom IDs, source Revisions, Claims, and Carrier bytes",
    "CA-O-080": "Atom Carrier Validation is a reusable Workflow with CA-O-088 as its sole Step and terminal results ending the Workflow Run",
    "CA-O-087": "Check Atoms is a Programmatic Action whose bounded selection and checking retain Atom, Revision, Carrier, Scope Unit, Properties, Relations, Evaluations, and Journal distinctions",
    "CA-O-088": "Check Atoms Step is a Workflow node which invokes exactly one Action with an admitted Workflow Run's inputs",
    "CA-O-004": "Select Reconciliation Sources is a reusable Action that returns exact selected source identities and Revisions as one source frontier without changing authority or publishing a Projection",
    "CA-O-005": "Assess Source Conflicts is a reusable Action that assesses one selected source frontier and separately retains Global Tier, exact Revision, Updated At, Claim, conflict, and Operator distinctions",
    "CA-O-006": "Propose Source Corrections is a reusable Action that keeps source authority, Claims, Relations, Evaluations, dependent authority, and confidence constraints distinct from a proposal",
    "CA-O-007": "Obtain Source Correction Decision is a reusable Action that obtains an Operator decision and records it in a Journal without applying a correction or changing source authority",
    "CA-O-008": "Apply Approved Source Corrections is a reusable Action that applies only authorized corrections through an owning source workflow, keeps Claims and selections in their owners, and records actual execution in the Journal",
}


GAPS = {
    "Applicable Methodology Compilation/Step: decide": "the candidate establishes no Applicable Methodology Compilation field, Step-node selector, or decide value domain",
    "Applicable Methodology Compilation/Step: correct": "the candidate establishes no Applicable Methodology Compilation field, Step-node selector, or correct value domain",
    "Applicable Methodology Compilation/Step: publish": "the candidate establishes no Applicable Methodology Compilation field, Step-node selector, or publish value domain",
    "Applicable Methodology/Conflict": "the candidate establishes no Applicable Methodology-owned Conflict field or conflict lifecycle",
    "Applicable Methodology/Source Frontier Digest": "the candidate establishes no Applicable Methodology-owned Source Frontier Digest field or its qualified value domain",
    "Atom/Claim": "the candidate's Substance umbrella and RMED-to-Claim role label are not a Claim identity, owner-field, or replacement rule",
    "Atom/Content Role: Evaluation": "the candidate does not establish an Atom Content Role field with Evaluation as its allowed value; its role label cannot change the field bearer",
    "Atom/Frontmatter": "the candidate establishes no Atom-frontmatter dependent field and says an Entity name is not a storage-field name",
    "Atom/Global Tier": "the candidate establishes no Atom-owned Global Tier field or its value domain",
    "Atom/Local Tier: Principle": "the candidate establishes no Atom-owned Local Tier field, Principle value domain, or qualified bearer",
    "Atom/Property": None,
    "Atom/Revision/Updated At": "the candidate excludes Atom/Revision paths and does not establish an Updated At property on the separate Revision root",
    "Atom/Summary": "the candidate names Atom.Summary as a generic example, but this current Action body does not establish Summary's source-specific relation or a migration target",
    "Autonomous Confidence Threshold": "the candidate establishes no Autonomous Confidence Threshold entity, field owner, or allowed-value domain",
    "Framework Instance Settings": "the candidate establishes no Framework Instance Settings identity or field topology",
    "Methodology Source": "the candidate establishes no Methodology Source identity or relation to an Operation definition",
    "Methodology Source/Expansion Boundary": "the candidate establishes no Methodology Source-owned Expansion Boundary field or its constraint semantics",
    "Owned Atoms": "the candidate confirms Scope Unit ownership but does not establish an Owned Atoms field name or query identity",
    "Project Settings": "the candidate establishes no Project Settings entity or field topology",
    "Project Structure": "the candidate permits Scope Unit nesting but does not establish Project Structure identity or its parentage-bearing field",
    "Projection/Type: Reconciled Projection": "the candidate confirms a derived Projection instance but establishes no Projection Type field or Reconciled Projection allowed-value domain",
    "Subtree-owned Atoms": "the candidate permits recursive Scope Unit nesting but establishes no Subtree-owned Atoms selector or membership semantics",
    "Workflow/Relation Kind: On Result": "the candidate establishes Relation as a root but no Workflow-owned Relation Kind field or On Result allowed-value domain",
}


UNCHANGED = {
    "Action",
    "Applicable Methodology",
    "Apply Approved Source Corrections",
    "Assess Source Conflicts",
    "Atom Carrier Validation",
    "Carrier",
    "Check Atoms",
    "Check Atoms Step",
    "Evaluation",
    "Global Tier",
    "Journal",
    "Local Tier",
    "Obtain Source Correction Decision",
    "Project Configuration",
    "Projection",
    "Propose Source Corrections",
    "Publish Reconciled Projection",
    "Relation",
    "Scope Unit",
    "Select Reconciliation Sources",
    "Step",
    "Workflow",
}


def operation_span(occurrence):
    path = occurrence["source_path"]
    raw = (BASE / path).read_bytes()
    lines = raw.splitlines(keepends=True)
    start, end = OPERATION_LINES[occurrence["source_atom_id"]]
    value = b"".join(lines[start - 1 : end])
    return {
        "path": path,
        "sha256": hashlib.sha256(raw).hexdigest(),
        "start_line": start,
        "end_line": end,
        "span_sha256": hashlib.sha256(value).hexdigest(),
        "reason": "The current Operation paragraph(s) define the owning subject context for this occurrence.",
    }


def distinctions(occurrence):
    return [
        "Current Operations-role source scope remains metadata; no key, body, grammar, native relation, identity, migration, or runtime change is made.",
        f"The exact current Subject {occurrence['old_value']!r}, field {occurrence['field']!r}, and index {occurrence['index']!r} remain individually covered.",
        "The frozen consolidated review is evidence only; its display paths are not used as mapping proof.",
        "All output rows are non-executable candidate/research records only.",
    ]


def proposed(occurrence):
    old = occurrence["old_value"]
    fact = SOURCE_FACT[occurrence["source_atom_id"]]
    if old in {"Operator", "AI Agent"}:
        type_index = 1 if old == "Operator" else 0
        return f"Actor.Type: {old}", 0.95, (
            f"Current Main Content says {fact}; the candidate confirms Actor identity is Actor Type plus optional Name and explicitly lists {old} as an Actor Type."
        ), [
            {"pointer": "/entity_identity_model/actor/identity", "reason": "The confirmed Actor identity is Actor Type plus optional Name."},
            {"pointer": f"/entity_identity_model/actor/type_examples/{type_index}", "reason": f"The candidate expressly includes {old} as an Actor Type example."},
        ], [f"{old} remains the allowed value of Actor.Type, not a slash subtype, Journal decision, authorization record, Carrier, or Execution."]
    if old in {"Artifact/Revision", "Atom/Revision"}:
        return "Revision", 0.95, (
            f"Current Main Content says {fact}; the candidate makes Revision a separate historical root and expressly excludes Artifact/Revision and Atom/Revision paths."
        ), [
            {"pointer": "#/root_entities/4", "reason": "The candidate defines Revision as a historical snapshot and expressly excludes Artifact/Revision and Atom/Revision paths."},
            {"pointer": "#/history_model/revision_role", "reason": "The candidate confirms Revision preserves a historical Artifact state."},
        ], ["Revision remains historical state, not an Atom or Artifact dependent field, Carrier, or actual Execution."]
    if old == "Workflow Run":
        return "Execution/Workflow Run", 0.95, (
            f"Current Main Content says {fact}; it uses Workflow Run as actual admitted execution context, and the candidate explicitly lists Workflow Run as an actual Execution kind."
        ), [
            {"pointer": "#/root_entities/6", "reason": "The candidate defines Execution as one actual run and expressly lists Workflow Run among its proposed kinds."},
            {"pointer": "#/execution_definition_policy", "reason": "The candidate distinguishes repeatable Operation definitions from actual Executions."},
        ], ["The actual Workflow Run remains distinct from the reusable Workflow, Step, Action, and Journal record."]
    if old == "Journal/Record":
        return "Journal.Record", 0.92, (
            f"Current Main Content says {fact}; the candidate directly names Journal.Record in its confirmed Journal-to-Execution relation proposal, preserving Record rather than treating it as the event."
        ), [
            {"pointer": "#/history_model/journal_role", "reason": "The candidate says Journal records what happened and that a record is not the event itself."},
            {"pointer": "#/history_model/relation_proposal/connections", "reason": "The candidate directly names Journal.Record in the confirmed Journal record connection."},
        ], ["Journal.Record remains distinct from an Operator decision, its source Claim, and the Execution it may record."]
    raise AssertionError(f"unsupported proposed Subject: {old}")


def review_occurrence(occurrence):
    out = dict(occurrence)
    old = occurrence["old_value"]
    fact = SOURCE_FACT[occurrence["source_atom_id"]]
    if old in {"Operator", "AI Agent", "Artifact/Revision", "Atom/Revision", "Workflow Run"}:
        value, confidence, reason, basis, extra = proposed(occurrence)
        decision = "proposed"
    elif old == "Journal/Record" and occurrence["source_atom_id"] != "CA-O-156":
        value, confidence, reason, basis, extra = proposed(occurrence)
        decision = "proposed"
    elif old == "Atom":
        decision, value, confidence = "unchanged", old, 0.95
        basis = [{"pointer": "/root_entities/0/narrower_entities/0", "reason": "The candidate confirms Atom as Artifact's narrower Entity; no display-only Artifact prefix is added."}]
        reason = f"Current Main Content says {fact}; Atom is already the confirmed current canonical Entity, so its literal Subject is retained without a display-only Artifact prefix."
        extra = ["Atom remains distinct from Carrier, Revision, Projection, Claim, and actual Execution."]
    elif old in {"Atom/Property", "Journal/Record"}:
        decision, value, confidence, basis = "unresolved", None, 0.5, []
        reason = f"Current Main Content says {fact}; the candidate does not support the proposed mapping without adding a display alias or unsupported Journal Record evidence."
        extra = [f"The complete qualified current Subject {old!r} remains visible pending a supported mapping."]
    elif old in GAPS and GAPS[old] is not None:
        decision, value, confidence, basis = "unresolved", None, 0.0, []
        reason = f"Current Main Content says {fact}; {GAPS[old]}. No candidate string is proposed because it would lose a captured qualifier, field owner, allowed-value domain, or identity boundary."
        extra = [f"The qualified current Subject {old!r} remains visible pending a notation-preserving mapping with its required meaning."]
    elif old in UNCHANGED:
        decision, value, confidence, basis = "unchanged", old, 1.0, []
        reason = f"Current Main Content says {fact}; the exact current Subject remains a valid identity because the candidate does not define a different notation that preserves all of this source's operation-definition meaning."
        extra = ["Retaining the exact current Subject does not infer a new root, field, allowed value, Carrier registry, native relation, alias, or actual Execution."]
    else:
        raise AssertionError(f"unclassified Subject: {old}")
    out.update(
        decision=decision,
        proposed_value=value,
        confidence=confidence,
        reason=reason,
        evidence=[operation_span(occurrence)],
        candidate_basis=basis,
        preserved_distinctions=distinctions(occurrence) + extra,
        question=None,
        executable=False,
    )
    return out


def main():
    source = json.loads((BASE / INPUT).read_text())
    source_reviews = []
    for selected in source["selected_sources"]:
        review = dict(selected)
        review["main_content_read"] = body_span(selected["relative_path"])
        review["finding_dispositions"] = [
            {"finding": finding, "reason": "No disposition changes the frozen input finding."}
            for finding in selected["findings"]
        ]
        review["questions"] = []
        source_reviews.append(review)
    occurrences = [review_occurrence(occurrence) for occurrence in source["occurrences"]]
    counts = {decision: sum(o["decision"] == decision for o in occurrences) for decision in ("proposed", "unchanged", "unresolved")}
    report = {
        "schema_version": 1,
        "non_authoritative": True,
        "source_migration": "not_performed",
        "native_admission": "not_performed",
        "task_id": "CA-P-2035",
        "batch_id": source["batch_id"],
        "input_batch_path": INPUT,
        "input_batch_sha256": digest(INPUT),
        "input_inventory_sha256": digest(INVENTORY),
        "evidence_pins": [
            {"path": CANDIDATE, "sha256": digest(CANDIDATE)},
            {"path": CONSOLIDATED, "sha256": digest(CONSOLIDATED), "git_commit": "a971d0e00c33c779f485fc8cad63194894d440fb"},
            {"path": CONTRACT, "sha256": digest(CONTRACT)},
            {"path": REVIEW_CONTRACT, "sha256": digest(REVIEW_CONTRACT)},
        ],
        "source_reviews": source_reviews,
        "occurrences": occurrences,
        "review_summary": {
            "source_count": len(source_reviews),
            "occurrence_count": len(occurrences),
            "decisions": counts,
            "quarantined_sources": sum(s["quarantined"] for s in source_reviews),
            "unresolved_identities": sorted({o["old_value"] for o in occurrences if o["decision"] == "unresolved"}),
            "boundary": "All rows are non-executable candidate/research records only; no current source, grammar, native relation, key, identity, migration, or runtime change is authorized.",
        },
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
