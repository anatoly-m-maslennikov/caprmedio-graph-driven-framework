---
atom_id: CA-R-1975
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Entity/Carrier/File Carrier.Filename
relations:
  child_of:
  - CA-R-1174
version: 1
updated_at: "2026-10-17 17:38:18 +0400"
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1975-CORE_META_MODEL--define-file-carrier-filename.md
  source_atom_id: CA-R-1975
  source_atom_revision: 1
  source_sha256: e9d17bc02c184450420594071cf7fa4371a7296c6cd5c3cc6caa1cb1dec6a33f
  original_relations_sha256: 2e54810b23dc6829999889d9dce55018a30d8606de806fb64b6f8578b2c66336
---
# Summary

Define File Carrier.Filename

## Scope

File Carrier names within their containing directories.

## Claim

A File Carrier's Filename **means** the name of its file within its containing directory, including any extension. It does **not** include the directory path.

## Details

CA-D-283 specifies filenames; CA-D-284 distinguishes filename tokens, Summary Slug and extension. Their concrete serialization patterns remain Delivery rules.

Active CA-R-1342 currently assigns Carrier definitions and classification to Delivery. That conflict remains for the later content migration; this draft does not change or supersede active rules.
