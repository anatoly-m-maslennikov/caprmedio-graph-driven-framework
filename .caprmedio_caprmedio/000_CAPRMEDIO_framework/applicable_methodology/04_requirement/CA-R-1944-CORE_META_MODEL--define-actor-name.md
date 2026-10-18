---
atom_id: CA-R-1944
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Entity/Continuant/Node/Actor.Name"
relations:
  child_of:
  - CA-R-1174
version: 2
updated_at: "2026-10-18 03:34:01 +0400"
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1944-CORE_META_MODEL--define-actor-name.md
  source_atom_id: CA-R-1944
  source_atom_revision: 2
  source_sha256: 34a6146aac6f2fbd6a39510a1c432c7edfae07deae3f014fc4bc0b7e6f777473
  original_relations_sha256: 2e54810b23dc6829999889d9dce55018a30d8606de806fb64b6f8578b2c66336
---
# Summary

Define Actor.Name

## Scope

Actor names.

## Claim

Actor.Name **means** the optional name of an Actor.

## Details

Candidate #5 makes Actor.Name optional and inherited by Actor Types; Candidate #6 retains Actor as a Continuant. CA-R-1422 defines Operator and CA-R-1552 governs AI Agent permissions, but neither defines this shared property. This draft does not make Name mandatory or prescribe its storage.
