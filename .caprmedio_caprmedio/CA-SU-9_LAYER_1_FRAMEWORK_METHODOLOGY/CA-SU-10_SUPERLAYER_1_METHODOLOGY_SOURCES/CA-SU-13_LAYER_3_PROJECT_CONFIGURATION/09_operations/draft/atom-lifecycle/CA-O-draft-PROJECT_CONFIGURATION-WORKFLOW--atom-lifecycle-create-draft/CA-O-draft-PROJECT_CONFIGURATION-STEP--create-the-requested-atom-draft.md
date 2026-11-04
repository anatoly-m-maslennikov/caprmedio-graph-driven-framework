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

This Step [RUNS](../../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2638-CORE_META_MODEL-DECLARATION--define-runs.md) exactly [Create one Atom Draft](../CA-O-draft-PROJECT_CONFIGURATION-ACTION--create-one-atom-draft.md). Under [CA-R-2639](../../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2639-CORE_META_MODEL-RULE--bind-step-parameters.md), bind either `newAtom` properties or one exact `sourceCurrent` selector with changed properties, plus Draft destination, model and permissions. Pass the Action's result unchanged.

