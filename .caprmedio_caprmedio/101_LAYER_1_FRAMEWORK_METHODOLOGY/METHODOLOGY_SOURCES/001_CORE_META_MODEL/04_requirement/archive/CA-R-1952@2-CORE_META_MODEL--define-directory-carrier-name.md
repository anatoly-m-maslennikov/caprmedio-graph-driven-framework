---
atom_id: CA-R-1952@2
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Subject/Engineering/Carrier/Directory Carrier.Name
relations:
  child_of:
  - CA-R-1174
version: 2
updated_at: 2026-10-23 03:14:50 +0400
---
# Summary

Define Directory Carrier.Name

## Scope

Directory Carrier names within their parent directories.

## Claim

A Directory Carrier's Name **means** the name of its directory within its parent directory, excluding the parent path.

## Details

CA-D-297 and CA-D-299 constrain authority and Delivery directory names. CA-D-445 permits explicit native layouts. The directory name is not universally identical to the carried Scope Unit's Name.

Active CA-R-1342 currently assigns Carrier definitions and classification to Delivery. That conflict remains for the later content migration; this draft does not change or supersede active rules.
