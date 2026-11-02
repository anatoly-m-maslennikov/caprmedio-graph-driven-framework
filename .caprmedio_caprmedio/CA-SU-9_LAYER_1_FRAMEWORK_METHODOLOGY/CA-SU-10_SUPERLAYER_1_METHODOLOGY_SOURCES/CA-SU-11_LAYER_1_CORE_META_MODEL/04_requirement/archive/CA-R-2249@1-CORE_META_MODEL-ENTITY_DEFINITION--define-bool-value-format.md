---
atom_id: CA-R-2249@1
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Entity/Graph Syntax > Format/bool
  depends_on:
  - Entity/Graph Syntax > Format
version: 1
relations: {}
tier: 1
updated_at: 2026-10-29 07:51:40 +0400
---
## Summary

Define bool Value Format

## Claim

The bool Value Format admits Boolean values: true and false. It does not set a
property's cardinality, default, nullability, or carrier representation.

### Formal claim

```text
Format/bool.Data Type: bool
```

## Semantics

bool is the value domain selected by a `[bool]` annotation on one direct
property value.
