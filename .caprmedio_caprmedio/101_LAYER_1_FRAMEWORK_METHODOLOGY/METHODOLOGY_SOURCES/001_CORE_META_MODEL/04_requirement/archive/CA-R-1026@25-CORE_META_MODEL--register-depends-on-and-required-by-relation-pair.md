---
subjects:
  governs: Entity/Graph Syntax > Relation
  depends_on:
  - Entity/Graph Syntax > Relation
  - Entity/Object/Continuant/Term//Artifact
version: 25
updated_at: 2026-10-29 07:45:26 +0400
relations: {}
atom_id: CA-R-1026@25
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Entity Definition
---
## Summary

Register depends_on and required_by relation pair

## Claim scope

the `depends_on` **and** `required_by` relation pair.

## Claim

`depends_on` **means** a direct dependency-ordering relation from a dependent Artifact **to** its prerequisite Artifact, with `required_by` as its inverse-derived view. Plan start dependencies use the Plan Graph's `BLOCKS` under CA-R-1580 instead; this Relation Kind **must not** duplicate that scheduling fact.

## Details
