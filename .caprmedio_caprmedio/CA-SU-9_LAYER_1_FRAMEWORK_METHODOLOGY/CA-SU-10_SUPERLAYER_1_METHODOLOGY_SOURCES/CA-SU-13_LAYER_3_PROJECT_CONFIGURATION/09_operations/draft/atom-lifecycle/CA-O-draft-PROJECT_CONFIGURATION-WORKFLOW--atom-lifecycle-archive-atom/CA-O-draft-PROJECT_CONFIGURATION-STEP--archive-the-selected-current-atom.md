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

This Step is the single Step of [Atom Lifecycle_Archive Atom](../CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-archive-atom.md) and handles one exact selected non-container Current Atom. It does not admit Archived inputs, select descendants, or cascade.

## Claim

This Step belongs to [Atom Lifecycle_Archive Atom](../CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-archive-atom.md) and RUNS [Archive one Current Atom](../CA-O-draft-PROJECT_CONFIGURATION-ACTION--archive-one-current-atom.md) under [CA-R-2638](../../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2638-CORE_META_MODEL-DECLARATION--define-runs.md). Bind the exact Current source, applicable model, destination, and authorization under [CA-R-2639](../../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2639-CORE_META_MODEL-RULE--bind-step-parameters.md), then return the Action result unchanged.
