---
atom_id: CA-R-1988
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Core
global_tier: 9
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Entity/Continuant/Node/Scope Unit.ID"
relations:
  child_of:
  - CA-R-1174
version: 2
updated_at: "2026-10-18 03:34:06 +0400"
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1988-CORE_META_MODEL-CORE--define-scope-unit-id.md
  source_atom_id: CA-R-1988
  source_atom_revision: 2
  source_sha256: 0d016b6b3a5c807b9fc75dcabb884cff5849dbda3d796d2fe8b205e76804dc01
  original_relations_sha256: 2e54810b23dc6829999889d9dce55018a30d8606de806fb64b6f8578b2c66336
---
# Summary

Define Scope Unit.ID

## Scope

Scope Unit identifiers.

## Claim

Scope Unit.ID **means** the identifier of one Scope Unit, distinct from its Name, Label and Path.

## Details

The Operator accepted a separate Scope Unit ID, and Candidate #5 includes it as an inherited property of Scope Unit Types. Candidate #6 decision 22 defines Path from parentage. CA-R-962 and CA-R-970 govern Name and its uniqueness; they do not define ID. This draft adds no new storage field or rename procedure.
