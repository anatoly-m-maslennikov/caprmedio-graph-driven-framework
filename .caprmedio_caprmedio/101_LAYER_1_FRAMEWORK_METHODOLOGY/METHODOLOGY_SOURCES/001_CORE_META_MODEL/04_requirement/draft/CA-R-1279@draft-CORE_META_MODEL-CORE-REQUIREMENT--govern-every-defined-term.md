---
subjects:
  governs: "GOVERNS"
  depends_on:
    ["Definition Atom", "Subject", "Entity/Continuant/Term", "Subject Path", "Entity/Continuant/Object/Atom.Substance"]
version: 14
updated_at: "2026-10-15 18:13:35 +0000"
relations: {}
atom_id: "CA-R-1279@draft"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Govern Every Defined Term

## Scope

defined Terms and their canonical direct GOVERNS Subject Relation.

## Claim

**every** Definition Atom **must** use its **`=1`** direct GOVERNS Subject Relation **to** identify the canonical target defined by its Claim, with the defined Term as the terminal name **in** that target's Subject Path. the defining Claim establishes that Term's meaning; the other Term components **in** the path are references **to** their own definitions, **not** additional definitions supplied by this Atom.

## Details
