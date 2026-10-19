---
subjects:
  governs: "Entity/Node/Continuant/Scope Unit.Parent"
  depends_on:
    []
version: 20
updated_at: "2026-10-19 11:41:56 +0000"
relations: {}
atom_id: "CA-R-1658@draft"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Prohibit skipped Scope Unit ownership

## Scope

Scope Unit ownership through a stored structural-parent relation.

## Claim

a Scope Unit **must not** own a descendant Scope Unit through a stored structural-parent relation **when** another active Scope Unit lies between them.

## Details
