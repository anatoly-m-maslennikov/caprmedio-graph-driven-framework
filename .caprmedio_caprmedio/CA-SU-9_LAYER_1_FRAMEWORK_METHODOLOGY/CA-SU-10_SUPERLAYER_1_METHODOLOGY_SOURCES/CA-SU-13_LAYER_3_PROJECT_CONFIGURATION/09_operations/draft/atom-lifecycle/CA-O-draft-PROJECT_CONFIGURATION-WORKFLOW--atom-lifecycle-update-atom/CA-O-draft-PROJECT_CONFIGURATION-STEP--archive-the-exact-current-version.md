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

Archive the exact Current Version

## Claim scope

One bound exact Current source within [Atom Lifecycle_Update Atom](../CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-update-atom.md).

## Claim

### Kind

Execution.

### Inputs

Bind the original `sourceCurrent`, internal `expectedSource`, and `projectContext` to the called Workflow. `targetStatus` remains enclosing-Workflow context.

### Fixed parameters

None.

### Runs

The Workflow [Atom Lifecycle_Archive Atom](../CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-archive-atom.md).

### Outputs

The called Workflow's declared Output.
