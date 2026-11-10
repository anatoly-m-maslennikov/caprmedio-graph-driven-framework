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

Atom Lifecycle_Change Current Status

## Claim scope

The invocation domain of [Set one Current Atom Status](CA-O-draft-PROJECT_CONFIGURATION-ACTION--set-one-current-atom-status.md).

## Claim

### Mermaid Scheme

```mermaid
graph TD;
    step1["Set the selected Current Status"];
    click step1 "./CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-change-current-status/CA-O-draft-PROJECT_CONFIGURATION-STEP--set-the-selected-current-status.md" "Open Step";
```

### Prose Claim

This Workflow's Purpose is Runtime; its scheme follows [CA-R-1570](../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1570-CORE_META_MODEL-RULE--keep-workflow-graphs-separate-from-step-bindings.md).

#### Input

One exact Atom selector and requested `targetStatus`.

The `projectContext` input port binds the Project, applicable model, and authorization.

#### Output

The `savedCurrentAtom`, warnings, and failure result.

#### Step handoffs

| Step | Receives | Produces |
| --- | --- | --- |
| [Set the selected Current Status](./CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-change-current-status/CA-O-draft-PROJECT_CONFIGURATION-STEP--set-the-selected-current-status.md) | selected Atom, `targetStatus`, and `projectContext` | `savedCurrentAtom`, warnings or a failure result |

#### Logical switches

| Condition | Behavior |
| --- | --- |
| Entry | Run Set the selected Current Status. |
| `savedCurrentAtom` is returned | Complete successfully. |
| A failure result is returned | Stop and report the explicit failure. |

If an Action requests additional input, return its short explanation and requested input dictionary and keep the Workflow pending. Resume with the supplied dictionary; cancellation is allowed while waiting and does not interrupt an Action.
