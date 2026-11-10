---
atom_id: CA-O-draft
role: Operations
form: Step
status: Draft
version: 1
updated_at: '2026-11-03 18:54:48 +0400'
tier: 3
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Role := Operations)/Step
  passive:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
relations: {}
---
## Summary

Create the requested Atom Draft

## Claim scope

One non-container Draft request passed by [Atom Lifecycle_Create Draft](../CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-create-draft.md).

## Claim

### Kind

Execution.

### Inputs

Validated `parameters`, warnings, `projectContext`.

### Fixed parameters

None.

### Runs

The Action [Create one Atom Draft](../CA-O-draft-PROJECT_CONFIGURATION-ACTION--create-one-atom-draft.md).

### Outputs

The called Action's declared Outputs.
