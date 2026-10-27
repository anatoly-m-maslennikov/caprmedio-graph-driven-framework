---
atom_id: CA-E-528
content_role: Evaluation
type: Eval Case
current_scope_unit: GET_EXECUTION_STATUS
status: Active
author: Anatoly Maslennikov
version: 8
updated_at: 2026-10-27 06:04:45 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Verification/Dynamic Testing
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - Subject/Graph Node/Domain/Occurrent/Execution
  - Subject/Graph Node/Domain/Continuant/History/Journal
relations: {}
tier: 3
---
# Summary

Verify GET_EXECUTION_STATUS

## Scope

the GET_EXECUTION_STATUS capability for Tool/GET_EXECUTION_STATUS.

## Claim

the Evaluation **must** check the GET_EXECUTION_STATUS Tool against its declared result **and** Carrier contract using an end-to-end mock Project.

## Details

- exercise running, completed, failed, interrupted, pending Actions, initial check results preserved through fixing, missing Runs, unsupported Action IDs, and recording failure.
- compare complete expected results with actual results; successful counts alone do **not** establish correctness.
- invoke the real MCP transport for the exposed schema **and** result boundary.
- retain existing RMED Atoms Base Revise behavior, including its initial evidence **and** absence of a saved-output recheck.
