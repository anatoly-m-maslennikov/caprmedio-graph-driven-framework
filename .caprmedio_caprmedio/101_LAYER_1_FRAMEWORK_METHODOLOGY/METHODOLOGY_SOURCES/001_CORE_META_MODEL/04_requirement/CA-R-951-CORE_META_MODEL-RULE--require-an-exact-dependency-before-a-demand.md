---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Requirement/Type: Demand'
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
version: 29
updated_at: 2026-10-27 20:00:12 +0400
relations:
  child_of:
  - CA-R-933
atom_id: CA-R-951
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
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
