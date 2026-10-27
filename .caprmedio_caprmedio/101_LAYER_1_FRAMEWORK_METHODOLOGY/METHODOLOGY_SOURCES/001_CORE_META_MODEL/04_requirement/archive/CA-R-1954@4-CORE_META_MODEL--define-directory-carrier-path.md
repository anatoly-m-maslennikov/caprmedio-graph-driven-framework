---
atom_id: CA-R-1954@4
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Subject/Engineering/Carrier/Directory Carrier.Path
relations:
  child_of:
  - CA-R-1174
version: 4
updated_at: 2026-10-24 01:37:42 +0400
tier: 3
type: Definition
---
# Summary

Define Directory Carrier.Path

## Scope

Directory Carrier filesystem locators.

## Claim

A Directory Carrier's Path **means** the locator of its directory within a filesystem, absolute or relative to a stated base. It does **not** define Scope Unit parentage or Carrier identity.

## Details

CA-D-445 separates physical layout from declared hierarchy; CA-R-1660 says physical containment must not silently replace logical parentage. The Operator distinguishes Carrier ID from path.

Active CA-R-1342 currently assigns Carrier definitions and classification to Delivery. That conflict remains for the later content migration; this draft does not change or supersede active rules.
