---
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Requirement/Type: Demand'
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom
version: 28
updated_at: 2026-10-25 17:32:27 +0400
relations:
  child_of:
  - CA-R-933
atom_id: CA-R-951@28
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 6
type: Rule
---
# Summary
Require an exact dependency before a Demand

## Scope

Consumer Scope Units with an accepted Goal.

## Claim

a Consumer Scope Unit **must** own a Demand Atom **only** **when** its accepted Goal authorizes an exact dependency on the demanded Producer result.

## Details
