---
atom_id: CA-R-1956
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Entity/Carrier/Directory Carrier
relations:
  child_of:
  - CA-R-1174
version: 1
updated_at: "2026-10-17 17:10:05 +0400"
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1956-CORE_META_MODEL--define-entity-carrier-directory-carrier.md
  source_atom_id: CA-R-1956
  source_atom_revision: 1
  source_sha256: 612f0d82033e4a21516c318a1824311d2bd8646f75dbea23561fac1b037d034b
  original_relations_sha256: 2e54810b23dc6829999889d9dce55018a30d8606de806fb64b6f8578b2c66336
---
# Summary

Define Entity/Carrier/Directory Carrier

## Scope

Directories that represent a carried Continuant.

## Claim

A Directory Carrier **means** a Carrier that uses a directory to represent its carried Continuant. Merely containing files does **not** make a directory a Directory Carrier.

## Details

CA-D-259 classifies Directory Carrier as narrower than Carrier. CA-D-451 distinguishes carrying directories from administrative placement; CA-D-464 permits a directory to represent an Atom. Their old Structural Entity and Revision wording remains for content migration.

Active CA-R-1342 currently assigns Carrier definitions and classification to Delivery. That conflict remains for the later content migration; this draft does not change or supersede active rules.
