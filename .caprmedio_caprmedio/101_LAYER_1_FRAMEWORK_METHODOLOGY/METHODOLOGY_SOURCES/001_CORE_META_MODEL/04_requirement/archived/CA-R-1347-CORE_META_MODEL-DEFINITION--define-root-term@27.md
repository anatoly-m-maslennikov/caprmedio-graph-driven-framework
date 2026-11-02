---
subjects:
  governs: Entity/Object/Continuant/Term
  depends_on:
  - Entity/Object/Continuant/Term
  - 'Entity/Object/Continuant/Projection/Type: Terms Graph'
  - Entity/Graph Syntax > Relation//NARROWER_THAN
version: 27
updated_at: 2026-10-29 17:09:47 +0400
relations: {}
atom_id: CA-R-1347
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Rule
---
## Summary

Define Root Term

## Claim scope

Terms in the Terms Graph.

## Claim

a Root Term **means** a Term with **`=0`** direct NARROWER_THAN parents **in** the Terms Graph.
