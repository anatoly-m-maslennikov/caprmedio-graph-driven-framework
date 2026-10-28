---
atom_id: CA-R-1808
content_role: Requirement
current_scope_unit: RESUME_EXECUTION_CONTEXT
status: Active
author: Anatoly Maslennikov
version: 11
updated_at: 2026-10-27 20:00:03 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Recovery
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

Load the remaining execution work

## Scope

the RESUME_EXECUTION_CONTEXT capability for Tool/RESUME_EXECUTION_CONTEXT.

## Claim

the RESUME_EXECUTION_CONTEXT Tool **must** return sufficient saved context to continue unfinished work under the same Run ID without replaying completed effects.

## Details

- implement the methodology Action CA-O-116-PROJECT_CONFIGURATION-ACTION--load-the-remaining-execution-work.
- accept a supported Run ID; return original request, frozen selection and criteria bindings, pending check or fix work, saved handoffs, current-source observations, and recording blockers.
- preserve the Operator's choice of what **to** execute; discovery, context retrieval, **and** observation provide capabilities.
- bounded **or** unavailable evidence **must** remain explicit **rather than** establish a successful assessment.
