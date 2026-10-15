---
subjects:
  governs: "CAPRMEDIO Graph"
  depends_on:
    ["Single Source of Truth", "Projection", "Atom", "Atom.Substance", "Structural Entity", "Journal", "Relation"]
version: 6
updated_at: "2026-10-15 12:12:40 +0000"
relations: {}
atom_id: "CA-R-1471@draft"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Draft"
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
