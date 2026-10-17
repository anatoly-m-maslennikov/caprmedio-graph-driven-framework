---
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Draft
author: Anatoly Maslennikov
subjects:
  governs: "Entity/Carrier/File Carrier.Extension"
version: 2
updated_at: "2026-10-16 13:07:45 +0000"
---
# Summary

Define File Carrier.Extension

## Scope

File Carriers whose filename uses an extension.

## Claim

A File Carrier's Extension **means** the filename suffix used to indicate its format. The extension does **not** establish the carried Entity's identity.

## Details

Disposition: proposed R definition; Draft only, without an assigned Atom ID.

CA-D-283 uses an extension segment; CA-D-284 constrains its case; CA-D-507 explicitly separates changes of extension from Entity identity. This draft does not require every file to have an extension.

Active CA-R-1342 currently assigns Carrier definitions and classification to Delivery. That conflict remains for the later content migration; this draft does not change or supersede active rules.
