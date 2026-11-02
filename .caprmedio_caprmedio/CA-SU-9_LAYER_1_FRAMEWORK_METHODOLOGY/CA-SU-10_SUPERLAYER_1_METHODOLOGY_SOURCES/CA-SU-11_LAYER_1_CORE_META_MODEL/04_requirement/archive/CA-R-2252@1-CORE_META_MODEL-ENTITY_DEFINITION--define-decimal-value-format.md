---
atom_id: CA-R-2252@1
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Entity/Graph Syntax > Format/decimal
  depends_on:
  - Entity/Graph Syntax > Format
version: 1
relations: {}
tier: 1
updated_at: 2026-10-29 07:51:40 +0400
---
## Summary

Define decimal Value Format

## Claim

The decimal Value Format admits decimal numeric values. It does not set scale,
precision, a numeric range, cardinality, uniqueness, or carrier
representation.

### Formal claim

```text
Format/decimal.Data Type: decimal
```

## Semantics

decimal is the value domain selected by a `[decimal]` annotation on one direct
property value.
