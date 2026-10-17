---
subjects:
  governs: "Entity/Continuant/Object/Atom/Content Role: Plan.Assignee"
  depends_on:
    ["Entity/Continuant/Object/Atom/Content Role: Plan", "Entity/Continuant/Actor"]
version: 7
updated_at: "2026-10-16 12:08:33 +0000"
relations: {"relates_to": ["CA-R-1575"]}
atom_id: "CA-R-1584"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Require an effective Assignee for Plan work

## Scope

Plan Atoms with their own work content, excluding pure Hubs **without** their own work.

## Claim

**every** Plan Atom with its own work content **must** have **`=1`** effective Assignee; a pure Hub **without** its own work does **not** require an additional Assignee merely because it organizes other Plans.

## Details
