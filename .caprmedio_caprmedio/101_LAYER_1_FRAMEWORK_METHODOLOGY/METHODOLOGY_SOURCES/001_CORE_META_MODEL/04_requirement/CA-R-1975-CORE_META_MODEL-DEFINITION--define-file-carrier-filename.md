---
atom_id: CA-R-1975
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Subject/CAPRMEDIO/Carrier/File.Filename
relations:
  child_of:
  - CA-R-1174
version: 8
updated_at: 2026-10-27 20:00:06 +0400
tier: 3
type: Definition
---
# Summary

Define File Carrier.Filename

## Scope

File Carrier names within their containing directories.

## Claim

A File Carrier's Filename **means** the name of its file within its containing directory, including any extension. It does **not** include the directory path.

## Details

CA-D-283 specifies filenames; CA-D-284 distinguishes filename tokens, Summary Slug and extension. Their concrete serialization patterns remain Delivery rules.

Active CA-R-1342 currently assigns Carrier definitions and classification to Delivery. That conflict remains for the later content migration; this draft does not change or supersede active rules.
