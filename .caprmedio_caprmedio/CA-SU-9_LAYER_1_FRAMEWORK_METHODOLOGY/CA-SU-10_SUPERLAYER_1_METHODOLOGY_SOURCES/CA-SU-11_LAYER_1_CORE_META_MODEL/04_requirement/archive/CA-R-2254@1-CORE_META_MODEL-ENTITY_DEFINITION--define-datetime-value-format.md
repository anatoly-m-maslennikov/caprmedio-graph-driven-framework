---
atom_id: CA-R-2254@1
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Entity/Graph Syntax > Format/datetime
  depends_on:
  - Entity/Graph Syntax > Format
version: 1
relations: {}
tier: 1
updated_at: 2026-10-29 07:51:41 +0400
---
## Summary

Define datetime Value Format

## Claim

The datetime Value Format admits date-and-time values. It does not set a
timezone convention, precision, cardinality, uniqueness, or carrier
representation.

### Formal claim

```text
Format/datetime.Data Type: datetime
```

## Semantics

datetime is the value domain selected by a `[datetime]` annotation on one
direct property value.
