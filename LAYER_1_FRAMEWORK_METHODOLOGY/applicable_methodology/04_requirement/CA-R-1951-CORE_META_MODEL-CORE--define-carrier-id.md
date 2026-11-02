---
atom_id: CA-R-1951
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Core
global_tier: 9
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Entity/Carrier.ID
relations:
  child_of:
  - CA-R-1174
version: 1
updated_at: "2026-10-17 17:32:45 +0400"
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1951-CORE_META_MODEL-CORE--define-carrier-id.md
  source_atom_id: CA-R-1951
  source_atom_revision: 1
  source_sha256: d47261e83bafcdd2c62a3df2e68fa8202338cda873a7346c2669d9c4d125c9d6
  original_relations_sha256: 2e54810b23dc6829999889d9dce55018a30d8606de806fb64b6f8578b2c66336
---
# Summary

Define Carrier.ID

## Scope

Identifiers of individual Carriers.

## Claim

A Carrier ID identifies one Carrier. Its filename and path are **not** its ID.

## Details

The Operator explicitly distinguished Carrier ID from filename and path. CA-D-507 separates Entity identity from Carrier format but does not define Carrier ID. This draft introduces no ID syntax, allocator or registry.

Active CA-R-1342 currently assigns Carrier definitions and classification to Delivery. That conflict remains for the later content migration; this draft does not change or supersede active rules.
