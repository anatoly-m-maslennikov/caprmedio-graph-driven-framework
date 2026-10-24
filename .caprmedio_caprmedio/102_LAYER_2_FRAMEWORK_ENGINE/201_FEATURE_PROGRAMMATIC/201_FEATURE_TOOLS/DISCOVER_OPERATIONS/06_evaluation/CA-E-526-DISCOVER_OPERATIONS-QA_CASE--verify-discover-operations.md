---
atom_id: CA-E-526
content_role: Evaluation
type: Eval Case
current_scope_unit: DISCOVER_OPERATIONS
status: Active
author: Anatoly Maslennikov
version: 3
updated_at: 2026-10-24 00:38:25 +0400
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
  - CA-R-1805
  - CA-D-513
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
