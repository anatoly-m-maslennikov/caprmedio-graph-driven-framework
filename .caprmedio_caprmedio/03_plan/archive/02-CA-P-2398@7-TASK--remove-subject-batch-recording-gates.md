---
atom_id: CA-P-2398@7
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Subject/Engineering/Tool
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Atom.Status
  - Subject/Domain/Node/Continuant/History/Journal
  - Subject/Engineering/Workflow
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
version: 7
updated_at: 2026-10-24 09:44:12 +0400
relations:
  is_decomposition_of:
  - CA-P-2388
tier: 3
---
# Summary

Remove Subject batch recording gates

## Objective

Remove existing Subject-batch Journal recording_errors admission/completion gates; preserve exact per-target authority, partial effects and stop on real execution failure.

## Details

### Observed completion — 2026-10-16

Subject-batch Journal recording_errors no longer gate admission or completion; actual per-target failure, partial effects and stop behavior remain. The implementation is integrated and scoped non-native Ruff F/E9 checks passed. Final Linux Subject-batch functional verification stays under CA-P-2389 and is not claimed by this leaf closure.

Estimated own work: at most 15 minutes. Apply the complete current mrt_programmatic_methods prompt. Exclusive ownership is recorded in the execution lane report; preserve other workers' changes. No invented identity, Journal admission, replay, broader release or historical cleanup.

### Definition of Done

The bounded deliverable passes its applicable source/functional checks with actual results and unresolved blockers distinguished. Review/update the next dependent before integration; preparation of independent exclusive files is not acceptance of unfinished dependencies.
