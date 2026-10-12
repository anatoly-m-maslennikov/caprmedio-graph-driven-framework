import hashlib
import json
from pathlib import Path

BASE = Path(".")
INPUT = ".caprmedio_caprmedio/_projection/core-entity-review/stage2/inputs/current-subjects.batch-033.json"
INVENTORY = ".caprmedio_caprmedio/_projection/core-entity-review/stage2/current-subjects.inventory.json"
CANDIDATE = ".caprmedio_caprmedio/_projection/core-entity-review/presentation/operator.entity-graph.candidate.json"
CONSOLIDATED = ".caprmedio_caprmedio/_projection/core-entity-review/consolidated/nodes.review.json"
CONTRACT = ".caprmedio_caprmedio/_projection/core-entity-review/stage2/current-subjects.contract.md"
REVIEW_CONTRACT = ".caprmedio_caprmedio/_projection/core-entity-review/stage2/current-subjects.review.contract.md"


def digest(path):
    return hashlib.sha256((BASE / path).read_bytes()).hexdigest()


def content_span(path):
    raw = (BASE / path).read_bytes()
    lines = raw.splitlines(keepends=True)
    delimiters = [i for i, line in enumerate(lines) if line.rstrip(b"\r\n") == b"---"]
    assert len(delimiters) >= 2, path
    start = delimiters[1] + 2
    body = b"".join(lines[start - 1 :])
    return {
        "path": path,
        "sha256": hashlib.sha256(raw).hexdigest(),
        "start_line": start,
        "end_line": len(lines),
        "span_sha256": hashlib.sha256(body).hexdigest(),
        "reason": "Current Main Content only, beginning immediately after the closing frontmatter delimiter; it includes the Claim grounding this occurrence.",
    }


STATEMENT = {
    "CA-E-458": "the Evaluation rejects Framework Instance Settings treated as an Atom or Projection and requires its exact Revision, digest, and Journal receipt",
    "CA-E-459": "the Evaluation rejects Project Settings treated as an Atom or Projection and checks its authoritative TOML Carrier, selected Project Name and Atom prefix",
    "CA-E-460": "the QA case derives ownership and targeting Atom sets while keeping the `spec` alias from becoming a separate Entity or authority",
    "CA-E-461": "the Evaluation warns about a selected-sibling Claim boundary without automatically splitting or retargeting the Atom",
    "CA-E-462": "the Evaluation checks Atom replacement evidence while preserving unresolved or failed event evidence without inventing a conforming replacement",
    "CA-E-463": "the Evaluation keeps Summary belonging to its Atom and rejects an independently identified, versioned, or timestamped Summary Artifact",
    "CA-E-464": "the Evaluation keeps Journal recording and canonical log Projections independent from Git as a second authority",
    "CA-E-466": "the Evaluation distinguishes authoritative source facts from secondary graph representations and rejects a Projection gaining independent authority",
    "CA-E-469": "the Evaluation validates Project Structure declarations, their Carrier schema, Scope Unit parentage, and qualified structural fields",
    "CA-E-470": "the Evaluation distinguishes Project Structure declarations from folders, Goals, Carriers, and structural Projection observations",
    "CA-E-471": "the Evaluation checks structural changes and no-change repeats without bypassing authorization, confidence, recovery, or Project boundaries",
    "CA-E-472": "the Evaluation rejects simplified wording that removes or changes a necessary distinction or substitutes unregistered terminology",
    "CA-E-473": "the QA case preserves retry-limit source, effective value, inherited-versus-explicit status, and accounting without granting authority",
    "CA-E-476": "the QA case keeps Journal storage admission independent from Project conformance and does not invent identities or repair observations",
    "CA-E-477": "the QA case evaluates RMEDO conflict resolution without inventing winners, successor Claims, or completion after incomplete rechecking",
    "CA-E-481": "the Evaluation checks declared normative-authority Relation edges for registered typing and acyclicity",
}

