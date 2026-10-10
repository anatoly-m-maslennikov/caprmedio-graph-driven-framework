import hashlib
import json
from pathlib import Path

BASE = Path(".")
INPUT = ".caprmedio_caprmedio/_projection/core-entity-review/stage2/inputs/current-subjects.batch-040.json"
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
    "CA-D-369": "the Claim requires the explicit Framework Instance Settings confidence default to use the named integer-percentage TOML field",
    "CA-D-370": "the Claim requires the Framework Instance Settings TOML Carrier to encode a Project control-root locator resolving to the prescribed Directory Carrier",
    "CA-D-371": "the Claim requires the Framework Instance Settings TOML Carrier to encode one or more code-root locators",
    "CA-D-372": "the Claim requires Framework Instance Settings to encode selected active and background Tools with per-Tool settings",
    "CA-D-373": "the Claim requires Framework Instance Settings to encode enabled or disabled Extensions with qualified revisions and settings",
    "CA-D-374": "the Claim assigns instance and Project Authority Mode fields while keeping unit overrides in authoritative Project Structure",
    "CA-D-375": "the Claim requires Project Settings to encode the Operator-selected lowercase Project Name before the first Project Atom or Implementation exists",
    "CA-D-376": "the Claim requires Project Settings to encode the Operator-selected Atom prefix before the first Project Atom exists",
    "CA-D-377": "the Claim excludes Atom metadata, Revision metadata, relations, rationale, and provenance from Framework Instance Settings TOML",
    "CA-D-378": "the Claim defines assigned Atom ID encoding, its Content Role letter domain, and the Plan-qualified P identifier",
    "CA-D-380": "the Claim specifies decimal Carrier renderings of Navigational Order Number without changing the stored numeric value",
    "CA-D-381": "the Claim specifies decimal Carrier renderings of Work Sequence Number",
    "CA-D-383": "the Claim requires a qualified reporting_mode field in Framework Instance Settings TOML",
    "CA-D-386": "the Claim makes Priority a Concern Atom Carrier field with a high/medium/low domain and requires non-Concern Atoms to omit it",
    "CA-D-387": "the Claim requires the named atomic-admission strictness field and its governed value domain in Framework Instance Settings TOML",
    "CA-D-389": "the Claim constrains Analysis Type filename tokens while expressly not renaming a Type, admitting a Type, or prescribing a YAML Type value",
    "CA-D-390": "the Claim permits a Framework Instance Settings Artifact timestamp-timezone field with local, UTC, or IANA values",
    "CA-D-391": "the Claim gives a retained Project Scope Unit Graph Projection only a derived effective authority_mode",
    "CA-D-392": "the Claim requires Project Scope Unit Graph Projections to expose canonical and obsolete Project names without becoming their authority",
    "CA-D-393": "the Claim derives external Type names from internal Type names without changing the registered Type domain",
}

GAPS = {
    "Atom/Carrier": "the candidate names separate Atom/Artifact and Carrier concepts but establishes no Atom-to-Carrier identity, cardinality, or per-field registry",
    "Atom/Content Role: Analysis/Type": "the candidate's Analysis-to-Question role label does not establish an Analysis Content Role Type bearer or value domain",
    "Atom/Content Role: Plan/Type: Plan": "the candidate does not establish the Plan Content Role and Type Plan allowed-value domains or their qualified bearer",
    "Atom/Content Role: Plan/Type: Plan/Identifier": "the candidate does not establish a Plan-qualified Type/Identifier nesting or its allowed-value domain",
    "Authority Mode": "the candidate names no Authority Mode field or allowed-value domain",
    "Framework Instance Settings/Artifact Timestamp Timezone": "the candidate names no Framework Instance Settings field topology or timezone allowed-value domain",
    "Framework Instance Settings/Authoritative Carrier/Content": "the candidate has no authoritative Carrier-content identity or field mapping for Framework Instance Settings",
    "Framework Instance Settings/Carrier/Atom metadata exclusion": "the candidate does not establish this carrier-qualified exclusion field and forbids inferring a per-property Carrier registry",
    "Framework Instance Settings/Confidence/Semantic Resolution Threshold/Carrier": "the candidate names no Framework Instance Settings confidence-field Carrier binding",
    "Framework Instance Settings/Extension selections": "the candidate has no Framework Instance Settings Extension-selection field or value domain",
    "Framework Instance Settings/Tool selections": "the candidate has no Framework Instance Settings Tool-selection field or value domain",
    "Framework Instance Settings/code-root locators": "the candidate has no Framework Instance Settings code-root locator field or Carrier binding",
    "Framework Instance Settings/framework control-root locator": "the candidate has no Framework Instance Settings control-root locator field or Directory Carrier binding",
    "Framework Instance Settings/interaction/reporting mode": "the candidate has no Framework Instance Settings interaction/reporting field or allowed-value domain",
    "Priority": "the candidate names no Concern-qualified Priority field or high/medium/low allowed-value domain",
    "Project Scope Unit Graph Projection": "the candidate has Projection lifecycle rules but does not establish the qualified Project Scope Unit Graph Projection identity",
    "Project Settings/Atom Prefix/Carrier": "the candidate has no Project Settings Atom Prefix Carrier binding and forbids treating a Carrier path as an identity",
    "Project Settings/Project identity/Carrier": "the candidate has no Project Settings Project identity Carrier binding and its Project-name relation remains qualified",
}

DISPLAY_ONLY_ARTIFACT_PREFIX_OCCURRENCES = {
    ("CA-D-375", "depends_on", 4),
    ("CA-D-376", "depends_on", 1),
    ("CA-D-377", "depends_on", 1),
    ("CA-D-378", "depends_on", 0),
    ("CA-D-378", "governs", None),
    ("CA-D-386", "depends_on", 0),
    ("CA-D-393", "depends_on", 0),
}


