#!/usr/bin/env python3
"""Build the bounded CA-P-1992 current-Subject review from its pinned inputs.

The report is deliberately derived only from batch 001, its current original
sources, and the two frozen review artifacts.  It makes no source mutation or
grammar/native-admission claim.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[5]
BATCH_REL = Path(
    ".caprmedio_caprmedio/_projection/core-entity-review/stage2/inputs/"
    "current-subjects.batch-001.json"
)
INVENTORY_REL = Path(
    ".caprmedio_caprmedio/_projection/core-entity-review/stage2/"
    "current-subjects.inventory.json"
)
OUTPUT_REL = Path(
    ".caprmedio_caprmedio/_projection/core-entity-review/stage2/reviews/"
    "current-subjects.batch-001.review.json"
)
CANDIDATE_REL = Path(
    ".caprmedio_caprmedio/_projection/core-entity-review/presentation/"
    "operator.entity-graph.candidate.json"
)
CONSOLIDATED_REVIEW_REL = Path(
    ".caprmedio_caprmedio/_projection/core-entity-review/consolidated/"
    "nodes.review.json"
)
SUBJECTS_CONTRACT_REL = Path(
    ".caprmedio_caprmedio/_projection/core-entity-review/stage2/"
    "current-subjects.contract.md"
)
REVIEW_CONTRACT_REL = Path(
    ".caprmedio_caprmedio/_projection/core-entity-review/stage2/"
    "current-subjects.review.contract.md"
)
CAPTURED_CORE_COMMIT = "a971d0e00c33c779f485fc8cad63194894d440fb"

EXPECTED = {
    BATCH_REL: "84355ad3a75e6f070b2580993580070f4ef7a43d49eb18f2b657a16baa6ee194",
    INVENTORY_REL: "e284dbe4943568bc75b7f9ba63ebf583372a60813e62eee3d43b5b75b270220a",
    CANDIDATE_REL: "99e7710f5ef83df2b1f3ec1ef4142547655e63bef7415266c5521380da7fa99b",
    CONSOLIDATED_REVIEW_REL: "e4cb9c76b441c13115e87e141890a9dab58634a7a62fb1b3bc32168dbac261f6",
    SUBJECTS_CONTRACT_REL: "5eb0d90022b68a7d1d2cd27cf60a147deaf4161cb9b2e1c8bdf6c4ef8f2a10bf",
    REVIEW_CONTRACT_REL: "b7c9c065f997d5bae1409f5c09b4223d08327a523decab6d26c2e4425fd2c28b",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main_content_span(relative_path: str, source_sha256: str) -> dict[str, Any]:
    """Return the full current Markdown Main Content span after front matter."""
    path = ROOT / relative_path
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != source_sha256:
        raise ValueError(f"stale source pin: {relative_path}")
    lines = raw.splitlines(keepends=True)
    delimiters = [
        index
        for index, line in enumerate(lines)
        if line.rstrip(b"\r\n") == b"---"
    ]
    if len(delimiters) < 2:
        raise ValueError(f"front matter not found: {relative_path}")
    first = next(
        (index for index in range(delimiters[1] + 1, len(lines)) if lines[index].strip()),
        None,
    )
    last = next(
        (index for index in range(len(lines) - 1, delimiters[1], -1) if lines[index].strip()),
        None,
    )
    if first is None or last is None:
        raise ValueError(f"missing Main Content: {relative_path}")
    span = b"".join(lines[first : last + 1])
    return {
        "path": relative_path,
        "sha256": source_sha256,
        "start_line": first + 1,
        "end_line": last + 1,
        "span_sha256": hashlib.sha256(span).hexdigest(),
    }


RELATION_VALUES = {
    "Rationale For Relation",
    "Method For Relation",
    "Evaluation For Relation",
    "Delivery For Relation",
    "Implementation Of Relation",
    "Evidence For Relation",
    "Concern About Relation",
}


def preserved_for(atom_id: str, old_value: str) -> list[str]:
    if old_value == "atom-boundary":
        return [
            "The legacy atom-boundary reference remains exact and pathless.",
            "No Artifact/Atom display path or new native identity is inferred.",
        ]
    if old_value == "relation-model":
        return [
            "The broad relation-model reference remains exact and pathless.",
            "Typed-relation endpoints and ownership are not collapsed into a root label.",
        ]
    if old_value == "lifecycle-traceability":
        return [
            "The lifecycle-traceability reference remains exact and pathless.",
            "Active/current, archived history, Journal, and Projection distinctions remain separate.",
        ]
    if old_value.startswith("Atom/Content Role:"):
        value = old_value.split(": ", 1)[1]
        return [
            f"The Content Role allowed value {value!r} remains qualified rather than collapsed.",
            "Evaluation target authority and Local Tier distinctions remain separate.",
        ]
    if old_value == "Atom/Local Tier":
        return [
            "Local Tier remains distinct from Content Role and relation target qualification.",
            "Standard versus Core/General behavior is retained without a storage-key rename.",
        ]
    if old_value == "Scope Unit/Scope":
        return [
            "Scope Unit Scope remains distinct from Atom Scope and Substance Scope applicability.",
            "No slash-to-dot conversion is inferred from the display notation.",
        ]
    if old_value == "Atom/Governed Subject":
        return [
            "The required single governed Subject is retained as a distinct constraint.",
            "It is not conflated with Scope Unit Scope or Claim restrictions.",
        ]
    if old_value == "Atom/Claim":
        return [
            "Claim constraints remain distinct from Scope and from the Atom's governing Subject.",
            "No Substance-path or body-key rename is inferred.",
        ]
    if old_value == "Atom/Scope":
        return [
            "Atom Scope retains its Scope Unit, governed Subject, and explicit Claim contributions.",
            "Substance Scope applicability is not substituted for ownership or scope.",
        ]
    if old_value == "Artifact":
        return [
            "The dependent-to-prerequisite Artifact direction is retained.",
            "The inverse-derived required_by view is not made a second primitive relation.",
        ]
    if "Disposition" in old_value:
        return [
            "The named Lineage Impact disposition remains distinct from other dispositions.",
            "Its Revision and traversal constraints are retained without a new root identity.",
        ]
    if "Relation" in old_value:
        return [
            "The named direct-relation meaning remains distinct from other relation kinds.",
            "Owner, direction, target cardinality, and inverse-derived status are retained where stated.",
        ]
    return [
        "The exact original Subject text is retained.",
        "No grammar, ownership, allowed-value, carrier, or native-admission change is made.",
    ]


def unresolved_reason(atom_id: str, old_value: str) -> str:
    if old_value == "atom-boundary":
        return (
            f"{atom_id}'s current Main Content can use an Atom as a relation endpoint, "
            "but it does not identify the legacy topic label 'atom-boundary' as the "
            "Artifact/Atom Entity identity. The candidate's compact Artifact/Atom example "
            "cannot prove that alias or preserve the boundary/topic qualification."
        )
    if old_value == "relation-model":
        return (
            f"{atom_id}'s current Main Content can define a relation rule, but it does not "
            "establish that the broad legacy topic 'relation-model' is the candidate Relation "
            "identity. The root list and generic typed-relation model do not prove an alias."
        )
    if old_value in RELATION_VALUES:
        return (
            f"{atom_id}'s current Main Content names {old_value!r} as a distinct direct "
            "relation meaning, but the candidate does not establish a Relation property that "
            "owns this relation-kind domain or admit this value there. 'Relation: …' would "
            "apply an allowed value to a root and invent that missing binding."
        )
    if old_value == "Operator":
        return (
            "CA-R-1014 uses Operator as an Author-registered fallback role. The candidate "
            "lists Operator as an Actor Type example, but establishes no Actor property or "
            "admitted allowed-value domain for a candidate Subject; 'Actor: Operator' would "
            "therefore apply a value directly to a root."
        )
    if old_value == "Scope Unit/Scope":
        return (
            "CA-R-1014's current Claim requires the current Scope Unit Scope, but the "
            "candidate confirms Scope Unit only as a root ownership boundary and does not "
            "establish a Scope dependent-field identity or extent. Scope Unit.Scope would "
            "therefore be an unsupported dot binding."
        )
    if old_value == "Atom/Scope":
        return (
            "CA-R-1014 defines Atom Scope as a composite of Scope Unit Scope or Operator "
            "fallback, one governed Subject, and explicit Claim constraints. The candidate "
            "separates ownership Scope Unit from Substance Scope applicability but does not "
            "supply one field that preserves this composite meaning."
        )
    if old_value == "Atom/Claim":
        return (
            "CA-R-1014 treats explicit Claim constraints as one contribution to the composite "
            "Atom Scope. The candidate names Substance as an umbrella and Claim as a role label, "
            "but does not establish Claim as an admitted Atom.Substance value or prove that this "
            "legacy field is that property; the proposed colon binding would invent both."
        )
    if old_value.startswith("Atom/Content Role:"):
        return (
            "CA-R-1018 defines a qualified Content Role domain of Evaluation, Requirement, "
            "Method, Delivery, and Operations for evaluation targets. The candidate confirms "
            "M/E views and Substance direction but does not establish a Content Role field "
            "or this complete allowed-value domain; a Substance-role replacement would collapse it."
        )
    if old_value == "Atom/Local Tier":
        return (
            "CA-R-1018 distinguishes Standard Evaluation target obligations from Core/General "
            "representation-independent policy. The candidate does not establish a Local Tier "
            "dependent-field identity, so Atom.Local Tier would be an unsupported dot binding."
        )
    if old_value == "Dependency Relation Pair":
        return (
            "CA-R-1026 defines depends_on together with required_by as its inverse-derived view. "
            "The candidate confirms constrained Relation Types but supplies no pair identity or "
            "serialization that retains both the declared direction and inverse-derived status."
        )
    if old_value == "Implementation Relation Pair":
        return (
            "CA-R-1027 defines implementation_of together with the inverse-derived implemented_by "
            "in the realization ordering domain. The candidate supplies no relation-pair target; "
            "mapping only the upstream kind would drop the inverse qualification."
        )
    if old_value == "lifecycle-traceability":
        return (
            "CA-R-1032 requires a Lineage Impact fixed point before release or downstream gates. "
            "The candidate separates Revision history, Journal records, and Execution but does "
            "not establish a Lineage Impact traceability field or relation identity."
        )
    if "Lineage Impact Disposition" in old_value:
        return (
            f"{atom_id}'s current Claim defines {old_value!r} with distinct Revision and "
            "traversal consequences. The candidate confirms Revision as a history root but "
            "does not establish a Lineage Impact disposition field or complete allowed-value "
            "domain, so a Claim or Operation path would be speculative."
        )
    return (
        f"{atom_id}'s current Main Content supplies the meaning relevant to {old_value!r}, "
        "but the candidate does not establish a canonical field, complete allowed-value domain, "
        "or qualified relation-pair target that preserves every stated distinction."
    )


def review_occurrence(occurrence: dict[str, Any], evidence: dict[str, Any]) -> dict[str, Any]:
    old_value = occurrence["old_value"]
    result = dict(occurrence)
    if old_value == "Atom/Governed Subject":
        result.update(
            {
                "decision": "proposed",
                "proposed_value": "Atom.Governed Subject",
                "confidence": 0.90,
                "reason": (
                    "CA-R-1014's current Claim requires exactly one Atom Governed "
                    "Subject. The candidate's dependent-entity identity is an owner "
                    "selector plus dependent field, and its Scope rule explicitly retains "
                    "the whole governed Subject, supporting this qualified Atom field."
                ),
                "candidate_basis": [
                    {
                        "pointer": "/entity_identity_model/dependent_entity/identity",
                        "reason": "A dependent Entity identity is owner selector plus dependent field.",
                    },
                    {
                        "pointer": "/entity_identity_model/dependent_entity/meaning",
                        "reason": "The candidate describes selecting an Atom then its dependent field.",
                    },
                    {
                        "pointer": "/content_direction/scope_omission",
                        "reason": "The confirmed Scope rule retains the whole governed Subject.",
                    },
                ],
                "preserved_distinctions": [
                    "The required cardinality of one governed Subject is retained.",
                    "Governed Subject remains distinct from Scope Unit Scope and Claim restrictions.",
                ],
                "question": None,
            }
        )
    elif old_value == "Artifact":
        result.update(
            {
                "decision": "unchanged",
                "proposed_value": "Artifact",
                "confidence": 1.0,
                "reason": (
                    "CA-R-1026's current Claim explicitly relates a dependent Artifact to "
                    "a prerequisite Artifact, and Artifact is the candidate's exact root name."
                ),
                "candidate_basis": [],
                "preserved_distinctions": [
                    "The dependent-to-prerequisite direction is retained.",
                    "required_by remains the inverse-derived view, not a second primitive relation.",
                ],
                "question": None,
            }
        )
    elif old_value == "Atom/Revision/Author":
        result.update(
            {
                "decision": "unresolved",
                "proposed_value": None,
                "confidence": 0.45,
                "reason": (
                    "CA-R-1014's current Claim names an Author's registered Operator "
                    "fallback, but does not establish a Revision-qualified Author identity. "
                    "The frozen candidate explicitly excludes Atom/Revision as a canonical "
                    "path, so no replacement can be supported without conflating author, "
                    "Actor, and history semantics."
                ),
                "candidate_basis": [],
                "preserved_distinctions": [
                    "The legacy Author reference is retained for research rather than discarded.",
                    "Author/Operator fallback semantics remain distinct from Revision history.",
                    "No Atom/Revision slash-to-dot conversion is inferred.",
                ],
                "question": None,
            }
        )
    else:
        result.update(
            {
                "decision": "unresolved",
                "proposed_value": None,
                "confidence": 0.50,
                "reason": unresolved_reason(occurrence["source_atom_id"], old_value),
                "candidate_basis": [],
                "preserved_distinctions": preserved_for(
                    occurrence["source_atom_id"], old_value
                ),
                "question": None,
            }
        )
    result["evidence"] = [
        {
            **evidence,
            "reason": (
                "Full current Main Content (Summary, Scope, Claim, and Details heading) "
                f"was read for {occurrence['source_atom_id']}; it is the current meaning "
                "evidence for this occurrence."
            ),
        }
    ]
    result["executable"] = False
    return result


def build() -> dict[str, Any]:
    for relative_path, expected in EXPECTED.items():
        actual = digest(ROOT / relative_path)
        if actual != expected:
            raise ValueError(f"stale required pin: {relative_path}: {actual}")

    batch = load_json(ROOT / BATCH_REL)
    source_evidence = {
        source["atom_id"]: main_content_span(
            source["relative_path"], source["full_file_sha256"]
        )
        for source in batch["selected_sources"]
    }
    source_reviews = []
    for source in batch["selected_sources"]:
        review = dict(source)
        span = source_evidence[source["atom_id"]]
        review.update(
            {
                "main_content_read": {"read": True, **span},
                "finding_dispositions": [],
                "questions": [],
            }
        )
        source_reviews.append(review)

    occurrences = [
        review_occurrence(occurrence, source_evidence[occurrence["source_atom_id"]])
        for occurrence in batch["occurrences"]
    ]
    output = {
        "schema_version": 1,
        "non_authoritative": True,
        "source_migration": "not_performed",
        "native_admission": "not_performed",
        "task_id": "CA-P-1992",
        "batch_id": batch["batch_id"],
        "input_batch_path": BATCH_REL.as_posix(),
        "input_batch_sha256": EXPECTED[BATCH_REL],
        "input_inventory_sha256": batch["input_inventory_sha256"],
        "evidence_pins": [
            {
                "kind": "frozen_candidate",
                "path": CANDIDATE_REL.as_posix(),
                "sha256": EXPECTED[CANDIDATE_REL],
            },
            {
                "kind": "consolidated_review",
                "path": CONSOLIDATED_REVIEW_REL.as_posix(),
                "sha256": EXPECTED[CONSOLIDATED_REVIEW_REL],
                "captured_git_commit": CAPTURED_CORE_COMMIT,
            },
            {
                "kind": "current_subjects_contract",
                "path": SUBJECTS_CONTRACT_REL.as_posix(),
                "sha256": EXPECTED[SUBJECTS_CONTRACT_REL],
            },
            {
                "kind": "review_contract",
                "path": REVIEW_CONTRACT_REL.as_posix(),
                "sha256": EXPECTED[REVIEW_CONTRACT_REL],
            },
        ],
        "source_reviews": source_reviews,
        "occurrences": occurrences,
    }
    verify(output, batch)
    return output


def verify(output: dict[str, Any], batch: dict[str, Any]) -> None:
    """Check the producer's pins, full coverage, and exact current spans."""
    if output["input_inventory_sha256"] != EXPECTED[INVENTORY_REL]:
        raise ValueError("wrong inventory pin")
    if [row["occurrence_id"] for row in output["occurrences"]] != [
        row["occurrence_id"] for row in batch["occurrences"]
    ]:
        raise ValueError("occurrence coverage/order differs from input")
    if [row["atom_id"] for row in output["source_reviews"]] != [
        row["atom_id"] for row in batch["selected_sources"]
    ]:
        raise ValueError("source coverage/order differs from input")
    for row in output["occurrences"]:
        if row["confidence"] < 0.90 and (
            row["decision"] != "unresolved" or row["proposed_value"] is not None
        ):
            raise ValueError(f"low-confidence non-unresolved row: {row['occurrence_id']}")
        if row["executable"] is not False:
            raise ValueError(f"executable row: {row['occurrence_id']}")
        evidence = row["evidence"]
        if not evidence:
            raise ValueError(f"missing evidence: {row['occurrence_id']}")
        span = evidence[0]
        raw = (ROOT / span["path"]).read_bytes().splitlines(keepends=True)
        exact = b"".join(raw[span["start_line"] - 1 : span["end_line"]])
        if hashlib.sha256(exact).hexdigest() != span["span_sha256"]:
            raise ValueError(f"wrong span hash: {row['occurrence_id']}")


def run() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT / OUTPUT_REL)
    args = parser.parse_args()
    output = build()
    output_path = args.output.resolve()
    if output_path != (ROOT / OUTPUT_REL).resolve():
        raise ValueError("CA-P-1992 helper may write only its owned review output")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    run()
