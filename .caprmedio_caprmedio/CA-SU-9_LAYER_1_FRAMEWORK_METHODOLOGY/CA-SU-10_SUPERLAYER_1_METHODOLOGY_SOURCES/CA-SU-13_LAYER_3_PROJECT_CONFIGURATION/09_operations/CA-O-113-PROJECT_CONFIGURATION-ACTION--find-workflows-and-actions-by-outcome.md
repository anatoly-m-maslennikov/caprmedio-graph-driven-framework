---
atom_id: CA-O-113
ref_id: CA-O-113
container:
  scope_unit: CA-SU-13
role: Operations
form: Action
topics:
  main_subject: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  dependencies:
  - "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Source Selection"
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
tier: 3
relations:
  depends_on:
  - CA-D-513
status: Active
version: 13
updated_at: 2026-10-27 19:59:46 +0400
carrier_destination:
  file:
    name: CA-O-113-PROJECT_CONFIGURATION-ACTION--find-workflows-and-actions-by-outcome.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations
current_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
---
# Summary

Find Workflows and Actions by outcome

## Operation

Workflow and Action discovery **means** the Programmatic Action implementing the following responsibility:

- search carried Operations Type, Summary, Operation, Scope Unit, and declared implementation bindings; report unknown execution kind explicitly.
- accept the declared inputs **and** return the declared results under CA-D-513-DISCOVER_OPERATIONS-ENG_DECISION--encode-discover-operations-tool-binding.
- report missing **or** ambiguous evidence as an explicit result.
- execution requires an Operator-authorized invocation; discovery **or** observation grants no mutation authority.

## Details

this Action provides the responsibility named by its Summary. a Workflow **may** invoke the Action through a Step. a direct call **may** use the same Action **without** creating a Workflow Run. observation preserves the original Run **and** evidence.
