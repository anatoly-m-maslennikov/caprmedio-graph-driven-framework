---
atom_id: CA-R-2355@1
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
subjects:
  governs: Entity/Graph Syntax > Relation.Name
relations: {}
version: 1
updated_at: 2026-10-29 17:09:47 +0400
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Relation Name

## Claim scope

Canonical names of reusable Relation Types.

## Claim

A reusable Relation Type Name is its canonical name. The named Type may connect many endpoint pairs; an actual edge remains the source/Type/target tuple and does not create a separate Relation ID.

### Formal claim

```text
Relation.Name[string]{1}
```

## Details

Source meaning: CA-R-2247. Scope-specific constraints remain in their governing Rs.
