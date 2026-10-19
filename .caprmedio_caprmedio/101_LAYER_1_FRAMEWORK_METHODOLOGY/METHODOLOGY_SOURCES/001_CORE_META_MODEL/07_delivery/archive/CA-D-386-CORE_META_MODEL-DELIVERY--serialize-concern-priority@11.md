---
subjects:
  governs: "Entity/Continuant/Node/Atom/Content Role: Concern.Priority"
  depends_on:
    ["Entity/Continuant/Node/Atom/Content Role", "Entity/Continuant/Node/Atom/Content Role: Concern.Priority", "Entity/Continuant/Node/Atom/Content Role: Plan"]
version: 11
updated_at: "2026-10-18 03:34:44 +0400"
relations: {}
atom_id: "CA-D-386"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Serialize Concern Priority

## Scope

Concern Atom Carriers and non-Concern Content Role Atom Carriers.

## Claim

a Concern Atom Carrier **must** serialize **`=1`** selected Priority as `priority` with the lowercase value `high`, `medium`, **or** `low`. **every** non-Concern Content Role Atom Carrier **must** omit `priority`; virtual `highest` **must not** be stored.

## Details
