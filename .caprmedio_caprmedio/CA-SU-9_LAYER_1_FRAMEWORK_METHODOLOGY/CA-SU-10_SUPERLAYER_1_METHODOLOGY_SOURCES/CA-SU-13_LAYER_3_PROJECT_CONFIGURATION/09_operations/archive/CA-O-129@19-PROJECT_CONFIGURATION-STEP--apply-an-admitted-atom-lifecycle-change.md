---
atom_id: CA-O-129
ref_id: CA-O-129@19
container:
  scope_unit: CA-SU-13
role: Operations
form: Step
topics:
  main_subject: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Step Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Step Run.Agentic Step Execution Context
tier: 3
status: archived
version: 19
updated_at: 2026-10-27 19:59:46 +0400
carrier_destination:
  file:
    name: CA-O-129@19-PROJECT_CONFIGURATION-STEP--apply-an-admitted-atom-lifecycle-change.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/archive
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
---
# Summary

Apply an admitted Atom lifecycle change

## Operation

### Kind

Execution.

### Inputs

The requested lifecycle operation, selected Atom or new properties, supplied changes, applicable model and Project context. For Move bind one existing Atom, its source and destination scope; the Action derives the path and preserves identity and content meaning. For a containment cascade the caller supplies one selected target per invocation under CA-R-1521 and CA-D-461/CA-D-467.

### Fixed parameters

None.

### Runs

CA-O-128, Apply authorized Atom lifecycle changes.

### Outputs

The Action's result, including any request for additional input or explicit failure. This Step adds no semantic assessment, retry, rollback, recovery or repair.
