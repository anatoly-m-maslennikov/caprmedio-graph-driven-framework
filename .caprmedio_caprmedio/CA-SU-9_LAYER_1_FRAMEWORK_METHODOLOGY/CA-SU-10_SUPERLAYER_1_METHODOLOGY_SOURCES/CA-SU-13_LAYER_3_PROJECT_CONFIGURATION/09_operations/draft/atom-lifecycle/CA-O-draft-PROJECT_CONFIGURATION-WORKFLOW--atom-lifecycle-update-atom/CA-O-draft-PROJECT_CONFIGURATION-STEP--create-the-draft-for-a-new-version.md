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

Create the Draft for a new Version

## Claim scope

Entry Step of [Atom Lifecycle_Update Atom](../CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-update-atom.md) for one non-container Current-backed proposal.

## Claim

This Step RUNS [Atom Lifecycle_Create Draft](../CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-create-draft.md) under [CA-R-2638](../../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2638-CORE_META_MODEL-DECLARATION--define-runs.md). Bind the required `sourceCurrent` with the requested property changes, Draft destination, applicable model, and authorization under [CA-R-2639](../../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2639-CORE_META_MODEL-RULE--bind-step-parameters.md). Forward changes without requiring unchanged source properties again. Forward the enclosing Workflow's captured `targetStatus`; the created Draft's Status does not replace it. Return the prepared Draft, called Workflow's `targetID` and `targetVersion`, `targetStatus`, diagnostics, and completed partial outputs after readback. This Step owns no algorithm or ID allocation; on failure return an explicit error and completed outputs without retry, replay, repair, or rollback.
