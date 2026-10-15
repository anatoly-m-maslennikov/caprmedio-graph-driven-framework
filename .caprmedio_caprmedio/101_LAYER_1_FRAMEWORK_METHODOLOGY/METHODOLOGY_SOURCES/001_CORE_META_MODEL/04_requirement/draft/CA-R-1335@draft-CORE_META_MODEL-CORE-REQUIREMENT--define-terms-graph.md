---
subjects:
  governs: "Entity/Continuant/Projection/Type: Terms Graph"
  depends_on:
    ["Entity/Continuant/Projection", "Entity/Continuant/Term", "Relation Kind", "Entity/Continuant/Object/Relation", "CAPRMEDIO Graph"]
version: 14
updated_at: "2026-10-15 18:13:57 +0000"
relations: {}
atom_id: "CA-R-1335@draft"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Define Terms Graph

## Scope

Terms Graph projections **and** their represented graph facts.

## Claim

Terms Graph **means** the Type value under Projection whose instances are derived CAPRMEDIO Graphs with native Term nodes **and** edges representing Relations admitted for that graph kind by their governing authority. their represented facts retain their appropriate source authority under CA-R-1746.

## Details

admitted external graph **or** source references under CA-R-1472 do **not** become native Term nodes merely by being referenced. those references retain their own endpoint classes **and** graph-qualified Relation authority.
