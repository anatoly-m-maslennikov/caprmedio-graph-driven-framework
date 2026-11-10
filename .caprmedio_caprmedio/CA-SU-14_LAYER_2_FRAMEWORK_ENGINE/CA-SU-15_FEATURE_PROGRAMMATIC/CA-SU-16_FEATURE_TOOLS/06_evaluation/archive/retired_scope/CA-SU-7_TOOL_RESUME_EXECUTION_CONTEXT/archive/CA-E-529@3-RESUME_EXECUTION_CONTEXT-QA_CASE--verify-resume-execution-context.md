---
atom_id: CA-E-529@3
content_role: Evaluation
type: Eval Case
current_scope_unit: RESUME_EXECUTION_CONTEXT
status: Archived
author: Anatoly Maslennikov
version: 3
updated_at: 2026-10-24 00:38:25 +0400
subjects:
  governs: Subject/Engineering/Programmatic Action/Execution Continuation Context Adapter
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Domain/Node/Occurrent/Execution
  - Subject/Domain/Node/Continuant/History/Journal
relations:
  relates_to:
  - CA-R-1808
  - CA-D-516
tier: 3
---
# Summary

Verify RESUME_EXECUTION_CONTEXT

## Scope

the RESUME_EXECUTION_CONTEXT capability for Tool/RESUME_EXECUTION_CONTEXT.

## Claim

the Evaluation **must** check the RESUME_EXECUTION_CONTEXT Tool against its declared result **and** Carrier contract using an end-to-end mock Project.

## Details

- exercise unfinished check continuation, pending repairs, terminal Runs, stale sources or criteria, retained handoffs, and completed-work exclusion.
- compare complete expected results with actual results; successful counts alone do **not** establish correctness.
- invoke the real MCP transport for the exposed schema **and** result boundary.
- retain existing RMED Atoms Base Revise behavior, including its initial evidence **and** absence of a saved-output recheck.
