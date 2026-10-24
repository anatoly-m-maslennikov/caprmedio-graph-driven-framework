---
subjects:
  governs: Subject/Graph/Relation
  depends_on:
  - lifecycle-traceability
version: 17
updated_at: 2026-10-24 01:37:42 +0400
relations: {}
atom_id: CA-R-1032
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 2
type: Rule
---
# Summary

Block dependent gates until Lineage Impact reaches a fixed point

## Scope

release **or** downstream gates that require a revised Atom.

## Claim

**every** release **or** downstream gate that requires a revised Atom **must** remain blocked **until** its Lineage Impact Analysis concludes that **every** affected branch has reached a fixed point.

## Details
