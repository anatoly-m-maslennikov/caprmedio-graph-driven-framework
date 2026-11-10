---
atom_id: CA-O-draft
role: Operations
form: Workflow
status: Draft
version: 1
updated_at: '2026-11-03 18:54:48 +0400'
tier: 3
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Workflow/(.Purpose := Runtime)
  passive:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
relations: {}
---



## Summary

Atom Lifecycle_Create Draft

## Claim scope

The invocation domain of [Create one Atom Draft](CA-O-draft-PROJECT_CONFIGURATION-ACTION--create-one-atom-draft.md).

## Claim

### Mermaid Scheme

```mermaid
graph TD;
    read["Read Workflow input"];
    check{"Check Draft input"};
    request[/Request Draft input/];
    create["Create the requested Atom Draft"];
    read --> check;
    check -->|valid input| create;
    check -->|requested_input| request;
    request -->|supplied corrections| check;
    click read "./CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-create-draft/CA-O-draft-PROJECT_CONFIGURATION-STEP--read-workflow-input.md" "Open Step";
    click check "./CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-create-draft/CA-O-draft-PROJECT_CONFIGURATION-STEP--check-draft-input.md" "Open Step";
    click request "./CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-create-draft/CA-O-draft-PROJECT_CONFIGURATION-STEP--request-draft-input.md" "Open Step";
    click create "./CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-create-draft/CA-O-draft-PROJECT_CONFIGURATION-STEP--create-the-requested-atom-draft.md" "Open Step";
```

### Prose Claim

This Workflow's Purpose is Runtime; its scheme follows [CA-R-1570](../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1570-CORE_META_MODEL-RULE--keep-workflow-graphs-separate-from-step-bindings.md).

#### Input

The [Read Workflow input](./CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-create-draft/CA-O-draft-PROJECT_CONFIGURATION-STEP--read-workflow-input.md) invocation-port contract supplies either `newAtom` properties, or an exact `sourceCurrent` selector plus requested property changes.

The `projectContext` input port binds the Project, applicable model, and authorization.


#### Output

The `savedDraft`, `requested_input`, intermediate results, warnings, and failure result.

#### Step handoffs

| Step | Receives | Produces |
| --- | --- | --- |
| [Read Workflow input](./CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-create-draft/CA-O-draft-PROJECT_CONFIGURATION-STEP--read-workflow-input.md) | invocation dictionary and `projectContext` | accumulated `parameters` |
| [Check Draft input](./CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-create-draft/CA-O-draft-PROJECT_CONFIGURATION-STEP--check-draft-input.md) | accumulated `parameters` and `projectContext` | logical `parameters`, `requested_input`, and warnings |
| [Request Draft input](./CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-create-draft/CA-O-draft-PROJECT_CONFIGURATION-STEP--request-draft-input.md) | `parameters`, `requested_input`, warnings, and `projectContext` | supplied corrections, warnings and intermediate results |
| [Create the requested Atom Draft](./CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-create-draft/CA-O-draft-PROJECT_CONFIGURATION-STEP--create-the-requested-atom-draft.md) | validated caller-bound `parameters`, warnings, `projectContext` | `savedDraft`, warnings, or a failure result |

#### Logical switches

| Condition | Behavior |
| --- | --- |
| Entry | Read Workflow input, then Check Draft input. |
| Check Draft input returns empty `requested_input` | Run Create the requested Atom Draft. |
| Check Draft input returns nonempty `requested_input` | Run Request Draft input and keep this Workflow incomplete while it waits. |
| Request Draft input supplies corrections | Check Draft input again; its Step defines the correction merge. |
| Create the requested Atom Draft returns `savedDraft` | Complete successfully. |
| A failure result is returned | Stop and report the explicit failure. |

If an Action requests additional input, return its short explanation and requested input dictionary and keep the Workflow pending. Resume with the supplied dictionary; cancellation is allowed while waiting and does not interrupt an Action.
