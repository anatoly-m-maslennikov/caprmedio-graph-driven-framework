---
subjects:
  governs: Subject/Graph/Relation
version: 16
updated_at: 2026-10-24 01:18:03 +0400
relations: {}
atom_id: CA-R-1030@16
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
---
# Prohibit silent non-compatible Impact dispositions

## Scope

the selection of non-compatible Impact dispositions.

## Claim

TOOLING **must not** select `update_required`, `replacement_required`, **or** `uncertain` **without** an explicit governed disposition.

## Details
