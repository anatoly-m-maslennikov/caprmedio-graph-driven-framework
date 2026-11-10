---
atom_id: CA-E-526@7
content_role: Evaluation
type: Eval Case
current_scope_unit: DISCOVER_OPERATIONS
status: Archived
author: Anatoly Maslennikov
version: 7
updated_at: 2026-10-26 05:59:45 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Aspect/Verification/Dynamic Testing
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - Subject/Graph Node/Domain/Occurrent/Execution
  - Subject/Graph Node/Domain/Continuant/History/Journal
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
