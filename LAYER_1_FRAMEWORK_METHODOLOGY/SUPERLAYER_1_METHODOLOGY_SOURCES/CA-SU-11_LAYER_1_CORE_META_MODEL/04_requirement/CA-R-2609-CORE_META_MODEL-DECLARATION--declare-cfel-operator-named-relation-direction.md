---
atom_id: CA-R-2609
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL<+Operator//NamedRelationDirection
version: 1
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---

## Summary

Declare CFEL operator named Relation direction

## Claim

```CFEL
@Operator//NamedRelationDirection == "((RELATION)) / <((RELATION))"
```

## Semantics

`Source ((RELATION)) Target` is forward and `Target <((RELATION)) Source`
is reverse for the same canonical Relation fact. Counts remain on written
endpoints; reverse normalization swaps canonical Source/Target and count slots.
This notation neither grants an inverse Relation nor makes field materialization
a derived Relation.
