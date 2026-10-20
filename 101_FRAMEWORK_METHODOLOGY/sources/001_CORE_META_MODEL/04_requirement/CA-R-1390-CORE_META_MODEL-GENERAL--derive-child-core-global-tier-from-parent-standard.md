---
subjects:
  governs: "Entity/Node/Continuant/Atom.Global Tier"
  depends_on:
    ["Entity/Node/Continuant/Atom.Local Tier: Core", "Entity/Node/Continuant/Scope Unit", "Entity/Node/Continuant/Scope Unit.Parent", "Entity/Node/Continuant/Scope Unit.Children"]
version: 15
updated_at: "2026-10-19 15:52:56 +0400"
relations: {}
atom_id: "CA-R-1390"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
---
# Summary

Derive Child Core Global Tier from Parent Standard

## Scope

Core Atoms scoped **to** non-Project Scope Units and their direct parent Scope Units.

## Claim

a Core Atom scoped **to** a non-Project Scope Unit **must** have a Global Tier one greater than the Standard Global Tier of its direct parent Scope Unit.

## Details