GAPS = {
    "Artifact/Carrier": "the candidate names separate Artifact and Carrier roots but does not establish this qualified carrier connection or its cardinality",
    "Atom/Claim": "the candidate's Substance umbrella and RMED-to-Claim label do not establish Claim as a replacement Atom field while retaining its governed-Claim meaning",
    "Atom/Claim/Target Scope Unit": "the candidate distinguishes Substance Scope applicability from ownership but does not establish a Claim Target Scope Unit bearer path",
    "Atom/Content Role: Evaluation": "the candidate names no Evaluation allowed-value domain for Content Role",
    "Atom/Content Role: Operations": "the candidate's Operations-to-Operation role label does not establish a Content Role allowed-value mapping or an Operation definition identity",
    "Atom/Content Role: Plan/Type: Plan": "the candidate does not establish the Plan Content Role and Type Plan value domains or their qualified bearer",
    "Atom/Content Role: Requirement/Type: Goal": "the candidate does not establish the Requirement/Goal Content Role and Type domains or their qualified bearer",
    "Atom/Global Tier": "the candidate names no Global Tier field or allowed-value domain",
    "Atom/Identifier/Project Prefix": "the candidate confirms a Scope Unit prefix format, not an Atom-qualified Project Prefix field",
    "Atom/Local Tier: Principle": "the candidate names no Local Tier field or Principle allowed-value domain",
    "Atom/Revision/Updated At": "the candidate keeps Revision separate from Artifact fields and names Atom.Updated At, but does not establish an Atom Revision Updated At bearer",
    "Framework Instance Settings/Authoritative Carrier": "the candidate does not establish an authoritative Carrier field or binding for Framework Instance Settings",
    "Framework Instance Settings/Revision Binding": "the candidate does not establish a Framework Instance Settings-to-Revision binding field or its evidence semantics",
    "Project Settings/Authoritative Carrier": "the candidate does not establish an authoritative Carrier field or binding for Project Settings",
    "Project Settings/Revision Binding": "the candidate does not establish a Project Settings-to-Revision binding field or its evidence semantics",
    "Projection/Type: Artifact Change Log": "the candidate describes Projection lifecycle and source traceability but does not establish this Projection Type allowed-value domain",
    "Projection/Type: Process Log": "the candidate describes Projection lifecycle and source traceability but does not establish this Projection Type allowed-value domain",
    "Project Scope Unit Graph Projection": "the candidate has Projection rebuild rules but does not establish the qualified Project Scope Unit Graph Projection identity",
    "Structural Entity": "the candidate root list does not establish Structural Entity as a root, subtype, or Scope Unit equivalence",
    "Work Journal/Event": "the candidate distinguishes Journal records, history, and Execution but does not establish whether this qualified Event is one of them",
    "Project/normative authority graph": "the candidate does not establish the qualified Project normative-authority graph identity or a safe replacement",
}


def distinctions(occurrence):
    return [
        "Current Evaluation role and CORE_META_MODEL source scope remain source metadata; no key, body, grammar, native relation, identity, migration, or runtime change.",
        f"Exact old Subject {occurrence['old_value']!r}, field {occurrence['field']!r}, and index {occurrence['index']!r} remain individually accounted for.",
        "Captured-current evidence remains separate from frozen consolidated evidence and the candidate; no display notation is adopted as source authority.",
        "All output rows are non-executable research records only.",
    ]


