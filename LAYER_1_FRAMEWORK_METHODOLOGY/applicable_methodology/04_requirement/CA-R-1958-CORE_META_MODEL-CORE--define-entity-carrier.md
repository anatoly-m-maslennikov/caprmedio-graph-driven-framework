---
atom_id: CA-R-1958
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Core
global_tier: 9
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Entity/Carrier
relations:
  child_of:
  - CA-R-1174
version: 1
updated_at: "2026-10-17 17:03:50 +0400"
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1958-CORE_META_MODEL-CORE--define-entity-carrier.md
  source_atom_id: CA-R-1958
  source_atom_revision: 1
  source_sha256: 3e3cc9f292dc0f3c460720349baac513e0e4bdcb1cbacbc5ae099c4bb91d8e19
  original_relations_sha256: 2e54810b23dc6829999889d9dce55018a30d8606de806fb64b6f8578b2c66336
---
# Summary

Define Entity/Carrier

## Scope

Carrier representations of Continuants.

## Claim

A Carrier **means** a storage representation of a Continuant, distinct from what it represents. A Carrier can represent a record of an Occurrent, **not** the Occurrent itself.

## Details

Candidate #6 retains Carrier as a separate root. CA-D-256 describes storage or representation of non-ephemeral Entities; CA-D-414 classifies Carrier. This draft does not adopt CA-D-505's obsolete binding-property notation.

Active CA-R-1342 currently assigns Carrier definitions and classification to Delivery. That conflict remains for the later content migration; this draft does not change or supersede active rules.
