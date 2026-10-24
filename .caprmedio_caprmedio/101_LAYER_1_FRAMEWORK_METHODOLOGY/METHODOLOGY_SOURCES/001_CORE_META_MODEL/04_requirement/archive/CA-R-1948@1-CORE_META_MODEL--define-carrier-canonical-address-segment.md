---
atom_id: CA-R-1948@1
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Entity/Carrier.Canonical Address.Segment
relations:
  child_of:
  - CA-R-1174
version: 1
updated_at: "2026-10-17 17:30:25 +0400"
---
# Summary

Define Carrier.Canonical Address.Segment

## Scope

Carriers whose canonical address format has component segments.

## Claim

A Canonical Address Segment **means** one component of a Carrier's Canonical Address under its applicable address format.

## Details

CA-D-301 governs project-owned address segments; CA-D-352 treats status subdirectories as placement components. Filesystem separators and portable-name restrictions are not imposed on every database address by this definition.

Active CA-R-1342 currently assigns Carrier definitions and classification to Delivery. That conflict remains for the later content migration; this draft does not change or supersede active rules.
