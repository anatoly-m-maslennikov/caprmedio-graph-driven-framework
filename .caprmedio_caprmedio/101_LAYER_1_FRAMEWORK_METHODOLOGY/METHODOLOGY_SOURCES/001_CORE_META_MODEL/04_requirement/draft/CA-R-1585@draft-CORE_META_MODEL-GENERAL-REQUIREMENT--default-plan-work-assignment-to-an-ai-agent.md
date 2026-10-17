---
subjects:
  governs: "Entity/Continuant/Node/Atom/Content Role: Plan.Assignee"
  depends_on:
    ["Entity/Continuant/Node/Atom/Content Role: Plan", "Entity/Continuant/Node/Actor/Type: AI Agent"]
version: 8
updated_at: "2026-10-17 23:24:14 +0000"
relations: {"relates_to": ["CA-R-1584"]}
atom_id: "CA-R-1585@draft"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 10
---
# Summary

Default Plan work assignment to an AI Agent

## Scope

a Plan Atom with its own work and no explicit Assignee.

## Claim

**if** a Plan Atom has its own work **and** no explicit Assignee, **then** its effective Assignee **must** be **=1** AI Agent selected **to** execute that work.

## Details
