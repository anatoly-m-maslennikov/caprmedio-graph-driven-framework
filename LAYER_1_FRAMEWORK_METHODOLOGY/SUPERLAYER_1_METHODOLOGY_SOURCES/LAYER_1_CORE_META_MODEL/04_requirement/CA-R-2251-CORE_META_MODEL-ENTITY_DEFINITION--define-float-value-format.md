---
atom_id: CA-R-2251
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Format/float
  passive:
  - CAPRMEDIO_MODEL <+ CFEL <+ Format
version: 6
updated_at: 2026-11-03 23:25:51 +0400
relations: {}
tier: 1
role: Requirement
form: Declaration
---
## Summary

Define float Value Format

## Claim

### Formal Claim

```CFEL
# model
CFEL <+ Format/float
```

### Prose Claim


The float Value Format admits floating-point numeric values. It does not set
precision, a numeric range, cardinality, uniqueness, or carrier
representation.



## Semantics

float is the value domain selected by a `[float]` annotation on one direct
Property value.
