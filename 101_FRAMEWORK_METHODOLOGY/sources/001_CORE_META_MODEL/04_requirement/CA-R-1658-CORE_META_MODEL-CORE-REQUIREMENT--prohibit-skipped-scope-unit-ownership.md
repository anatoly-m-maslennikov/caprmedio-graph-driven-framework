---
subjects:
  governs: "Entity/Continuant/Node/Scope Unit.Parent"
  depends_on:
    []
version: 19
updated_at: "2026-10-18 03:33:47 +0400"
relations: {}
atom_id: "CA-R-1658"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
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
