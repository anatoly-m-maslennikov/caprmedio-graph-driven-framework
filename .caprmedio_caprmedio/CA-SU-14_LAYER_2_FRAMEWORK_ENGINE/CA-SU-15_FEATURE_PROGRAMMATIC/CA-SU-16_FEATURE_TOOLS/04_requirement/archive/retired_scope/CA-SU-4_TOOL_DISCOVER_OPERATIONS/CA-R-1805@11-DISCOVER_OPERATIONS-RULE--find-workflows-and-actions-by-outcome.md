---
atom_id: CA-R-1805
ref_id: CA-R-1805
container:
  scope_unit: CA-SU-16
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Source
    Selection
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
tier: 3
status: Archived
version: 11
updated_at: 2026-10-27 20:00:03 +0400
carrier_destination:
  file:
    name: CA-R-1805@11-DISCOVER_OPERATIONS-RULE--find-workflows-and-actions-by-outcome.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/04_requirement/archive/retired_scope/CA-SU-4_TOOL_DISCOVER_OPERATIONS
current_scope_unit: TOOLS
author: Anatoly Maslennikov
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
