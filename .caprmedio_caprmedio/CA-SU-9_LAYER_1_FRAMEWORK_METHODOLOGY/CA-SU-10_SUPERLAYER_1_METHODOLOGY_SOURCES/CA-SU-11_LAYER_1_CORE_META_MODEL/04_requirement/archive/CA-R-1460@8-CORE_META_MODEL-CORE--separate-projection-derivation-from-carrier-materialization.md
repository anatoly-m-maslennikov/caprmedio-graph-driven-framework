---
subjects:
  governs: "Entity/Node/Continuant/Projection"
  depends_on:
    ["Entity/Carrier", "Type", "Entity/Node/Continuant/Atom.Substance"]
version: 8
updated_at: "2026-10-19 15:53:09 +0400"
relations: {}
atom_id: CA-R-1460@8
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: Archived
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Separate Projection derivation from Carrier materialization

## Scope

the derivation of a Projection and its Carrier materialization.

## Claim

the governing derivation logic of a Projection **must** remain distinct from its Carrier materialization strategy. whether **and** how its result is represented **or** persisted **in** Carriers does **not**, by itself, define the transformation **or** content-preservation behavior of that derivation, its semantic Type, **or** its refresh behavior; those remain determined by their applicable governing Claims. describing a derivation as direct **or** content-preserving does **not** select a persistence strategy.

## Details
