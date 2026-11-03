---
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation
version: 27
updated_at: 2026-11-02 19:44:26 +0400
relations: {}
atom_id: CA-R-1030
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
---
## Summary
Prohibit silent non-compatible Impact dispositions

## Claim scope

the selection of non-compatible Impact dispositions.

## Claim

TOOLING **must not** select `update_required`, `replacement_required`, **or** `uncertain` **without** an explicit governed disposition.
