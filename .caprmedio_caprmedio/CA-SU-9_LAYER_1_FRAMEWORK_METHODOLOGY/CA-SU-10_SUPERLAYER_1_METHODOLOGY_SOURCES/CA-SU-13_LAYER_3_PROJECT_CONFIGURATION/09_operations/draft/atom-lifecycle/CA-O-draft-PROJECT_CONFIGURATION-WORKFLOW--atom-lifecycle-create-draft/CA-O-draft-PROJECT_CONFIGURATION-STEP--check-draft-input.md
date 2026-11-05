---
atom_id: CA-O-draft
role: Operations
form: Step
status: Draft
version: 1
updated_at: '2026-11-05 18:54:16 +0400'
tier: 3
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Role := Operations)/Step
  passive:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
relations: {}
---
## Summary

Check Draft input

## Claim scope

One accumulated Draft request from [Atom Lifecycle_Create Draft](../CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-create-draft.md).

## Claim

### Kind

Decision.

### Inputs

Accumulated `parameters` and `projectContext`.

### Fixed parameters

None.

### Runs

The Action [Check Draft input formats and allowed values](../CA-O-draft-PROJECT_CONFIGURATION-ACTION--check-draft-input-formats-and-allowed-values.md).

### Outputs

`parameters`, `requested_input`, and warnings returned by the called Action.
