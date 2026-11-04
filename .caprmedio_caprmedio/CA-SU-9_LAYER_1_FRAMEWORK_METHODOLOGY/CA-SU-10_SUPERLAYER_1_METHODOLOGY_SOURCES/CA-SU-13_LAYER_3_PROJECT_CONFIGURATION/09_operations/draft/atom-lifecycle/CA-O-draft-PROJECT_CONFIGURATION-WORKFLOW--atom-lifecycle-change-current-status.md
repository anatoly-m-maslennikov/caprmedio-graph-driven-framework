---
atom_id: CA-O-draft
role: Operations
form: Workflow
status: Draft
version: 1
updated_at: '2026-11-03 18:54:48 +0400'
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
    step1["Set the selected Current Status<br/>Success: saved Current with requested Status<br/>Failure: stop with error and completed outputs"]
    click step1 "./CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-change-current-status/CA-O-draft-PROJECT_CONFIGURATION-STEP--set-the-selected-current-status.md" "Open Step"
```

## Summary

Atom Lifecycle_Change Current Status

## Claim scope

One exact non-container Current Atom and one requested Status in its model's Current group.

## Claim

This Workflow's Purpose is Runtime.

Run [Set the selected Current Atom Status](CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-change-current-status/CA-O-draft-PROJECT_CONFIGURATION-STEP--set-the-selected-current-status.md) once for the selected Atom and Status.

Return the saved carrier. The Action changes only Status and synchronizes filename/location. On failure, return the error with completed outputs under [CA-R-1432](../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft/lifecycle-in-place-edits/CA-R-1432@28-draft-CORE_META_MODEL-RULE--classify-admitted-atom-changes-by-semantic-effect.md).
