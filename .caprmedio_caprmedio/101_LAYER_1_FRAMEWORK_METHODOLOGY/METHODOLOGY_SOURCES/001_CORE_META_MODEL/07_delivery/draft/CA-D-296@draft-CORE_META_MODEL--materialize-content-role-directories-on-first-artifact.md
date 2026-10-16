---
subjects:
  governs: "Entity/Carrier.Canonical Address"
  depends_on:
    ["Entity/Continuant/Object/Atom/Content Role", "Entity/Continuant/Object/Scope Unit", "Entity/Continuant/Object/Atom", "Entity/Carrier/Directory Carrier"]
version: 16
updated_at: "2026-10-16 12:00:56 +0000"
relations: {}
atom_id: "CA-D-296@draft"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Materialize Content Role Directories on First Artifact

## Scope

administrative Content Role directories in Scope Units.

## Claim

a Scope Unit's administrative Content Role directory **must** be materialized for canonical Artifact placement **only** **when** the first current Artifact requires that placement.

## Details

an absent Content Role directory **must** represent empty role placement, **not** an absent Scope Unit. this administrative directory does **not** itself carry a Structural Entity **or** become a Directory Carrier under CA-D-451. this materialization condition does **not** require deletion of an existing empty directory.
