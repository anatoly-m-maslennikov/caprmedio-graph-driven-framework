---
identity:
  atom_id: CA-O-10012
  ref_id: CA-O-10012
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
  - CA-O-10002
state:
  status: Active
  version: 1
  updated_at: 2026-11-11 14:05:36 +0400
destination:
  file:
    name: CA-O-10012-PROJECT_CONFIGURATION-STEP--check-draft-input.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/CA-O-10016-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-create-draft
---
## Summary

Check Draft input

## Claim scope

One accumulated Draft request from [Atom Lifecycle_Create Draft](../CA-O-10016-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-create-draft.md).

## Claim

### Kind

Decision.

### Inputs

Accumulated `parameters` and `projectContext`.

### Fixed parameters

None.

### Runs

The Action [Check Draft input formats and allowed values](../CA-O-10002-PROJECT_CONFIGURATION-ACTION--check-draft-input-formats-and-allowed-values.md).

### Outputs

`parameters`, `requested_input`, and warnings returned by the called Action.
