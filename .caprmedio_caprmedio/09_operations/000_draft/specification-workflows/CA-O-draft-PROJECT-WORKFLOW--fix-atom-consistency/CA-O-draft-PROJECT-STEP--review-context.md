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
    name: CA-O-draft-PROJECT-STEP--review-context.md
    path: .caprmedio_caprmedio/09_operations/000_draft/specification-workflows/CA-O-draft-PROJECT-WORKFLOW--fix-atom-consistency
---

## Summary

Review context

## Claim scope

One binding within [Fix Atom Consistency](../CA-O-draft-PROJECT-WORKFLOW--fix-atom-consistency.md).

## Claim

### Prose Claim

#### Kind

Execution.

#### Inputs

`project_root`, `selected_context`, selection evidence, `task_instructions`, applicable model/query schema, `approved_model_definition` when applying a model change, `settled_decisions`, prior proposal and mapping.

#### Fixed parameters

None.

#### Runs

The Action [Review a selected Atom set](../CA-O-draft-PROJECT-ACTION--review-a-selected-atom-set.md).

#### Outputs

Return `findings`, `proposed_change_sql`, `write_mode`, `mapping`, and `requested_input` dictionary, or no-change/failure. Propose exact SQL find/replace corrections only; do not automatically rewrite meaning.
