---
atom_id: CA-R-1951@2
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Core
global_tier: 9
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Subject/Engineering/Carrier.ID
relations:
  child_of:
  - CA-R-1174
version: 2
updated_at: 2026-10-23 03:14:50 +0400
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
