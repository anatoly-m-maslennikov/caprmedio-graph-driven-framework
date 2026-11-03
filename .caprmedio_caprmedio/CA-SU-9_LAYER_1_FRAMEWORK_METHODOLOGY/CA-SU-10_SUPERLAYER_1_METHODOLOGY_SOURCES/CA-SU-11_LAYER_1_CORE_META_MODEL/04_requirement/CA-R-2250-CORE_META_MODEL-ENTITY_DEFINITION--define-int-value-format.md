---
atom_id: CA-R-2250
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Format/int
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

Define int Value Format

## Claim

### Formal Claim

```CFEL
# model
CFEL <+ Format/int
```

### Prose Claim


The int Value Format admits integer numeric values with no fractional part. It
does not set a numeric range, cardinality, uniqueness rule, or carrier
representation.



## Semantics

int is the value domain selected by an `[int]` annotation on one direct
Property value.
