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
    name: CA-O-draft-PROJECT-STEP--preview-change.md
    path: .caprmedio_caprmedio/09_operations/draft/specification-workflows/CA-O-draft-PROJECT-WORKFLOW--consolidate-specifications
---

## Summary

Preview change

## Claim scope

One binding within [Consolidate Specifications](../CA-O-draft-PROJECT-WORKFLOW--consolidate-specifications.md).

## Claim

### Prose Claim

#### Kind

Execution.

#### Inputs

`project_root`, checked `proposed_change_sql`, `write_mode`, settled mapping and current source state after any lifecycle effects.

#### Fixed parameters

None.

#### Runs

The Action [CA-O-240](../../../../CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/09_operations/CA-O-240-WORKBENCH_BACKEND-ACTION--execute-workbench-sql-statements.md).

#### Outputs

One fresh preview request with that exact SQL and mode against the current source state; return per-change preview and per-statement results, or failure, with no apply.
