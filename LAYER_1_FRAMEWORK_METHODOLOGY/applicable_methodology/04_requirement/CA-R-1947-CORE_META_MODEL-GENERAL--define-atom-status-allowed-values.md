---
atom_id: CA-R-1947
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: General
global_tier: 10
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Entity/Node/Continuant/Atom.Status"
relations:
  child_of:
  - CA-R-1174
version: 3
updated_at: "2026-10-19 15:54:10 +0400"
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1947-CORE_META_MODEL-GENERAL--define-atom-status-allowed-values.md
  source_atom_id: CA-R-1947
  source_atom_revision: 3
  source_sha256: ca65ea189912acb3605517a2a8dbe3e76cb402dc018df6d6ca167decd16b218f
  original_relations_sha256: 2e54810b23dc6829999889d9dce55018a30d8606de806fb64b6f8578b2c66336
---
# Summary

Define Atom.Status allowed values

## Scope

The base allowed values inherited by narrower Atom kinds.

## Claim

Atom.Status **must** admit (Draft, Active, Archived). Narrower Atom kinds inherit these values and **may** add allowed values under their applicable Content Role or Type. An inherited value does **not** require a separate declaration for every narrower kind.

## Details

CA-R-1412 requires exactly one Status but does not declare the base allowed values. CA-R-1309 declares Draft, Active and Archived only for Requirements; it must not be retargeted to all Atoms as a Subjects-only change.

Later content alignment is needed: CA-R-1539's exact Plan set excludes inherited Draft, CA-R-1875's Analysis set excludes inherited Active, and CA-R-1608 uses a different Concern spelling/domain. C/A content remains deferred. CA-R-1308 and CA-R-1313 also need alignment with additive inheritance. This draft does not change transition procedures, existing Status values or any active source.
