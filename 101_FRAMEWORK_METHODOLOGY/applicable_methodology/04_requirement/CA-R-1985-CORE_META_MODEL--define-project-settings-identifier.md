---
atom_id: CA-R-1985
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Entity/Continuant/Node/Project.Settings.Identifier"
relations:
  child_of:
  - CA-R-1174
version: 2
updated_at: "2026-10-18 03:34:05 +0400"
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1985-CORE_META_MODEL--define-project-settings-identifier.md
  source_atom_id: CA-R-1985
  source_atom_revision: 2
  source_sha256: 7f04f13c4e33f473910448294ada74ea56fae9f4e128dcb9d2f502be90c220a1
  original_relations_sha256: 2e54810b23dc6829999889d9dce55018a30d8606de806fb64b6f8578b2c66336
---
# Summary

Define Project.Settings.Identifier

## Scope

the identifier of a Project's authoritative Settings configuration.

## Claim

Project Settings Identifier identifies the Project's authoritative Settings configuration, **not** an Atom.

## Details

Evidence: CA-R-1738 defines Project Settings, CA-R-1401 keeps it outside the Atom type, and CA-D-362 supplies concrete identification. Candidate #6 decisions 11 and 18 preserve the Project path and distinguish Project identity from the delivered framework's name. This generic definition adds no filename, identifier spelling or duplicate Project Name setting.
