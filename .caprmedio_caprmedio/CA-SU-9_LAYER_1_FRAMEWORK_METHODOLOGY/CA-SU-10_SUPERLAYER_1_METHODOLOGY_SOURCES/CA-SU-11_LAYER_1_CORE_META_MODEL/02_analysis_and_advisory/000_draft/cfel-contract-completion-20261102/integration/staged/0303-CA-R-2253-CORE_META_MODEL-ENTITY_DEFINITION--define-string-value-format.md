---
atom_id: CA-R-2253
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CFEL <+ Format/string
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

Define string Value Format

## Claim

The string Value Format admits textual string values. It does not turn null
into a string or set a property's cardinality, uniqueness, or carrier
representation.


```CFEL
CFEL <+ Format/string
```

## Semantics

string is the value domain selected by a `[string]` annotation on one direct
Property value.
