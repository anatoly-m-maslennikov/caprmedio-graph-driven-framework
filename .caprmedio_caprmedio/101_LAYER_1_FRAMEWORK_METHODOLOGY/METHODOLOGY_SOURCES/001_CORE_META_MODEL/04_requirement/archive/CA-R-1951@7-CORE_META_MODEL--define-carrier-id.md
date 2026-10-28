---
atom_id: CA-R-1951@7
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Subject/Graph Node/Carrier.ID
relations:
  child_of:
  - CA-R-1174
version: 7
updated_at: 2026-10-27 06:04:45 +0400
tier: 1
type: Rule
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
