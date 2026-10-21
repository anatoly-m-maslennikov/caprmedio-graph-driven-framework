---
atom_id: CA-R-1955
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Entity/Carrier/Database Carrier
relations:
  child_of:
  - CA-R-1174
version: 1
updated_at: "2026-10-17 17:08:59 +0400"
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1955-CORE_META_MODEL--define-entity-carrier-database-carrier.md
  source_atom_id: CA-R-1955
  source_atom_revision: 1
  source_sha256: 0ff4189a029c177fcd1675188d88fa120478baef1545bd731b210106d5582912
  original_relations_sha256: 2e54810b23dc6829999889d9dce55018a30d8606de806fb64b6f8578b2c66336
---
# Summary

Define Entity/Carrier/Database Carrier

## Scope

Database Carriers.

## Claim

A Database Carrier **means** a Carrier that represents content in a database.

## Details

Candidate #6 explicitly admits Database Carrier. CA-R-1745 permits local or remote databases as Journal storage. This draft selects no database technology or table/row granularity.

Active CA-R-1342 currently assigns Carrier definitions and classification to Delivery. That conflict remains for the later content migration; this draft does not change or supersede active rules.
