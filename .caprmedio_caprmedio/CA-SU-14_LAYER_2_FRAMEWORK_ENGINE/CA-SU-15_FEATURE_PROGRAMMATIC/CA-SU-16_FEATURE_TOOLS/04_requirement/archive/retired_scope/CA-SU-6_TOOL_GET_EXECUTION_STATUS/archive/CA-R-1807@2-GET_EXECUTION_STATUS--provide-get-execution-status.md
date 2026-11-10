---
atom_id: CA-R-1807@2
content_role: Requirement
current_scope_unit: GET_EXECUTION_STATUS
local_tier: Standard
global_tier: 14
status: Archived
author: Anatoly Maslennikov
version: 2
updated_at: 2026-10-23 01:47:30 +0400
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
  - CA-O-115
  - CA-R-1810
type: Rule
---
# Summary

Read execution status and saved results

## Scope

the GET_EXECUTION_STATUS capability for Tool/GET_EXECUTION_STATUS.

## Claim

the GET_EXECUTION_STATUS Tool **must** return the saved Workflow Run status and requested Action results with evidence references, distinguishing work outcomes from evidence-recording failures.

## Details

- implement the methodology Action CA-O-115-PROJECT_CONFIGURATION-ACTION--get-execution-status.
- accept a supported Run ID, optional Action ID and selection ordinal, and whether full saved results are requested; return status, output, results, progress, recording blockers, and report references.
- preserve the Operator's choice of what **to** execute; discovery, context retrieval, **and** observation provide capabilities.
- bounded **or** unavailable evidence **must** remain explicit **rather than** establish a successful assessment.
