---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Role:=Operations)/Workflow
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Role := Operations)/Step
  - CAPRMEDIO_MODEL <+ Atom/(.Role:=Operations)/Action
  - CAPRMEDIO_MODEL <+ Atom/(.Role:=Operations)/Workflow
version: 26
relations: {}
atom_id: CA-R-1570
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
updated_at: 2026-11-02 17:54:42 +0400
---
## Summary

Keep Workflow graphs separate from Step bindings

## Claim scope

a Workflow graph scheme.

## Claim

A Workflow graph scheme **must** identify Step references, declared order, structural Relations, entry points, and terminal outcomes.

The graph references Step bindings and called definitions. Its declared graph determines control flow; folder nesting and file order **must not** replace it.
