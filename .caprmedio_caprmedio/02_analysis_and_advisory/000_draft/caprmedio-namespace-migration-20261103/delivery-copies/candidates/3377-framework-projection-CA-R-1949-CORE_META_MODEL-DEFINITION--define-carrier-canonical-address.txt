---
atom_id: CA-R-1949
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Carrier.Canonical Address
relations:
  child_of:
  - CA-R-1174
version: 11
updated_at: 2026-11-02 00:18:22 +0400
tier: 3
role: Requirement
form: Entity Definition
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1949-CORE_META_MODEL-DEFINITION--define-carrier-canonical-address.md
  source_atom_id: CA-R-1949
  source_atom_revision: 11
  source_sha256: 8584be41c1182031fe07dad762bd8d3a55842a7317d57e6f45bcfab3b40b92f7
  original_relations_sha256: 2e54810b23dc6829999889d9dce55018a30d8606de806fb64b6f8578b2c66336
---
## Summary

Define Carrier.Canonical Address

## Claim scope

Canonical locators of Carriers.

## Claim

A Carrier's Canonical Address **means** its designated locator under the applicable addressing rules. It is **not** the Carrier's ID.

## Details

CA-D-267 refers to registered canonical Carrier addresses; CA-D-301 governs address segments. The Operator distinguishes Carrier ID from filename/path. CA-D-267's non-Atom property-derivation policy is not made universal here.

Active CA-R-2515 currently assigns Carrier definitions and classification to Delivery. That conflict remains for the later content migration; this draft does not change or supersede active rules.
