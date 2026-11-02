---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  - 'Entity/Node/Continuant/Atom/Content Role: Plan.Status: Done'
version: 10
updated_at: 2026-10-23 03:06:32 +0400
relations:
  relates_to:
  - CA-R-1580
  - CA-R-1583
  - CA-R-1538
atom_id: CA-R-1592@10
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: General
status: Archived
author: Anatoly Maslennikov
global_tier: 10
---
# Summary

Keep Plan completion prerequisites acyclic

## Scope

Plan execution.

## Claim

Plan execution **must not** contain a cycle of completion prerequisites, including one formed jointly by `BLOCKS` **and** the requirement **to** complete decomposed work **before** its Hub can be Done.

## Details
