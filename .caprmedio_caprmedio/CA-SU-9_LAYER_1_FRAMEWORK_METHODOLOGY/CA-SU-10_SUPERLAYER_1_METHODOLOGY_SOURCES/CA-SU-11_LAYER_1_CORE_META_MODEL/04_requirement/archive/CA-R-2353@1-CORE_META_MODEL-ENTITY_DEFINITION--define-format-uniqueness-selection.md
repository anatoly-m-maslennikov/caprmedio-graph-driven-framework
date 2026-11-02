---
atom_id: CA-R-2353@1
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
subjects:
  governs: Entity/Graph Syntax > Format.Uniqueness Selection
relations: {}
version: 1
updated_at: 2026-10-29 17:09:47 +0400
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Format Uniqueness Selection

## Claim scope

Optional comparison-population selection in a Value Format.

## Claim

A Format Uniqueness Selection identifies the comparison population for a property uniqueness check; it is optional and does not itself impose uniqueness or define a notation.

### Formal claim

```text
Format.Uniqueness Selection[string]{0..1}
```

## Details

Source meaning: CA-R-2248. Scope-specific constraints remain in their governing Rs.
