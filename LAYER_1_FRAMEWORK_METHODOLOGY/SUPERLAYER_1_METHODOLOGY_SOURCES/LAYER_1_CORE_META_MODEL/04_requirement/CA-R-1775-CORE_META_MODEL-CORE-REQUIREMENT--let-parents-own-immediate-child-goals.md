---
version: 18
updated_at: "2026-10-19 15:54:04 +0400"
relations:
  child_of:
    - CA-M-001
subjects:
  governs: "Entity/Node/Continuant/Atom/Content Role: Requirement/Type: Goal"
  depends_on:
    ["Entity/Node/Continuant/Scope Unit", "Entity/Node/Continuant/Atom", "Owned Atoms", "Targeting Atoms"]
atom_id: "CA-R-1775"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Let Parents Own Immediate Child Goals

## Scope

parent Scope Units and their immediate child Scope Units.

## Claim

**every** parent Scope Unit **must** own the Goal Atoms for its immediate child Scope Units under CA-R-926; those Goal Atoms belong **to** the parent's Owned Atoms **and** the child's Targeting Atoms **without** transferring their ownership.

## Details
