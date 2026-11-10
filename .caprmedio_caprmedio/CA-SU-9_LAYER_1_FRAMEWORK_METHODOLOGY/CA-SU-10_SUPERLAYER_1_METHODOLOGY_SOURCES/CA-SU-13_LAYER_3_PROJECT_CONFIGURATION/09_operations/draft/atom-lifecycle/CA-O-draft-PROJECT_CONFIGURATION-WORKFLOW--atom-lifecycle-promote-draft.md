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



## Summary

Atom Lifecycle_Promote Draft

## Claim scope

The invocation domain of [Promote one Atom Draft](CA-O-draft-PROJECT_CONFIGURATION-ACTION--promote-one-atom-draft.md).

## Claim

### Mermaid Scheme

```mermaid
graph TD;
    step1["Promote the selected Atom Draft"];
    click step1 "./CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-promote-draft/CA-O-draft-PROJECT_CONFIGURATION-STEP--promote-the-selected-atom-draft.md" "Open Step";
```

### Prose Claim

This Workflow's Purpose is Runtime; its scheme follows [CA-R-1570](../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1570-CORE_META_MODEL-RULE--keep-workflow-graphs-separate-from-step-bindings.md).

#### Input

One exact Draft selector and an allowed Current `targetStatus`; an optional `savedArchivedAtom` identifies a target already archived by a composed Update.

The `projectContext` input port binds the Project, applicable model, and authorization.

#### Output

The `savedCurrentAtom`, `removedDraft`, warnings, and failure result.

#### Step handoffs

| Step | Receives | Produces |
| --- | --- | --- |
| [Promote the selected Atom Draft](./CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-promote-draft/CA-O-draft-PROJECT_CONFIGURATION-STEP--promote-the-selected-atom-draft.md) | selected Draft, `targetStatus`, optional `savedArchivedAtom`, and `projectContext` | `savedCurrentAtom`, `removedDraft`, warnings or a failure result |

#### Logical switches

| Condition | Behavior |
| --- | --- |
| Entry | Run Promote the selected Atom Draft. |
| `savedCurrentAtom` and `removedDraft` are returned | Complete successfully. |
| A failure result is returned | Stop and report the explicit failure. |

If an Action requests additional input, return its short explanation and requested input dictionary and keep the Workflow pending. Resume with the supplied dictionary; cancellation is allowed while waiting and does not interrupt an Action.
