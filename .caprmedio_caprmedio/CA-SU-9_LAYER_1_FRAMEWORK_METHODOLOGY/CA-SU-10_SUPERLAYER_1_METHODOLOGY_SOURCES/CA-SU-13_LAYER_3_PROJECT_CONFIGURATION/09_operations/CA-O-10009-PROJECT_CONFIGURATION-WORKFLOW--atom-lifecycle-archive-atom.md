---
identity:
  atom_id: CA-O-10009
  ref_id: CA-O-10009
context:
  container:
    scope_unit: CA-SU-13
  role: Operations
  form: Workflow
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)/Workflow/(.Purpose
      := Runtime)
    dependencies:
    - CAPRMEDIO_MODEL <+ Atom
    - CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
  tier: 3
state:
  status: Active
  version: 2
  updated_at: 2026-11-11 14:19:47 +0400
destination:
  file:
    name: CA-O-10009-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-archive-atom.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations
relations:
  IS_REPLACEMENT_FOR:
  - CA-O-127
---
## Summary

Atom Lifecycle_Archive Atom

## Claim scope

The invocation domain of [Archive one Current Atom](CA-O-10001-PROJECT_CONFIGURATION-ACTION--archive-one-current-atom.md).

## Claim

### Mermaid Scheme

```mermaid
graph TD;
    step1["Archive the selected Current Atom"];
    click step1 "./CA-O-10009-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-archive-atom/CA-O-10008-PROJECT_CONFIGURATION-STEP--archive-the-selected-current-atom.md" "Open Step";
```

### Prose Claim

This Workflow's Purpose is Runtime; its scheme follows [CA-R-1570](../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1570-CORE_META_MODEL-RULE--keep-workflow-graphs-separate-from-step-bindings.md).

#### Input

One exact Current Atom selector. For a folder-backed parent, the caller first archives all recursively contained latest Atoms through independent one-Atom invocations under CA-R-1521, CA-D-461 and CA-D-467. References outside the Carrier tree and older archived revisions are excluded. Stop at the first failure and report completed effects and remaining targets.

The `projectContext` input port binds the Project and applicable model.

#### Output

The `savedArchivedAtom`, warnings, and failure result.

#### Step handoffs

| Step | Receives | Produces |
| --- | --- | --- |
| [Archive the selected Current Atom](./CA-O-10009-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-archive-atom/CA-O-10008-PROJECT_CONFIGURATION-STEP--archive-the-selected-current-atom.md) | selected Atom, `projectContext`,  | `savedArchivedAtom`, warnings or a failure result |

#### Logical switches

| Condition | Behavior |
| --- | --- |
| Entry | Run Archive the selected Current Atom. |
| `savedArchivedAtom` is returned | Complete successfully. |
| A failure result is returned | Stop and report the explicit failure. |

If an Action requests additional input, return its short explanation and requested input dictionary and keep the Workflow pending. Resume with the supplied dictionary; cancellation is allowed while waiting and does not interrupt an Action.
