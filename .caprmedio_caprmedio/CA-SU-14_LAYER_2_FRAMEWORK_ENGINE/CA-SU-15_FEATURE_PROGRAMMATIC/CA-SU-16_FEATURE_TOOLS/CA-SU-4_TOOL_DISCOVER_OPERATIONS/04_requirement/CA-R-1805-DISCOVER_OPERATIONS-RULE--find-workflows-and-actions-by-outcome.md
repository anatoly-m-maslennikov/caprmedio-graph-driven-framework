---
atom_id: CA-R-1805
content_role: Requirement
current_scope_unit: DISCOVER_OPERATIONS
status: Active
author: Anatoly Maslennikov
version: 11
updated_at: 2026-10-27 20:00:03 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Source Selection
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

Find Workflows and Actions by outcome

## Scope

the DISCOVER_OPERATIONS capability for Tool/DISCOVER_OPERATIONS.

## Claim

the DISCOVER_OPERATIONS Tool **must** return a ranked, bounded selection of active Workflow and Action definitions matching the requested outcome and filters.

## Details

- implement the methodology Action CA-O-113-PROJECT_CONFIGURATION-ACTION--find-workflows-and-actions-by-outcome.
- accept a query, Workflow or Action kind, Scope Unit and execution-kind filters, offset, and result limit; return summaries, definition bindings, and implementation availability.
- preserve the Operator's choice of what **to** execute; discovery, context retrieval, **and** observation provide capabilities.
- bounded **or** unavailable evidence **must** remain explicit **rather than** establish a successful assessment.
