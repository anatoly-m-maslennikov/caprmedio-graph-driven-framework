---
atom_id: CA-R-1963
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Core
global_tier: 9
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Entity/Relation"
relations:
  child_of:
  - CA-R-1174
version: 3
updated_at: "2026-10-19 15:54:11 +0400"
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1963-CORE_META_MODEL-CORE--define-entity-continuant-object-relation.md
  source_atom_id: CA-R-1963
  source_atom_revision: 3
  source_sha256: c38c54209c7967bc60079c86e7dc6fb47a233c2f63e2e26e9e316db039a91be6
  original_relations_sha256: 2e54810b23dc6829999889d9dce55018a30d8606de806fb64b6f8578b2c66336
---
# Summary

Define Entity/Continuant/Object/Relation

## Scope

typed connections between identified endpoints.

## Claim

a Relation **means** a typed connection between identified endpoints. its admitted kind determines the connection's meaning and direction.

## Details

Candidate #6 retains Relation under Object. CA-R-806 and CA-R-1246 govern Relation Kind metadata and graph-qualified identity; CA-R-1437 governs source authority; CA-R-1472 governs admitted endpoint contexts. This definition adds no Relation Kind, inferred connection or endpoint permission.
