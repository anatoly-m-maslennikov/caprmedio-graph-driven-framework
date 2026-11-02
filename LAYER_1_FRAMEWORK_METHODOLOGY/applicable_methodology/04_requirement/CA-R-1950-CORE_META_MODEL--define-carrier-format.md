---
atom_id: CA-R-1950
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Entity/Carrier.Format
relations:
  child_of:
  - CA-R-1174
version: 1
updated_at: "2026-10-17 17:31:34 +0400"
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1950-CORE_META_MODEL--define-carrier-format.md
  source_atom_id: CA-R-1950
  source_atom_revision: 1
  source_sha256: 765a46f18ab03d3fd6100849f4dce969adce51b313c3044b59612c8b82b41356
  original_relations_sha256: 2e54810b23dc6829999889d9dce55018a30d8606de806fb64b6f8578b2c66336
---
# Summary

Define Carrier.Format

## Scope

Carriers with an applicable representation format.

## Claim

A Carrier's Format **means** the rules for encoding and interpreting its represented content.

## Details

CA-D-262 admits registered File Carrier formats including Markdown, TOML, YAML and JSON; CA-D-507 distinguishes format from identity. This definition does not require a format value for every Directory Carrier.

Active CA-R-1342 currently assigns Carrier definitions and classification to Delivery. That conflict remains for the later content migration; this draft does not change or supersede active rules.
