---
atom_id: CA-R-2253@1
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Entity/Graph Syntax > Format/string
  depends_on:
  - Entity/Graph Syntax > Format
version: 1
relations: {}
tier: 1
updated_at: 2026-10-29 07:51:40 +0400
---
## Summary

Define string Value Format

## Claim

The string Value Format admits textual string values. It does not turn null
into a string or set a property’s cardinality, uniqueness, or carrier
representation.

### Formal claim

```text
Format/string.Data Type: string
```

## Semantics

string is the value domain selected by a `[string]` annotation on one direct
property value.
