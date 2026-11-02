---
atom_id: CA-E-526
content_role: Evaluation
type: Eval Case
current_scope_unit: DISCOVER_OPERATIONS
status: Active
author: Anatoly Maslennikov
version: 9
updated_at: 2026-10-27 19:59:36 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification/Dynamic Testing
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
relations: {}
tier: 3
---
# Summary

Verify DISCOVER_OPERATIONS

## Scope

the DISCOVER_OPERATIONS capability for Tool/DISCOVER_OPERATIONS.

## Claim

the Evaluation **must** check the DISCOVER_OPERATIONS Tool against its declared result **and** Carrier contract using an end-to-end mock Project.

## Details

- exercise Workflow and Action separation, Agentic or Programmatic filters, inactive definitions, duplicate identifiers, no results, and declared but unavailable implementations.
- compare complete expected results with actual results; successful counts alone do **not** establish correctness.
- invoke the real MCP transport for the exposed schema **and** result boundary.
- retain existing RMED Atoms Base Revise behavior, including its initial evidence **and** absence of a saved-output recheck.
