---
subjects:
  governs: "Entity/Continuant/Object/Atom/Content Role: Plan.Status"
  depends_on:
    ["Entity/Continuant/Object/Atom/Content Role: Plan", "Entity/Continuant/Object/Atom.Status"]
version: 7
updated_at: "2026-10-17 13:00:36 +0000"
relations: {"relates_to": ["CA-R-1412"]}
atom_id: "CA-R-1539"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
---
# Summary

Register Core Plan Status Values

## Scope

Core Plan Status values.

## Claim

the Core Plan Status model **must** inherit the allowed values of Atom.Status and add (Backlog, Done, Canceled). Planned **must not** be a distinct Plan Status.

## Details
