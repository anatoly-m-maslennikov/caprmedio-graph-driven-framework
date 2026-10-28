---
subjects:
  governs: 'Subject/Graph Relation/Type: IS_ALLOWED_VALUE_OF'
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Term//Property
  - 'Subject/Graph Node/Domain/Continuant/Projection/Type: Entities Graph'
  - Subject/Graph Relation
version: 18
updated_at: 2026-10-26 17:20:40 +0400
relations: {}
atom_id: CA-R-1436@18
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Definition
---
# Summary

Define IS_ALLOWED_VALUE_OF

## Scope

the IS_ALLOWED_VALUE_OF Relation **in** the Entities Graph.

## Claim

an IS_ALLOWED_VALUE_OF Relation from value V **to** Property P **in** the Entities Graph **means** that governing authority admits V as a possible value of P **in** its qualified context; this Relation does **not** assign V **to** a particular Property occurrence **or** determine that Property's cardinality.
