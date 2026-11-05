---
atom_id: CA-R-2254
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Format/datetime
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

Define datetime Value Format

## Claim

### Formal Claim

```CFEL
# model
CFEL <+ Format/datetime
```

### Prose Claim


The datetime Value Format admits date-and-time values. It does not set a
timezone convention, precision, cardinality, uniqueness, or carrier
representation.



## Semantics

datetime is the value domain selected by a `[datetime]` annotation on one
direct Property value.
