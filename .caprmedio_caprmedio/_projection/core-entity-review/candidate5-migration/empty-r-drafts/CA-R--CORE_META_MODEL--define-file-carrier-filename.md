---
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Draft
author: Anatoly Maslennikov
subjects:
  governs: "Entity/Carrier/File Carrier.Filename"
version: 2
updated_at: "2026-10-16 13:07:45 +0000"
---
# Summary

Define File Carrier.Filename

## Scope

File Carrier names within their containing directories.

## Claim

A File Carrier's Filename **means** the name of its file within its containing directory, including any extension. It does **not** include the directory path.

## Details

Disposition: proposed R definition; Draft only, without an assigned Atom ID.

CA-D-283 specifies filenames; CA-D-284 distinguishes filename tokens, Summary Slug and extension. Their concrete serialization patterns remain Delivery rules.

Active CA-R-1342 currently assigns Carrier definitions and classification to Delivery. That conflict remains for the later content migration; this draft does not change or supersede active rules.