def proposal(occurrence):
    old = occurrence["old_value"]
    statement = STATEMENT[occurrence["source_atom_id"]]
    if old == "Operator":
        return (
            "Actor/Operator", 0.95,
            f"Current Main Content says {statement}; the candidate explicitly includes Operator as an Actor Type. The candidate-only slash form preserves Operator as a subtype of Actor.",
            [
                {"pointer": "#/root_entities/2", "reason": "The pinned candidate defines Actor as who performs work."},
                {"pointer": "#/entity_identity_model/actor/type_examples", "reason": "The pinned candidate expressly includes Operator as an Actor Type example."},
            ],
            ["Operator remains a collective or generic Actor Type as applicable; it is not an authorization record, Carrier, or Execution."],
        )
    if old == "Atom":
        return (
            "Artifact/Atom", 0.95,
            f"Current Main Content says {statement}; the candidate expressly makes Atom narrower than Artifact and supplies Artifact/Atom as its compact candidate form.",
            [
                {"pointer": "#/root_entities/0/narrower_entities/0", "reason": "The pinned candidate expressly lists Atom as a narrower Entity of Artifact."},
                {"pointer": "#/dependent_entities/compact_examples", "reason": "The pinned candidate's compact examples expressly include Artifact/Atom."},
            ],
            ["Slash denotes the candidate subtype relation; Atom remains distinct from a Carrier, Revision, Projection, or actual Execution."],
        )
    if old == "Atom/Status":
        return (
            "Artifact/Atom.Status", 0.95,
            f"Current Main Content says {statement}; the candidate explicitly names Status as a dependent Atom Entity and uses Atom.Status as compact notation.",
            [
                {"pointer": "#/root_entities/0/narrower_entities/0/named_dependent_entity_examples", "reason": "The candidate expressly lists Status among named dependent Atom Entities."},
                {"pointer": "#/dependent_entities/compact_examples", "reason": "The candidate expressly uses Atom.Status for a dependent field."},
            ],
            ["Dot denotes a dependent field; Status remains distinct from lifecycle history, Revision, and deletion."],
        )
    if old == "Atom/Summary":
        return (
            "Artifact/Atom.Summary", 0.95,
            f"Current Main Content says {statement}; the candidate explicitly names Summary as a dependent Atom Entity and uses Atom.Summary as compact notation.",
            [
                {"pointer": "#/root_entities/0/narrower_entities/0/named_dependent_entity_examples", "reason": "The candidate expressly lists Summary among named dependent Atom Entities."},
                {"pointer": "#/dependent_entities/compact_examples", "reason": "The candidate expressly uses Atom.Summary for a dependent field."},
            ],
            ["Summary remains Atom-borne with no independent identity, Version, Updated At, Carrier, or lifecycle."],
        )
    if old == "Atom/Content Role":
        return (
            "Artifact/Atom.Content Role", 0.95,
            f"Current Main Content says {statement}; read with the candidate's Atom-under-Artifact and dependent-Property rules, this notation preserves Content Role as an Atom field rather than an allowed value or a root.",
            [
                {"pointer": "#/root_entities/0/narrower_entities/0", "reason": "The candidate places Atom as a narrower Entity of Artifact."},
                {"pointer": "#/dependent_entities/property_node_vs_relation", "reason": "The candidate defines a Property as a dependent Entity node of its owning Entity."},
                {"pointer": "#/dependent_entities/compact_examples", "reason": "The candidate uses dot notation for named dependent Atom fields."},
            ],
            ["Content Role remains distinct from its role-specific and Type allowed-value domains."],
        )
    if old == "Atom/Identifier":
        return (
            "Artifact/Atom.Identifier", 0.92,
            f"Current Main Content says {statement}; the candidate's dependent-entity identity rule selects an Atom by atom_id before a dependent field, supporting Identifier as an Atom-borne field without a standalone lifecycle.",
            [
                {"pointer": "#/root_entities/0/narrower_entities/0", "reason": "The candidate places Atom as a narrower Entity of Artifact."},
                {"pointer": "#/entity_identity_model/dependent_entity", "reason": "The candidate gives atom_id as the owner selector for dependent field identity."},
            ],
            ["The Atom identifier remains distinct from a Scope Unit prefix, Carrier path, Revision, and dependent-field display address."],
        )
    assert old in {"Atom/Revision", "Artifact/Revision"}, old
    return (
        "Revision", 0.95,
        f"Current Main Content says {statement}; the candidate expressly makes Revision a separate historical root and excludes Artifact.Revision, Artifact/Revision, Atom.Revision, and Atom/Revision as bearer-qualified paths.",
        [
            {"pointer": "#/root_entities/4", "reason": "The candidate defines Revision as a historical snapshot of an Artifact and expressly excludes Artifact/Revision and Atom/Revision paths."},
            {"pointer": "#/history_model/revision_role", "reason": "The candidate confirms Revision preserves a historical Artifact state."},
        ],
        ["Revision remains history rather than a dependent Artifact or Atom field; Version Number, Status, and Updated At domains are not broadened beyond their current evidence."],
    )


def review_occurrence(occurrence):
    out = dict(occurrence)
    old = occurrence["old_value"]
    statement = STATEMENT[occurrence["source_atom_id"]]
    if old in {"Operator", "Atom", "Atom/Status", "Atom/Summary", "Atom/Content Role", "Atom/Identifier", "Atom/Revision", "Artifact/Revision"}:
        value, confidence, reason, basis, extra = proposal(occurrence)
        decision = "proposed"
    elif old in GAPS:
        decision, value, confidence, basis = "unresolved", None, 0.0, []
        reason = f"Current Main Content says {statement}; {GAPS[old]}. No candidate-only string is proposed because it would alter or omit the captured qualification, field bearer, allowed-value domain, or Definition-versus-Execution distinction."
        extra = [f"The captured qualified identity {old!r} remains preserved pending evidence for a notation-preserving candidate mapping."]
    else:
        decision, value, confidence, basis = "unchanged", old, 1.0, []
        reason = f"Current Main Content says {statement}; the exact current Subject is retained because the candidate does not establish a narrower, notation-preserving replacement that keeps every captured qualification and domain."
        extra = ["The exact current Subject remains the proposed value; this does not infer a new root, dependent field, allowed value, identity, Carrier registry, native relation, or Execution." ]
    out.update(
        decision=decision,
        proposed_value=value,
        confidence=confidence,
        reason=reason,
        evidence=[content_span(occurrence["source_path"])],
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
        review["main_content_read"] = True
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
        "task_id": "CA-P-2024",
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
            "boundary": "All rows are non-executable display/research records only; no current source, grammar, native relation, key, identity, migration, or runtime change is authorized.",
        },
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
