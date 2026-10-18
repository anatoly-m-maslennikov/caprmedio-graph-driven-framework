---
atom_id: CA-R-1993
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Core
global_tier: 9
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Entity/Continuant/Relation/Type: CARRIES"
  depends_on:
  - Entity/Carrier
  - Entity
  - "Entity/Continuant/Relation"
relations:
  child_of:
  - CA-R-1174
version: 2
updated_at: "2026-10-18 03:34:08 +0400"
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1993-CORE_META_MODEL--define-carries.md
  source_atom_id: CA-R-1993
  source_atom_revision: 2
  source_sha256: 464824af0f5b46666649b644845894a80648203ed5c48ba021b03983ee4536b7
  original_relations_sha256: 2e54810b23dc6829999889d9dce55018a30d8606de806fb64b6f8578b2c66336
---
# Summary

Define CARRIES

## Scope

Carrier bindings of non-ephemeral Entities.

## Claim

CARRIES **means** the directed Relation from a Carrier **to** the non-ephemeral Entity that it stores **or** represents.

## Details

IS_CARRIED_BY **means** the inverse of CARRIES, directed from a non-ephemeral Entity to its Carrier. The Entity/Carrier binding exposes this inverse direction; it is not a separately authored primitive Relation fact. This preserves the existing meaning defined by CA-D-257. Neither direction requires a separately registered binding for each YAML field or Markdown section, a new Carrier, a snapshot or a historical record. The applicable D policy specifies how the represented Entity is bound and represented. No additional endpoint class, graph ownership, cardinality or inference permission is introduced by moving this definition to R.
