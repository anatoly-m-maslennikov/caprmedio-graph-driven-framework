---
atom_id: CA-R-2557
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Event Record
version: 4
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---
## Summary

Declare Event Record

## Claim

An Event Record is immutable.

```CFEL
Event Record {:0}((IS_PROPERTY_OF));
Event Record ((NARROWER_THAN)) @Continuant;
Event Record// {:1}((IS_CONTAINED_BY)) Journal//
```

## Semantics

An Event Record is a persistent description of an event and its recorded evidence.
