---
atom_id: CA-O-draft
role: Operations
form: Step
status: Draft
version: 1
updated_at: '2026-11-03 19:01:50 +0400'
tier: 3
subjects:
  active: 'CAPRMEDIO_MODEL <+ Atom/(.Role := Operations)/Step'
  passive:
    - 'CAPRMEDIO_MODEL <+ Atom'
    - 'CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION'
relations: {}
---
## Summary

Apply the requested Direct Atom Update

## Claim scope

One bound non-container Atom within [Atom Lifecycle_Update Atom Directly](../CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-update-atom-directly.md).

## Claim

### Kind

Execution.

### Inputs

Selected Atom; requested changes; `projectContext`; and any existing expected-source binding.

### Fixed parameters

None.

### Runs

The Action [Apply one Direct Atom Update](../CA-O-draft-PROJECT_CONFIGURATION-ACTION--apply-one-direct-atom-update.md).

### Outputs

The called Action's declared Outputs.
