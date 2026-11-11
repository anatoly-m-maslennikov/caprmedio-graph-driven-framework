---
subjects:
  active: CFEL <+ Relation
version: 31
updated_at: 2026-11-02 19:44:26 +0400
relations:
  child_of:
  - CA-R-1756
atom_id: CA-R-1659
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Requirement
form: Rule
---
## Summary

Derive inverse structural ownership

## Claim scope

the inverse `structural_children` view derived from stored `structural_parent` relations.

## Claim

CAPRMEDIO **must** derive the inverse `structural_children` view from stored `structural_parent` relations **and** **must not** persist that inverse separately.
