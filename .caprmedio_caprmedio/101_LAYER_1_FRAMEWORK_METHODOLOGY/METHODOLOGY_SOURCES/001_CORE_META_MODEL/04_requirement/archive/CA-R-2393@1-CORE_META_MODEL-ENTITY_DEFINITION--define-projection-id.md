---
atom_id: CA-R-2393@1
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
subjects:
  governs: Entity/Object/Continuant/Projection.ID
relations: {}
version: 1
updated_at: 2026-10-29 17:09:47 +0400
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Projection ID

## Claim


Projection.ID is the stable identity of a Projection for its Projection Type, named source selection and source of truth. Rebuilding from changed source content or at another time keeps the ID while that identity tuple stays the same. Changing any tuple component requires a different ID under CA-R-1943.

### Formal claim

```text
Entity/Object/Continuant/Projection.ID[string]{1}
```

## Details

Source meaning: CA-R-1746, CA-R-1943. Scope-specific constraints remain in their governing Rs.
