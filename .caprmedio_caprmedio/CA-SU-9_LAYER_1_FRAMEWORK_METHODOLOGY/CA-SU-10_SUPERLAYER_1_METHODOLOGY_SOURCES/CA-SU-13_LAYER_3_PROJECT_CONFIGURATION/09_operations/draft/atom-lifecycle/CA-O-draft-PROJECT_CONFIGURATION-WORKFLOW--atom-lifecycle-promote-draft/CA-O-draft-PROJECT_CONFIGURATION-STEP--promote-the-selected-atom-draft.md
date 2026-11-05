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

Promote the selected Atom Draft

## Claim scope

One exact non-container Draft binding within [Atom Lifecycle_Promote Draft](../CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-promote-draft.md).

## Claim

### Kind

Execution.

### Inputs

Selected Draft, `targetStatus`, and `projectContext`.

### Fixed parameters

None.

### Runs

The Action [Promote one Atom Draft](../CA-O-draft-PROJECT_CONFIGURATION-ACTION--promote-one-atom-draft.md).

### Outputs

The called Action's declared Outputs.
