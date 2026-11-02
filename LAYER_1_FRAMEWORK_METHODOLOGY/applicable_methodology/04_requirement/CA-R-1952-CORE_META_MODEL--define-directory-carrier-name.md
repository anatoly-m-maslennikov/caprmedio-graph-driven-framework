---
atom_id: CA-R-1952
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Entity/Carrier/Directory Carrier.Name
relations:
  child_of:
  - CA-R-1174
version: 1
updated_at: "2026-10-17 17:33:52 +0400"
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1952-CORE_META_MODEL--define-directory-carrier-name.md
  source_atom_id: CA-R-1952
  source_atom_revision: 1
  source_sha256: 23f39a7a3966cc4413a3ca049fff2dfbf961b11d020508e936e54e963ad06b68
  original_relations_sha256: 2e54810b23dc6829999889d9dce55018a30d8606de806fb64b6f8578b2c66336
---
# Summary

Define Directory Carrier.Name

## Scope

Directory Carrier names within their parent directories.

## Claim

A Directory Carrier's Name **means** the name of its directory within its parent directory, excluding the parent path.

## Details

CA-D-297 and CA-D-299 constrain authority and Delivery directory names. CA-D-445 permits explicit native layouts. The directory name is not universally identical to the carried Scope Unit's Name.

Active CA-R-1342 currently assigns Carrier definitions and classification to Delivery. That conflict remains for the later content migration; this draft does not change or supersede active rules.
