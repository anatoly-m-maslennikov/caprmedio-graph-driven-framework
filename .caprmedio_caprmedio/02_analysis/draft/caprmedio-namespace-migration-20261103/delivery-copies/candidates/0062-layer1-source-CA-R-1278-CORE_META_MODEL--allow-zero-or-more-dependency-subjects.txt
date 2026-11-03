---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom.Subjects
  passive:
  - CAPRMEDIO <+ MODEL <+ CFEL > Relation//DEPENDS_ON
version: 23
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1278
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
---
## Summary

Allow Zero or More Dependency Subjects

## Claim scope

direct DEPENDS_ON targets in an Atom's Subjects Property.

## Claim

**every** Atom **may** declare **`>=0`** distinct direct DEPENDS_ON targets **in** its Subjects Property.
