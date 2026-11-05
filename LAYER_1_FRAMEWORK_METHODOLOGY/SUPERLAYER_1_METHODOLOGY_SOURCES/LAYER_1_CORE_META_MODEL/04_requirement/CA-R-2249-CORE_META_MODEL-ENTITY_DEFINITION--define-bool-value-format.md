---
atom_id: CA-R-2249
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Format/bool
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

Define bool Value Format

## Claim

### Formal Claim

```CFEL
# model
CFEL <+ Format/bool
```

### Prose Claim


The bool Value Format admits the Boolean values true and false. It does not set a
property's cardinality, default, nullability, or carrier representation.



## Semantics

bool is the value domain selected by a `[bool]` annotation on one direct
Property value.
