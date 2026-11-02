---
atom_id: CA-E-530
content_role: Evaluation
type: Eval Case
current_scope_unit: WATCH_EXECUTION
status: Active
author: Anatoly Maslennikov
version: 9
updated_at: 2026-10-27 19:59:37 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control
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

Verify WATCH_EXECUTION

## Scope

the WATCH_EXECUTION capability for Tool/WATCH_EXECUTION.

## Claim

the Evaluation **must** check the WATCH_EXECUTION Tool against its declared result **and** Carrier contract using an end-to-end mock Project.

## Details

- exercise completion, failure, interruption, reconnect replay, cursor validation and Run correlation, timeout, recording acknowledgements, and nonblocking concurrent callers.
- compare complete expected results with actual results; successful counts alone do **not** establish correctness.
- invoke the real MCP transport for the exposed schema **and** result boundary.
- retain existing RMED Atoms Base Revise behavior, including its initial evidence **and** absence of a saved-output recheck.
