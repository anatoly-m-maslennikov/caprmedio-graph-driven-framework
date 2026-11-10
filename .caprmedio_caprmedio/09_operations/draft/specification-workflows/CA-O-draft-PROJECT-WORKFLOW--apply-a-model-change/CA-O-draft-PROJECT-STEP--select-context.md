---
atom_id: CA-O-draft
container:
  scope_unit: CA-SU-00
role: Operations
form: Step
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Step
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Project
tier: 3
relations: {}
status: Draft
version: 1
updated_at: '2026-11-11 00:16:05 +0400'
current_scope_unit: caprmedio
destination:
  file:
    name: CA-O-draft-PROJECT-STEP--select-context.md
    path: .caprmedio_caprmedio/09_operations/draft/specification-workflows/CA-O-draft-PROJECT-WORKFLOW--apply-a-model-change
---

## Summary

Select context

## Claim scope

One binding within [Apply a Model Change](../CA-O-draft-PROJECT-WORKFLOW--apply-a-model-change.md).

## Claim

### Prose Claim

#### Kind

Execution.

#### Inputs

`project_root`, `selection_sql` (caller AI may supply it), applicable query schema, and `approved_model_definition` when applying a model change.

#### Fixed parameters

None.

#### Runs

The Action [CA-O-240](../../../../CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/09_operations/CA-O-240-WORKBENCH_BACKEND-ACTION--execute-workbench-sql-statements.md).

#### Outputs

One SELECT Run request using `project_root` and `selection_sql`. Return `selected_context`, per-statement results and selection evidence, or explicit failure. The supplied approved model definition precedes selection: select its exact affected Current and Draft Atom set and relevant context.
