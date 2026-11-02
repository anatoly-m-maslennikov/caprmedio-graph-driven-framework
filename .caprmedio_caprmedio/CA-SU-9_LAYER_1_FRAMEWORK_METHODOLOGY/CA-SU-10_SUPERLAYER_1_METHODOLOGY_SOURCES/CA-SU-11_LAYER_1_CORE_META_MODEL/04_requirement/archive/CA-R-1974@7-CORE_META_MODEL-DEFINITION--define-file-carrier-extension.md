---
atom_id: CA-R-1974@7
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Subject/Graph Node/Carrier/File.Extension
relations:
  child_of:
  - CA-R-1174
version: 7
updated_at: 2026-10-27 06:04:45 +0400
tier: 3
type: Definition
---
# Summary

Define File Carrier.Extension

## Scope

File Carriers whose filename uses an extension.

## Claim

A File Carrier's Extension **means** the filename suffix used to indicate its format. The extension does **not** establish the carried Entity's identity.

## Details

CA-D-283 uses an extension segment; CA-D-284 constrains its case; CA-D-507 explicitly separates changes of extension from Entity identity. This draft does not require every file to have an extension.

Active CA-R-1342 currently assigns Carrier definitions and classification to Delivery. That conflict remains for the later content migration; this draft does not change or supersede active rules.
