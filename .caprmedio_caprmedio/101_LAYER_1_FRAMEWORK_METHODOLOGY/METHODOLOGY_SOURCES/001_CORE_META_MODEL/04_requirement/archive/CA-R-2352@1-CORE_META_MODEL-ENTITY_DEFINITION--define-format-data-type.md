---
atom_id: CA-R-2352@1
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
subjects:
  governs: Entity/Graph Syntax > Format.Data Type
relations: {}
version: 1
updated_at: 2026-10-29 17:09:47 +0400
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Format Data Type

## Claim scope

Direct value-domain names in a Value Format.

## Claim

A Format Data Type names the admissible value domain of each direct property value, separately from cardinality. The initial vocabulary is provisional; list, map and reference semantics remain prose under the governing format definition.

### Formal claim

```text
Format.Data Type[string]{1}
```

## Details

Source meaning: CA-R-2248. Scope-specific constraints remain in their governing Rs.
