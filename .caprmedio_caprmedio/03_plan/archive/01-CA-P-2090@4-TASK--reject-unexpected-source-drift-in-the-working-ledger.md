---
atom_id: CA-P-2090@4
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Entity
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject
  - Subject/Domain/Node/Continuant/Projection
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  - Tool
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
version: 4
updated_at: 2026-10-24 06:12:13 +0400
relations:
  is_decomposition_of:
  - CA-P-2086
tier: 3
---
# Summary

Reject unexpected source drift in the working ledger

## Objective

The one-off working ledger fails the concrete incorrect-data cases found in Root review.

## Details

Estimated own work: at most 15 minutes. Read working-ledger.contract.md. Correct only the one-off consolidator's fail-closed drift gates: permit the five declared grammar effects at exact after pins/versions and field/index/text; permit new-ID/path rebinding only for the declared CA-R-1204 to CA-R-1931 lineage. Unexpected same-ID hashes, path movement, or missing baseline/current counterparts fail. Add small isolated negative probes. Do not infer grammar acceptance or author source changes. Existing unaccepted derived draft may be regenerated only after Root authorizes its exact replacement. Own stage2/support/consolidate_reviewed_mappings.py and its generated working-ledger drafts, not the independent verifier.

Workers are not alone. Preserve original Core Subjects/content, captured reports, frozen baseline, unrelated work and the existing guarded migration route. No MCP/FPF/runtime, selector adoption, native admission or authority writes. Root owns receipts, lifecycle and a commit after each Task. If the bound is exhausted, return partial evidence for decomposition.

### Completion

The one-off consolidator admits only five exact declared grammar effects, rejects unexpected source/path/counterpart/text drift and preserves all unaccepted grammar rows as null. Existing derived drafts were not replaced. Exact verification is recorded in `_projection/core-entity-review/stage2/task-2090.receipt.json`.

### Definition of Done

Not Done if the assigned live gate or negative probes fail, expected layers or lineage are missing, guesses are executable, captured/source bytes are changed, or own work exceeds the bound without decomposition.
