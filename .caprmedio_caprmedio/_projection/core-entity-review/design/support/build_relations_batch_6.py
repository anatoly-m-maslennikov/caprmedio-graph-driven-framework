"""Fail-closed CA-P-1918 relation ledger from current pinned Main Content."""
import hashlib
import json
import re
from pathlib import Path

root = Path(".caprmedio_tmp/planning/core-entity-review/design")
source = json.loads((root / "batch-6.input.json").read_text())
pins = {item["atom_id"]: item for item in source["current_source_pins"]}
claim_display = {
    "Project Settings/Identifier": ("CA-D-362", "identifier qualification"),
    "Project Settings/Project identity": ("CA-D-375", "project-identity qualification"),
    "Project Settings/Atom Prefix": ("CA-D-376", "atom-prefix qualification"),
    "Framework Instance Settings/Artifact Timestamp Timezone": ("CA-D-390", "timestamp-timezone qualification"),
    "Markdown Atom Carrier/YAML Frontmatter": ("CA-D-276", "frontmatter qualification"),
    "Markdown Atom Carrier/Main Content": ("CA-D-279", "main-content qualification"),
    "RMED Atom Review Workflow/coverage/Step": ("CA-O-119", "coverage-substep context"),
    "RMED Atom Review Workflow/coverage": ("CA-O-118", "coverage-action context"),
    "Find and Fetch Journal Events/Step": ("CA-O-163", "query-step context"),
    "Framework Instance Settings/Tool selections": ("CA-D-372", "tool-selection qualification"),
    "Framework Instance Settings/framework control-root locator": ("CA-D-370", "control-root-locator qualification"),
    "Markdown Atom Carrier/YAML Frontmatter/Scalar": ("CA-D-277", "frontmatter-scalar qualification"),
    "Markdown Atom Carrier/Main Content/CCE Operator": ("CA-D-280", "CCE-operator qualification"),
    "Atom Carrier/Filename/Summary Slug": ("CA-D-282", "summary-slug qualification"),
    "Proof Carrier/Dependency Frontier": ("CA-D-329", "dependency-frontier qualification"),
    "Producer Result/Flow Direction": ("CA-R-945", "flow-direction qualification"),
}

def content_evidence(ref):
    path = Path(ref["carrier_path"])
    raw = path.read_text()
    digest = hashlib.sha256(raw.encode()).hexdigest()
    if digest != ref["carrier_sha256"]:
        raise ValueError(f"stale pin: {path}")
    lines = raw.splitlines()
    starts = [i for i, line in enumerate(lines) if re.match(r"^## Claim\b", line)]
    if not starts:
        starts = [i for i, line in enumerate(lines) if re.match(r"^## Operation\b", line)]
    if not starts:
        starts = [i for i, line in enumerate(lines) if re.match(r"^## (Definition|Requirement|Delivery|Procedure|Condition|Details|Scope|Evaluation)\b", line)]
    if not starts:
        starts = [i for i, line in enumerate(lines) if line.startswith("# Summary")]
    if not starts:
        raise ValueError(f"no Main Content span: {path}")
    start = starts[0]
    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
    quote_start = start + 1
    quote = "\n".join(lines[quote_start:end])
    return {"atom_id": ref["atom_id"], "atom_revision": ref["atom_revision"], "carrier_path": ref["carrier_path"], "carrier_sha256": digest, "start_line": quote_start + 1, "end_line": end, "quote": quote, "text_sha256": hashlib.sha256(quote.encode()).hexdigest()}

rows = []
context_tokens = ("Carrier", "Identifier", "Filename", "Format", "Extension", "Prefix", "Tier", "Content", "source", "resolution", "selection", "Context", "Invocation", "Tool Call", "timezone", "Binding", "Record", "Member", "Catalog", "Scalar", "Operator", "Parameters", "mode", "Interaction", "Scope Unit", "Projection", "Flow Direction")
structural_tokens = ("Containment", "Nesting", "Expansion Boundary", "Installed Extensions", "minimum model")
for case in source["cases"]:
    occurrences = case["occurrences"]
    governing = [o for o in occurrences if o["role"] == "GOVERNS"]
    chosen = (governing or occurrences)[0]["source_ref"]
    child = case["child_term"]
    is_structural = any(token.casefold() in child.casefold() for token in structural_tokens)
    is_context = any(token.casefold() in child.casefold() for token in context_tokens)
    if case["old_child"] in claim_display:
        atom_id, meaning = claim_display[case["old_child"]]
        chosen = pins[atom_id]
        disposition, confidence = "not-native", 90
        display = {"display_operator": ".", "qualified_parent": case["old_parent"], "qualified_child": case["old_child"], "semantic_intent": meaning, "native_admission": "not_performed"}
        reason = f"The pinned Claim expressly governs this {meaning}; it supports display-only '.' qualification, but does not identify an immediate dependent Entity required for native IS_BORNE_BY."
        question = None
    else:
        disposition, confidence, display = "unresolved", 0, None
        reason = f"The quoted current Claim/Main Content for {case['old_parent']} / {case['old_child']} was checked, but does not by itself establish a >=90% canonical relation direction, immediate dependent identity, or narrower fact."
        question = f"Does the checked Claim make {case['old_child']} a general qualification of {case['old_parent']}, a structural/taxonomic relation, or neither? State the intended relation and direction."
    row = {"case_id": case["case_id"], "old_parent": case["old_parent"], "old_child": case["old_child"], "disposition": disposition, "confidence_percent": confidence, "proposal": None, "evidence": [content_evidence(chosen)], "checks_performed": ["selected-current-source-pin-sha256-matched", "quoted-current-main-content-not-subjects", "no-metadata-filename-or-incidence-semantic-inference", "no-native-admission"], "reason": reason, "question": question}
    if display:
        row["display_candidate"] = display
    rows.append(row)

out = {k: source[k] for k in ("source_task", "batch_number", "baseline_inventory_sha256", "source_binding", "partition_sha256")}
out.update({"non_authoritative": True, "source_migration": "not_performed", "semantic_admission": "not_performed", "cases": rows})
(root / "relations.batch-6.json").write_text(json.dumps(out, indent=2) + "\n")
