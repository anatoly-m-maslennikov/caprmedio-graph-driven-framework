---
identity:
  atom_id: CA-O-10013
  ref_id: CA-O-10013
context:
  container:
    atom: CA-O-10016
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
  - CA-O-10003
state:
  status: Active
  version: 1
  updated_at: 2026-11-11 14:05:36 +0400
destination:
  file:
    name: CA-O-10013-PROJECT_CONFIGURATION-STEP--create-the-requested-atom-draft.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/CA-O-10016-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-create-draft
---
## Summary

Create the requested Atom Draft

## Claim scope

One non-container Draft request passed by [Atom Lifecycle_Create Draft](../CA-O-10016-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-create-draft.md).

## Claim

### Kind

Execution.

### Inputs

Validated `parameters`, warnings, `projectContext`.

### Fixed parameters

None.

### Runs

The Action [Create one Atom Draft](../CA-O-10003-PROJECT_CONFIGURATION-ACTION--create-one-atom-draft.md).

### Outputs

The called Action's declared Outputs.
