---
subjects:
  governs: "Entity/Node/Continuant/Atom/Content Role: Plan.Status"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Plan", "Entity/Node/Continuant/Atom.Status"]
version: 9
updated_at: "2026-10-19 11:40:55 +0000"
relations: {"relates_to": ["CA-R-1412"]}
atom_id: "CA-R-1539@draft"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Draft"
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
