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

Archive the selected Current Atom

## Claim scope

One exact non-container Current Atom binding within [Atom Lifecycle_Archive Atom](../CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-archive-atom.md).

## Claim

### Kind

Execution.

### Inputs

Selected source, `projectContext`, and any internal `expectedSource`.

### Fixed parameters

None.

### Runs

The Action [Archive one Current Atom](../CA-O-draft-PROJECT_CONFIGURATION-ACTION--archive-one-current-atom.md).

### Outputs

The called Action's declared Outputs.
