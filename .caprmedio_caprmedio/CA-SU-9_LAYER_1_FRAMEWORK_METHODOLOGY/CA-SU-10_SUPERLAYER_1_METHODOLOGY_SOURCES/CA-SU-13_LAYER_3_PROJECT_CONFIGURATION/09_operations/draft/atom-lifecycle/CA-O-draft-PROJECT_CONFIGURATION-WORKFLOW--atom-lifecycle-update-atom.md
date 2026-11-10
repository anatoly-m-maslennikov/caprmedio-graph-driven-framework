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

Atom Lifecycle_Update Atom

## Claim scope

Composed lifecycle update in PROJECT_CONFIGURATION.

## Claim

### Mermaid Scheme

```mermaid
graph TD;
    step1["Create the Draft for a new Version"];
    step2["Archive the exact Current Version"];
    step3["Promote the prepared Draft"];
    step1 -->|saved Draft| step2;
    step2 -->|Archived Atom| step3;
    click step1 "./CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-update-atom/CA-O-draft-PROJECT_CONFIGURATION-STEP--create-the-draft-for-a-new-version.md" "Open Step";
    click step2 "./CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-update-atom/CA-O-draft-PROJECT_CONFIGURATION-STEP--archive-the-exact-current-version.md" "Open Step";
    click step3 "./CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-update-atom/CA-O-draft-PROJECT_CONFIGURATION-STEP--promote-the-prepared-draft.md" "Open Step";
```

### Prose Claim

This Workflow's Purpose is Runtime; its scheme follows [CA-R-1570](../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1570-CORE_META_MODEL-RULE--keep-workflow-graphs-separate-from-step-bindings.md).

#### Input

One exact `sourceCurrent` selector and requested property changes. Before Step 1, read the selected Current source once; bind its Status from the same read as internal `targetStatus`.

The `projectContext` input port binds the Project, applicable model, and authorization.

Promotion skips a replacement target already archived by Step 2. This same-status binding applies only to this composed Update; generic Promote accepts any supplied allowed Current Status.

#### Output

The `savedCurrentAtom`, `savedArchivedAtom`, `removedDraft`, `requested_input`, intermediate results, warnings, and failure result.

#### Step handoffs

| Step | Receives | Produces |
| --- | --- | --- |
| [Create the Draft for a new Version](./CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-update-atom/CA-O-draft-PROJECT_CONFIGURATION-STEP--create-the-draft-for-a-new-version.md) | `sourceCurrent`, requested changes, `projectContext` | `savedDraft`, `requested_input`, warnings, intermediate results, or a failure result |
| [Archive the exact Current Version](./CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-update-atom/CA-O-draft-PROJECT_CONFIGURATION-STEP--archive-the-exact-current-version.md) | original `sourceCurrent`, warnings, and `projectContext` | `savedArchivedAtom`, warnings, or a failure result |
| [Promote the prepared Draft](./CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-update-atom/CA-O-draft-PROJECT_CONFIGURATION-STEP--promote-the-prepared-draft.md) | `savedDraft`, captured `targetStatus`, `savedArchivedAtom`, warnings, and `projectContext` | `savedCurrentAtom`, `removedDraft`, warnings, or a failure result |

#### Logical switches

| Condition | Behavior |
| --- | --- |
| Entry | Run Create the Draft for a new Version. |
| Step 1 returns nonempty `requested_input` | Keep this Workflow pending; corrections resume Step 1 with captured `targetStatus` preserved. |
| Step 1 returns `savedDraft` | Run Archive the exact Current Version. |
| Step 2 returns `savedArchivedAtom` | Run Promote the prepared Draft. |
| Step 3 returns `savedCurrentAtom` and `removedDraft` | Complete successfully. |
| A failure result is returned | Stop and report the explicit failure. |
