---
atom_id: CA-R-1949
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Entity/Carrier.Canonical Address
relations:
  child_of:
  - CA-R-1174
version: 1
updated_at: "2026-10-17 17:29:08 +0400"
---
# Summary

Define Carrier.Canonical Address

## Scope

Canonical locators of Carriers.

## Claim

A Carrier's Canonical Address **means** its designated locator under the applicable addressing rules. It is **not** the Carrier's ID.

## Details

CA-D-267 refers to registered canonical Carrier addresses; CA-D-301 governs address segments. The Operator distinguishes Carrier ID from filename/path. CA-D-267's non-Atom property-derivation policy is not made universal here.

Active CA-R-1342 currently assigns Carrier definitions and classification to Delivery. That conflict remains for the later content migration; this draft does not change or supersede active rules.
