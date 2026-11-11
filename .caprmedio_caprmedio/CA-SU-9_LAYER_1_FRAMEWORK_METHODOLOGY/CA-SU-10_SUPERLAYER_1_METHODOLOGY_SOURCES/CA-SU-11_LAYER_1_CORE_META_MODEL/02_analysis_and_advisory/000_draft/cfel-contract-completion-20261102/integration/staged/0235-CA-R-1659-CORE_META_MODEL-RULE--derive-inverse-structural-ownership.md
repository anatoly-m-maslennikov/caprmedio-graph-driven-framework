---
subjects:
  active: CFEL <+ Relation
  passive: []
version: 30
updated_at: 2026-11-02 07:49:21 +0400
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
