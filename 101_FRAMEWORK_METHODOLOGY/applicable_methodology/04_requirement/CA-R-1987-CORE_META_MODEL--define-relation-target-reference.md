---
atom_id: CA-R-1987
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Entity/Continuant/Relation.Target Reference"
relations:
  child_of:
  - CA-R-1174
version: 2
updated_at: "2026-10-18 03:34:06 +0400"
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1987-CORE_META_MODEL--define-relation-target-reference.md
  source_atom_id: CA-R-1987
  source_atom_revision: 2
  source_sha256: 05c00e2b595c0e0aff5756c7b6cef6c804202f400374a600da5db0909e458e5f
  original_relations_sha256: 2e54810b23dc6829999889d9dce55018a30d8606de806fb64b6f8578b2c66336
---
# Summary

Define Relation.Target Reference

## Scope

the target endpoint of a Relation.

## Claim

Relation.Target Reference **means** the reference to the endpoint to which the Relation's declared direction points.

## Details

Candidate #5 includes Source Reference and Target Reference as Relation properties. CA-R-1017 gives a concrete directed relation; CA-R-1472 governs endpoint admission and CA-D-268 governs target serialization for authored Atom relations. This definition changes no endpoint eligibility, direction, cardinality or storage syntax.
