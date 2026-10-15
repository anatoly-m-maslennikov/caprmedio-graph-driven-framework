---
subjects:
  governs: "Relation/Type: On Result"
  depends_on:
    ["Workflow", "Step", "Execution/Step Run", "Execution/Workflow Run", "Relation Kind"]
version: 5
updated_at: "2026-10-15 12:22:18 +0000"
relations: {}
atom_id: "CA-R-1513"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
---
# Summary

Define Workflow result transition

## Scope

the Workflow-scoped directed Relation from a source Step to a next Step.

## Claim

ON_RESULT **means** the Workflow-scoped directed Relation from a source Step **to** a next Step, qualified by an explicit condition on the source Step Run's result.

## Details

- **every** endpoint refers **to** a Step **in** the same Workflow, **not** directly **to** an Action definition.
- a transition **may** be followed **only** **when** its condition **and** the Workflow's authorization **and** retry gates are satisfied.
- a terminal outcome ends the Workflow Run **without** inventing a Step **or** Action for that outcome. this Relation does **not** redefine Subject DEPENDS_ON **or** a Task prerequisite Relation.
