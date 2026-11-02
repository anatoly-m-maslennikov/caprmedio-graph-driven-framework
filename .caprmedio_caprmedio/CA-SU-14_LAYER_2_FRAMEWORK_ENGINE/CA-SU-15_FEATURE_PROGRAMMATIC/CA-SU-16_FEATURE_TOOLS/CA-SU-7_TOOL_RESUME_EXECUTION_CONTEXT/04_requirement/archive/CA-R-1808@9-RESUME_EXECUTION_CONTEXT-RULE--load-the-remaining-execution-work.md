---
atom_id: CA-R-1808@9
content_role: Requirement
current_scope_unit: RESUME_EXECUTION_CONTEXT
status: Archived
author: Anatoly Maslennikov
version: 9
updated_at: 2026-10-26 05:59:45 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Aspect/Execution Control/Recovery
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - Subject/Graph Node/Domain/Occurrent/Execution
  - Subject/Graph Node/Domain/Continuant/History/Journal
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
