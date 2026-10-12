"""Build the non-authoritative CA-P-1930 node-review envelope.

This producer deliberately does not infer model admission from paths, repeated
labels, or the inventory's structural edges.  It only assembles captured Main Content
spans from the source pins supplied by the batch input and records a bounded
review disposition.  The four rows whose parent/serialization meaning is not
settled are left as explicit Operator questions.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[4]
NODES_DIR = ROOT / ".caprmedio_caprmedio" / "_projection" / "core-entity-review" / "nodes"
INPUT_PATH = NODES_DIR / "inputs" / "nodes.batch-2.input.json"
BASELINE_PATH = ROOT / ".caprmedio_caprmedio" / "_projection" / "core-entity-review" / "baseline.inventory.json"
OUTPUT_PATH = NODES_DIR / "nodes.batch-2.review.json"
SCOPE_DECISION_PATH = NODES_DIR / "scope.omission.decision.md"
SUPPORT_DIR = NODES_DIR / "support"
sys.path.insert(0, str(SUPPORT_DIR))
from snapshot_sources import COMMIT, read_source, source_pins  # noqa: E402


# A small evidence override table keeps the selected evidence tied to the
# actual claim that defines each identity.  Every ID is checked against the
# input row before it can be emitted.
PREFERRED_EVIDENCE: dict[int, tuple[str, ...]] = {
    0: ("CA-R-794",),
    1: ("CA-R-1398",),
    2: ("CA-R-1506",),
    3: ("CA-M-264",),
    4: ("CA-M-265",),
    5: ("CA-R-1343",),
    6: ("CA-R-1340", "CA-R-1767"),
    7: ("CA-R-1397",),
    8: ("CA-R-1530",),
    9: ("CA-R-1874",),
    10: ("CA-R-1565",),
    11: ("CA-D-457",),
    12: ("CA-R-1562",),
    13: ("CA-R-1564",),
    14: ("CA-R-1569",),
    15: ("CA-R-1563",),
    16: ("CA-R-1338",),
    17: ("CA-D-460", "CA-D-461"),
    18: ("CA-R-1542",),
    19: ("CA-D-461",),
    20: ("CA-R-1541",),
    21: ("CA-R-1537",),
    22: ("CA-R-1534",),
    23: ("CA-R-1539",),
    24: ("CA-R-1541",),
    25: ("CA-R-1542",),
    26: ("CA-R-1545",),
    27: ("CA-D-378",),
    28: ("CA-R-1574", "CA-M-306"),
    29: ("CA-R-1584",),
    30: ("CA-D-473",),
    31: ("CA-R-1587",),
    32: ("CA-D-472",),
    33: ("CA-D-475",),
    34: ("CA-D-475",),
    35: ("CA-R-1580", "CA-E-504"),
    36: ("CA-D-471",),
    37: ("CA-E-502",),
    38: ("CA-D-470",),
    39: ("CA-D-469",),
    40: ("CA-D-460",),
    41: ("CA-R-1536", "CA-E-507"),
    42: ("CA-D-481",),
    43: ("CA-R-1599",),
    44: ("CA-R-1586",),
    45: ("CA-D-378",),
    46: ("CA-R-1576",),
    47: ("CA-R-1537",),
    48: ("CA-D-475",),
    49: ("CA-R-1583",),
    50: ("CA-R-1577",),
    51: ("CA-R-991",),
    52: ("CA-R-1339", "CA-R-1694"),
    53: ("CA-R-1309",),
    54: ("CA-D-286",),
    55: ("CA-R-932", "CA-E-243"),
    56: ("CA-R-951",),
    57: ("CA-R-1294",),
    58: ("CA-R-933",),
    59: ("CA-D-287",),
    60: ("CA-R-925", "CA-R-1775"),
    61: ("CA-D-292",),
    62: ("CA-D-286",),
    63: ("CA-D-342",),
    64: ("CA-D-304",),
    65: ("CA-D-268",),
    66: ("CA-D-478",),
    67: ("CA-R-1444", "CA-R-1389"),
    68: ("CA-R-1363",),
    69: ("CA-D-378",),
    70: ("CA-D-366",),
    71: ("CA-D-304",),
    72: ("CA-M-276",),
    73: ("CA-R-1287",),
    74: ("CA-D-285",),
    75: ("CA-M-272",),
    76: ("CA-R-659",),
    77: ("CA-R-1431",),
    78: ("CA-R-658",),
    79: ("CA-R-660",),
    80: ("CA-D-478", "CA-R-1598"),
}


# These identities have captured references, but the supplied claims do not
# settle whether the path is an independently modelled parent or only a
# serialization/grouping token.  The question is intentionally narrower than
# a generic “needs review” marker.
QUESTION_ROWS: dict[int, tuple[int, str]] = {
    27: (
        82,
        "Does `Atom/Content Role: Plan/Type` have an independently modelled Type meaning, "
        "or is it only the parent grouping for the qualified Plan Type leaves? The selected "
        "CA-D-378 claim establishes Plan ID encoding, not this parent node's semantic contract.",
    ),
    54: (
        82,
        "Does `Atom/Content Role: Requirement/Type` have an independently modelled Type "
        "meaning, or is it only the parent grouping for Demand and Goal/Reference leaves? "
        "The selected CA-D-286 claim establishes a filename Type token, not the parent "
        "node's semantic contract.",
    ),
    64: (
        80,
        "Is `Atom/Direct Relation` an independently modelled semantic relation concept, "
        "or only a grouping for direct-relation serialization? CA-D-304 proves identity and "
        "relation preservation during carrier recoding, but does not define this generic node.",
    ),
    48: (
        84,
        "Does `Atom/Content Role: Plan/Type: Plan/Status` have a qualified Type-status "
        "meaning distinct from `Atom/Content Role: Plan/Status`, or is it only a carrier or "
        "container representation? The checked CA-D-475 claim defines the backlog directory "
        "as a Status container but does not define this qualified Type path.",
    ),
    70: (
        84,
        "Should `Atom/Identifier/Project Prefix` be admitted as a model Property, or remain "
        "a carrier/configuration token? The checked Project Settings and identifier claims "
        "do not establish a distinct Atom-level semantic contract for this path.",
    ),
}


STYLE_BY_INDEX: dict[int, str] = {}
for _i in (0, 5, 6, 8, 12, 13, 14, 15, 16, 18, 21, 22, 26, 28, 29, 31, 35, 43, 44, 50, 52, 55, 56, 57, 58, 60, 67, 68, 71, 72, 75):
    STYLE_BY_INDEX[_i] = "model"
for _i in (1, 7, 9, 10, 23, 24, 25, 33, 34, 48, 49, 53, 76, 77, 78, 79):
    STYLE_BY_INDEX[_i] = "domain"
for _i in (11, 17, 19, 30, 32, 36, 37, 38, 39, 40, 42, 45, 46, 51, 59, 61, 62, 63, 65, 66, 69, 74, 80):
    STYLE_BY_INDEX[_i] = "carrier"
for _i in (2, 3, 4, 20, 27, 41, 47, 54, 64, 70, 73):
    STYLE_BY_INDEX[_i] = "scope"

STYLE_CLAUSE = {
    "model": "the checked Claim gives it a role, type, relation, constraint, or reusable model meaning",
    "domain": "the checked Claim fixes a qualified status, tier, or allowed-value domain",
    "carrier": "the checked Claim fixes a carrier, field, filename, placement, or serialization meaning",
    "scope": "the checked Claim fixes a scope, target, qualification, or parent/child boundary",
}

QUALIFIER_BY_INDEX = {
    21: "The captured CA-R-1537 claim supports the direct DECOMPOSES_INTO relation basis used by recursive closure; it is not an independent full definition and not the transitive/recursive relation itself.",
}

# CA-D-478's first paragraph introduces the one-location rule, while the
# following bullets contain the actual Frontmatter/Main Content and relation
# placement constraints requested by the review. Keep this exact captured span
# rather than replacing it with a paraphrase or a metadata-only excerpt.
CAPTURED_SPAN_OVERRIDES = {
    "CA-D-478": (33, 38),
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_text(text: str) -> str:
    return sha256_bytes(text.encode("utf-8"))


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def claim_span(atom_id: str, raw: bytes) -> tuple[int, int, str]:
    """Return a short exact captured Main Content span, never frontmatter."""

    lines = raw.decode("utf-8").splitlines()
    override = CAPTURED_SPAN_OVERRIDES.get(atom_id)
    if override is not None:
        start, end = override
        if not (1 <= start <= end <= len(lines)):
            raise AssertionError(f"invalid captured span override for {atom_id}")
        return start, end, "\n".join(lines[start - 1 : end])
    frontmatter_end = 0
    if lines and lines[0].strip() == "---":
        for pos in range(1, len(lines)):
            if lines[pos].strip() == "---":
                frontmatter_end = pos + 1
                break
    header = None
    for pos in range(frontmatter_end, len(lines)):
        if lines[pos].strip().lower() in {"## claim", "## operation", "## procedure", "## condition", "## definition", "## evaluation"}:
            header = pos
            break
    if header is None:
        raise ValueError(f"no semantic Main Content section in captured source {atom_id}")

    start = header + 1
    while start < len(lines) and not lines[start].strip():
        start += 1
    if start >= len(lines) or lines[start].startswith("## "):
        raise ValueError(f"semantic section has no substantive Claim text in captured source {atom_id}")
    end = start + 1
    while end < len(lines) and lines[end].strip() and not lines[end].startswith("## "):
        end += 1
    span = "\n".join(lines[start:end])
    if not span:
        raise ValueError(f"semantic section has no substantive Claim text in captured source {atom_id}")
    return start + 1, end, span


def pin_index(baseline: dict[str, Any]) -> dict[str, dict[str, Any]]:
    pins: dict[str, dict[str, Any]] = {}
    for item in baseline.get("source_atoms", []) + baseline.get("excluded_sources", []):
        atom_id = item.get("atom_id")
        if atom_id:
            pins[atom_id] = item
    return pins


def checked_pin(atom_id: str, pins: dict[str, dict[str, Any]]) -> tuple[dict[str, Any], bytes]:
    pin = pins.get(atom_id)
    if pin is None:
        raise AssertionError(f"source atom {atom_id} is absent from the captured baseline pin catalogue")
    raw = read_source(atom_id)
    actual = sha256_bytes(raw)
    if actual != pin["carrier_sha256"]:
        raise AssertionError(f"captured source pin mismatch {atom_id}: {actual} != {pin['carrier_sha256']}")
    return pin, raw


def evidence_for(
    node_index: int,
    node: dict[str, Any],
    pins: dict[str, dict[str, Any]],
    evidence_catalogue: list[dict[str, Any]],
    cache: dict[str, dict[str, Any]],
) -> tuple[list[str], list[str]]:
    source_ids = list(node["source_atom_ids"])
    available = set(source_ids)
    selected = PREFERRED_EVIDENCE.get(node_index, ())
    if not selected:
        selected = tuple(node.get("governing_source_atom_ids", ())) or tuple(source_ids[:1])
    missing = [atom_id for atom_id in selected if atom_id not in available]
    if missing:
        raise AssertionError(f"preferred evidence is not a source candidate for node {node_index}: {missing}")

    checked: list[str] = []
    for atom_id in source_ids:
        pin, _ = checked_pin(atom_id, pins)
        checked.append(atom_id)
        cache.setdefault(atom_id, pin)

    refs: list[str] = []
    for atom_id in selected:
        pin, raw = checked_pin(atom_id, pins)
        if atom_id in cache and any(item["atom_id"] == atom_id for item in evidence_catalogue):
            refs.append(next(item["evidence_ref"] for item in evidence_catalogue if item["atom_id"] == atom_id))
            continue
        start_line, end_line, quote = claim_span(atom_id, raw)
        evidence_ref = f"CA-P-1930-b2-e{len(evidence_catalogue) + 1:03d}"
        evidence_catalogue.append(
            {
                "evidence_ref": evidence_ref,
                "atom_id": atom_id,
                "atom_revision": pin["atom_revision"],
                "carrier_path": pin["carrier_path"],
                "carrier_sha256": pin["carrier_sha256"],
                "start_line": start_line,
                "end_line": end_line,
                "quote": quote,
                "text_sha256": sha256_text(quote),
            }
        )
        refs.append(evidence_ref)
        cache[atom_id] = pin
    return checked, refs


def check_bundle(identity: str, index: int, refs: list[str], question: bool) -> dict[str, dict[str, Any]]:
    if question:
        return {
            "duplicates": {
                "finding": "unresolved_no_duplicate_proof",
                "reason": f"{identity}: the checked claims do not settle whether this parent/token is a duplicate or an independent node.",
                "evidence_refs": refs,
            },
            "redundancy": {
                "finding": "unresolved_no_redundancy_proof",
                "reason": f"{identity}: qualified descendants and carrier forms cannot establish redundancy without the Operator's semantic choice.",
                "evidence_refs": refs,
            },
            "empty_definition": {
                "finding": "unresolved_definition_scope",
                "reason": f"{identity}: a missing dedicated definition is not treated as proof of an empty node.",
                "evidence_refs": refs,
            },
            "distinct_meaning": {
                "finding": "unresolved_distinct_meaning",
                "reason": f"{identity}: captured evidence is insufficient to distinguish a semantic parent from a grouping/serialization token.",
                "evidence_refs": refs,
            },
            "generalization": {
                "finding": "not_proposed",
                "reason": f"{identity}: no generalization is proposed while the parent/token meaning remains unresolved.",
                "evidence_refs": refs,
            },
        }

    style = STYLE_BY_INDEX.get(index, "model")
    clause = STYLE_CLAUSE[style]
    qualifier = QUALIFIER_BY_INDEX.get(index, "")
    suffix = f" {qualifier}" if qualifier else ""
    return {
        "duplicates": {
            "finding": "no_same_meaning_duplicate_proven",
            "reason": f"{identity}: {clause}; repeated leaf labels and qualified paths are not treated as duplicate proof.{suffix}",
            "evidence_refs": refs,
        },
        "redundancy": {
            "finding": "not_redundant_on_captured_claims",
            "reason": f"{identity}: its checked captured claim carries a distinct {style} boundary, so adjacent paths are retained rather than collapsed.{suffix}",
            "evidence_refs": refs,
        },
        "empty_definition": {
            "finding": "meaningful_captured_claim",
            "reason": f"{identity}: the selected captured Main Content is substantive; absence of a separate definition is not used as an empty/drop signal.{suffix}",
            "evidence_refs": refs,
        },
        "distinct_meaning": {
            "finding": "distinct_meaning_evidenced",
            "reason": f"{identity}: the checked captured claim preserves its {style} meaning separately from source provenance, ownership, and carrier metadata.{suffix}",
            "evidence_refs": refs,
        },
        "generalization": {
            "finding": "generalization_not_proposed",
            "reason": f"{identity}: no broader replacement is proposed because it could erase this qualified {style} distinction and alter references or queries.{suffix}",
            "evidence_refs": refs,
        },
    }


def retain_reason(identity: str, index: int, evidence_atom_ids: list[str]) -> str:
    style = STYLE_BY_INDEX.get(index, "model")
    clause = STYLE_CLAUSE[style]
    atoms = ", ".join(evidence_atom_ids)
    qualifier = QUALIFIER_BY_INDEX.get(index, "")
    return (
        f"Retain {identity}: {clause} in captured pinned Main Content ({atoms}). "
        f"Preserve the qualified {style} distinction, identity/history references, and any "
        "declared relation or constraint boundaries; no move, consolidation, drop, or "
        f"generalization is justified by this batch.{(' ' + qualifier) if qualifier else ''}"
    )


def retain_proposal(identity: str) -> dict[str, Any]:
    """Record preservation effects without proposing migration or admission."""

    return {
        "kind": "retain_preserved_baseline_identity_only",
        "replacement_identity": None,
        "native_admission": "not_performed",
        "relations_impact": "no relation creation, removal, or rewrite proposed",
        "constraints_impact": "no constraint change proposed",
        "historical_references_impact": f"preserved at the original baseline identity {identity}",
        "queries_impact": "identity-based queries preserve the original baseline identity",
        "preserved_distinctions": [identity],
        "lost_distinctions": [],
    }


def main() -> None:
    raw_input = INPUT_PATH.read_bytes()
    batch_input = json.loads(raw_input)
    baseline_raw = BASELINE_PATH.read_bytes()
    baseline = json.loads(baseline_raw)
    if batch_input.get("batch") != 2 or batch_input.get("identity_count") != 81:
        raise AssertionError("CA-P-1930 input is not the expected 81-node batch 2 partition")
    baseline_pin = batch_input["baseline"]
    if sha256_bytes(baseline_raw) != baseline_pin["sha256"]:
        raise AssertionError("CA-P-1930 input baseline pin is stale")
    if baseline["inventory_sha256"] != baseline_pin["inventory_sha256"]:
        raise AssertionError("CA-P-1930 baseline inventory digest does not match the input pin")
    decision = batch_input["operator_decision"]
    decision_path = ROOT / decision["path"]
    if sha256_bytes(decision_path.read_bytes()) != decision["sha256"]:
        raise AssertionError("CA-P-1930 Operator decision pin is stale")
    nodes = batch_input["nodes"]
    if len(nodes) != 81 or len({node["identity"] for node in nodes}) != 81:
        raise AssertionError("node input is not exactly-once")

    pins = source_pins()
    if len(pins) != 908:
        raise AssertionError("unexpected captured source pin count")
    evidence_catalogue: list[dict[str, Any]] = []
    evidence_cache: dict[str, dict[str, Any]] = {}
    reviewed: list[dict[str, Any]] = []
    seen: set[str] = set()

    for index, node in enumerate(nodes):
        identity = node["identity"]
        if identity in seen:
            raise AssertionError(f"duplicate node identity {identity}")
        seen.add(identity)
        checked_ids, evidence_refs = evidence_for(index, node, pins, evidence_catalogue, evidence_cache)
        is_question = index in QUESTION_ROWS
        if is_question:
            confidence, question = QUESTION_ROWS[index]
            disposition = "question"
            reason = f"Questioned rather than admitted: {question}"
            proposal = None
        else:
            confidence = 95
            question = None
            disposition = "retain"
            reason = retain_reason(identity, index, [item["atom_id"] for item in evidence_catalogue if item["evidence_ref"] in evidence_refs])
            proposal = retain_proposal(identity)
        reviewed.append(
            {
                "identity": identity,
                "disposition": disposition,
                "confidence_percent": confidence,
                "reason": reason,
                "checks": check_bundle(identity, index, evidence_refs, is_question),
                "evidence_refs": evidence_refs,
                "checked_source_atom_ids": checked_ids,
                "proposal": proposal,
                "question": question,
            }
        )

    envelope = {
        "source_task": "CA-P-1930",
        "batch": 2,
        "baseline_inventory_sha256": baseline["inventory_sha256"],
        "input_file_sha256": sha256_bytes(raw_input),
        "partition_sha256": batch_input["partition_sha256"],
        "non_authoritative": True,
        "semantic_admission": "not_performed",
        "source_migration": "not_performed",
        "source_context": "captured_snapshot",
        "git_commit": COMMIT,
        "operator_decision": batch_input["operator_decision"],
        "scope_omission_decision": {
            "path": str(SCOPE_DECISION_PATH.relative_to(ROOT)),
            "sha256": sha256_bytes(SCOPE_DECISION_PATH.read_bytes()),
            "applied_to_batch": False,
        },
        "evidence_catalogue": evidence_catalogue,
        "nodes": reviewed,
    }
    OUTPUT_PATH.write_text(json.dumps(envelope, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(OUTPUT_PATH), "nodes": len(reviewed), "questions": len(QUESTION_ROWS), "evidence": len(evidence_catalogue)}, sort_keys=True))


if __name__ == "__main__":
    main()
