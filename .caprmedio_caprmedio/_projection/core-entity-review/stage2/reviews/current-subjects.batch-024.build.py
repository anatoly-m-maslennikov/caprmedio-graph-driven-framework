import hashlib
import json
from pathlib import Path


BASE = Path(".")
INPUT = ".caprmedio_caprmedio/_projection/core-entity-review/stage2/inputs/current-subjects.batch-024.json"
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
    markers = [i for i, line in enumerate(lines) if line.rstrip(b"\r\n") == b"---"]
    assert len(markers) >= 2, path
    start = markers[1] + 2
    content = b"".join(lines[start - 1 :])
    return {
        "path": path,
        "sha256": hashlib.sha256(raw).hexdigest(),
        "start_line": start,
        "end_line": len(lines),
        "span_sha256": hashlib.sha256(content).hexdigest(),
        "reason": "Current Main Content only, beginning immediately after the closing frontmatter delimiter; it includes the Claim grounding this occurrence.",
    }


STATEMENTS = {
    "CA-R-380": "the Claim requires an Operator-configurable semantic-resolution Confidence Threshold instance default",
    "CA-R-626": "the Claim distinguishes declared Scope Unit facts from Project Structure, derived values, Settings, and Carrier materialization",
    "CA-R-643": "the Claim requires every governed Claim to have exactly one authoritative Atom owner",
    "CA-R-655": "the Claim defines an Atom as the smallest independently governed Artifact",
    "CA-R-658": "the Claim defines Principle as the Project-only highest Local Tier",
    "CA-R-659": "the Claim defines Core as the foundational Spec tier governing greater Global Tiers within its Scope Unit",
    "CA-R-660": "the Claim defines Standard as the default lowest Local Tier within a Scope Unit",
    "CA-R-680": "the Claim restricts a Project Scope Unit to ordered Principle, Core, and Standard Atom Local Tiers",
    "CA-R-718": "the Claim keeps an Atom Claim Target Scope Unit reference and Main Content applicability from altering structural ownership",
    "CA-R-728": "the Claim defines Project Atom ID as the immutable identity of one accepted Project-owned Atom",
    "CA-R-740": "the Claim requires every Atom to have exactly one Content Role",
    "CA-R-771": "the Claim requires an Atom split when content can be independently accepted, replaced, or retired",
    "CA-R-794": "the Claim classifies Evaluation Atoms by applicable Local Tier without deriving tier from Claim Scope breadth",
    "CA-R-796": "the Claim requires every tier-parent relation between Atoms to connect Atoms with the same Atom Scope",
    "CA-R-806": "the Claim requires each admitted Relation Kind to have one canonical metadata record with explicit endpoint and authority constraints",
    "CA-R-807": "the Claim confines replacement history to an authoritative Journal event and defers replacement relations",
    "CA-R-808": "the Claim requires declared relations to follow their registered family ordering domains",
    "CA-R-829": "the Claim makes active Current-scope Requirement Atoms in one Local Tier authority peers",
    "CA-R-833": "the Claim requires the normative-authority subgraph to be explicit, typed, and acyclic",
    "CA-R-834": "the Claim partitions governed project-containment Primary Entity nodes into Artifact or Structural Entity",
}

GAPS = {
    "Framework Instance Settings/Confidence/Semantic Resolution Threshold": "the candidate names no Framework Instance Settings-to-Confidence field topology or threshold value domain",
    "Atom/Content Role: Requirement/Type: Goal": "the candidate names neither the Requirement/Goal Content Role domain nor its Type bearer",
    "Project Scope Unit Graph Projection": "the candidate has Projection rebuild rules but does not establish the qualified Project Scope Unit Graph Projection identity",
    "Claim": "the candidate's RMED-to-Claim label does not establish Claim as a replacement property/value for this governed Claim identity",
    "Atom/Local Tier": "the candidate names no Local Tier field or allowed-value domain",
    "Atom/Local Tier: Principle": "the candidate names no Local Tier field or Principle allowed-value domain",
    "Atom/Global Tier": "the candidate names no Global Tier field or allowed-value domain",
    "Atom/Claim": "the candidate does not establish Claim as an Atom dependent field while preserving the Claim qualifier",
    "Atom/Local Tier: General": "the candidate names no Local Tier field or General allowed-value domain",
    "Atom/Local Tier: Standard": "the candidate names no Local Tier field or Standard allowed-value domain",
    "Atom/Local Tier: Core": "the candidate names no Local Tier field or Core allowed-value domain",
    "Atom/Claim/Target Scope Unit": "the candidate does not establish a Claim Target Scope Unit dependent field or its qualified owner",
    "Markdown Atom Carrier/Main Content": "the separate Carrier root does not establish a Main Content carrier/property connection",
    "Atom/Content Role: Evaluation": "the candidate names no Evaluation Content Role allowed-value domain",
    "Atom/Scope": "the candidate calls Substance Scope an applicability condition but does not establish it as an Atom Scope field or qualified owner",
    "Atom/Content Role: Evaluation/Local Tier": "the candidate names neither the Evaluation Content Role nor Local Tier domains or their relationship",
    "artifact-model": "the candidate defines Artifact but not an artifact-model identity or model-view mapping",
    "relation-model": "the candidate defines Relation and Relation Type/Kind but not a relation-model identity or model-view mapping",
    "atom-boundary": "the candidate's Artifact/Atom boundary does not establish the captured atom-boundary identity",
    "authority": "the candidate does not establish an authority identity or an owner/property path for it",
    "Project/normative authority graph": "the candidate does not establish the qualified Project normative-authority graph identity",
    "Primary Entity": "the candidate root list does not establish Primary Entity as a subtype, field, or exhaustive partition bearer",
    "Structural Entity": "the candidate does not establish Structural Entity as a root, subtype, or Scope Unit equivalence",
    "project-containment graph": "the candidate does not establish the project-containment graph identity or a safe replacement",
}


