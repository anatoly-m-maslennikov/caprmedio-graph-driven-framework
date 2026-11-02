---
subjects:
  governs: Subject/Domain/Node/Continuant/Scope Unit.Parent
  depends_on: []
version: 21
updated_at: 2026-10-23 03:14:50 +0400
relations: {}
atom_id: CA-R-1658@21
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Core
status: Archived
author: Anatoly Maslennikov
global_tier: 9
---
# Summary

Prohibit skipped Scope Unit ownership

## Scope

Scope Unit ownership through a stored structural-parent relation.

## Claim

a Scope Unit **must not** own a descendant Scope Unit through a stored structural-parent relation **when** another active Scope Unit lies between them.

## Details
