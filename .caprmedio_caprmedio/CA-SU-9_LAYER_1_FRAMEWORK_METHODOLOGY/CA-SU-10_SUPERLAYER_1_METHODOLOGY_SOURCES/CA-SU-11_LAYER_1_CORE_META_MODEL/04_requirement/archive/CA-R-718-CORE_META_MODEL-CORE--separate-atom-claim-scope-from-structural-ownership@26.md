---
subjects:
  governs: "Entity/Continuant/Node/Atom.Target Scope Unit"
  depends_on:
    ["Entity/Continuant/Node/Atom.Substance", "Entity/Continuant/Node/Scope Unit", "Entity/Continuant/Node/Project.Structure", "Entity/Continuant/Node/Atom.Substance Scope"]
version: 26
updated_at: "2026-10-18 03:34:10 +0400"
relations:
  child_of:
    - CA-R-1776
atom_id: "CA-R-718"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Separate Atom Claim Scope from structural ownership

## Scope

the relationship between an Atom's Claim targeting, textual applicability, **and** structural ownership.

## Claim

an Atom's Claim Target Scope Unit reference **and** applicability restrictions **in** its Main Content **must not**, by themselves, establish an additional edge **in** the Scope Unit tree **or** alter structural-parent ownership.

## Details
