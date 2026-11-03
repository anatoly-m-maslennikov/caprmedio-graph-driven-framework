---
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation
  passive:
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Atom.Local Scope Unit
  - CAPRMEDIO_MODEL <+ Atom.Target Scope Unit
version: 37
updated_at: 2026-11-02 08:06:47 +0400
relations:
  child_of:
  - CA-R-932@37
atom_id: CA-R-935
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 5
role: Requirement
form: Rule
---
## Summary
Prohibit Demands between ancestors and descendants

## Claim

### Prose Claim


Demand Atoms.


a Demand Atom's Claim Target Scope Unit **must not** be an ancestor **or** descendant of its Consumer Scope Unit.