def distinctions(occurrence):
    return [
        "Current Requirement role and CORE_META_MODEL source scope remain source metadata; no key, body, grammar, native relation, identity, migration, or runtime change.",
        f"Exact old Subject {occurrence['old_value']!r}, field {occurrence['field']!r}, and index {occurrence['index']!r} remain individually accounted for.",
        "Captured-current evidence remains separate from frozen consolidated evidence and the candidate; no display notation is adopted as source authority.",
        "All output rows are non-executable research records only.",
    ]


def proposal(occurrence):
    old = occurrence["old_value"]
    statement = STATEMENTS[occurrence["source_atom_id"]]
    if old == "Operator":
        return (
            "Actor/Operator",
            0.95,
            f"Current Main Content says {statement}; the candidate explicitly includes Operator as an Actor Type. The candidate-only slash form preserves Operator as a subtype of Actor.",
            [
                {"pointer": "#/root_entities/2", "reason": "The pinned candidate defines Actor as who performs work."},
                {"pointer": "#/entity_identity_model/actor/type_examples", "reason": "The pinned candidate expressly includes Operator as an Actor Type example."},
            ],
            ["Operator remains a collective or generic Actor Type as applicable; it is not an authorization record, a Carrier, or an Execution."],
        )
    if old == "Atom":
        return (
            "Artifact/Atom",
            0.95,
            f"Current Main Content says {statement}; the candidate expressly makes Atom narrower than Artifact and supplies Artifact/Atom as its compact candidate form.",
            [
                {"pointer": "#/root_entities/0/narrower_entities/0", "reason": "The pinned candidate expressly lists Atom as a narrower Entity of Artifact."},
                {"pointer": "#/dependent_entities/compact_examples", "reason": "The pinned candidate's compact examples expressly include Artifact/Atom."},
            ],
            ["Slash denotes the candidate subtype relation; Atom keeps its captured independently-governed meaning and is not reduced to a property or Carrier."],
        )
    if old == "Atom/Content Role":
        return (
            "Artifact/Atom.Content Role",
            0.95,
            f"Current Main Content says {statement}; read with the candidate's Atom-under-Artifact and named dependent Property rules, the notation preserves Content Role as the Atom field rather than an allowed value or a new root.",
            [
                {"pointer": "#/root_entities/0/narrower_entities/0", "reason": "The pinned candidate places Atom as a narrower Entity of Artifact."},
                {"pointer": "#/dependent_entities/property_node_vs_relation", "reason": "The pinned candidate defines a Property as a dependent Entity node of its owning Entity."},
                {"pointer": "#/dependent_entities/compact_examples", "reason": "The pinned candidate uses dot notation for named dependent Atom fields."},
            ],
            ["Dot denotes the candidate dependent-property relation; Content Role remains distinct from its qualified allowed-value and Type domains."],
        )
    assert old in {"Artifact/Identity", "Project Atom ID"}, old
    return (
        "Artifact/Atom.Project Atom ID",
        0.95,
        f"Current Main Content says {statement}; the candidate's owner-selector-plus-field rule supports retaining Project Atom ID as the named Atom field inside Artifact without treating it as a Carrier path or standalone lifecycle.",
        [
            {"pointer": "#/root_entities/0/narrower_entities/0", "reason": "The pinned candidate places Atom as a narrower Entity of Artifact."},
            {"pointer": "#/entity_identity_model/dependent_entity", "reason": "The pinned candidate confirms dependent identity as owner selector plus dependent field."},
        ],
        ["The Project-owned Atom qualification and immutable-identity meaning remain explicit; dot denotes the dependent field, not a native parser or key migration."],
    )


def review_occurrence(occurrence):
    out = dict(occurrence)
    old = occurrence["old_value"]
    statement = STATEMENTS[occurrence["source_atom_id"]]
    if old in {"Operator", "Atom", "Atom/Content Role", "Artifact/Identity", "Project Atom ID"}:
        value, confidence, reason, basis, extra = proposal(occurrence)
        decision = "proposed"
    elif old in GAPS:
        decision, value, confidence, basis = "unresolved", None, 0.0, []
        reason = f"Current Main Content says {statement}; {GAPS[old]}. No candidate-only string is proposed because it would alter or omit the captured qualification, field bearer, or allowed-value domain."
        extra = [f"The captured qualified identity {old!r} remains preserved pending evidence for a notation-preserving candidate mapping."]
    else:
        decision, value, confidence, basis = "unchanged", old, 1.0, []
        reason = f"Current Main Content says {statement}; the exact current Subject is retained because the candidate does not establish a narrower, notation-preserving replacement that keeps every captured qualifier and domain."
        extra = ["The exact current Subject remains the proposed value; this does not infer a new root, dependent field, allowed value, identity, or native relation."]
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
    assert counts == {"proposed": 10, "unchanged": 23, "unresolved": 37}, counts
    report = {
        "schema_version": 1,
        "non_authoritative": True,
        "source_migration": "not_performed",
        "native_admission": "not_performed",
        "task_id": "CA-P-2015",
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
