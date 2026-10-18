---
atom_id: CA-R-1949
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Entity/Carrier.Canonical Address
relations:
  child_of:
  - CA-R-1174
version: 1
updated_at: "2026-10-17 17:29:08 +0400"
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1949-CORE_META_MODEL--define-carrier-canonical-address.md
  source_atom_id: CA-R-1949
  source_atom_revision: 1
  source_sha256: ae7495ce78ce7efe5f85e2563e32e7c828700f65cf94dee86b4ba158a793ff01
  original_relations_sha256: 2e54810b23dc6829999889d9dce55018a30d8606de806fb64b6f8578b2c66336
---
# Summary

Define Carrier.Canonical Address

## Scope

Canonical locators of Carriers.

## Claim

A Carrier's Canonical Address **means** its designated locator under the applicable addressing rules. It is **not** the Carrier's ID.

## Details

CA-D-267 refers to registered canonical Carrier addresses; CA-D-301 governs address segments. The Operator distinguishes Carrier ID from filename/path. CA-D-267's non-Atom property-derivation policy is not made universal here.

Active CA-R-1342 currently assigns Carrier definitions and classification to Delivery. That conflict remains for the later content migration; this draft does not change or supersede active rules.
