---
identity:
  atom_id: CA-O-10019
  ref_id: CA-O-10019
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
  - CA-O-10009
state:
  status: Active
  version: 1
  updated_at: 2026-11-11 14:05:36 +0400
destination:
  file:
    name: CA-O-10019-PROJECT_CONFIGURATION-STEP--archive-the-exact-current-version.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/CA-O-10024-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-update-atom
---
## Summary

Archive the exact Current Version

## Claim scope

One bound exact Current source within [Atom Lifecycle_Update Atom](../CA-O-10024-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-update-atom.md).

## Claim

### Kind

Execution.

### Inputs

Bind the original `sourceCurrent`, `projectContext` to the called Workflow. `targetStatus` remains enclosing-Workflow context.

### Fixed parameters

None.

### Runs

The Workflow [Atom Lifecycle_Archive Atom](../CA-O-10009-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-archive-atom.md).

### Outputs

The called Workflow's declared Output.
