"""Create-only CA-P-1932 review from current pinned Main Content."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path.cwd()
HERE = ROOT / ".caprmedio_caprmedio/_projection/core-entity-review/nodes"
INPUT = HERE / "inputs/nodes.batch-4.input.json"
BASELINE = ROOT / ".caprmedio_caprmedio/_projection/core-entity-review/baseline.inventory.json"
SCOPE_DECISION = HERE / "scope.omission.decision.md"
OUTPUT = HERE / "nodes.batch-4.review.json"
SECTIONS = {"claim", "operation", "procedure", "condition", "definition", "evaluation"}


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def substantive_lines(raw: str) -> list[tuple[int, str]]:
    parts = raw.split("\n---\n", 1)
    start = len(parts[0].splitlines()) + 2 if len(parts) == 2 else 1
    body = parts[-1].splitlines()
    active = False
    found: list[tuple[int, str]] = []
    for offset, line in enumerate(body):
        if line.startswith("## "):
            active = line[3:].strip().casefold() in SECTIONS
            continue
        if active and line.strip():
            found.append((start + offset, line))
    return found


def normalized(text: str) -> str:
    return re.sub(r"[`*_]", "", text).casefold()


def exact_definition(identity: str, quote: str) -> bool:
    """Require the identity itself to be the asserted subject, never a mention."""
    subject = re.escape(normalized(identity))
    text = normalized(quote)
    return bool(
        re.search(rf"^(?:an?|the(?:\s+term)?|term)\s+{subject}\s+.*\bmeans\b", text)
        or re.search(rf"^{subject}\s+.*\bmeans\b", text)
        or re.search(rf"^(?:the\s+)?term\s+{subject}\s+narrowerthan\b", text)
    )


def evidence_for(node: dict, pins: dict[str, dict], catalogue: list[dict], index: dict) -> tuple[list[str], list[str]]:
    identity = node["identity"]
    checked: list[str] = []
    best = None
    for atom_id in node["source_atom_ids"]:
        pin = pins[atom_id]
        raw = (ROOT / pin["carrier_path"]).read_bytes()
        if sha(raw) != pin["carrier_sha256"]:
            raise ValueError(f"stale pin {atom_id}")
        checked.append(atom_id)
        for line_number, quote in substantive_lines(raw.decode()):
            if exact_definition(identity, quote):
                candidate = (atom_id, pin, line_number, quote)
                if best is None:
                    best = candidate
    if best is None:
        return [], checked
    atom_id, pin, line_number, quote = best
    key = (atom_id, line_number, quote)
    if key not in index:
        index[key] = f"e{len(catalogue) + 1}"
        catalogue.append({
            "evidence_ref": index[key],
            "atom_id": atom_id,
            "atom_revision": pin["atom_revision"],
            "carrier_path": pin["carrier_path"],
            "carrier_sha256": pin["carrier_sha256"],
            "start_line": line_number,
            "end_line": line_number,
            "quote": quote,
            "text_sha256": sha(quote.encode()),
        })
    return [index[key]], checked


def checks(identity: str, refs: list[str]) -> dict:
    common = {"evidence_refs": refs}
    if refs:
        return {
            "duplicates": {**common, "finding": "no_proven_duplicate", "reason": f"Current Main Content defines {identity}; no same-meaning replacement is evidenced."},
            "redundancy": {**common, "finding": "not_proven_redundant", "reason": f"No checked source makes {identity} redundant; qualified-label repetition is not duplicate proof."},
            "empty_definition": {**common, "finding": "definition_evidenced", "reason": f"The cited current Main Content directly defines {identity}."},
            "distinct_meaning": {**common, "finding": "current_meaning_evidenced", "reason": f"The cited current Main Content gives {identity} an explicit distinct meaning."},
            "generalization": {**common, "finding": "not_proposed", "reason": f"No broader replacement for {identity} is proposed without loss analysis."},
        }
    gap = f"No checked current Main Content line directly defines {identity}; this absence is not treated as emptiness, duplication, or a deletion permission."
    return {
        "duplicates": {**common, "finding": "unresolved", "reason": f"No checked source proves a same-meaning duplicate of {identity}."},
        "redundancy": {**common, "finding": "unresolved", "reason": f"No checked source proves {identity} redundant or supplies a replacement."},
        "empty_definition": {**common, "finding": "unresolved_absence_not_empty", "reason": gap},
        "distinct_meaning": {**common, "finding": "unresolved", "reason": gap},
        "generalization": {**common, "finding": "not_proposed", "reason": f"No generalization for {identity} is proposed without preserved/lost distinction analysis."},
    }


def retain_proposal(identity: str) -> dict:
    return {
        "kind": "retain_preserved_baseline_identity_only",
        "replacement_identity": None,
        "native_admission": "not_performed",
        "relations_impact": "no relation creation, removal, or rewrite proposed",
        "constraints_impact": "no constraint change proposed",
        "historical_references_impact": "preserved at the original baseline identity",
        "queries_impact": "identity-based queries preserve the original baseline identity",
        "preserved_distinctions": [identity],
        "lost_distinctions": [],
    }


def main() -> None:
    if OUTPUT.exists():
        raise FileExistsError(f"create-only output already exists: {OUTPUT}")
    packet = json.loads(INPUT.read_text())
    baseline_raw = BASELINE.read_bytes()
    if sha(baseline_raw) != packet["baseline"]["sha256"]:
        raise ValueError("baseline input hash mismatch")
    expected_scope = "d4ea636d540b0558c1a0fbb8263760947e1f0768840c43b3ed1d05c96b497453"
    if sha(SCOPE_DECISION.read_bytes()) != expected_scope:
        raise ValueError("scope omission decision hash mismatch")
    baseline = json.loads(baseline_raw)
    pins = {entry["atom_id"]: entry for entry in baseline["source_atoms"]}
    catalogue: list[dict] = []
    index: dict = {}
    rows: list[dict] = []
    for node in packet["nodes"]:
        refs, checked = evidence_for(node, pins, catalogue, index)
        supported = bool(refs)
        identity = node["identity"]
        rows.append({
            "identity": identity,
            "disposition": "retain" if supported else "question",
            "confidence_percent": 95 if supported else 0,
            "reason": (
                "Current pinned Main Content directly defines this preserved identity; retain it without admitting a new native Property, allowed-value assignment, root kind, or relation."
                if supported else
                "Current checked Main Content has no exact defining assertion for this preserved identity. It remains preserved and unresolved; no drop, consolidation, generalization, ownership, or native fact is inferred."
            ),
            "checks": checks(identity, refs),
            "evidence_refs": refs,
            "checked_source_atom_ids": checked,
            "proposal": retain_proposal(identity) if supported else None,
            "question": None if supported else (
                f"Which current Core Main Content assertion defines the distinct meaning of {identity} and, if applicable, its property, allowed-value, root-kind, or ownership status?"
            ),
        })
    if len(rows) != packet["identity_count"] or {row["identity"] for row in rows} != {node["identity"] for node in packet["nodes"]}:
        raise ValueError("identity coverage mismatch")
    result = {
        "source_task": packet["source_task"],
        "batch": packet["batch"],
        "baseline_inventory_sha256": packet["baseline"]["inventory_sha256"],
        "input_file_sha256": sha(INPUT.read_bytes()),
        "partition_sha256": packet["partition_sha256"],
        "non_authoritative": True,
        "semantic_admission": "not_performed",
        "source_migration": "not_performed",
        "operator_decision": packet["operator_decision"],
        "scope_omission_decision": {"path": str(SCOPE_DECISION.relative_to(ROOT)), "sha256": expected_scope, "applied_to_batch": False},
        "evidence_catalogue": catalogue,
        "nodes": rows,
    }
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    main()
