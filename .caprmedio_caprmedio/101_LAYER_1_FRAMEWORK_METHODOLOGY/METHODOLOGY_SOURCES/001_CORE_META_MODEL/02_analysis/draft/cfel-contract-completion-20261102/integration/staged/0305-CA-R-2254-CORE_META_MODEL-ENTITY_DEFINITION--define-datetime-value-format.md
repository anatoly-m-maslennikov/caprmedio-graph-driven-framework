---
atom_id: CA-R-2254
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CFEL <+ Format/datetime
  passive:
  - CFEL <+ Format
version: 5
updated_at: 2026-11-02 07:52:54 +0400
relations: {}
tier: 1
role: Requirement
form: Entity Definition
---
## Summary

Define datetime Value Format

## Claim

The datetime Value Format admits date-and-time values. It does not set a
timezone convention, precision, cardinality, uniqueness, or carrier
representation.


```CFEL
CFEL <+ Format/datetime
```

## Semantics

datetime is the value domain selected by a `[datetime]` annotation on one
direct Property value.
