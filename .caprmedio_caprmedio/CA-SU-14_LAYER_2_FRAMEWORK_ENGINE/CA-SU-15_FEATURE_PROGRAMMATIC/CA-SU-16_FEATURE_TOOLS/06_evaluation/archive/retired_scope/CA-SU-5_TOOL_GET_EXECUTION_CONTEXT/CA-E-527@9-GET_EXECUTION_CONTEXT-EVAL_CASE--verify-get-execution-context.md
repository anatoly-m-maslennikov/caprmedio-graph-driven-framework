---
atom_id: CA-E-527
ref_id: CA-E-527
container:
  scope_unit: CA-SU-16
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Quality/Verification/Dynamic
    Testing
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
version: 9
updated_at: 2026-10-27 19:59:36 +0400
carrier_destination:
  file:
    name: CA-E-527@9-GET_EXECUTION_CONTEXT-EVAL_CASE--verify-get-execution-context.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/06_evaluation/archive/retired_scope/CA-SU-5_TOOL_GET_EXECUTION_CONTEXT
current_scope_unit: TOOLS
author: Anatoly Maslennikov
---
# Summary

Verify GET_EXECUTION_CONTEXT

## Scope

the GET_EXECUTION_CONTEXT capability for Tool/GET_EXECUTION_CONTEXT.

## Claim

the Evaluation **must** check the GET_EXECUTION_CONTEXT Tool against its declared result **and** Carrier contract using an end-to-end mock Project.

## Details

- exercise exact resolution, unknown or ambiguous identifiers, Workflow Step context, prompt freshness, unrelated-content exclusion, and incomplete-context reporting at the byte budget.
- compare complete expected results with actual results; successful counts alone do **not** establish correctness.
- invoke the real MCP transport for the exposed schema **and** result boundary.
- retain existing RMED Atoms Base Revise behavior, including its initial evidence **and** absence of a saved-output recheck.
