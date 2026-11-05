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

Read Workflow input

## Claim scope

One root or nested invocation of [Atom Lifecycle_Create Draft](../CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-create-draft.md) and its input dictionary.

## Claim

### Kind

Input.

### Inputs

The invocation dictionary declared by the called Action; `projectContext`; the bound Workflow Run and request.

### Fixed parameters

None.

### Runs

The Action [Read Workflow intake input](../CA-O-draft-PROJECT_CONFIGURATION-ACTION--read-workflow-intake-input.md).

### Outputs

Bind the returned invocation dictionary to `parameters`.
