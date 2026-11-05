---
atom_id: CA-E-529
ref_id: CA-E-529
role: Evaluation
form: Eval Case
current_scope_unit: RESUME_EXECUTION_CONTEXT
status: Active
author: Anatoly Maslennikov
version: 9
updated_at: 2026-10-27 19:59:36 +0400
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Recovery
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
tier: 3
container:
  scope_unit: CA-SU-7
carrier_destination:
  file:
    name: CA-E-529-RESUME_EXECUTION_CONTEXT-EVAL_CASE--verify-resume-execution-context.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/CA-SU-7_TOOL_RESUME_EXECUTION_CONTEXT/06_evaluation
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
