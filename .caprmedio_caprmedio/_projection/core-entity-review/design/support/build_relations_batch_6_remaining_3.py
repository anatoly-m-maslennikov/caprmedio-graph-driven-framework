"""Build the bounded CA-P-1925 remaining context-relation handoff.

The input is a review partition, not authority.  This producer verifies every
listed current pin, quotes exact Main Content Claim spans, and records clear
configuration/representation/execution qualifications as non-native display
candidates.  It never turns those qualifications into admitted graph facts.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).parent
INPUT = HERE / "remaining-3.input.json"
OUTPUT = HERE / "relations.batch-6.remaining-3.json"


# Exact current evidence selected for each partition case.  Every identifier
# is deliberately present in that case's content_source_candidates list.
EVIDENCE_IDS = {
    0: ("CA-D-266",),
    1: ("CA-R-1228",),
    2: ("CA-R-1628",),
    3: ("CA-D-309",),
    4: ("CA-R-1220",),
    5: ("CA-D-258", "CA-R-1217"),
    6: ("CA-R-1652",),
    7: ("CA-R-1402", "CA-R-1750"),
    8: ("CA-R-1873",),
    9: ("CA-D-497", "CA-R-1750"),
    10: ("CA-D-309", "CA-E-500"),
    11: ("CA-R-1428",),
}


# Genuine gaps are intentionally below the confidence threshold and include a
# precise Operator question.  These are not generic zero-confidence rows:
# each one records what the reviewed Claim does establish and what remains
# absent from the closed relation vocabulary.
UNRESOLVED = {
    5: (
        78,
        "The selected Claims define File Carrier as a Carrier term and Extension as a distinct immutable Methodology Source, but they do not establish whether this slash path is a field, a source qualification, or a native relation.",
        "Should File Carrier/Extension remain a representation or source qualification, or is there an explicitly governed native relation between those distinct terms?",
    ),
    7: (
        80,
        "The selected Claims establish Framework Instance Settings as an authoritative configuration Artifact and assign ownership to that Artifact, but the reviewed candidates do not provide an exact Framework Instance Settings-to-Carrier binding Claim.",
        "Which current Main Content Claim, if any, proves the Framework Instance Settings Carrier binding, and is it only a display qualification or a native relation?",
    ),
    10: (
        82,
        "The selected Claims establish recoverable Carrier bindings for materialized representations and preserve Workflow graph meaning across storage, but they do not explicitly identify a Hub-to-Carrier binding for this path.",
        "Which current Main Content Claim explicitly identifies the Hub Carrier binding, and should it remain display-only rather than become a native relation?",
    ),
}


# Clear non-native qualifications.  The semantic intent is intentionally
# explicit: a display candidate is not a proposal and has no canonical kind.
DOT_INTENT = {
    1: "configuration_collection_qualification",
    2: "configuration_field_qualification",
    3: "general_bearer_qualification",
    4: "configuration_collection_qualification",
    6: "configuration_field_qualification",
    8: "execution_context_qualification",
    9: "configuration_field_qualification",
    11: "execution_context_qualification",
}


def sha256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def content_span(path: Path) -> tuple[int, int, str]:
    """Quote the first exact semantic Main Content section, never metadata."""
    lines = path.read_text(encoding="utf-8").splitlines()
    heading = next(
        (
            name
            for name in (
                "## Claim",
                "## Operation",
                "## Procedure",
                "## Condition",
                "## Definition",
                "## Evaluation",
            )
            if name in lines
        ),
        None,
    )
    if heading is None:
        raise ValueError(f"missing semantic Main Content heading: {path}")
    start = lines.index(heading)
    end = start + 1
    saw_text = False
    while end < len(lines):
        line = lines[end]
        if line.startswith("## ") and not line.startswith("### "):
            break
        if line.strip():
            saw_text = True
            end += 1
            continue
        if saw_text:
            break
        end += 1
    while end > start + 1 and not lines[end - 1].strip():
        end -= 1
    if end <= start:
        raise ValueError(f"empty semantic Main Content section: {path}")
    quote = "\n".join(lines[start:end])
    return start + 1, end, quote


def make_evidence(pin: dict[str, object]) -> dict[str, object]:
    path = Path(str(pin["carrier_path"]))
    raw = path.read_bytes()
    actual = sha256(raw)
    if actual != pin["carrier_sha256"]:
        raise ValueError(f"stale current source pin: {pin['atom_id']}")
    start, end, quote = content_span(path)
    return {
        "atom_id": pin["atom_id"],
        "atom_revision": pin["atom_revision"],
        "carrier_path": pin["carrier_path"],
        "carrier_sha256": actual,
        "start_line": start,
        "end_line": end,
        "quote": quote,
        "text_sha256": sha256(quote.encode("utf-8")),
    }


def common_checks() -> list[str]:
    return [
        "verified every listed current candidate source pin against current carrier bytes",
        "quoted an exact current semantic Main Content span outside frontmatter and Subjects",
        "compared the reviewed meaning with the closed relation vocabulary without manufacturing a new kind",
        "did not infer semantics from legacy path text, filename, metadata, or source incidence",
        "preserved qualified references and performed no native admission",
    ]


def main() -> None:
    source = json.loads(INPUT.read_text(encoding="utf-8"))
    if source.get("source_task") != "CA-P-1925":
        raise ValueError("unexpected source task")
    if source.get("batch_number") != 6 or source.get("sub_batch_number") != 3:
        raise ValueError("unexpected batch binding")
    if len(source.get("cases", [])) != 12 or len(EVIDENCE_IDS) != 12:
        raise ValueError("unexpected remaining case count")

    pins = {str(pin["atom_id"]): pin for pin in source["current_source_pins"]}
    rows = []
    for index, item in enumerate(source["cases"]):
        selected_ids = EVIDENCE_IDS[index]
        candidates = set(item["content_source_candidates"])
        if not set(selected_ids) <= candidates:
            raise ValueError(f"selected evidence is not a candidate for case {index}")

        # Recheck the full candidate frontier so a stale non-selected source
        # cannot silently weaken the review boundary.
        for atom_id in item["content_source_candidates"]:
            pin = pins.get(atom_id)
            if pin is None:
                raise ValueError(f"missing current pin: {atom_id}")
            path = Path(str(pin["carrier_path"]))
            if sha256(path.read_bytes()) != pin["carrier_sha256"]:
                raise ValueError(f"stale current candidate pin: {atom_id}")
        evidence = [make_evidence(pins[atom_id]) for atom_id in selected_ids]

        if index in UNRESOLVED:
            confidence, reason, question = UNRESOLVED[index]
            disposition = "unresolved"
            display_candidate = None
        else:
            confidence = {
                0: 97,
                1: 95,
                2: 99,
                3: 96,
                4: 95,
                6: 99,
                8: 97,
                9: 96,
                11: 96,
            }[index]
            disposition = "not-native"
            question = None
            display_candidate = (
                {
                    "display_operator": ".",
                    "qualified_parent": item["old_parent"],
                    "qualified_child": item["old_child"],
                    "semantic_intent": DOT_INTENT[index],
                    "native_admission": "not_performed",
                }
                if index in DOT_INTENT
                else None
            )
            if index == 0:
                reason = (
                    "The current Claim explicitly prohibits persisting derived CONTAINS and IS_CONTAINED_BY declarations; "
                    "the legacy containment path is therefore a derived representation, not a native relation."
                )
                display_candidate = None
            elif index == 1:
                reason = (
                    "The current Claim defines Installed Extensions as a contribution within the Applicable Methodology source set, "
                    "including an explicitly empty contribution. This is a configuration collection qualification, not a native edge."
                )
            elif index == 2:
                reason = (
                    "The current Claim requires exactly one interaction reporting setting with a closed value set. "
                    "This is a Framework Instance Settings field qualification, not an entity relation."
                )
            elif index == 3:
                reason = (
                    "The current Claim requires each admitted materialized representation Carrier to bind recoverably to its canonical source Revision. "
                    "That is a representation/carrier qualification; it does not prove an immediate native IS_BORNE_BY identity edge."
                )
            elif index == 4:
                reason = (
                    "The current Claim requires each Installed Extensions Catalog Entry to identify one immutable Extension Candidate by explicit fields. "
                    "The slash path is a catalog/configuration qualification, not a native relation."
                )
            elif index == 6:
                reason = (
                    "The current Claim defines Necessary Information Threshold as an Operator-configurable integer-percentage setting. "
                    "This is a configuration field qualification, not a native relation."
                )
            elif index == 8:
                reason = (
                    "The current Claim explicitly describes the governed execution derivation RMED → using O → I and preserves native I as actual-state authority. "
                    "This is an execution-context qualification; no closed native derivation kind is asserted here."
                )
            elif index == 9:
                reason = (
                    "The current Claims assign Framework Instance Settings ownership to selected behavior/configuration choices and define TOML setting encodings. "
                    "The interaction path is a configuration qualification, not a native relation."
                )
            elif index == 11:
                reason = (
                    "The current Claim defines the effective Confidence Threshold source precedence across Operator input, Plan properties, Hub inheritance, and Framework Instance Settings. "
                    "This is an execution/configuration-source qualification, not a native relation."
                )
            else:
                raise AssertionError(f"missing disposition reason for case {index}")

        row = {
            "case_id": item["case_id"],
            "old_parent": item["old_parent"],
            "old_child": item["old_child"],
            "disposition": disposition,
            "confidence_percent": confidence,
            "proposal": None,
            "evidence": evidence,
            "checks_performed": common_checks(),
            "reason": reason,
            "question": question,
        }
        if display_candidate is not None:
            row["display_candidate"] = display_candidate
        rows.append(row)

    result = {
        "source_task": source["source_task"],
        "batch_number": source["batch_number"],
        "baseline_inventory_sha256": source["baseline_inventory_sha256"],
        "source_binding": source["source_binding"],
        "partition_sha256": source["partition_sha256"],
        "non_authoritative": True,
        "source_migration": "not_performed",
        "semantic_admission": "not_performed",
        "cases": rows,
    }
    OUTPUT.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