def distinctions(occurrence):
    return [
        "Current Delivery role and CORE_META_MODEL source scope remain source metadata; no key, body, grammar, native relation, identity, migration, or runtime change.",
        f"Exact old Subject {occurrence['old_value']!r}, field {occurrence['field']!r}, and index {occurrence['index']!r} remain individually accounted for.",
        "Captured-current evidence remains separate from frozen consolidated evidence and the candidate; no display notation is adopted as source authority.",
        "All output rows are non-executable research records only.",
    ]


def proposal(occurrence):
    old = occurrence["old_value"]
    statement = STATEMENT[occurrence["source_atom_id"]]
    if old == "Atom":
        return (
            "Artifact/Atom", 0.95,
            f"Current Main Content says {statement}; the candidate expressly makes Atom narrower than Artifact and supplies Artifact/Atom as its compact candidate form.",
            [
                {"pointer": "#/root_entities/0/narrower_entities/0", "reason": "The candidate expressly lists Atom as a narrower Entity of Artifact."},
                {"pointer": "#/dependent_entities/compact_examples", "reason": "The candidate's compact examples expressly include Artifact/Atom."},
            ],
            ["Slash denotes the candidate subtype relation; Atom remains distinct from a Carrier, Revision, Projection, or actual Execution."],
        )
    if old == "Atom/Content Role":
        return (
            "Artifact/Atom.Content Role", 0.95,
            f"Current Main Content says {statement}; read with the candidate's Atom-under-Artifact and dependent-Property rules, this notation preserves Content Role as the Atom field rather than a role value, Type value, or root.",
            [
                {"pointer": "#/root_entities/0/narrower_entities/0", "reason": "The candidate places Atom as a narrower Entity of Artifact."},
                {"pointer": "#/dependent_entities/property_node_vs_relation", "reason": "The candidate defines a Property as a dependent Entity node of its owning Entity."},
                {"pointer": "#/dependent_entities/compact_examples", "reason": "The candidate uses dot notation for named dependent Atom fields."},
            ],
            ["Content Role remains distinct from role-specific, Type, and identifier allowed-value domains."],
        )
    if old == "Atom/Identifier":
        return (
            "Artifact/Atom.Identifier", 0.92,
            f"Current Main Content says {statement}; the candidate's dependent-entity identity rule selects an Atom by atom_id before a dependent field, supporting Identifier as Atom-borne rather than an independent lifecycle.",
            [
                {"pointer": "#/root_entities/0/narrower_entities/0", "reason": "The candidate places Atom as a narrower Entity of Artifact."},
                {"pointer": "#/entity_identity_model/dependent_entity", "reason": "The candidate gives atom_id as the owner selector for dependent field identity."},
            ],
            ["The assigned Atom identifier remains distinct from a Project Settings prefix, Carrier path, Type letter, and Revision."],
        )
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
    assert old == "Artifact/Revision", old
    return (
        "Revision", 0.95,
        f"Current Main Content says {statement}; the candidate expressly makes Revision a separate historical root and excludes Artifact.Revision, Artifact/Revision, Atom.Revision, and Atom/Revision as bearer-qualified paths.",
        [
            {"pointer": "#/root_entities/4", "reason": "The candidate defines Revision as a historical snapshot of an Artifact and expressly excludes Artifact/Revision paths."},
            {"pointer": "#/history_model/revision_role", "reason": "The candidate confirms Revision preserves a historical Artifact state."},
        ],
        ["Revision remains history rather than a dependent Artifact field; the current Atom-metadata exclusion does not create a per-field Carrier or version registry."],
    )


def review_occurrence(occurrence):
    out = dict(occurrence)
    old = occurrence["old_value"]
    statement = STATEMENT[occurrence["source_atom_id"]]
    occurrence_key = (occurrence["source_atom_id"], occurrence["field"], occurrence["index"])
    if occurrence_key in DISPLAY_ONLY_ARTIFACT_PREFIX_OCCURRENCES:
        decision, value, confidence, basis = "unresolved", None, 0.0, []
        reason = (
            f"Current Main Content says {statement}; the candidate's Artifact/Atom compact example is display notation only "
            "and does not establish a changed canonical identity or an adopted namespace for this occurrence. "
            "No candidate-only string is proposed."
        )
        extra = [
            f"The captured identity {old!r} remains preserved pending source-specific proof of a non-display-only candidate mapping."
        ]
    elif old in {"Atom", "Atom/Content Role", "Atom/Identifier", "Operator", "Artifact/Revision"}:
        value, confidence, reason, basis, extra = proposal(occurrence)
        decision = "proposed"
    elif old in GAPS:
        decision, value, confidence, basis = "unresolved", None, 0.0, []
        reason = f"Current Main Content says {statement}; {GAPS[old]}. No candidate-only string is proposed because it would alter or omit the captured qualification, field bearer, allowed-value domain, alias boundary, or Carrier distinction."
        extra = [f"The captured qualified identity {old!r} remains preserved pending evidence for a notation-preserving candidate mapping."]
    else:
        decision, value, confidence, basis = "unchanged", old, 1.0, []
        reason = f"Current Main Content says {statement}; the exact current Subject is retained because the candidate does not establish a narrower, notation-preserving replacement that keeps every captured qualification and domain."
        extra = ["The exact current Subject remains the proposed value; this does not infer a new root, dependent field, allowed value, identity, Carrier registry, native relation, alias, or Execution."]
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
        "task_id": "CA-P-2031",
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
