#!/usr/bin/env python3
"""Build the bounded CA-P-1917 contextual/operations relation review batch."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path.cwd()
DESIGN = ROOT / ".caprmedio_tmp/planning/core-entity-review/design"
INPUT = DESIGN / "batch-5.input.json"
OUTPUT = DESIGN / "relations.batch-5.json"

# These labels cannot be supported even as a contextual qualification by the
# selected source's authored Claim/Operation; Subject incidence is not evidence.
UNRESOLVED_ENDPOINTS = {
    ("Project Settings/Project identity", "Project Settings/Project identity/Carrier"),
    ("Markdown Atom Carrier/YAML Frontmatter", "Markdown Atom Carrier/YAML Frontmatter/Default"),
    ("Methodology Source", "Methodology Source/Carrier"),
    ("Applicable Methodology/Sources", "Applicable Methodology/Sources/CORE_META_MODEL"),
    ("RMED Atom Review Workflow/coverage", "RMED Atom Review Workflow/coverage/Action"),
    ("Tool", "Tool/Workflow Operations"),
    ("Applicable Methodology", "Applicable Methodology/Source Frontier Digest"),
}


def sha256(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def source_lines(ref: dict) -> list[str]:
    raw = (ROOT / ref["carrier_path"]).read_bytes()
    assert sha256(raw) == ref["carrier_sha256"], ref["atom_id"]
    return raw.decode("utf-8").splitlines()


def first_authored_span(ref: dict) -> dict:
    """Return the first paragraph under an authored semantic heading."""
    lines = source_lines(ref)
    headings = ("## Claim", "## Procedure", "## Condition", "## Operation")
    header = next((i for i, line in enumerate(lines) if line in headings), None)
    if header is None:
        raise ValueError(f"No Claim/Procedure/Condition/Operation: {ref['atom_id']}")
    start = next((i for i in range(header + 1, len(lines)) if lines[i].strip()), None)
    if start is None:
        raise ValueError(f"Empty authored section: {ref['atom_id']}")
    end = start + 1
    while end < len(lines) and lines[end].strip() and not lines[end].startswith("## "):
        end += 1
    quote = "\n".join(lines[start:end])
    return {
        "atom_id": ref["atom_id"],
        "atom_revision": ref["atom_revision"],
        "carrier_path": ref["carrier_path"],
        "carrier_sha256": ref["carrier_sha256"],
        "start_line": start + 1,
        "end_line": end,
        "quote": quote,
        "text_sha256": sha256(quote.encode("utf-8")),
    }


def verify_all_case_sources(case: dict) -> list[str]:
    """Check every source pin and report sources without a semantic section."""
    missing_semantic_section = []
    for occurrence in case["occurrences"]:
        ref = occurrence["source_ref"]
        lines = source_lines(ref)
        if not any(line in ("## Claim", "## Procedure", "## Condition", "## Operation") for line in lines):
            missing_semantic_section.append(ref["atom_id"])
    return sorted(set(missing_semantic_section))


def evidence_for(case: dict) -> dict | None:
    # Preserve the first verifier-compatible authored semantic span. All source
    # pins are rechecked separately; this selected span is concrete contextual
    # evidence, never a Subject path or frontmatter surrogate.
    errors = []
    for occurrence in case["occurrences"]:
        try:
            return first_authored_span(occurrence["source_ref"])
        except ValueError as error:
            errors.append(str(error))
    return None


def row(case: dict) -> dict:
    missing_semantic_section = verify_all_case_sources(case)
    parent, child = case["old_parent"], case["old_child"]
    selected_evidence = evidence_for(case)
    evidence = [selected_evidence] if selected_evidence is not None else []
    common = {
        "case_id": case["case_id"],
        "old_parent": parent,
        "old_child": child,
        "evidence": evidence,
        "checks_performed": [
            "verified every listed current source pin against carrier bytes",
            "read eligible authored Claim/Procedure/Condition/Operation Main Content; ignored Summary, frontmatter, and Subjects incidence",
            "did not infer native same-referent/narrower or immediate bearer/dependent coverage from contextual wording",
            "preserved legacy qualified references without rebasing or semantic admission",
        ] + (
            [
                "no authored Claim/Procedure/Condition/Operation exists in pin-matched source(s): "
                + ", ".join(missing_semantic_section)
            ]
            if missing_semantic_section
            else []
        ),
    }
    if (parent, child) in UNRESOLVED_ENDPOINTS:
        no_structured_span = selected_evidence is None
        result = {
            **common,
            "disposition": "unresolved",
            "confidence_percent": 0,
            "proposal": None,
            "display_candidate": None,
            "reason": (
                "The pinned current Operations sources contain no verifier-compatible Claim/Procedure/Condition/Details prose for this row. "
                "Their Operation text and Subject occurrence were not treated as sufficient proof."
                if no_structured_span
                else "The pin-matched authored span does not establish this exact legacy child as a contextual qualification of its parent, "
                "and declares no registered native relation; the Subject occurrence was not treated as proof."
            ),
            "question": (
                "Evidence-format family: should an Operations-only source provide a reviewed semantic Claim/Procedure/Condition/Details span before this legacy occurrence is classified?"
                if no_structured_span
                else "Contextual-label family: what exact non-native contextual meaning, if any, connects "
                f"{parent} to {child}; otherwise should this legacy occurrence be retired as not-native?"
            ),
        }
        if no_structured_span:
            result["reviewed_candidate_atom_ids"] = sorted(
                {occurrence["source_ref"]["atom_id"] for occurrence in case["occurrences"]}
            )
        return result
    return {
        **common,
        "disposition": "not-native",
        "confidence_percent": 90,
        "proposal": None,
        "display_candidate": {
            "display_operator": ".",
            "qualified_parent": parent,
            "qualified_child": child,
            "semantic_intent": "contextual qualification only; not native admission",
        },
        "reason": (
            "The pin-matched authored span supports the legacy qualified display context, but does not declare a registered "
            "same-referent/narrower or immediate bearer/dependent native relation."
        ),
        "question": None,
    }


def main() -> None:
    if OUTPUT.exists():
        raise FileExistsError(f"Refusing to replace existing output: {OUTPUT}")
    source = json.loads(INPUT.read_text(encoding="utf-8"))
    output = {
        "source_task": source["source_task"],
        "batch_number": source["batch_number"],
        "baseline_inventory_sha256": source["baseline_inventory_sha256"],
        "source_binding": source["source_binding"],
        "partition_sha256": source["partition_sha256"],
        "non_authoritative": True,
        "source_migration": "not_performed",
        "semantic_admission": "not_performed",
        "cases": [row(case) for case in source["cases"]],
    }
    OUTPUT.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
