---
atom_id: CA-R-1950@1
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Entity/Carrier.Format
relations:
  child_of:
  - CA-R-1174
version: 1
updated_at: "2026-10-17 17:31:34 +0400"
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
