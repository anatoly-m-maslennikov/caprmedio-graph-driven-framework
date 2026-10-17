---
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Draft
author: Anatoly Maslennikov
subjects:
  governs: "Entity/Carrier/File Carrier.Path"
version: 2
updated_at: "2026-10-16 13:07:45 +0000"
---
# Summary

Define File Carrier.Path

## Scope

File Carrier filesystem locators.

## Claim

A File Carrier's Path **means** the locator of its file within a filesystem, absolute or relative to a stated base. It is a locator, **not** the Carrier's ID.

## Details

Disposition: proposed R definition; Draft only, without an assigned Atom ID.

The Operator distinguishes Carrier ID from path. CA-D-445 requires unambiguous bindings inside authorized path boundaries. Path is the filesystem representation of the locator, not a second independently maintained identity.

Active CA-R-1342 currently assigns Carrier definitions and classification to Delivery. That conflict remains for the later content migration; this draft does not change or supersede active rules.
