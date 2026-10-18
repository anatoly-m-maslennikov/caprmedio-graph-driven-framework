---
atom_id: CA-R-1953
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Entity/Carrier/Directory Carrier.Numeric Prefix
relations:
  child_of:
  - CA-R-1174
version: 1
updated_at: "2026-10-17 17:34:57 +0400"
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1953-CORE_META_MODEL--define-directory-carrier-numeric-prefix.md
  source_atom_id: CA-R-1953
  source_atom_revision: 1
  source_sha256: 684a0517447bd09d8d9537ae6330196bd99da0b74aa3b0d0df13dbc44f0f93f9
  original_relations_sha256: 2e54810b23dc6829999889d9dce55018a30d8606de806fb64b6f8578b2c66336
---
# Summary

Define Directory Carrier.Numeric Prefix

## Scope

Directory Carrier names whose applicable naming convention uses a numeric prefix.

## Claim

A Directory Carrier's Numeric Prefix **means** the leading numeric part of its Name when the applicable naming convention uses one.

## Details

CA-D-300 specifies the default-convention encoding from Structural Level and Navigational Order Number. CA-D-445 allows explicit native bindings. This definition does not require a prefix for every directory.

Active CA-R-1342 currently assigns Carrier definitions and classification to Delivery. That conflict remains for the later content migration; this draft does not change or supersede active rules.
