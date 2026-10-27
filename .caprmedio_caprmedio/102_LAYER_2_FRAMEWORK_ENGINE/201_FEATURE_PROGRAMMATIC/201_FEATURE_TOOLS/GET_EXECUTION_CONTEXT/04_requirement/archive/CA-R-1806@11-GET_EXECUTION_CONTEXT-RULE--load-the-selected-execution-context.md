---
atom_id: CA-R-1806@11
content_role: Requirement
current_scope_unit: GET_EXECUTION_CONTEXT
status: Archived
author: Anatoly Maslennikov
version: 11
updated_at: 2026-10-26 00:46:35 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Aspect/Execution Control
  depends_on:
  - Subject/Graph Node/Engineering/Continuant/Tool//GET_EXECUTION_CONTEXT
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - Subject/Graph Node/Engineering/Programmatic Action/Execution Context Retrieval Adapter
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  - Subject/Graph Node/Domain/Continuant/History/Journal
relations:
  relates_to:
  - CA-O-114
  - CA-R-1810
tier: 3
type: Rule
---
# Summary

Load the selected execution context

## Scope

the GET_EXECUTION_CONTEXT capability for Tool/GET_EXECUTION_CONTEXT.

## Claim

the GET_EXECUTION_CONTEXT Tool **must** return the selected capability's exact current definition, implementation binding, input schema when supported, and relevant authority and operational context.

## Details

- implement the methodology Action CA-O-114-PROJECT_CONFIGURATION-ACTION--load-the-selected-execution-context.
- accept a Tool name or Operations Atom ID and a context budget; return source-bound content, related Workflow Steps and Actions, applicable RMED, implementation and prompt references, and explicit context gaps.
- preserve the Operator's choice of what **to** execute; discovery, context retrieval, **and** observation provide capabilities.
- bounded **or** unavailable evidence **must** remain explicit **rather than** establish a successful assessment.
