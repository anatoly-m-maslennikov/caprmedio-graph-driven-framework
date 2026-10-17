---
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Draft
author: Anatoly Maslennikov
subjects:
  governs: "Entity/Carrier.Canonical Address.Segment"
version: 2
updated_at: "2026-10-16 13:07:45 +0000"
---
# Summary

Define Carrier.Canonical Address.Segment

## Scope

Carriers whose canonical address format has component segments.

## Claim

A Canonical Address Segment **means** one component of a Carrier's Canonical Address under its applicable address format.

## Details

Disposition: proposed R definition; Draft only, without an assigned Atom ID.

CA-D-301 governs project-owned address segments; CA-D-352 treats status subdirectories as placement components. Filesystem separators and portable-name restrictions are not imposed on every database address by this definition.

Active CA-R-1342 currently assigns Carrier definitions and classification to Delivery. That conflict remains for the later content migration; this draft does not change or supersede active rules.
