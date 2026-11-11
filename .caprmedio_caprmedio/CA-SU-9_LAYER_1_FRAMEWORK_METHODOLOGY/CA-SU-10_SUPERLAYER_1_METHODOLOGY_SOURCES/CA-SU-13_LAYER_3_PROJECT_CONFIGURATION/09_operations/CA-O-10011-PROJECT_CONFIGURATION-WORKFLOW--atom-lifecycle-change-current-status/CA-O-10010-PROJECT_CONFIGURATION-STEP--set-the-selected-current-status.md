---
identity:
  atom_id: CA-O-10010
  ref_id: CA-O-10010
context:
  container:
    atom: CA-O-10011
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
  - CA-O-10007
state:
  status: Active
  version: 1
  updated_at: 2026-11-11 14:05:36 +0400
destination:
  file:
    name: CA-O-10010-PROJECT_CONFIGURATION-STEP--set-the-selected-current-status.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/CA-O-10011-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-change-current-status
---
## Summary

Set the selected Current Status

## Claim scope

One Current-Status binding within [Atom Lifecycle_Change Current Status](../CA-O-10011-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-change-current-status.md).

## Claim

### Kind

Execution.

### Inputs

Selected Atom, requested `targetStatus`, and `projectContext`.

### Fixed parameters

None.

### Runs

The Action [Set one Current Atom Status](../CA-O-10007-PROJECT_CONFIGURATION-ACTION--set-one-current-atom-status.md).

### Outputs

The called Action's declared Outputs.
