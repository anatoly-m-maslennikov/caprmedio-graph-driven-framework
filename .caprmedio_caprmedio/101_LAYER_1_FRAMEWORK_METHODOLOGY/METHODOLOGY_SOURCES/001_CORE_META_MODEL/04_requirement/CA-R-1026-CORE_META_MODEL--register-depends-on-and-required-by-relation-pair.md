---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Relation
  depends_on:
  - Subject/CAPRMEDIO/Graph/Relation
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Term//Artifact
version: 23
updated_at: 2026-10-27 19:59:49 +0400
relations: {}
atom_id: CA-R-1026
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Definition
---
# Summary

Register depends_on and required_by relation pair

## Scope

the `depends_on` **and** `required_by` relation pair.

## Claim

`depends_on` **means** a direct dependency-ordering relation from a dependent Artifact **to** its prerequisite Artifact, with `required_by` as its inverse-derived view. Plan start dependencies use the Plan Graph's `BLOCKS` under CA-R-1580 instead; this Relation Kind **must not** duplicate that scheduling fact.

## Details
