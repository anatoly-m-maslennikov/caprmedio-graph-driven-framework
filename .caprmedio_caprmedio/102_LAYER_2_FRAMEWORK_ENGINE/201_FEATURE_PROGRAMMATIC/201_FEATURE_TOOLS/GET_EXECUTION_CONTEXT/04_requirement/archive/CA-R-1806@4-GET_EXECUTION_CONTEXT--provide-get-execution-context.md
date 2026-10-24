---
atom_id: CA-R-1806@4
content_role: Requirement
current_scope_unit: GET_EXECUTION_CONTEXT
status: Archived
author: Anatoly Maslennikov
version: 4
updated_at: 2026-10-24 00:38:25 +0400
subjects:
  governs: Tool/GET_EXECUTION_CONTEXT
  depends_on:
  - Tool
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Scope Unit
  - Implementation
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
  - Journal
relations:
  relates_to:
  - CA-O-114
  - CA-R-1810
tier: 3
---
# Summary

Load the selected execution context

## Scope

the GET_EXECUTION_CONTEXT capability for Tool/GET_EXECUTION_CONTEXT.

## Claim

the GET_EXECUTION_CONTEXT Tool **must** return the selected capability's exact current definition, implementation binding, input schema when supported, and relevant authority and operational context.

## Details

- implement the methodology Action CA-O-114-PROJECT_CONFIGURATION-ACTION--get-execution-context.
- accept a Tool name or Operations Atom ID and a context budget; return source-bound content, related Workflow Steps and Actions, applicable RMED, implementation and prompt references, and explicit context gaps.
- preserve the Operator's choice of what **to** execute; discovery, context retrieval, **and** observation provide capabilities.
- bounded **or** unavailable evidence **must** remain explicit **rather than** establish a successful assessment.
