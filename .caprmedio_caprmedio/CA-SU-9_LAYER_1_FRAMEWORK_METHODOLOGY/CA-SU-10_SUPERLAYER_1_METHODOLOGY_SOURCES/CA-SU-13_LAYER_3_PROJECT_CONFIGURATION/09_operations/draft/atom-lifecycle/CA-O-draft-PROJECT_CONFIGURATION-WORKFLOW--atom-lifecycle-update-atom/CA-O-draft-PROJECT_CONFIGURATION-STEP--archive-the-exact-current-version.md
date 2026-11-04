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

Archive the exact Current Version

## Claim scope

Second Step of [Atom Lifecycle_Update Atom](../CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-update-atom.md) for one non-container Current source.

## Claim

This Step RUNS [Atom Lifecycle_Archive Atom](../CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-archive-atom.md) under [CA-R-2638](../../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2638-CORE_META_MODEL-DECLARATION--define-runs.md). Bind the exact `sourceCurrent`, ordinary model/placement/authorization context and optional known `targetID`; retain the prepared Draft, `targetVersion` and `targetStatus` in the enclosing Workflow context under [CA-R-2639](../../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2639-CORE_META_MODEL-RULE--bind-step-parameters.md). Archive that exact Current after Step 1 succeeds; the Archived carrier's Status does not replace `targetStatus`. Return the verified archival result with the prepared context unchanged; archival preserves Version and Updated At and creates no N+1. On failure return an explicit error and completed outputs without retry, replay, repair, or rollback.
