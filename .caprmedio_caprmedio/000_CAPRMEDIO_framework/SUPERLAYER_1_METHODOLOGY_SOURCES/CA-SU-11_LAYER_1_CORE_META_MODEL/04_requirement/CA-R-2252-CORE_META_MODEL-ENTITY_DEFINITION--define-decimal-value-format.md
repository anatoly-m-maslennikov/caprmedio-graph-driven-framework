---
atom_id: CA-R-2252
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CFEL <+ Format/decimal
  passive:
  - CFEL <+ Format
version: 5
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 1
role: Requirement
form: Entity Definition
---
## Summary

Define decimal Value Format

## Claim

The decimal Value Format admits decimal numeric values. It does not set scale,
precision, a numeric range, cardinality, uniqueness, or carrier
representation.


```CFEL
CFEL <+ Format/decimal
```

## Semantics

decimal is the value domain selected by a `[decimal]` annotation on one direct
Property value.
