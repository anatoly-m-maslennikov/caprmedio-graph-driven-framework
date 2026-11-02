---
subjects:
  governs: Entity/Graph Syntax > Relation
version: 21
updated_at: 2026-10-29 07:17:15 +0400
relations: {}
atom_id: CA-R-1030@21
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
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
