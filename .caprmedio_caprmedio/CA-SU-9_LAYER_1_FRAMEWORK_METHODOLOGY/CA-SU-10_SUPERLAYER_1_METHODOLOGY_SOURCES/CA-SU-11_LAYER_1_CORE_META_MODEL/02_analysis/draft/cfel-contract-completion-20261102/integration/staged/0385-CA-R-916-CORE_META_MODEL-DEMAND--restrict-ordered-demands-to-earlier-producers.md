---
subjects:
  active: CFEL <+ Relation
  passive:
  - Entity/Object/Continuant/Governing Objects/Atom.Local Scope Unit
  - Entity/Object/Continuant/Governing Objects/Atom.Target Scope Unit
version: 37
updated_at: 2026-11-02 07:49:21 +0400
relations:
  child_of:
  - CA-R-932@37
atom_id: CA-R-916
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 5
role: Requirement
form: Demand
---
## Summary
Restrict ordered Demands to earlier Producers

## Claim scope

Demand Atoms whose Consumer Atom Scope Unit and Producer Claim Target Scope Unit are ordered siblings.

## Claim

**if** a Demand Atom's Consumer Atom Scope Unit **and** Producer Claim Target Scope Unit are ordered siblings, **then** its Producer Claim Target Scope Unit **must** precede its Consumer Atom Scope Unit.
