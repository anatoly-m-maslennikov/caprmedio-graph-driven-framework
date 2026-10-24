---
subjects:
  governs: "Entity/Node/Continuant/Atom/Content Role: Plan.Assignee"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Plan", "Entity/Node/Continuant/Actor/Type: AI Agent"]
version: 9
updated_at: "2026-10-19 15:53:36 +0400"
relations: {"relates_to": ["CA-R-1584"]}
atom_id: CA-R-1585@9
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: Archived
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
