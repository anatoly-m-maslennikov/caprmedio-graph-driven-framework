---
atom_id: CA-E-530
ref_id: CA-E-530
container:
  scope_unit: CA-SU-8
role: Evaluation
form: Eval Case
topics:
  main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control"
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
tier: 3
status: Active
version: 9
updated_at: 2026-10-27 19:59:37 +0400
carrier_destination:
  file:
    name: CA-E-530-WATCH_EXECUTION-EVAL_CASE--verify-watch-execution.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/CA-SU-8_TOOL_WATCH_EXECUTION/06_evaluation
current_scope_unit: WATCH_EXECUTION
author: Anatoly Maslennikov
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
