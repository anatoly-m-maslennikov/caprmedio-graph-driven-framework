---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Relation
version: 20
updated_at: 2026-10-27 19:59:49 +0400
relations: {}
atom_id: CA-R-1030
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 2
type: Rule
---
# Prohibit silent non-compatible Impact dispositions

## Scope

the selection of non-compatible Impact dispositions.

## Claim

TOOLING **must not** select `update_required`, `replacement_required`, **or** `uncertain` **without** an explicit governed disposition.

## Details
