---
atom_id: CA-R-2252@2
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
version: 2
relations: {}
tier: 1
updated_at: 2026-10-29 09:46:50 +0400
---
## Summary

Define decimal Value Format

## Claim

The decimal Value Format admits decimal numeric values. It does not set scale,
precision, a numeric range, cardinality, uniqueness, or carrier
representation.

### Formal claim

```text
Entity/Graph Syntax > Format/decimal
```

## Semantics

decimal is the value domain selected by a `[decimal]` annotation on one direct
property value.
