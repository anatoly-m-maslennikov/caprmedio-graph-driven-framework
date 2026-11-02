---
atom_id: CA-R-1954
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Entity/Carrier/Directory Carrier.Path
relations:
  child_of:
  - CA-R-1174
version: 1
updated_at: "2026-10-17 17:36:06 +0400"
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1954-CORE_META_MODEL--define-directory-carrier-path.md
  source_atom_id: CA-R-1954
  source_atom_revision: 1
  source_sha256: cad2daf5cfb5207e07b41cff1721b20799089f78483664f3e14fe819619fdbd5
  original_relations_sha256: 2e54810b23dc6829999889d9dce55018a30d8606de806fb64b6f8578b2c66336
---
# Summary

Define Directory Carrier.Path

## Scope

Directory Carrier filesystem locators.

## Claim

A Directory Carrier's Path **means** the locator of its directory within a filesystem, absolute or relative to a stated base. It does **not** define Scope Unit parentage or Carrier identity.

## Details

CA-D-445 separates physical layout from declared hierarchy; CA-R-1660 says physical containment must not silently replace logical parentage. The Operator distinguishes Carrier ID from path.

Active CA-R-1342 currently assigns Carrier definitions and classification to Delivery. That conflict remains for the later content migration; this draft does not change or supersede active rules.
