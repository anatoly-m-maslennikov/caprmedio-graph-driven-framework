---
atom_id: CA-O-draft
role: Operations
form: Step
status: Draft
version: 1
updated_at: '2026-11-03 18:54:48 +0400'
tier: 3
subjects:
  active: 'CAPRMEDIO_MODEL <+ Atom/(.Role := Operations)/Step'
  passive:
    - 'CAPRMEDIO_MODEL <+ Atom'
    - 'CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION'
relations: {}
---
## Summary

Set the selected Current Status

## Claim scope

One Current-Status binding within [Atom Lifecycle_Change Current Status](../CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-change-current-status.md).

## Claim

### Kind

Execution.

### Inputs

Selected Atom, requested `targetStatus`, and `projectContext`.

### Fixed parameters

None.

### Runs

The Action [Set one Current Atom Status](../CA-O-draft-PROJECT_CONFIGURATION-ACTION--set-one-current-atom-status.md).

### Outputs

The called Action's declared Outputs.
