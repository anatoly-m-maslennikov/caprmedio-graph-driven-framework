---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Role := Plan)
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Role := Plan)
version: 22
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1534
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
---
## Summary

Keep Plan Atom Identity Independent from Decomposition

## Claim scope

the identity of a Hub Atom **and** related decomposed Plan Atoms.

## Claim

adding, removing, reordering, **or** changing a decomposed Plan Atom **must not** establish **or** replace the Hub Atom's identity; **every** related Atom retains its independent Claim **and** lifecycle.
