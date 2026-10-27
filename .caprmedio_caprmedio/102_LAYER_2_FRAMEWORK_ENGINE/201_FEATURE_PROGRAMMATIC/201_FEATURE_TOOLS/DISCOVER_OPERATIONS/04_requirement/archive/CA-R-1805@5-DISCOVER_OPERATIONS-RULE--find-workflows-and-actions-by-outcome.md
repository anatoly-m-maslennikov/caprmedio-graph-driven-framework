---
atom_id: CA-R-1805@5
content_role: Requirement
current_scope_unit: DISCOVER_OPERATIONS
status: Archived
author: Anatoly Maslennikov
version: 5
updated_at: 2026-10-24 13:39:34 +0400
subjects:
  governs: Subject/Engineering/Programmatic Action/Workflow and Action Discovery Adapter
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Domain/Node/Occurrent/Execution
  - Subject/Domain/Node/Continuant/History/Journal
relations:
  relates_to:
  - CA-O-113
  - CA-R-1810
type: Rule
tier: 3
---
# Summary

Find Workflows and Actions by outcome

## Scope

the DISCOVER_OPERATIONS capability for Tool/DISCOVER_OPERATIONS.

## Claim

the DISCOVER_OPERATIONS Tool **must** return a ranked, bounded selection of active Workflow and Action definitions matching the requested outcome and filters.

## Details

- implement the methodology Action CA-O-113-PROJECT_CONFIGURATION-ACTION--discover-operations.
- accept a query, Workflow or Action kind, Scope Unit and execution-kind filters, offset, and result limit; return summaries, definition bindings, and implementation availability.
- preserve the Operator's choice of what **to** execute; discovery, context retrieval, **and** observation provide capabilities.
- bounded **or** unavailable evidence **must** remain explicit **rather than** establish a successful assessment.
