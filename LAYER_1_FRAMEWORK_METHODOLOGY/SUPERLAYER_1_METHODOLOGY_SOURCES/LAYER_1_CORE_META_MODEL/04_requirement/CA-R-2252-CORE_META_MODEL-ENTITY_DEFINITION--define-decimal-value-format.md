---
atom_id: CA-R-2252
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Format/decimal
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

Define decimal Value Format

## Claim

### Formal Claim

```CFEL
# model
CFEL <+ Format/decimal
```

### Prose Claim


The decimal Value Format admits decimal numeric values. It does not set scale,
precision, a numeric range, cardinality, uniqueness, or carrier
representation.



## Semantics

decimal is the value domain selected by a `[decimal]` annotation on one direct
Property value.
