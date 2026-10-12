"""Produce the conservative CA-P-1915 relation-batch handoff.

Legacy Subject paths and candidate lists are discovery aids only.  This producer
therefore validates every current candidate pin and records every old relation
as unresolved unless a reviewer supplies an exact Main Content proof for a
native relation.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


HERE = Path(__file__).parent
INPUT = HERE / "batch-3.input.json"
OUTPUT = HERE / "relations.batch-3.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main_content(text: str) -> list[tuple[int, str]]:
    """Return substantive Claim/Procedure/Condition lines, not summary headings."""
    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        body_start, body = 1, text.splitlines()
    else:
        body_start, body = len(parts[0].splitlines()) + 2, parts[1].splitlines()
    selected, active = [], False
    for offset, line in enumerate(body):
        if line.startswith("## "):
            active = line[3:].strip().casefold() in {"claim", "procedure", "condition"}
            continue
        if active:
            selected.append((body_start + offset, line))
    return selected


def terminal_terms(value: str) -> list[str]:
    """Terms useful for finding a contextual statement, not semantic proof."""
    term = value.rsplit("/", 1)[-1]
    return [part.strip() for part in term.split(":", 1) if len(part.strip()) > 2]


def source_candidates(item: dict) -> list[str]:
    """Use occurrence sources for negative review when prepared candidates lack any."""
    direct = item["content_source_candidates"]
    if direct:
        return direct
    return list(dict.fromkeys(
        occurrence["source_ref"]["atom_id"] for occurrence in item["occurrences"]
    ))


def contextual_evidence(item: dict, pins: dict) -> dict | None:
    """Find one pin-matched authored span naming both qualified endpoints."""
    parent_terms = terminal_terms(item["old_parent"])
    child_terms = terminal_terms(item["old_child"])
    best = None
    for atom_id in source_candidates(item):
        pin = pins[atom_id]
        carrier = Path(pin["carrier_path"])
        if not carrier.is_file() or sha256(carrier) != pin["carrier_sha256"]:
            raise ValueError(f"stale or missing pin for {atom_id}")
        for line_number, line in main_content(carrier.read_text()):
            lowered = line.casefold()
            parent_hits = sum(term.casefold() in lowered for term in parent_terms)
            child_hits = sum(term.casefold() in lowered for term in child_terms)
            # Require terms from each endpoint, in authored body rather than
            # frontmatter. This supports a display qualification only.
            if parent_hits and child_hits:
                score = parent_hits + child_hits
                candidate = (score, atom_id, pin, line_number, line)
                if best is None or candidate[0] > best[0]:
                    best = candidate
    if best is None:
        return None
    _, atom_id, pin, line_number, quote = best
    return {
        "atom_id": atom_id,
        "atom_revision": pin["atom_revision"],
        "carrier_path": pin["carrier_path"],
        "carrier_sha256": pin["carrier_sha256"],
        "start_line": line_number,
        "end_line": line_number,
        "quote": quote,
        "text_sha256": hashlib.sha256(quote.encode()).hexdigest(),
    }


def unresolved_question(item: dict) -> str:
    """Group genuine missing-evidence questions without inventing a relation."""
    text = f"{item['old_parent']} {item['old_child']}"
    if "Revision" in text:
        family = "revision lineage/history"
    elif "Plan" in text:
        family = "plan substructure and Carrier binding"
    elif "Artifact" in text:
        family = "artifact property"
    elif "Identity" in text:
        family = "identity collision repair"
    elif "Carrier" in text:
        family = "Carrier reconciliation"
    elif "Evaluation" in text:
        family = "evaluation grouping"
    else:
        family = "Atom direct-relation ownership"
    return (
        f"{family} family: which current Claim, Procedure, or Condition explicitly "
        "connects these qualified endpoints?"
    )


def main() -> None:
    source = json.loads(INPUT.read_text())
    pins = {pin["atom_id"]: pin for pin in source["current_source_pins"]}
    cases = []
    for item in source["cases"]:
        candidate_ids = source_candidates(item)
        checked = []
        for atom_id in candidate_ids:
            pin = pins.get(atom_id)
            if pin is None:
                raise ValueError(f"missing current pin for {atom_id}")
            carrier = Path(pin["carrier_path"])
            if not carrier.is_file() or sha256(carrier) != pin["carrier_sha256"]:
                raise ValueError(f"stale or missing pin for {atom_id}")
            checked.append(atom_id)
        evidence = contextual_evidence(item, pins)
        if evidence:
            disposition = "not-native"
            confidence = 90
            reason = (
                "The pin-matched authored span supports the legacy qualified "
                "display context, but does not declare native same-referent/"
                "narrower or bearer/dependent kind coverage."
            )
            question = None
            display_candidate = {
                "display_operator": ".",
                "qualified_parent": item["old_parent"],
                "qualified_child": item["old_child"],
                "semantic_intent": "contextual qualification only; not native admission",
            }
        else:
            disposition = "unresolved"
            confidence = 0
            reason = (
                "The legacy slash path and candidate list do not prove a native "
                "relation, and no pin-matched authored span names both endpoints "
                "for even a display qualification in this bounded pass."
            )
            question = unresolved_question(item)
            display_candidate = None
        cases.append(
            {
                "case_id": item["case_id"],
                "old_parent": item["old_parent"],
                "old_child": item["old_child"],
                "disposition": disposition,
                "confidence_percent": confidence,
                "proposal": None,
                "display_candidate": display_candidate,
                "evidence": [evidence] if evidence else [],
                "checks_performed": [
                    "verified each listed current candidate source pin against carrier bytes",
                    "read only authored Claim/Procedure/Condition Main Content; ignored Summary, frontmatter, Subjects/source incidence",
                    "did not infer native same-referent/narrower or bearer/dependent coverage from contextual wording",
                    "preserved the legacy qualified references without rebasing or semantic admission",
                ],
                "reason": reason,
                "question": question,
                "reviewed_candidate_atom_ids": checked,
            }
        )
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
    OUTPUT.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
