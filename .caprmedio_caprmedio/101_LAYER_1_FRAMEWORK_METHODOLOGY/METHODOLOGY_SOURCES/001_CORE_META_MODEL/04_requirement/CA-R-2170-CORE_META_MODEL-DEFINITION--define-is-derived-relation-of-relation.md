---
atom_id: CA-R-2170
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
author: Anatoly Maslennikov
status: Active
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Relation/Type: IS_DERIVED_RELATION_OF'
  depends_on:
  - Subject/CAPRMEDIO/Graph/Relation
version: 2
updated_at: 2026-10-27 20:00:08 +0400
relations: {}
tier: 1
type: Definition
---
# Summary

Define is derived relation of relation

## Scope

Type-level derivation between Relation Type instances.

## Claim

`IS_DERIVED_RELATION_OF` **means** a direct relation from one derived Relation
Type instance to one source Relation Type instance from which its relation
meaning is derived.

## Details

This relation does not itself define an endpoint transformation, source-storage
direction, mandatory evidence, provenance, or inference behavior. A
pair-specific definition states any such meaning. `IS_DERIVED_RELATION_OF` is
not `DERIVED_FROM`, which links a derived Artifact Revision to an exact source
Artifact Revision.

