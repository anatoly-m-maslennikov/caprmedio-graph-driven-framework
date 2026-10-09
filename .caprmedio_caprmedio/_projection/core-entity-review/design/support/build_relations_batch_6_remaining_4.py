#!/usr/bin/env python3
"""Build CA-P-1926's source-pinned remaining contextual relation review."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path.cwd()
DESIGN = ROOT / ".caprmedio_tmp/planning/core-entity-review/design"
INPUT = DESIGN / "remaining-4.input.json"
OUTPUT = DESIGN / "relations.batch-6.remaining-4.json"
SEMANTIC_HEADINGS = ("## Claim", "## Procedure", "## Condition", "## Operation", "## Definition")

# Evidence selection is deliberate: it chooses the source whose authored Claim
# most directly expresses the specific legacy qualified context, not the first
# occurrence by incidental input order.
DISPLAY_CASES = {
    ("Runtime Journal", "Runtime Journal/Carrier"): ("CA-D-559", 92,
        "CA-D-559 makes configured Carriers delivery destinations for Runtime Journals, which supports display context but does not declare an immediate native carrier binding or endpoint identity."),
    ("Work Journal/Event", "Work Journal/Event/Carrier Serialization"): ("CA-D-340", 92,
        "CA-D-340 constrains serialization in a Work Journal Event Carrier record; that is a representation context, not a registered native relation for this qualified path."),
    ("Project Settings", "Project Settings/Authoritative Carrier"): ("CA-D-364", 95,
        "CA-D-364 requires one authoritative TOML File Carrier for Project Settings, but supplies a configuration/representation binding rather than a declared native relation with independently identified endpoints."),
    ("Default Settings/Carrier", "Default Settings/Carrier/Content"): ("CA-D-408", 92,
        "CA-D-408 constrains parameter values carried in the Default Settings TOML Carrier; it supports the content qualification but declares no native bearer/dependent relation."),
    ("Applicable Methodology", "Applicable Methodology/Member Selection"): ("CA-R-1315", 90,
        "CA-R-1315 constrains which current active Atom Revisions Applicable Methodology membership may contain; this is a membership-selection context, not a declared native relation."),
    ("Atom Carrier/Filename", "Atom Carrier/Filename/Local Tier"): ("CA-D-484", 95,
        "CA-D-484 constrains filename rendering while expressly keeping Local Tier internal to the Atom; it supports a rendering context and not a native dependent identity."),
    ("Framework Instance Settings/Confidence/Semantic Resolution Threshold", "Framework Instance Settings/Confidence/Semantic Resolution Threshold/Carrier"): ("CA-D-369", 90,
        "CA-D-369 stores the semantic-resolution confidence default in the Framework Instance Settings TOML Carrier; it does not identify a Carrier of the Threshold itself or declare a native binding."),
    ("Framework Instance Settings", "Framework Instance Settings/Revision Binding"): ("CA-D-360", 92,
        "CA-D-360 constrains revision-and-digest binding through the authoritative carrier and a Journal receipt; it supports a revision-binding context, not a declared native relation."),
    ("Applicable Methodology", "Applicable Methodology/Member"): ("CA-R-1314", 95,
        "CA-R-1314 defines a member's direct DERIVED_FROM relation to its source Atom Revision; membership is supported as display context, while that distinct relation is not recast as a native slash edge."),
    ("Scope Expression/Canonical Scope Signature", "Scope Expression/Canonical Scope Signature/Projection"): ("CA-D-347", 95,
        "CA-D-347 defines delivery of the Canonical Scope Signature Projection as a non-authoritative report; it supports projection context but declares no native bearer/dependent relation."),
    ("CAPRMEDIO Framework Instance", "CAPRMEDIO Framework Instance/Carrier Root"): ("CA-D-317", 90,
        "CA-D-317 places the serving Framework Instance's governance under a Project Directory Carrier; this is a placement context and does not identify a native Carrier Root relation for the instance."),
}

UNRESOLVED = {
    ("Work Journal", "Work Journal/Record"): (
        "CA-D-360 and CA-D-365 bind Settings revisions through a completed governed-change Work Journal receipt, but neither identifies that receipt as a Work Journal Record or declares a Work-Journal-to-Record relation.",
        "Record/receipt family: does current Core identify a completed governed-change Work Journal receipt as a Work Journal Record, and if so what exact relation kind and direction connects it to the Work Journal?",
    ),
}


def sha256(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def read_source(ref: dict) -> list[str]:
    raw = (ROOT / ref["carrier_path"]).read_bytes()
    if sha256(raw) != ref["carrier_sha256"]:
        raise ValueError(f"stale current source pin: {ref['atom_id']}")
    return raw.decode("utf-8").splitlines()


def evidence(ref: dict) -> dict:
    lines = read_source(ref)
    header = next((i for i, line in enumerate(lines) if line in SEMANTIC_HEADINGS), None)
    if header is None:
        raise ValueError(f"no authored semantic section: {ref['atom_id']}")
    start = next((i for i in range(header + 1, len(lines)) if lines[i].strip()), None)
    if start is None:
        raise ValueError(f"empty authored semantic section: {ref['atom_id']}")
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


def references(case: dict) -> dict[str, dict]:
    by_atom = {}
    for occurrence in case["occurrences"]:
        ref = occurrence["source_ref"]
        read_source(ref)
        by_atom.setdefault(ref["atom_id"], ref)
    return by_atom


def case_row(case: dict) -> dict:
    parent, child = case["old_parent"], case["old_child"]
    endpoint = (parent, child)
    refs = references(case)
    shared = {
        "case_id": case["case_id"],
        "old_parent": parent,
        "old_child": child,
        "proposal": None,
        "checks_performed": [
            "verified every listed occurrence source against its current selected carrier SHA-256",
            "quoted only current authored Claim, Procedure, Condition, Operation, or Definition Main Content; ignored Summary, frontmatter, Subjects, and source incidence",
            "required an exact owning native kind, direction, and immediate endpoint identity before any native assertion",
            "preserved legacy qualified references without rebasing or semantic admission",
        ],
        "reviewed_candidate_atom_ids": sorted(refs),
    }
    if endpoint in DISPLAY_CASES:
        atom_id, confidence, reason = DISPLAY_CASES[endpoint]
        if atom_id not in refs:
            raise ValueError(f"selected source {atom_id} not assigned to {endpoint}")
        return {
            **shared,
            "disposition": "not-native",
            "confidence_percent": confidence,
            "display_candidate": {
                "display_operator": ".",
                "qualified_parent": parent,
                "qualified_child": child,
                "semantic_intent": "authored contextual qualification only; native admission not asserted",
            },
            "evidence": [evidence(refs[atom_id])],
            "reason": reason,
            "question": None,
        }
    if endpoint in UNRESOLVED:
        reason, question = UNRESOLVED[endpoint]
        return {
            **shared,
            "disposition": "unresolved",
            "confidence_percent": 0,
            "display_candidate": None,
            "evidence": [],
            "reason": reason,
            "question": question,
        }
    raise ValueError(f"unclassified assigned endpoint: {endpoint}")


def main() -> None:
    if OUTPUT.exists():
        raise FileExistsError(f"refusing to replace existing output: {OUTPUT}")
    source = json.loads(INPUT.read_text(encoding="utf-8"))
    result = {
        "source_task": source["source_task"],
        "batch_number": source["batch_number"],
        "baseline_inventory_sha256": source["baseline_inventory_sha256"],
        "source_binding": source["source_binding"],
        "partition_sha256": source["partition_sha256"],
        "non_authoritative": True,
        "source_migration": "not_performed",
        "semantic_admission": "not_performed",
        "cases": [case_row(case) for case in source["cases"]],
    }
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
