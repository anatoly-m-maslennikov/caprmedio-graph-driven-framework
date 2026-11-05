---
atom_id: CA-O-114
ref_id: CA-O-114
role: Operations
form: Action
current_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
version: 13
updated_at: 2026-10-27 19:59:46 +0400
topics:
  main_subject: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Source Retrieval
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
relations:
  depends_on:
  - CA-D-514
tier: 3
container:
  scope_unit: CA-SU-13
carrier_destination:
  file:
    name: CA-O-114-PROJECT_CONFIGURATION-ACTION--load-the-selected-execution-context.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations
---
# Summary

Load the selected execution context

## Operation

Execution context retrieval **means** the Programmatic Action implementing the following responsibility:

- resolve exact identifiers; load the selected definition and directly related Step or Action definitions, relevant bound prompts, and applicable RMED from declared Scope Unit ancestry.
- accept the declared inputs **and** return the declared results under CA-D-514-GET_EXECUTION_CONTEXT-ENG_DECISION--encode-get-execution-context-tool-binding.
- report missing **or** ambiguous evidence as an explicit result.
- execution requires an Operator-authorized invocation; discovery **or** observation grants no mutation authority.

## Details

this Action provides the responsibility named by its Summary. a Workflow **may** invoke the Action through a Step. a direct call **may** use the same Action **without** creating a Workflow Run. observation preserves the original Run **and** evidence.
