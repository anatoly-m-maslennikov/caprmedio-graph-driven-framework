---
atom_id: CA-R-1976
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Entity/Carrier/File Carrier.Path
relations:
  child_of:
  - CA-R-1174
version: 1
updated_at: "2026-10-17 17:39:30 +0400"
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1976-CORE_META_MODEL--define-file-carrier-path.md
  source_atom_id: CA-R-1976
  source_atom_revision: 1
  source_sha256: c21111551352de005fd9696f63d9f7c2c298aa324efabfabc4a10240afa68841
  original_relations_sha256: 2e54810b23dc6829999889d9dce55018a30d8606de806fb64b6f8578b2c66336
---
# Summary

Define File Carrier.Path

## Scope

File Carrier filesystem locators.

## Claim

A File Carrier's Path **means** the locator of its file within a filesystem, absolute or relative to a stated base. It is a locator, **not** the Carrier's ID.

## Details

The Operator distinguishes Carrier ID from path. CA-D-445 requires unambiguous bindings inside authorized path boundaries. Path is the filesystem representation of the locator, not a second independently maintained identity.

Active CA-R-1342 currently assigns Carrier definitions and classification to Delivery. That conflict remains for the later content migration; this draft does not change or supersede active rules.
