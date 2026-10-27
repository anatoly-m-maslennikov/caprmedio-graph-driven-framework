---
subjects:
  governs: Subject/Domain/Node/Continuant/Scope Unit.Parent
  depends_on: []
version: 24
updated_at: 2026-10-24 10:48:25 +0400
relations: {}
atom_id: CA-R-1658@24
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Prohibit skipped Scope Unit ownership

## Scope

Scope Unit ownership through a stored structural-parent relation.

## Claim

a Scope Unit **must not** own a descendant Scope Unit through a stored structural-parent relation **when** another active Scope Unit lies between them.

## Details
