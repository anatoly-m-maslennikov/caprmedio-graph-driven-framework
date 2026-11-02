---
atom_id: CA-R-1974
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Entity/Carrier/File Carrier.Extension
relations:
  child_of:
  - CA-R-1174
version: 1
updated_at: "2026-10-17 17:37:12 +0400"
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1974-CORE_META_MODEL--define-file-carrier-extension.md
  source_atom_id: CA-R-1974
  source_atom_revision: 1
  source_sha256: 8bf2feab01ec0b2bd2730052d1028e83c29a015378ed2afd40bb3ae2cf67283c
  original_relations_sha256: 2e54810b23dc6829999889d9dce55018a30d8606de806fb64b6f8578b2c66336
---
# Summary

Define File Carrier.Extension

## Scope

File Carriers whose filename uses an extension.

## Claim

A File Carrier's Extension **means** the filename suffix used to indicate its format. The extension does **not** establish the carried Entity's identity.

## Details

CA-D-283 uses an extension segment; CA-D-284 constrains its case; CA-D-507 explicitly separates changes of extension from Entity identity. This draft does not require every file to have an extension.

Active CA-R-1342 currently assigns Carrier definitions and classification to Delivery. That conflict remains for the later content migration; this draft does not change or supersede active rules.
