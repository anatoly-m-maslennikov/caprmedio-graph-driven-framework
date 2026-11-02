---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Projection/Type: Terms Graph'
  depends_on:
  - Subject/Domain/Node/Continuant/Projection
  - Entity/Node/Continuant/Term
  - Relation Kind
  - Subject/Graph/Relation
  - CAPRMEDIO Graph
version: 18
updated_at: 2026-10-24 00:38:25 +0400
relations: {}
atom_id: CA-R-1335@18
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
---
# Summary

Define Terms Graph

## Scope

Terms Graph projections **and** their represented graph facts.

## Claim

Terms Graph **means** the Type value under Projection whose instances are derived CAPRMEDIO Graphs with native Term nodes **and** edges representing Relations admitted for that graph kind by their governing authority. their represented facts retain their appropriate source authority under CA-R-1746.

## Details

admitted external graph **or** source references under CA-R-1472 do **not** become native Term nodes merely by being referenced. those references retain their own endpoint classes **and** graph-qualified Relation authority.
