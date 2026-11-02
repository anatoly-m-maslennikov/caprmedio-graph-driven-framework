---
atom_id: CA-R-2251@2
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Entity/Graph Syntax > Format/float
  depends_on:
  - Entity/Graph Syntax > Format
version: 2
relations: {}
tier: 1
updated_at: 2026-10-29 09:46:50 +0400
---
## Summary

Define float Value Format

## Claim

The float Value Format admits floating-point numeric values. It does not set
precision, a numeric range, cardinality, uniqueness, or carrier
representation.

### Formal claim

```text
Entity/Graph Syntax > Format/float
```

## Semantics

float is the value domain selected by a `[float]` annotation on one direct
property value.
