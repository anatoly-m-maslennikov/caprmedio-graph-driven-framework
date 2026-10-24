---
atom_id: CA-R-1953@1
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Entity/Carrier/Directory Carrier.Numeric Prefix
relations:
  child_of:
  - CA-R-1174
version: 1
updated_at: "2026-10-17 17:34:57 +0400"
---
# Summary

Define Directory Carrier.Numeric Prefix

## Scope

Directory Carrier names whose applicable naming convention uses a numeric prefix.

## Claim

A Directory Carrier's Numeric Prefix **means** the leading numeric part of its Name when the applicable naming convention uses one.

## Details

CA-D-300 specifies the default-convention encoding from Structural Level and Navigational Order Number. CA-D-445 allows explicit native bindings. This definition does not require a prefix for every directory.

Active CA-R-1342 currently assigns Carrier definitions and classification to Delivery. That conflict remains for the later content migration; this draft does not change or supersede active rules.
