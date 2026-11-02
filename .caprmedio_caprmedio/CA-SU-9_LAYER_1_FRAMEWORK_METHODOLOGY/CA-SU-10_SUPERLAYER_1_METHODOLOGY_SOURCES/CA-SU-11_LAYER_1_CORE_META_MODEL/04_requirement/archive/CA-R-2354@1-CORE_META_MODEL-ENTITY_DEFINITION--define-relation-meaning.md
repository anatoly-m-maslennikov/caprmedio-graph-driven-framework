---
atom_id: CA-R-2354@1
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
subjects:
  governs: Entity/Graph Syntax > Relation.Meaning
relations: {}
version: 1
updated_at: 2026-10-29 17:09:47 +0400
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Relation Meaning

## Claim scope

Canonical meaning of a reusable Relation Type.

## Claim

A reusable Relation Type Meaning is its canonical meaning; direction, derived inverse and transitivity describe the Type rather than any one actual edge. Actual source and target endpoints remain tuple facts.

### Formal claim

```text
Relation.Meaning[string]{1}
```

## Details

Source meaning: CA-R-2247. Scope-specific constraints remain in their governing Rs.
