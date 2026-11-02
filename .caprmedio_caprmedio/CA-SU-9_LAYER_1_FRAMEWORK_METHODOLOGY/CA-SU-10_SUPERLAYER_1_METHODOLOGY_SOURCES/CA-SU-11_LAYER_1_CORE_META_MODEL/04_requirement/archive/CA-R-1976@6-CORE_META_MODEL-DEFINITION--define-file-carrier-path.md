---
atom_id: CA-R-1976@6
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Subject/Graph Node/Engineering/Continuant/Carrier/File Carrier.Path
relations:
  child_of:
  - CA-R-1174
version: 6
updated_at: 2026-10-25 17:32:27 +0400
tier: 3
type: Definition
---
# Summary

Define File Carrier.Path

## Scope

File Carrier filesystem locators.

## Claim

A File Carrier's Path **means** the locator of its file within a filesystem, absolute or relative to a stated base. It is a locator, **not** the Carrier's ID.

## Details

The Operator distinguishes Carrier ID from path. CA-D-445 requires unambiguous bindings inside authorized path boundaries. Path is the filesystem representation of the locator, not a second independently maintained identity.

Active CA-R-1342 currently assigns Carrier definitions and classification to Delivery. That conflict remains for the later content migration; this draft does not change or supersede active rules.
