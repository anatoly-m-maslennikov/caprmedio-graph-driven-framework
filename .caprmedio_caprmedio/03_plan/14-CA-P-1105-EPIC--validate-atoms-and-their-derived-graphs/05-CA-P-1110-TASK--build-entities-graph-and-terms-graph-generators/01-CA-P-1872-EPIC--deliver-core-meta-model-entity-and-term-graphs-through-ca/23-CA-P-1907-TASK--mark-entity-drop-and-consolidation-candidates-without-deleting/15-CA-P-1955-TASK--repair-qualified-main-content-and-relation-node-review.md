---
atom_id: CA-P-1955
content_role: Plan
type: Plan
label: Task
work_sequence_number: 15
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Projection
  depends_on: [Entity, Atom, Carrier, Plan]
version: 1
updated_at: "2026-10-10 04:26:00 +0400"
relations:
  is_decomposition_of: [CA-P-1907]
  blocks: [CA-P-1937]
---
# Summary

Repair qualified Main Content and Relation node review

## Objective

Correct false missing-meaning questions and review rationales in captured batch 5 before integration.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent.

Input receipt: CA-P-1933 is already Done. Preserve that historical receipt and the existing correctly repaired rows.

Use only captured Core commit `a971d0e00c33c779f485fc8cad63194894d440fb`, the original partition, `nodes/contract.md` and `nodes/support/snapshot_sources.py`. The Operator chose **Finish against the captured snapshot only**.

Known false-gap examples: Markdown Atom Carrier/Main Content (CA-D-357@9), its Paragraph and Structure qualifications (CA-D-279@12 and CA-D-356@9), Journal/Carrier (CA-D-308@11), Implementation Of Relation (CA-R-1020@15), Implementation Relation Pair (CA-R-1027@15), and Normative Atom Prose Authoring (CA-M-233@12). The review already quotes some meanings but incorrectly requires a literal identity in a governing primary contribution. Inspect all 40 question rows for this same false gate. A naturally qualified constraint supports bounded retention; literal path wording, GOVERNS incidence, native admission, an independent universal definition and replacement proof are not prerequisites for retaining an unchanged identity. Preserve genuine uncertainty separately.

Own only `nodes/nodes.batch-5.review.json` and a temporary helper under `.caprmedio_tmp/planning/core-entity-review/nodes/`. Preserve all 80 identities, original input pins, correct positive rows, raw quotations and genuine unresolved questions. Add exact captured Main Content spans, substantive target-specific reasons for all five checks in each corrected row, and truthful checked/unassessed source coverage. Record CA-P-1955 repair provenance and the prior review SHA; Git retains the original review.

Root owns Plans, Git and integration. You are not alone; preserve other edits. No Core, Subject, baseline, runtime, implementation, MCP or FPF changes, deletion, adoption or native admission. Use uv only and apply_patch for authored edits. Below 90% confidence, preserve a specific question. Return a checkpoint for further decomposition if this cannot finish within 15 minutes.

### Definition of Done

the Plan is **not** Done **if** ((a known false-gap example still falsely describes its meaning as absent) **or** (a corrected positive row lacks exact captured Main Content evidence and five substantive checks) **or** (original identities, correct rows, input pins or genuine uncertainty are lost) **or** (source coverage or captured-context claims are false) **or** (the batch verifier or independent meaning check fails) **or** (the input receipt is **not** Done) **or** (the bounded exclusive scope is exceeded)).
