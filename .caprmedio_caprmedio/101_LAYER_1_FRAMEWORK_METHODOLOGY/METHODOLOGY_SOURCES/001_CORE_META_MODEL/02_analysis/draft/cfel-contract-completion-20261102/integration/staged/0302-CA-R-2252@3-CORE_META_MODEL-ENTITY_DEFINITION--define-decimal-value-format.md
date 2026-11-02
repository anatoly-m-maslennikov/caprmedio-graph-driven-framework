---
atom_id: CA-R-2252@3
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
subjects:
  active: CFEL > Format/decimal
  passive:
  - CFEL > Format
version: 3
relations: {}
tier: 1
updated_at: 2026-11-02 00:18:22 +0400
role: Requirement
form: Entity Definition
---
## Summary

Define decimal Value Format

## Claim

The decimal Value Format admits decimal numeric values. It does not set scale,
precision, a numeric range, cardinality, uniqueness, or carrier
representation.

### Formal claim

```text
CFEL > Format/decimal
```

## Semantics

decimal is the value domain selected by a `[decimal]` annotation on one direct
property value.
