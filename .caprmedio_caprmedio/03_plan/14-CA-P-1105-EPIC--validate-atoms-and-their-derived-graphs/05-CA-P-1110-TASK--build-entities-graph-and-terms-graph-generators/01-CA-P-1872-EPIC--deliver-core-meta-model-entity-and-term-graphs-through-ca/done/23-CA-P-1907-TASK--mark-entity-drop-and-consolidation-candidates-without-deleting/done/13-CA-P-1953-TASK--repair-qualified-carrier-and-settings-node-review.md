---
atom_id: CA-P-1953
content_role: Plan
type: Plan
label: Task
work_sequence_number: 13
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: Projection
  depends_on: [Entity, Atom, Carrier, Plan]
version: 2
updated_at: "2026-10-10 04:37:00 +0400"
relations:
  is_decomposition_of: [CA-P-1907]
  blocks: [CA-P-1937]
---
# Summary

Repair qualified Carrier and settings node review

## Objective

Correct false missing-meaning questions and review rationales in the captured batch 4 before integration.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent.

Input receipt: CA-P-1932 is already Done. The completed original batch is a historical receipt; this repair does not silently replace that history.

Use only captured Core commit `a971d0e00c33c779f485fc8cad63194894d440fb`, the original input partition, `nodes/contract.md` and `nodes/support/snapshot_sources.py`. The Operator chose **Finish against the captured snapshot only**. Do not refresh CA-D-494 or claim live-Core validation.

Known false-gap examples: Entity/Carrier (CA-D-505@1 and CA-D-506@1), Default Settings/Carrier/Content (CA-D-408@7), Framework Instance Settings/Carrier/Atom metadata exclusion (CA-D-377@7), and File Carrier/Extension (CA-D-507@1). Inspect the existing questions and five check rationales in this batch for the same defect. A naturally qualified constraint can supply bounded meaning for retaining an unchanged identity. Retention does not require literal path spelling, a newly admitted native relation, an independent universal definition, or safe replacement proof. Preserve any separate spelling or applicability uncertainty; do not pretend the evidenced meaning is absent. Leave genuine unresolved meaning questions visible.

Own only `nodes/nodes.batch-4.review.json` and a temporary repair helper under `.caprmedio_tmp/planning/core-entity-review/nodes/`. Preserve all original identities, input pins and unaffected rows. Add exact captured Main Content spans, truthful checked/unassessed source coverage, and target-specific reasons for all five checks in each corrected row. Correct captured-versus-current narration outside raw quotations. Record repair provenance and the prior review SHA; Git preserves the original receipt. Do not modify the completed original Plan.

Root owns Plans, Git and integration. You are not alone; preserve other edits. No Core, Subject, baseline, runtime, implementation, MCP or FPF writes. Use uv only. Below 90% confidence, retain a specific unresolved question. If this bounded repair cannot finish in 15 minutes, return a checkpoint for decomposition before further execution. No deletion, adoption or native fact admission.

### Completion receipt

Final review: nodes/nodes.batch-4.review.json; SHA-256: d877f1665c61a65d013851cf3b8810edd38d7ca6c0848080873909d2133746eb.

Captured-only repair verified: 81 identities, 55 retain decisions, 26 preserved questions, 62 exact nonempty Main Content evidence spans and 249 captured source pins checked. Independent read-only meaning audit by definition_implementation passed for all 36 corrected rows, including target-specific five-check rationales and no native admission. Original completed batch receipt remains historical; no Core, Subject or baseline change was performed.

### Definition of Done

the Plan is **not** Done **if** ((a known false-gap example remains unsupported or falsely describes its meaning as absent) **or** (a corrected positive row lacks exact captured Main Content evidence and five substantive checks) **or** (original identities, input pins or genuine uncertainty are lost) **or** (a checked-source or captured-context claim is false) **or** (the batch verifier or independent meaning check fails) **or** (the input receipt is **not** Done) **or** (the bounded exclusive scope is exceeded)).
