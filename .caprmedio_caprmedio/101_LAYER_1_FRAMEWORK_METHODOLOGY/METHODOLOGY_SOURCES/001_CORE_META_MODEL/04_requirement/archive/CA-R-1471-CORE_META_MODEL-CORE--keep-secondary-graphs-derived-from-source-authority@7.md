---
subjects:
  governs: "CAPRMEDIO Graph"
  depends_on:
    ["Single Source of Truth", "Entity/Continuant/Projection", "Entity/Continuant/Object/Atom", "Entity/Continuant/Object/Atom.Substance", "Structural Entity", "Entity/Continuant/History/Journal", "Entity/Continuant/Object/Relation"]
version: 7
updated_at: "2026-10-15 18:43:29 +0000"
relations: {}
atom_id: "CA-R-1471"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Keep secondary graphs derived from source authority

## Scope

secondary CAPRMEDIO Graphs.

## Claim

secondary CAPRMEDIO Graphs **must** be Projections derived from their selected authoritative sources **or** source-traceable upstream Projections. their nodes **and** Relations **must** preserve source identities **and** traceability **to** the governing derivation authority **and** source facts.

storing, composing, filtering, **or** rebuilding a secondary graph **must not** make its contents another source of authority. a represented source fact is corrected **at** its authoritative source; an incorrect derivation is corrected under its governing methodology. neither case is resolved by independently editing the projected fact **or** fabricating source history.

## Details
