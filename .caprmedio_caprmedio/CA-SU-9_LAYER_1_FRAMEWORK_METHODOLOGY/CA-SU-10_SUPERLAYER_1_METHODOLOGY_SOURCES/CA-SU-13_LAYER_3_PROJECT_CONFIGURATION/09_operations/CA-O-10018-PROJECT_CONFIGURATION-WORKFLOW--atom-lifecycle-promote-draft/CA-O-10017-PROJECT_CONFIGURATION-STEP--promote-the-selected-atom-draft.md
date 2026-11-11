---
identity:
  atom_id: CA-O-10017
  ref_id: CA-O-10017
context:
  container:
    atom: CA-O-10018
  role: Operations
  form: Step
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)/Step
    dependencies:
    - CAPRMEDIO_MODEL <+ Atom
    - CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
  tier: 3
relations:
  RUNS:
  - CA-O-10005
state:
  status: Active
  version: 1
  updated_at: 2026-11-11 14:05:36 +0400
destination:
  file:
    name: CA-O-10017-PROJECT_CONFIGURATION-STEP--promote-the-selected-atom-draft.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/CA-O-10018-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-promote-draft
---
## Summary

Promote the selected Atom Draft

## Claim scope

One exact non-container Draft binding within [Atom Lifecycle_Promote Draft](../CA-O-10018-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-promote-draft.md).

## Claim

### Kind

Execution.

### Inputs

Selected Draft, allowed Current `targetStatus`, optional `savedArchivedAtom`, and `projectContext`.

### Fixed parameters

None.

### Runs

The Action [Promote one Atom Draft](../CA-O-10005-PROJECT_CONFIGURATION-ACTION--promote-one-atom-draft.md).

### Outputs

The called Action's declared Outputs.
