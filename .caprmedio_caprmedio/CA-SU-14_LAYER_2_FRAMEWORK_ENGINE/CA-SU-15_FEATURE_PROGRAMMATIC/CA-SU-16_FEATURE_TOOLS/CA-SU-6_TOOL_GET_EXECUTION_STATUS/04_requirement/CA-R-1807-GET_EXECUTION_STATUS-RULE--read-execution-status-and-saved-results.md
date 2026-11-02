---
atom_id: CA-R-1807
content_role: Requirement
current_scope_unit: GET_EXECUTION_STATUS
status: Active
author: Anatoly Maslennikov
version: 11
updated_at: 2026-10-27 20:00:03 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
relations: {}
type: Rule
tier: 3
---
# Summary

Read execution status and saved results

## Scope

the GET_EXECUTION_STATUS capability for Tool/GET_EXECUTION_STATUS.

## Claim

the GET_EXECUTION_STATUS Tool **must** return the saved Workflow Run status and requested Action results with evidence references, distinguishing work outcomes from evidence-recording failures.

## Details

- implement the methodology Action CA-O-115-PROJECT_CONFIGURATION-ACTION--read-execution-status-and-saved-results.
- accept a supported Run ID, optional Action ID and selection ordinal, and whether full saved results are requested; return status, output, results, progress, recording blockers, and report references.
- preserve the Operator's choice of what **to** execute; discovery, context retrieval, **and** observation provide capabilities.
- bounded **or** unavailable evidence **must** remain explicit **rather than** establish a successful assessment.
