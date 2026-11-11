---
atom_id: CA-P-2398
ref_id: CA-P-2398
container:
  atom: CA-P-2388
role: Plan
form: Plan
label: Task
topics:
  main_subject: Subject/Graph Node/Engineering/Continuant/Tool
  dependencies:
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Atom.Header.State.Status
  - Subject/Graph Node/Domain/Continuant/History/Journal
  - Subject/Graph Node/Engineering/Workflow
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
tier: 3
relations:
  is_decomposition_of:
  - CA-P-2388
status: Done
version: 8
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 2-CA-P-2398-TASK--remove-subject-batch-recording-gates.md
    path: .caprmedio_caprmedio/03_plan/30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution/done/61-CA-P-2385-TASK--remove-history-and-journal-gates-from-atom-status-operations/done/3-CA-P-2388-TASK--allow-requested-status-on-atom-create-and-update/done
work_sequence_number: 2
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
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
