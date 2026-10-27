---
atom_id: CA-E-528@4
content_role: Evaluation
type: Eval Case
current_scope_unit: GET_EXECUTION_STATUS
status: Archived
author: Anatoly Maslennikov
version: 4
updated_at: 2026-10-24 11:58:20 +0400
subjects:
  governs: Subject/Engineering/Programmatic Action/Execution Observation Adapter
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Domain/Node/Occurrent/Execution
  - Subject/Domain/Node/Continuant/History/Journal
relations:
  relates_to:
  - CA-R-1807
  - CA-D-515
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
