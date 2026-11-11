---
atom_id: CA-R-2251
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CFEL <+ Format/float
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

Define float Value Format

## Claim

The float Value Format admits floating-point numeric values. It does not set
precision, a numeric range, cardinality, uniqueness, or carrier
representation.


```CFEL
CFEL <+ Format/float
```

## Semantics

float is the value domain selected by a `[float]` annotation on one direct
Property value.
