---
atom_id: CA-R-2250@2
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Entity/Graph Syntax > Format/int
  depends_on:
  - Entity/Graph Syntax > Format
version: 2
relations: {}
tier: 1
updated_at: 2026-10-29 09:46:50 +0400
---
## Summary

Define int Value Format

## Claim

The int Value Format admits integer numeric values with no fractional part. It
does not set a numeric range, cardinality, uniqueness rule, or carrier
representation.

### Formal claim

```text
Entity/Graph Syntax > Format/int
```

## Semantics

int is the value domain selected by an `[int]` annotation on one direct
property value.
