---
atom_id: CA-R-1966
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Core
global_tier: 9
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Entity/Continuant/Node/Selection"
relations:
  child_of:
  - CA-R-1174
version: 2
updated_at: "2026-10-18 03:34:04 +0400"
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1966-CORE_META_MODEL-CORE--define-entity-continuant-selection.md
  source_atom_id: CA-R-1966
  source_atom_revision: 2
  source_sha256: 97a3d356abda8b102dcc8cff55545c8a096b4abbf5e53e390bb24c2181add015
  original_relations_sha256: 2e54810b23dc6829999889d9dce55018a30d8606de806fb64b6f8578b2c66336
---
# Summary

Define Entity/Continuant/Selection

## Scope

Selections and named Selections.

## Claim

a Selection **means** criteria for choosing members. a named Selection gives those criteria a name; it does **not** create another Object or independent copies of the selected members.

## Details

Candidate #6 preserves Selection separately from Object and concrete named selections separately from abstract Core kinds. CA-R-1447 defines Owned Atoms and CA-R-1448 defines Targeting Atoms; they define particular selections, not the general kind. This draft adds no selector syntax or mandatory materialization.
