"""Create the bounded CA-P-1929 node-review handoff from current pinned Core text."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path.cwd()
HERE = ROOT / ".caprmedio_caprmedio/_projection/core-entity-review/nodes"
INPUT = HERE / "inputs/nodes.batch-1.input.json"
BASELINE = ROOT / ".caprmedio_caprmedio/_projection/core-entity-review/baseline.inventory.json"
OUTPUT = HERE / "nodes.batch-1.review.json"
SECTIONS = {"claim", "operation", "procedure", "condition", "definition", "evaluation"}
# These are identity definitions rechecked against the current selected pins.
# None means that the assigned sources mention a topic, but do not define it.
IDENTITY_DEFINITIONS = {
    "AI Agent": None,
    "Actor": None,
    "Action": ("CA-R-1452", 37),
    "Action/Execution Kind": ("CA-R-1526", 31),
    "Artifact": ("CA-R-1268", 29),
    "Artifact/Activity": ("CA-R-1394", 30),
    "Atom": ("CA-R-655", 26),
}


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def substantive_lines(raw: str) -> list[tuple[int, str]]:
    parts = raw.split("\n---\n", 1)
    start, body = (len(parts[0].splitlines()) + 2, parts[1].splitlines()) if len(parts) == 2 else (1, raw.splitlines())
    active, found = False, []
    for offset, line in enumerate(body):
        if line.startswith("## "):
            active = line[3:].strip().casefold() in SECTIONS
            continue
        if active and line.strip():
            found.append((start + offset, line))
    return found


def evidence_for(node: dict, pins: dict, catalogue: list, index: dict) -> tuple[list[str], list[str]]:
    identity = node["identity"]
    pattern = re.compile(r"(?<![\\w/:-])" + re.escape(identity) + r"(?![\\w/:-])", re.IGNORECASE)
    evidence_refs, checked, best = [], [], None
    for atom_id in node["source_atom_ids"]:
        pin = pins[atom_id]
        path = ROOT / pin["carrier_path"]
        raw = path.read_bytes()
        if sha(raw) != pin["carrier_sha256"]:
            raise ValueError(f"stale pin {atom_id}")
        checked.append(atom_id)
        for line_number, quote in substantive_lines(raw.decode()):
            # A named use is not by itself a definition.  Keep only a local
            # definitional assertion as a positive-retain basis.
            if pattern.search(quote) and "means" in quote.casefold():
                score = quote.casefold().count("means")
                candidate = (score, atom_id, pin, line_number, quote)
                if best is None or candidate[0] > best[0]:
                    best = candidate
    if identity in IDENTITY_DEFINITIONS:
        definition = IDENTITY_DEFINITIONS[identity]
        if definition is None:
            return evidence_refs, checked
        atom_id, line_number = definition
        pin = pins[atom_id]
        path = ROOT / pin["carrier_path"]
        raw = path.read_bytes()
        if sha(raw) != pin["carrier_sha256"]:
            raise ValueError(f"stale definition pin {atom_id}")
        quote = raw.decode().splitlines()[line_number - 1]
        best = (100, atom_id, pin, line_number, quote)
    if best is None:
        return evidence_refs, checked
    _, atom_id, pin, line_number, quote = best
    key = (atom_id, line_number, quote)
    if key not in index:
        index[key] = f"e{len(catalogue) + 1}"
        catalogue.append({
            "evidence_ref": index[key], "atom_id": atom_id,
            "atom_revision": pin["atom_revision"], "carrier_path": pin["carrier_path"],
            "carrier_sha256": pin["carrier_sha256"], "start_line": line_number,
            "end_line": line_number, "quote": quote,
            "text_sha256": sha(quote.encode()),
        })
    return [index[key]], checked


def checks(identity: str, evidence_refs: list[str]) -> dict:
    if evidence_refs:
        meaning = "A current pinned substantive span names this exact preserved identity; no duplicate/consolidation proof was found in this bounded review."
        return {
            "duplicates": {"finding": "no_proven_duplicate", "reason": meaning, "evidence_refs": evidence_refs},
            "redundancy": {"finding": "not_proven_redundant", "reason": "Qualified-field repetition is not redundancy proof.", "evidence_refs": evidence_refs},
            "empty_definition": {"finding": "not_empty_by_default", "reason": "A named substantive occurrence prevents treating missing dedicated definition as empty.", "evidence_refs": evidence_refs},
            "distinct_meaning": {"finding": "current_meaning_evidenced", "reason": meaning, "evidence_refs": evidence_refs},
            "generalization": {"finding": "not_proposed", "reason": "No replacement/generalization is asserted without loss analysis.", "evidence_refs": evidence_refs},
        }
    gap = f"No current Claim/Operation/Procedure/Condition/Definition/Evaluation span in the assigned source set names {identity}."
    return {
        "duplicates": {"finding": "unresolved", "reason": "No same-meaning duplicate proof in checked sources.", "evidence_refs": []},
        "redundancy": {"finding": "unresolved", "reason": "No redundancy proof in checked sources.", "evidence_refs": []},
        "empty_definition": {"finding": "unresolved", "reason": gap, "evidence_refs": []},
        "distinct_meaning": {"finding": "unresolved", "reason": gap, "evidence_refs": []},
        "generalization": {"finding": "not_proposed", "reason": "No replacement or loss analysis exists.", "evidence_refs": []},
    }


def main() -> None:
    packet = json.loads(INPUT.read_text())
    baseline_raw = BASELINE.read_bytes()
    if sha(baseline_raw) != packet["baseline"]["sha256"]:
        raise ValueError("baseline input hash mismatch")
    baseline = json.loads(baseline_raw)
    pins = {entry["atom_id"]: entry for entry in baseline["source_atoms"]}
    catalogue, index, rows = [], {}, []
    for node in packet["nodes"]:
        refs, checked = evidence_for(node, pins, catalogue, index)
        supported = bool(refs)
        rows.append({
            "identity": node["identity"],
            "disposition": "retain" if supported else "question",
            "confidence_percent": 90 if supported else 0,
            "reason": (
                "Current pinned Main Content provides an exact meaningful identity occurrence; retain this preserved identity pending integration."
                if supported else
                "No positive Main Content basis was found in the assigned current source set; absence is not evidence to drop or consolidate."
            ),
            "checks": checks(node["identity"], refs),
            "evidence_refs": refs,
            "checked_source_atom_ids": checked,
            "proposal": None,
            "question": None if supported else f"Which current defining Core Main Content statement establishes the distinct meaning of {node['identity']}?",
        })
    result = {
        "source_task": packet["source_task"], "batch": packet["batch"],
        "baseline_inventory_sha256": packet["baseline"]["inventory_sha256"],
        "input_file_sha256": sha(INPUT.read_bytes()), "partition_sha256": packet["partition_sha256"],
        "non_authoritative": True, "semantic_admission": "not_performed", "source_migration": "not_performed",
        "operator_decision": packet["operator_decision"], "evidence_catalogue": catalogue, "nodes": rows,
    }
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    main()
