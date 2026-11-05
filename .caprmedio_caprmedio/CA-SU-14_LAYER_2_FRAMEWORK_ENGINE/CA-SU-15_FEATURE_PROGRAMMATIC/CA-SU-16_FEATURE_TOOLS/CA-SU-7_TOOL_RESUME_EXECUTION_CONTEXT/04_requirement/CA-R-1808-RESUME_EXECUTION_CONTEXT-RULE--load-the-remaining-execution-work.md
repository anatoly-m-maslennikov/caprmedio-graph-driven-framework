---
atom_id: CA-R-1808
ref_id: CA-R-1808
role: Requirement
current_scope_unit: RESUME_EXECUTION_CONTEXT
status: Active
author: Anatoly Maslennikov
version: 11
updated_at: 2026-10-27 20:00:03 +0400
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Recovery
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
form: Rule
tier: 3
container:
  scope_unit: CA-SU-7
carrier_destination:
  file:
    name: CA-R-1808-RESUME_EXECUTION_CONTEXT-RULE--load-the-remaining-execution-work.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/CA-SU-7_TOOL_RESUME_EXECUTION_CONTEXT/04_requirement
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
