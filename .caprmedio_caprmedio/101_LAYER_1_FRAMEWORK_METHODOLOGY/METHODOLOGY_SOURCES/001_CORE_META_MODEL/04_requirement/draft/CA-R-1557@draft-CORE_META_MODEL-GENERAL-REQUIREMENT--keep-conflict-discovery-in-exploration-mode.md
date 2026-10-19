---
subjects:
  governs: "Entity/Node/Continuant/Actor/Type: AI Agent"
  depends_on:
    ["Entity/Node/Continuant/Actor/Type: AI Agent", "Entity/Node/Continuant/Actor/Type: Operator", "Exploration Mode", "Entity/Node/Continuant/Atom/Content Role: Concern"]
version: 8
updated_at: "2026-10-19 11:41:04 +0000"
relations: {"child_of":["CA-R-1702"]}
atom_id: "CA-R-1557@draft"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 10
---
# Summary

Keep conflict discovery in Exploration Mode

## Scope

AI Agent discovery of conflicts in Exploration Mode.

## Claim

an AI Agent **must** keep a discovered conflict **in** Exploration Mode; it **may** create a Concern for that conflict **only** **when** the Operator requests persistence **or** defers its resolution.

## Details
