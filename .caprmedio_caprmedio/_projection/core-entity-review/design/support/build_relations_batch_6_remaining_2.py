"""Build the CA-P-1924 source-pinned, display-only relation review."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).parent
INPUT = HERE / "remaining-2.input.json"
OUTPUT = HERE / "relations.batch-6.remaining-2.json"
SECTIONS = {"claim", "operation", "procedure", "condition"}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def candidates(case: dict) -> list[str]:
    direct = case["content_source_candidates"]
    if direct:
        return direct
    return list(dict.fromkeys(row["source_ref"]["atom_id"] for row in case["occurrences"]))


def endpoint_terms(value: str) -> list[str]:
    terminal = value.rsplit("/", 1)[-1]
    return [part.strip() for part in terminal.split(":", 1) if len(part.strip()) > 2]


def substantive_lines(text: str) -> list[tuple[int, str]]:
    parts = text.split("\n---\n", 1)
    if len(parts) == 2:
        start, body = len(parts[0].splitlines()) + 2, parts[1].splitlines()
    else:
        start, body = 1, text.splitlines()
    active, result = False, []
    for offset, line in enumerate(body):
        if line.startswith("## "):
            active = line[3:].strip().casefold() in SECTIONS
            continue
        if active:
            result.append((start + offset, line))
    return result


def exact_context(case: dict, pins: dict) -> tuple[dict | None, list[str]]:
    parent = endpoint_terms(case["old_parent"])
    child = endpoint_terms(case["old_child"])
    best, reviewed = None, []
    for atom_id in candidates(case):
        pin = pins.get(atom_id)
        if pin is None:
            raise ValueError(f"missing current source pin {atom_id}")
        path = Path(pin["carrier_path"])
        if not path.is_file() or digest(path) != pin["carrier_sha256"]:
            raise ValueError(f"stale current source pin {atom_id}")
        reviewed.append(atom_id)
        for line_number, quote in substantive_lines(path.read_text()):
            lowered = quote.casefold()
            parent_hits = sum(term.casefold() in lowered for term in parent)
            child_hits = sum(term.casefold() in lowered for term in child)
            if parent_hits and child_hits:
                item = (parent_hits + child_hits, pin, line_number, quote)
                if best is None or item[0] > best[0]:
                    best = item
    if best is None:
        return None, reviewed
    _, pin, line_number, quote = best
    return {
        "atom_id": pin["atom_id"],
        "atom_revision": pin["atom_revision"],
        "carrier_path": pin["carrier_path"],
        "carrier_sha256": pin["carrier_sha256"],
        "start_line": line_number,
        "end_line": line_number,
        "quote": quote,
        "text_sha256": hashlib.sha256(quote.encode()).hexdigest(),
    }, reviewed


def question(case: dict) -> str:
    return (
        "Which current Claim, Operation, Procedure, or Condition supplies an "
        f"explicit relation-kind and direction for {case['old_parent']} to "
        f"{case['old_child']}, rather than only contextual qualification?"
    )


def main() -> None:
    source = json.loads(INPUT.read_text())
    pins = {pin["atom_id"]: pin for pin in source["current_source_pins"]}
    cases = []
    for raw in source["cases"]:
        evidence, reviewed = exact_context(raw, pins)
        if evidence:
            disposition, confidence, display, why, asked = (
                "not-native",
                90,
                {
                    "display_operator": ".",
                    "qualified_parent": raw["old_parent"],
                    "qualified_child": raw["old_child"],
                    "semantic_intent": "authored contextual qualification only; native admission not asserted",
                },
                "The exact current authored span supports the qualified display context, but it does not state an owning native relation kind, direction, and immediate identity.",
                None,
            )
        else:
            disposition, confidence, display, why, asked = (
                "unresolved",
                0,
                None,
                "All current pinned defining/occurrence sources were checked in substantive authored sections, but none supplied an exact span naming both endpoints.",
                question(raw),
            )
        cases.append({
            "case_id": raw["case_id"],
            "old_parent": raw["old_parent"],
            "old_child": raw["old_child"],
            "disposition": disposition,
            "confidence_percent": confidence,
            "proposal": None,
            "display_candidate": display,
            "evidence": [evidence] if evidence else [],
            "checks_performed": [
                "verified every defining candidate or fallback occurrence source against its current selected carrier SHA-256",
                "reviewed only authored Claim, Operation, Procedure, and Condition sections; ignored Summary, frontmatter, Subjects, and source incidence",
                "required explicit native kind, direction, and immediate identity before any native assertion",
            ],
            "reason": why,
            "question": asked,
            "reviewed_candidate_atom_ids": reviewed,
        })
    result = {
        "source_task": "CA-P-1924",
        "batch_number": 6,
        "baseline_inventory_sha256": source["baseline_inventory_sha256"],
        "source_binding": source["source_binding"],
        "partition_sha256": source["partition_sha256"],
        "non_authoritative": True,
        "source_migration": "not_performed",
        "semantic_admission": "not_performed",
        "cases": cases,
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
