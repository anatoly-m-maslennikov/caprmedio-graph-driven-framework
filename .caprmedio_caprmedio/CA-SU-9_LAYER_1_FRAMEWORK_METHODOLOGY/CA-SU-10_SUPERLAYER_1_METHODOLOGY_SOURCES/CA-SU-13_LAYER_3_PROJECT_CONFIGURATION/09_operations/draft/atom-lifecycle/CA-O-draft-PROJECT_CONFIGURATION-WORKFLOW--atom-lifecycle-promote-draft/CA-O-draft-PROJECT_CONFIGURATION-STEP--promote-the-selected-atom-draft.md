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

This Step belongs to [Atom Lifecycle_Promote Draft](../CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-promote-draft.md) and RUNS exactly [Promote one Atom Draft](../CA-O-draft-PROJECT_CONFIGURATION-ACTION--promote-one-atom-draft.md) under [CA-R-2638](../../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2638-CORE_META_MODEL-DECLARATION--define-runs.md).

**Preconditions:** Bind the exact Draft, applicable model, explicit Current Status, destination, resolved `targetID`, and `targetVersion` from Workflow inputs under [CA-R-2639](../../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2639-CORE_META_MODEL-RULE--bind-step-parameters.md). In a composed Update, bind the prepared identity/version and original Current Status captured before archival; do not use a Draft/Archived Status, `Active` fallback, or archive receipt as a gate. **Intended effect:** pass these bindings to the Action exactly once; the Action reads the Draft and owns content/mandatory-field validation.

**Returned evidence:** Return the Action's saved, readback-verified publication and Draft removal, explicit error, or partial completed outputs unchanged. This Step adds no archive, ID inference, second Action, retry, replay, repair, or rollback.

