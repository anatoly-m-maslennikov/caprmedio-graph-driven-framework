---
atom_id: CA-O-draft
role: Operations
form: Workflow
status: Draft
version: 1
updated_at: '2026-11-03 19:01:50 +0400'
tier: 3
subjects:
  active: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Workflow/(.Purpose := Runtime)'
  passive:
    - 'CAPRMEDIO_MODEL <+ Atom'
    - 'CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION'
relations: {}
---

```mermaid
flowchart TD
    %% Entry: step1. Success terminal: step1. Failure at any Step is terminal.
    step1["Apply the requested Direct Atom Update<br/>Success: saved Atom<br/>Failure: stop with error and completed outputs"]
    click step1 "./CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-update-atom-directly/CA-O-draft-PROJECT_CONFIGURATION-STEP--apply-the-requested-direct-atom-update.md" "Open Step"
```

## Summary

Atom Lifecycle_Update Atom Directly

## Claim scope

One exactly selected non-container Atom: a Draft for semantic in-place editing, or a Current/Archived carrier for technical in-place editing.

## Claim

This Workflow's Purpose is Runtime.

Accept one exact target and requested changes, derive the Draft, Current, or Archived case from Status and its model, then run [Apply the requested Direct Atom Update](CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-update-atom-directly/CA-O-draft-PROJECT_CONFIGURATION-STEP--apply-the-requested-direct-atom-update.md) once. Return the saved result or an explicit error with completed partial outputs. A semantic Current request is an explicit error; the caller may separately select [Atom Lifecycle_Update Atom](./CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-update-atom.md). Invalid, ambiguous, stale, or conflicting input stops without writing.

Draft content is edited in place with Version and Updated At preserved and Current untouched. A Summary/Role change updates the role-only intent marker and filename while retaining Draft metadata; promotion publishes the canonical Atom at Version 1. Current and Archived edits are technical-only, in place, preserve Version and Updated At, and synchronize filename/location. Current creates no archive or successor; Archived cannot publish Current or promote a Draft.

This Workflow owns one Step, the Step owns bindings, and the Action owns effects under [CA-R-1570](../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1570-CORE_META_MODEL-RULE--keep-workflow-graphs-separate-from-step-bindings.md), [CA-R-2639](../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2639-CORE_META_MODEL-RULE--bind-step-parameters.md), and [CA-R-2638](../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2638-CORE_META_MODEL-DECLARATION--define-runs.md). Containers, descendants, and cascades are excluded. A failed mutation returns completed outputs and an error; do not retry, replay, or roll back. Journal records business events only and is nonblocking.
