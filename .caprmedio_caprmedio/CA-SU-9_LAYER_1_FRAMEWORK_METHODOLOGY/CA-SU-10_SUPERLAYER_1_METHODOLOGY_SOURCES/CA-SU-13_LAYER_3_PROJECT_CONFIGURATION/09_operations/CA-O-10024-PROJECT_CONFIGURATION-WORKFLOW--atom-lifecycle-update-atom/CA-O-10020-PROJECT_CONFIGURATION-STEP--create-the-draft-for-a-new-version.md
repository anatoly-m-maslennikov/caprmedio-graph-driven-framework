---
identity:
  atom_id: CA-O-10020
  ref_id: CA-O-10020
context:
  container:
    atom: CA-O-10024
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
  - CA-O-10016
state:
  status: Active
  version: 1
  updated_at: 2026-11-11 14:05:36 +0400
destination:
  file:
    name: CA-O-10020-PROJECT_CONFIGURATION-STEP--create-the-draft-for-a-new-version.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/CA-O-10024-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-update-atom
---
## Summary

Create the Draft for a new Version

## Claim scope

One bound Current-backed proposal within [Atom Lifecycle_Update Atom](../CA-O-10024-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-update-atom.md).

## Claim

### Kind

Execution.

### Inputs

Bind `sourceCurrent`, requested changes, `projectContext` to the called Workflow. Keep `targetStatus` in the enclosing Workflow context.

### Fixed parameters

None.

### Runs

The Workflow [Atom Lifecycle_Create Draft](../CA-O-10016-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-create-draft.md).

### Outputs

The called Workflow's declared Output.
