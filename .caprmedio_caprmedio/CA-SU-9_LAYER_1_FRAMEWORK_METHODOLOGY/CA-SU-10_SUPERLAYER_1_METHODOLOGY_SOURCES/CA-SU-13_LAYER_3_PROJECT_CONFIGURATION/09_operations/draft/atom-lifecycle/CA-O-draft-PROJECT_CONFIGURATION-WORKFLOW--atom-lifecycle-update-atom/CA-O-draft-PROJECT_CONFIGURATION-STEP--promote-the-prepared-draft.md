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

Promote the prepared Draft

## Claim scope

Terminal Step of [Atom Lifecycle_Update Atom](../CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-update-atom.md) for one prepared non-container Draft.

## Claim

This Step RUNS [Atom Lifecycle_Promote Draft](../CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-promote-draft.md) under [CA-R-2638](../../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2638-CORE_META_MODEL-DECLARATION--define-runs.md). Bind the prepared Draft, `targetID` and `targetVersion` from Step 1, placement, and the enclosing Workflow's captured `targetStatus` under [CA-R-2639](../../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2639-CORE_META_MODEL-RULE--bind-step-parameters.md). After archival succeeds, promote using exactly that `targetID`, `targetVersion`, and `targetStatus`; do not rederive identity or Status. Return the readback-verified publication, mapping, diagnostics, and completed partial outputs, verifying that saved Status equals `targetStatus`. On failure return an explicit error and completed outputs without retry, replay, repair, or rollback.
