---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Relation/Type
  depends_on:
  - Subject
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
version: 36
updated_at: 2026-10-27 20:00:11 +0400
relations: {}
atom_id: CA-R-806
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 2
type: Rule
---
# Summary

Register Complete Relation Kind Metadata

## Scope

admitted Relation Types and their defining source Claims.

## Claim

The canonical name and meaning of each Relation Type **are** defined in its governing R Claim(s). A governing Claim **may** state a relevant inverse, derivation, or transitivity rule; no such optional property is required when it is not relevant.

## Details

Relation Type names are shared and unique in the Project. Existing Graph Rules, where applicable, supply graph-specific admission, endpoint classes, endpoint graph contexts, cardinality, and other permissions or prohibitions; this contract does not require a separate Graph Rule for every known Type or choose default-allow/default-deny semantics. The Type definition retains its canonical meaning and any evidenced optional inverse, derivation, or transitivity semantics. A declared direct direction identifies the one authored fact where relevant; inverse or derived navigation remains derived under its defining authority. A name such as IS_CONTAINED_BY does not make that direction an inverse. Existing endpoint and admissibility constraints remain in their governing Graph Rules; this contract does not itself rewrite them.
