"""Build the bounded, non-authoritative CA-P-1914 relation review.

This producer deliberately keeps the legacy slash references unchanged.  It
uses only the current pins supplied by the partition and quotes a short exact
``## Claim`` span from each selected carrier.  A display candidate is not a
native graph fact: it records only the reviewed operator notation where the
claim describes a property or an entity/carrier qualification.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).parent
INPUT = HERE / "batch-2.input.json"
OUTPUT = HERE / "relations.batch-2.json"


# The chosen pins are current content candidates for their corresponding
# cases.  They are intentionally explicit so a changed source cannot silently
# change the reviewed meaning or evidence selection.
EVIDENCE_IDS = {
    0: ("CA-E-506",),
    1: ("CA-R-1531",),
    2: ("CA-R-1287",),
    3: ("CA-R-1595",),
    4: ("CA-R-991",),
    5: ("CA-D-290",),
    6: ("CA-D-463",),
    7: ("CA-R-1708",),
    8: ("CA-D-378",),
    9: ("CA-R-1608",),
    10: ("CA-R-1198",),
    11: ("CA-R-366",),
    12: ("CA-D-285",),
    13: ("CA-D-296",),
    14: ("CA-R-1444",),
    15: ("CA-R-1565",),
    16: ("CA-R-1284",),
    17: ("CA-E-502",),
    18: ("CA-R-1398",),
    19: ("CA-R-1730",),
    20: ("CA-D-386",),
    21: ("CA-R-1406",),
    22: ("CA-R-1534",),
    23: ("CA-R-1571",),
    24: ("CA-D-470",),
    25: ("CA-D-274",),
    26: ("CA-R-1588",),
    27: ("CA-R-1416",),
    28: ("CA-D-268",),
    29: ("CA-D-506", "CA-R-1268"),
    30: ("CA-R-1412",),
    31: ("CA-D-352",),
    32: ("CA-R-1371",),
    33: ("CA-R-1757",),
    34: ("CA-E-502",),
    35: ("CA-R-1287",),
    36: ("CA-E-502",),
    37: ("CA-R-1587",),
    38: ("CA-D-285",),
    39: ("CA-R-1394",),
    40: ("CA-R-1417",),
    41: ("CA-D-568",),
    42: ("CA-R-1763",),
    43: ("CA-R-1500",),
    44: ("CA-D-475",),
    45: ("CA-R-933", "CA-R-954"),
    46: ("CA-D-506", "CA-R-655"),
}


# These cases have a concrete current claim but no closed registry kind that
# fits the path.  They remain explicit questions rather than invented facts.
UNRESOLVED = {
    3: (
        72,
        "The current Claim explicitly addresses a Claim Target Scope Unit, but the closed registry has no approved relation kind for that target context; it cannot be equated with IS_BORNE_BY or NARROWER_THAN.",
        "Which reviewed native relation kind, if any, should represent an Atom Claim's target Scope Unit without changing Scope Unit ownership?",
    ),
    17: (
        70,
        "The current Plan Carrier Evaluation describes carrier identity and placement, but it does not establish an Assignee-to-Carrier identity relation for this qualified path.",
        "Is Plan/Type: Plan/Assignee/Carrier intended as an explicit native relation, or is it only a carrier/assignment representation?",
    ),
    20: (
        55,
        "The selected current candidate Claim concerns Atom Carrier priority and does not establish a Current Scope Unit binding for an Atom Carrier; no sufficient native relation evidence is available in this partition.",
        "Which current Main Content Claim explicitly proves the Atom Carrier to Current Scope Unit binding, and which closed relation kind should own it?",
    ),
    26: (
        75,
        "The current Plan Claim Target rule establishes a target Scope Unit context, but no closed registry relation kind represents that context edge and the path is not a bearer identity.",
        "Should the Plan Claim Target Scope Unit remain a property/context reference, or is a separately governed native relation required?",
    ),
    33: (
        76,
        "The current Scope Unit definition establishes an ownership boundary, but does not prove a distinct nested Scope property relation that belongs to the closed relation registry.",
        "Does Scope Unit/Scope denote a separately modelled entity relation, or only the Scope Unit's own ownership-boundary meaning?",
    ),
    45: (
        78,
        "The current Demand rules explicitly constrain a Producer or Implementation result, but that flow is not one of the closed relation kinds and must not mint a new relation here.",
        "Which approved native relation kind, if any, should represent Demand to Producer Result while preserving the existing Demand constraints?",
    ),
}


# A dot candidate records the approved general-bearer/property display only;
# it never becomes a proposal or a native fact in this handoff.
DOT_DISPLAY = {
    1,
    2,
    6,
    7,
    9,
    14,
    15,
    16,
    18,
    23,
    27,
    29,
    30,
    35,
    39,
    43,
    46,
}


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def claim_span(path: Path) -> tuple[int, int, str]:
    """Return a compact exact Claim heading/span outside frontmatter."""
    lines = path.read_text(encoding="utf-8").splitlines()
    try:
        start = lines.index("## Claim")
    except ValueError as error:
        raise ValueError(f"missing exact Claim heading: {path}") from error

    # Keep the heading and the first complete paragraph.  Some Evaluation
    # sources put a nested "### Claim checked" heading immediately below the
    # top-level Claim heading; include it and its first paragraph as well.
    end = start + 1
    saw_text = False
    saw_blank_after_text = False
    while end < len(lines):
        line = lines[end]
        if line.startswith("## ") and not line.startswith("### "):
            break
        if line.strip():
            saw_text = True
            saw_blank_after_text = False
            end += 1
            continue
        if saw_text:
            saw_blank_after_text = True
            end += 1
            # Stop at the first blank after the initial paragraph.  The blank
            # itself is omitted from the quoted span.
            break
        end += 1
    while end > start + 1 and not lines[end - 1].strip():
        end -= 1
    if end <= start:
        raise ValueError(f"empty Claim span: {path}")
    quote = "\n".join(lines[start:end])
    return start + 1, end, quote


def evidence(pin: dict[str, object]) -> dict[str, object]:
    path = Path(str(pin["carrier_path"]))
    raw = path.read_bytes()
    actual = digest(raw)
    if actual != pin["carrier_sha256"]:
        raise ValueError(f"stale selected source pin: {pin['atom_id']}")
    start, end, quote = claim_span(path)
    return {
        "atom_id": pin["atom_id"],
        "atom_revision": pin["atom_revision"],
        "carrier_path": pin["carrier_path"],
        "carrier_sha256": actual,
        "start_line": start,
        "end_line": end,
        "quote": quote,
        "text_sha256": digest(quote.encode("utf-8")),
    }


def common_checks() -> list[str]:
    return [
        "verified every listed current candidate source pin against current carrier bytes",
        "quoted exact current ## Claim span outside frontmatter and Subjects",
        "compared the Claim with the closed registry kinds IS_BORNE_BY, IS_ALLOWED_VALUE_OF, and NARROWER_THAN",
        "did not infer semantics from legacy path text, filename, metadata, or source incidence",
        "preserved qualified references and performed no native admission",
    ]


def main() -> None:
    source = json.loads(INPUT.read_text(encoding="utf-8"))
    if source["source_task"] != "CA-P-1914" or source["batch_number"] != 2:
        raise ValueError("unexpected CA-P-1914 input binding")
    if len(source["cases"]) != 47 or len(EVIDENCE_IDS) != 47:
        raise ValueError("unexpected case count")

    pins = {str(pin["atom_id"]): pin for pin in source["current_source_pins"]}
    cases = []
    for index, item in enumerate(source["cases"]):
        selected = EVIDENCE_IDS[index]
        candidate_ids = set(item["content_source_candidates"])
        if not set(selected) <= candidate_ids:
            raise ValueError(f"selected evidence is not a candidate for case {index}")
        for atom_id in item["content_source_candidates"]:
            pin = pins.get(atom_id)
            if pin is None:
                raise ValueError(f"missing current pin for {atom_id}")
            if digest(Path(str(pin["carrier_path"])).read_bytes()) != pin["carrier_sha256"]:
                raise ValueError(f"stale candidate pin: {atom_id}")
        refs = [evidence(pins[atom_id]) for atom_id in selected]

        if index in UNRESOLVED:
            confidence, reason, question = UNRESOLVED[index]
            disposition = "unresolved"
            display_candidate = None
        else:
            confidence = 94
            disposition = "not-native"
            display_candidate = (
                {
                    "display_operator": ".",
                    "qualified_parent": item["old_parent"],
                    "qualified_child": item["old_child"],
                    "semantic_intent": "general_bearer_qualification",
                    "native_admission": "not_performed",
                }
                if index in DOT_DISPLAY
                else None
            )
            question = None
            if index in {6, 29, 46}:
                reason = (
                    "The current Claim supports an Entity/Carrier or authoritative carrier binding, "
                    "but it does not prove this exact legacy qualified path as an immediate IS_BORNE_BY identity edge; "
                    "the dot display candidate remains non-authoritative."
                )
            elif index in {1, 2, 7, 9, 14, 15, 16, 18, 23, 27, 30, 35, 39, 43}:
                reason = (
                    "The current Claim explicitly describes the child as a Property, value, coordinate, or derived "
                    "classification of the parent. That supports only the approved non-authoritative dot display; "
                    "the closed registry has no property-ownership relation fact for this path."
                )
            elif index in {0, 4, 5, 8, 11, 12, 13, 19, 21, 22, 24, 25, 28, 31, 32, 34, 36, 37, 38, 40, 41, 42, 44}:
                reason = (
                    "The current Claim constrains serialization, placement, identity, provenance, navigation, or "
                    "carrier content. It does not assert a closed native relation kind for this legacy qualified path."
                )
            elif index == 10:
                reason = (
                    "The current Claim defines Atom Subjects as a property that serializes owned direct relations; "
                    "the nested serialization path is not itself a native relation fact."
                )
            elif index == 26:
                raise AssertionError("unresolved case missing from map")
            elif index == 33:
                raise AssertionError("unresolved case missing from map")
            elif index == 45:
                raise AssertionError("unresolved case missing from map")
            else:
                raise AssertionError(f"missing semantic disposition for case {index}")

        row = {
            "case_id": item["case_id"],
            "old_parent": item["old_parent"],
            "old_child": item["old_child"],
            "disposition": disposition,
            "confidence_percent": confidence,
            "proposal": None,
            "evidence": refs,
            "checks_performed": common_checks(),
            "reason": reason,
            "question": question,
        }
        if display_candidate is not None:
            row["display_candidate"] = display_candidate
        cases.append(row)

    result = {
        "source_task": source["source_task"],
        "batch_number": source["batch_number"],
        "baseline_inventory_sha256": source["baseline_inventory_sha256"],
        "source_binding": source["source_binding"],
        "partition_sha256": source["partition_sha256"],
        "non_authoritative": True,
        "source_migration": "not_performed",
        "semantic_admission": "not_performed",
        "cases": cases,
    }
    OUTPUT.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
