"""Build the bounded, non-authoritative CA-P-2039 current-Subject review."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
STAGE = ROOT / ".caprmedio_caprmedio/_projection/core-entity-review/stage2"
INPUT = STAGE / "inputs/current-subjects.batch-048.json"
OUTPUT = STAGE / "reviews/current-subjects.batch-048.review.json"
CANDIDATE = ROOT / ".caprmedio_caprmedio/_projection/core-entity-review/presentation/operator.entity-graph.candidate.json"
CONSOLIDATED = ROOT / ".caprmedio_caprmedio/_projection/core-entity-review/consolidated/nodes.review.json"
PREPARATION = STAGE / "current-subjects.contract.md"
REVIEW = STAGE / "current-subjects.review.contract.md"
ENTITIES_GRAPH_TYPE = ROOT / ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1438-CORE_META_MODEL-CORE--define-entities-graph.md"
TERMS_GRAPH_TYPE = ROOT / ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1335-CORE_META_MODEL-CORE-REQUIREMENT--define-terms-graph.md"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def main_content_span(source: dict[str, object]) -> dict[str, object]:
    path = ROOT / str(source["relative_path"])
    raw = path.read_bytes()
    expected = str(source["full_file_sha256"])
    if digest(path) != expected:
        raise ValueError(f"stale source pin: {source['relative_path']}")
    lines = raw.splitlines(keepends=True)
    delimiters = [i for i, line in enumerate(lines) if line.rstrip(b"\r\n") == b"---"]
    if len(delimiters) < 2:
        raise ValueError(f"missing front matter: {source['relative_path']}")
    start = next((i for i in range(delimiters[1] + 1, len(lines)) if lines[i].strip()), None)
    end = next((i for i in range(len(lines) - 1, delimiters[1], -1) if lines[i].strip()), None)
    if start is None or end is None:
        raise ValueError(f"missing Main Content: {source['relative_path']}")
    return {
        "path": source["relative_path"],
        "sha256": expected,
        "start_line": start + 1,
        "end_line": end + 1,
        "span_sha256": sha256(b"".join(lines[start : end + 1])).hexdigest(),
        "reason": "The owning current Main Content was read in full and supplies this occurrence's meaning and uncertainty boundary.",
    }


def fixed_current_span(path: Path, expected_sha256: str, start_line: int, end_line: int, reason: str) -> dict[str, object]:
    """Pin a current supporting definition without confusing it with frozen evidence."""
    raw = path.read_bytes()
    if digest(path) != expected_sha256:
        raise ValueError(f"stale supporting source pin: {relative(path)}")
    lines = raw.splitlines(keepends=True)
    return {
        "path": relative(path),
        "sha256": expected_sha256,
        "start_line": start_line,
        "end_line": end_line,
        "span_sha256": sha256(b"".join(lines[start_line - 1 : end_line])).hexdigest(),
        "reason": reason,
    }


DEPENDENT_BASIS = [
    {
        "pointer": "#/dependent_entities/meaning",
        "reason": "The candidate confirms named Properties are dependent Entities inside an Artifact.",
    },
    {
        "pointer": "#/entity_identity_model/dependent_entity/identity",
        "reason": "The candidate confirms owner selector plus dependent field identity when current content establishes the owner and field.",
    },
]


def proposal(old: str) -> tuple[str, float, str, list[dict[str, str]], list[str]] | None:
    if old in {"Artifact/Revision", "Atom/Revision"}:
        return (
            "Revision",
            0.96,
            "The current body uses this Revision as historical or exact-definition evidence, distinct from the current Artifact. The candidate selects Revision as the historical snapshot root and explicitly excludes the legacy Artifact/Revision and Atom/Revision paths.",
            [
                {"pointer": "#/root_entities/4", "reason": "The candidate selects Revision as a historical Artifact snapshot."},
                {"pointer": "#/history_model/revision_role", "reason": "The candidate confirms Revision preserves historical Artifact state."},
            ],
            ["Historical Revision evidence remains separate from the current Artifact.", "No Artifact.Revision or Atom.Revision dependent-property identity is introduced."],
        )
    if old == "Workflow Run":
        return (
            "Execution/Workflow Run",
            0.96,
            "The current body distinguishes an actual Workflow Run and its evidence from the reusable Workflow definition. The candidate selects Workflow Run as an Execution kind.",
            [
                {"pointer": "#/root_entities/6", "reason": "The candidate selects Execution for actual runs of Operations."},
                {"pointer": "#/root_entities/6/proposed_kinds/2", "reason": "Workflow Run is the confirmed candidate Execution kind."},
            ],
            ["The actual Workflow Run remains distinct from its Workflow definition.", "No new native relation, retry route, or Run record grammar is admitted."],
        )
    if old == "Step Run":
        return (
            "Execution/Step Run",
            0.96,
            "The current body distinguishes an actual Step Run and its evidence from the reusable Step definition. The candidate selects Step Run as an Execution kind.",
            [
                {"pointer": "#/root_entities/6", "reason": "The candidate selects Execution for actual runs of Operations."},
                {"pointer": "#/root_entities/6/proposed_kinds/1", "reason": "Step Run is the confirmed candidate Execution kind."},
            ],
            ["The actual Step Run remains distinct from its Step definition.", "No new native relation, retry route, or Run record grammar is admitted."],
        )
    if old == "Operator":
        return (
            "Actor.Type: Operator",
            0.96,
            "The current body identifies Operator as the person who authorizes, performs, or retains the stated choice. The candidate defines Actor identity through Actor Type plus optional Name and explicitly lists Operator as a Type value.",
            [
                {"pointer": "#/entity_identity_model/actor/identity", "reason": "Actor identity is Actor Type plus optional Name, so Type is the dependent classification rather than a subtype hierarchy."},
                {"pointer": "#/entity_identity_model/actor/type_examples/1", "reason": "Operator is an explicit Actor Type example."},
            ],
            ["Operator remains the Actor Type value, not an invented individual identity or a new Actor subtype.", "Authorization and actual effects remain separate from the Actor classification."],
        )
    if old == "AI Agent":
        return (
            "Actor.Type: AI Agent",
            0.96,
            "The current body identifies AI Agent as a possible performer within its stated authority boundary. The candidate defines Actor identity through Actor Type plus optional Name and explicitly lists AI Agent as a Type value.",
            [
                {"pointer": "#/entity_identity_model/actor/identity", "reason": "Actor identity is Actor Type plus optional Name, so Type is the dependent classification rather than a subtype hierarchy."},
                {"pointer": "#/entity_identity_model/actor/type_examples/0", "reason": "AI Agent is an explicit Actor Type example."},
            ],
            ["AI Agent remains the Actor Type value, not an invented individual identity or a new Actor subtype.", "The source's permission and execution boundary is retained."],
        )
    if old == "Atom/Summary":
        return (
            "Atom.Summary",
            0.96,
            "The current body names Summary as an Atom fact preserved by the lifecycle action. The candidate's compact example confirms Atom-owned Summary notation.",
            DEPENDENT_BASIS + [{"pointer": "#/dependent_entities/compact_examples/1", "reason": "The candidate gives Atom.Summary as the compact dependent-field example."}],
            ["Summary remains Atom-owned and is not treated as a Carrier or separate lifecycle.", "No body-key rename or native admission follows from the notation proposal."],
        )
    if old == "Status":
        return (
            "Atom.Status",
            0.94,
            "The lifecycle body explicitly resolves the selected Atom's current and requested Status under its qualified model. The candidate's compact example confirms Atom-owned Status notation.",
            DEPENDENT_BASIS + [{"pointer": "#/dependent_entities/compact_examples/2", "reason": "The candidate gives Atom.Status as the compact dependent-field example."}],
            ["Status remains the selected Atom's dependent field under its role/type transition model.", "No universal status value set or storage-key migration is inferred."],
        )
    if old == "Atom/Content Role: Plan/Type: Plan":
        return (
            "Atom.Content Role: Plan/Type: Plan",
            0.94,
            "The current body identifies the bounded Plan through Content Role Plan and Type Plan. The proposal changes only the Atom-to-dependent-field separator and retains both role and Type/value qualifications.",
            DEPENDENT_BASIS + [{"pointer": "#/dependent_entities/compact_examples/1", "reason": "The candidate confirms dot notation for an Atom-owned dependent property."}],
            ["Content Role Plan and Type Plan remain separately qualified.", "No new allowed-value domain, Claim role, or Plan lifecycle is inferred."],
        )
    if old == "Atom/Content Role: Plan/Type: Plan/Definition of Done":
        return (
            "Atom.Content Role: Plan/Type: Plan.Definition of Done",
            0.94,
            "The current body requires the bounded Plan's Definition of Done as a distinct falsifying-condition field. The proposal retains the Plan role and Type chain while qualifying the named field.",
            DEPENDENT_BASIS,
            ["Definition of Done remains qualified by Content Role Plan and Type Plan.", "Its completion/falsification meaning is not flattened into Status or a generic completion claim."],
        )
    if old == "Projection/Type: Entities Graph":
        return (
            "Projection.Type: Entities Graph",
            0.92,
            "The current body names an Entities Graph as the requested derived Projection and keeps its source authority separate. Current CA-R-1438 defines Entities Graph as the Type value under Projection; the candidate supplies the generic owner-field model and derived-Projection boundary.",
            [
                {"pointer": "#/projection_member_model", "reason": "The candidate confirms Projection as the derived set of Atom instances with its own lifecycle."},
                {"pointer": "#/entity_identity_model/dependent_entity/identity", "reason": "The candidate confirms an owner selector plus dependent field identity; current CA-R-1438 establishes Projection as the owner and Type as the field."},
                {"pointer": "#/graph_model", "reason": "The candidate confirms Entities are graph nodes connected by typed Relations."},
            ],
            ["The Entities Graph remains derived rather than a new authoritative root.", "Source selection, Relation endpoint constraints, and Revision traceability are retained."],
        )
    if old == "Projection/Type: Terms Graph":
        return (
            "Projection.Type: Terms Graph",
            0.92,
            "The current body names a Terms Graph as the requested derived Projection and preserves governing Term authority. Current CA-R-1335 defines Terms Graph as the Type value under Projection; the candidate supplies the generic owner-field model and separate-Terms-graph boundary.",
            [
                {"pointer": "#/projection_member_model", "reason": "The candidate confirms Projection as a derived set with its own lifecycle."},
                {"pointer": "#/entity_identity_model/dependent_entity/identity", "reason": "The candidate confirms an owner selector plus dependent field identity; current CA-R-1335 establishes Projection as the owner and Type as the field."},
                {"pointer": "#/terms_graph_boundary", "reason": "The candidate confirms Terms belong to a separate graph."},
            ],
            ["The Terms Graph remains derived and separate from the Entities Graph.", "No Term meaning, cross-graph Relation, or source authority is admitted."],
        )
    return None


def unchanged(old: str) -> tuple[str, float, str, list[str]] | None:
    if old in {"Atom", "Artifact", "Carrier", "Entity", "Property", "Relation"}:
        return (
            old,
            0.96,
            "The current body uses this as the direct Entity category selected by the candidate. Retaining the exact root does not add a display prefix, owner, endpoint, or Carrier binding.",
            ["The direct Entity category remains unqualified.", "No new hierarchy, property, relation endpoint, or storage convention is inferred."],
        )
    if old in {"Journal", "Relation Kind"}:
        return (
            old,
            0.94,
            "The current body uses this confirmed concept directly. The candidate confirms its meaning but does not require a new Subject identity or grammar rewrite, so the exact current label is retained.",
            ["The current history or typed-relation distinction is retained.", "No Journal-record relation, endpoint, or lexical renaming is admitted."],
        )
    return None


def unresolved(old: str) -> tuple[float, str, list[str]]:
    if old in {"Action", "Step", "Workflow"}:
        return (
            0.5,
            "The current body uses this as an Operation definition, while the candidate distinguishes Operation definitions from actual Execution and selects no independent candidate identity for this definition kind.",
            ["The Operation definition remains distinct from Action, Step, or Workflow Runs.", "No Execution-kind substitution is made for a definition."],
        )
    if old in {"Evaluation", "Implementation", "Spec"}:
        return (
            0.5,
            "The current body uses this role or source-class distinction, but the candidate does not establish an exact root, owner-qualified field, or allowed-value domain preserving that meaning.",
            ["The role/source-class meaning remains distinct from Substance and from implementation evidence.", "No unadmitted allowed value or new identity is inferred."],
        )
    if old in {"Term", "Governed Term", "Definition Atom"}:
        return (
            0.5,
            "The current body uses this within Terms-graph authority. The candidate keeps Terms in a separate graph but does not select a replacement identity for this qualified Term meaning.",
            ["The Terms-graph boundary and qualified Term meaning are retained.", "No Entity-root or cross-graph Relation is invented."],
        )
    if old in {"Workflow/Relation Kind: On Result", "Step/Agentic Execution Context"}:
        return (
            0.5,
            "The current body requires an exact typed execution binding. The candidate does not establish a replacement retaining its endpoint, context, direction, and cardinality qualifications.",
            ["The typed execution relation/context remains distinct from the generic Execution root.", "No new native Relation kind or Subject grammar is admitted."],
        )
    if old in {"Atom/Claim", "Atom/Content Role: Plan/Status"}:
        return (
            0.5,
            "The current body uses this qualified Atom fact, but the candidate does not establish a path retaining every Content Role, Claim, or status-model distinction in the legacy expression.",
            ["Role, Claim, and status-model distinctions remain separate.", "No blind slash-to-dot rewrite or generic Status substitution is made."],
        )
    return (
        0.5,
        "The current body supplies this bounded operational meaning, but the candidate selects no exact root, bearer-qualified field, allowed-value domain, or Relation identity that preserves it.",
        ["The source-specific operational meaning remains explicit.", "No unsupported identity, namespace prefix, or grammar admission is inferred."],
    )


def occurrence_review(occurrence: dict[str, object], span: dict[str, object]) -> dict[str, object]:
    old = str(occurrence["old_value"])
    row = dict(occurrence)
    proposed = proposal(old)
    if proposed is not None:
        value, confidence, reason, basis, distinctions = proposed
        row.update(decision="proposed", proposed_value=value, confidence=confidence, reason=reason, candidate_basis=basis, preserved_distinctions=distinctions, question=None)
    else:
        retained = unchanged(old)
        if retained is not None:
            value, confidence, reason, distinctions = retained
            row.update(decision="unchanged", proposed_value=value, confidence=confidence, reason=reason, candidate_basis=[], preserved_distinctions=distinctions, question=None)
        else:
            confidence, reason, distinctions = unresolved(old)
            row.update(decision="unresolved", proposed_value=None, confidence=confidence, reason=reason, candidate_basis=[], preserved_distinctions=distinctions, question=None)
    evidence = [span]
    if old == "Projection/Type: Entities Graph":
        evidence.append(fixed_current_span(ENTITIES_GRAPH_TYPE, "d8eea5e569edc4fe12d24b987724901091a1129e894586b2fe875b62af27ab71", 22, 36, "Current CA-R-1438 explicitly defines Entities Graph as the Type value under Projection; it supports the owner and allowed value retained by this proposal."))
    elif old == "Projection/Type: Terms Graph":
        evidence.append(fixed_current_span(TERMS_GRAPH_TYPE, "98ef6a5058ada19dd51563545a1c3ad46e8b18a637305dce90dde15eb5bfddf1", 22, 36, "Current CA-R-1335 explicitly defines Terms Graph as the Type value under Projection; it supports the owner and allowed value retained by this proposal."))
    row.update(evidence=evidence, executable=False)
    return row


def main() -> None:
    batch = json.loads(INPUT.read_text(encoding="utf-8"))
    if digest(INPUT) != "dfa30de3e07116c8bede7cb5690c1762ad9faac02311f3d2e495842853aa0343":
        raise ValueError("batch-048 input pin changed")
    sources = batch["selected_sources"]
    spans = {str(source["relative_path"]): main_content_span(source) for source in sources}
    source_reviews = []
    for source in sources:
        review = dict(source)
        review.update(main_content_read={"read": True, **spans[str(source["relative_path"])]}, finding_dispositions=[{"finding": finding, "reason": "The input finding remains recorded; this review does not repair source metadata."} for finding in source["findings"]], questions=[])
        source_reviews.append(review)
    report = {
        "schema_version": 1,
        "non_authoritative": True,
        "source_migration": "not_performed",
        "native_admission": "not_performed",
        "task_id": "CA-P-2039",
        "batch_id": batch["batch_id"],
        "input_batch_path": ".caprmedio_caprmedio/_projection/core-entity-review/stage2/inputs/current-subjects.batch-048.json",
        "input_batch_sha256": digest(INPUT),
        "input_inventory_sha256": batch["input_inventory_sha256"],
        "evidence_pins": {
            "frozen_candidate": {"path": relative(CANDIDATE), "sha256": digest(CANDIDATE)},
            "consolidated_review": {"path": relative(CONSOLIDATED), "sha256": digest(CONSOLIDATED), "git_commit": "a971d0e00c33c779f485fc8cad63194894d440fb"},
            "preparation_contract": {"path": relative(PREPARATION), "sha256": digest(PREPARATION)},
            "review_contract": {"path": relative(REVIEW), "sha256": digest(REVIEW)},
            "current_entities_graph_type_definition": {"path": relative(ENTITIES_GRAPH_TYPE), "sha256": digest(ENTITIES_GRAPH_TYPE)},
            "current_terms_graph_type_definition": {"path": relative(TERMS_GRAPH_TYPE), "sha256": digest(TERMS_GRAPH_TYPE)},
        },
        "source_reviews": source_reviews,
        "occurrences": [occurrence_review(occurrence, spans[str(occurrence["source_path"])]) for occurrence in batch["occurrences"]],
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
