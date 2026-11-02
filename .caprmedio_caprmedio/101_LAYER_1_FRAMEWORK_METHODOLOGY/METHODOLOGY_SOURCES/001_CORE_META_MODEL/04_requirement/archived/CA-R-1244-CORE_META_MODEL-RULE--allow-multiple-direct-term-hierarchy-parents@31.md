---
subjects:
  governs: Entity/Graph Syntax > Relation//NARROWER_THAN
  depends_on:
  - 'Entity/Object/Continuant/Projection/Type: Terms Graph'
  - Entity/Object/Continuant/Term
version: 31
updated_at: 2026-10-29 10:13:48 +0400
relations: {}
atom_id: CA-R-1244
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 2
type: Rule
---
## Summary

Allow multiple direct Term hierarchy parents

## Claim scope

Direct NARROWER_THAN parents of a Term.

## Claim

a Term **may** have **`>=0`** direct NARROWER_THAN parents.
