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

The sole Step of [Atom Lifecycle_Update Atom Directly](../CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-update-atom-directly.md), for one non-container Atom.

## Claim

### Kind

Execution.

### Inputs

Exact non-container target; requested changes; applicable model; Scope Unit; expected source/currentness; placement; authorization.

### Fixed parameters

None.

### Runs

The Action [Apply one Direct Atom Update](../CA-O-draft-PROJECT_CONFIGURATION-ACTION--apply-one-direct-atom-update.md) under [CA-R-2638](../../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2638-CORE_META_MODEL-DECLARATION--define-runs.md). Bind the inputs under [CA-R-2639](../../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2639-CORE_META_MODEL-RULE--bind-step-parameters.md).

### Outputs

The Action's saved Atom or its explicit error with completed results, passed unchanged.
