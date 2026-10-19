---
atom_id: CA-R-1608
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: General
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Entity/Continuant/Node/Atom/Content Role: Concern.Status"
  depends_on:
    ["Entity/Continuant/Node/Atom/Content Role: Concern", "Entity/Continuant/Node/Atom.Status"]
version: 7
updated_at: "2026-10-18 03:33:45 +0400"
relations:
  relates_to:
    - CA-R-1308
    - CA-R-1313
    - CA-R-1336
global_tier: 10
---
# Summary

Register Core Concern Status Values

## Scope

the Core Concern Status model.

## Claim

the Core Concern Status model **must** inherit the allowed values of Atom.Status and add (Resolved, Canceled).

## Details
