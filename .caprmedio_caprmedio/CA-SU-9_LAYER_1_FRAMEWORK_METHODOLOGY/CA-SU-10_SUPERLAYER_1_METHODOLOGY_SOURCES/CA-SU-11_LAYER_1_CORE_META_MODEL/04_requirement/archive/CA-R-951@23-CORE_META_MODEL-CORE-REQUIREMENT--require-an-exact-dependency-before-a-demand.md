---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Requirement/Type: Demand'
  depends_on:
  - Consumer Goal
  - Producer Result
version: 23
updated_at: 2026-10-24 01:37:42 +0400
relations:
  child_of:
  - CA-R-933
atom_id: CA-R-951@23
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary
Require an exact dependency before a Demand

## Scope

Consumer Scope Units with an accepted Goal.

## Claim

a Consumer Scope Unit **must** own a Demand Atom **only** **when** its accepted Goal authorizes an exact dependency on the demanded Producer result.

## Details
