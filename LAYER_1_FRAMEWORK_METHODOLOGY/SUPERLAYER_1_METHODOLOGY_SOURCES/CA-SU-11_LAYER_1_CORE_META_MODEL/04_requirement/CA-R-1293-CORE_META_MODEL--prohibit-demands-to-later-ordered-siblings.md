---
subjects:
  active: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Demand).Target Scope Unit'
  passive:
  - CAPRMEDIO_MODEL <+ Scope Unit.order.number
  - CAPRMEDIO_MODEL <+ Scope Unit
version: 29
updated_at: 2026-11-02 19:44:26 +0400
relations: {}
atom_id: CA-R-1293
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
---
## Summary

Prohibit Demands to Later Ordered Siblings

## Claim

### Prose Claim


Demand Atoms owned by Ordered Scope Units.


a Demand Atom owned by an Ordered Scope Unit **must not** target a later Ordered sibling under the same direct parent.
