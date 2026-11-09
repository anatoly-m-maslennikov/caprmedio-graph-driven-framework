---
atom_id: CA-R-1806
ref_id: CA-R-1806
container:
  scope_unit: CA-SU-5
role: Requirement
form: Rule
topics:
  main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control"
  dependencies:
  - "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Source Retrieval"
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
tier: 3
status: Active
version: 14
updated_at: 2026-10-27 20:00:03 +0400
carrier_destination:
  file:
    name: CA-R-1806-GET_EXECUTION_CONTEXT-RULE--load-the-selected-execution-context.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/CA-SU-5_TOOL_GET_EXECUTION_CONTEXT/04_requirement
current_scope_unit: GET_EXECUTION_CONTEXT
author: Anatoly Maslennikov
---
# Summary

Load the selected execution context

## Scope

the GET_EXECUTION_CONTEXT capability for Tool/GET_EXECUTION_CONTEXT.

## Claim

the GET_EXECUTION_CONTEXT Tool **must** return the selected capability's exact current definition, implementation binding, input schema when supported, and relevant authority and operational context.

## Details

- implement the methodology Action CA-O-114-PROJECT_CONFIGURATION-ACTION--load-the-selected-execution-context.
- accept a Tool name or Operations Atom ID and a context budget; return source-bound content, related Workflow Steps and Actions, applicable RMED, implementation and prompt references, and explicit context gaps.
- preserve the Operator's choice of what **to** execute; discovery, context retrieval, **and** observation provide capabilities.
- bounded **or** unavailable evidence **must** remain explicit **rather than** establish a successful assessment.
