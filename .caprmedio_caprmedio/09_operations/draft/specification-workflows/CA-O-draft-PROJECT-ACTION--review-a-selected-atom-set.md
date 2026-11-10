---
atom_id: CA-O-draft
container:
  scope_unit: CA-SU-00
role: Operations
form: Action
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Action
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
    name: CA-O-draft-PROJECT-ACTION--review-a-selected-atom-set.md
    path: .caprmedio_caprmedio/09_operations/draft/specification-workflows
---

## Summary

Review a selected Atom set

## Claim

### Prose Claim

#### Inputs

`project_root`, complete `selected_context` and selection evidence, `task_instructions`, applicable model and query schema, `approved_model_definition` (required for model-change review; absent otherwise), `settled_decisions`, and any existing `proposed_change_sql`, `write_mode` and `mapping`.

#### Effect

Review only the bound context, instructions and decisions; compile evidence-linked findings and concrete change SQL and mappings. Do not mutate source or accept unresolved proposals. In consistency work propose exact find/replace corrections only, without automatic semantic rewrites.

#### Outputs

`findings`, concrete `proposed_change_sql`, `write_mode`, `mapping`, and `requested_input` dictionary containing unresolved decisions (empty when settled); alternatively a no-change result or explicit failure. Preserve the context, prior answers and proposals needed for the next invocation.
