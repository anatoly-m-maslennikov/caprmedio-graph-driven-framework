---
subjects:
  governs: Entity/Graph Syntax <+ Relation//NARROWER_THAN
  depends_on:
  - 'Entity/Object/Continuant/Projection/(.Type: Terms Graph)'
  - Entity/Term
version: 32
updated_at: 2026-10-30 16:45:26 +0400
relations: {}
atom_id: CA-R-1244@32
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
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
