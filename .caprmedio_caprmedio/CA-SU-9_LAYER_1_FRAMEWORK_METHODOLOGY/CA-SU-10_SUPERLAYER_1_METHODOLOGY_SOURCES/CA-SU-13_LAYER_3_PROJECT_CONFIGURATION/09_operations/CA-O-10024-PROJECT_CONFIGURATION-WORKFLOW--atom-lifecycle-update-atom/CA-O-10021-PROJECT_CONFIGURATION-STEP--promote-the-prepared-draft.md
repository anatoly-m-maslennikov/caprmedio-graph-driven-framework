---
identity:
  atom_id: CA-O-10021
  ref_id: CA-O-10021
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
  - CA-O-10018
state:
  status: Active
  version: 1
  updated_at: 2026-11-11 14:05:36 +0400
destination:
  file:
    name: CA-O-10021-PROJECT_CONFIGURATION-STEP--promote-the-prepared-draft.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/CA-O-10024-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-update-atom
---
## Summary

Promote the prepared Draft

## Claim scope

One bound prepared Draft within [Atom Lifecycle_Update Atom](../CA-O-10024-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-update-atom.md).

## Claim

### Kind

Execution.

### Inputs

Bind `savedDraft`, captured `targetStatus`, `savedArchivedAtom`, and `projectContext` to the called Workflow. The called Workflow skips the target already archived by this Update.

### Fixed parameters

None.

### Runs

The Workflow [Atom Lifecycle_Promote Draft](../CA-O-10018-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-promote-draft.md).

### Outputs

The called Workflow's declared Output.
