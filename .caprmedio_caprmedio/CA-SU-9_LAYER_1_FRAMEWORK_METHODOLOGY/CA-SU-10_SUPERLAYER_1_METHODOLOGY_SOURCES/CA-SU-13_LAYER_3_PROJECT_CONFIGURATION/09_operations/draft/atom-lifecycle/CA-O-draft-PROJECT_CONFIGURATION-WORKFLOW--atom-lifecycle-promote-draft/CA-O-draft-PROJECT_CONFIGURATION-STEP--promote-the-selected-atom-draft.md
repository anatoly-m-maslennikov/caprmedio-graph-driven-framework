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

This Step operates on the one exact non-container Draft selected by its parent Workflow. It has no descendant selection, cascade, or earlier Step output.

## Claim

### Kind

Execution.

### Inputs

Selected Draft; applicable model; destination; explicit Current Status.

### Fixed parameters

None.

### Runs

The Action [Promote one Atom Draft](../CA-O-draft-PROJECT_CONFIGURATION-ACTION--promote-one-atom-draft.md) under [CA-R-2638](../../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2638-CORE_META_MODEL-DECLARATION--define-runs.md). Bind the inputs under [CA-R-2639](../../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2639-CORE_META_MODEL-RULE--bind-step-parameters.md).

### Outputs

The Action's published Current Atom and completed Draft removal, or its explicit error with completed results, passed unchanged.

