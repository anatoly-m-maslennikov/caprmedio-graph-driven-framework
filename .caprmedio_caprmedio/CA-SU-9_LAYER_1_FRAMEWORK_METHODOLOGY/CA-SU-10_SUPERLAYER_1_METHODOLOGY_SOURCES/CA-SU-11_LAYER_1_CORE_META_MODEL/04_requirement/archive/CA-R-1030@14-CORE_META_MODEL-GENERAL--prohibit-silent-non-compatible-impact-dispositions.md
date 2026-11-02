---
subjects:
  governs: Subject/Graph/Relation
  depends_on:
  - atom-boundary
version: 14
updated_at: 2026-10-23 03:06:32 +0400
relations: {}
atom_id: CA-R-1030@14
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: General
status: Archived
author: Anatoly Maslennikov
global_tier: 10
---
# Prohibit silent non-compatible Impact dispositions

## Scope

the selection of non-compatible Impact dispositions.

## Claim

TOOLING **must not** select `update_required`, `replacement_required`, **or** `uncertain` **without** an explicit governed disposition.

## Details
