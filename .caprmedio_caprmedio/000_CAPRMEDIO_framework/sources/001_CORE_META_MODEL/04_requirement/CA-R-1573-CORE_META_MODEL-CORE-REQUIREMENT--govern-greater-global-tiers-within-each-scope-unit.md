---
subjects:
  governs: "Entity/Continuant/Node/Atom.Global Tier"
  depends_on:
    ["Entity/Continuant/Node/Atom", "Entity/Continuant/Node/Scope Unit", "Entity/Continuant/Node/Atom/Content Role"]
version: 8
updated_at: "2026-10-18 03:33:41 +0400"
relations: {"relates_to": ["CA-R-1444", "CA-R-917"]}
atom_id: "CA-R-1573"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Govern greater Global Tiers within each Scope Unit

## Scope

Global Tier governance within each Scope Unit.

## Claim

**in** **every** Scope Unit, **every** Atom at Global Tier `N` **must** govern **all** Atoms at Global Tiers **`>`** `N`, across **all** Content Roles.

## Details
