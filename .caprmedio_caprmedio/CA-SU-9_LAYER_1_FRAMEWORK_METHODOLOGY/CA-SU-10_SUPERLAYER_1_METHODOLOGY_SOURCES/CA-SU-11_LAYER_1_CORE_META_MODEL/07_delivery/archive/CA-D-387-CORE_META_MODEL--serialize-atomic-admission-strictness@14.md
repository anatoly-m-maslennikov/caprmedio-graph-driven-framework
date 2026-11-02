---
subjects:
  governs: "Entity/Continuant/Node/Project.Framework Settings"
  depends_on:
    ["Entity/Continuant/Node/Project.Framework Settings"]
version: 14
updated_at: "2026-10-18 07:32:42 +0400"
relations:
  child_of:
    - CA-D-361
  relates_to:
    - CA-R-1630
atom_id: "CA-D-387"
content_role: "Delivery"
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Serialize Atomic Admission Strictness

## Scope

an explicit atomic admission strictness selection in the Framework Instance Settings TOML Carrier.

## Claim

an explicit atomic admission strictness selection **in** the Framework Instance Settings TOML Carrier **must** use `creation_strictness` **in** `[artifacts]`, using the allowed values governed by CA-R-1630.

## Details
