---
atom_id: CA-R-1957
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Entity/Carrier/File Carrier
relations:
  child_of:
  - CA-R-1174
version: 1
updated_at: "2026-10-17 17:12:05 +0400"
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1957-CORE_META_MODEL--define-entity-carrier-file-carrier.md
  source_atom_id: CA-R-1957
  source_atom_revision: 1
  source_sha256: 1803b14c2fd93e40eccdf365b0e3b6ee6ba4b36309595bbca4352227d4cad571
  original_relations_sha256: 2e54810b23dc6829999889d9dce55018a30d8606de806fb64b6f8578b2c66336
---
# Summary

Define Entity/Carrier/File Carrier

## Scope

File Carriers.

## Claim

A File Carrier **means** a Carrier that represents content in a file.

## Details

CA-D-258 classifies File Carrier as narrower than Carrier; CA-D-283 and CA-D-356 specify file representations. Filename and format conventions remain Delivery rules.

Active CA-R-1342 currently assigns Carrier definitions and classification to Delivery. That conflict remains for the later content migration; this draft does not change or supersede active rules.
