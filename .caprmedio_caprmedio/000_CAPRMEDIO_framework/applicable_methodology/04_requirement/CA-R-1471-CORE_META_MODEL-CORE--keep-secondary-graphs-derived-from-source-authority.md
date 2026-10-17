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
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1471-CORE_META_MODEL-CORE--keep-secondary-graphs-derived-from-source-authority.md
  source_atom_id: CA-R-1471
  source_atom_revision: 7
  source_sha256: 43ece714768515461c65bd284e19226aa7cef432ffea2bdd7d2dc4d898f27010
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Keep secondary graphs derived from source authority

## Scope

secondary CAPRMEDIO Graphs.

## Claim

secondary CAPRMEDIO Graphs **must** be Projections derived from their selected authoritative sources **or** source-traceable upstream Projections. their nodes **and** Relations **must** preserve source identities **and** traceability **to** the governing derivation authority **and** source facts.

storing, composing, filtering, **or** rebuilding a secondary graph **must not** make its contents another source of authority. a represented source fact is corrected **at** its authoritative source; an incorrect derivation is corrected under its governing methodology. neither case is resolved by independently editing the projected fact **or** fabricating source history.

## Details
