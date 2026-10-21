---
subjects:
  governs: "CAPRMEDIO Graph"
  depends_on:
    ["Single Source of Truth", "Entity/Node/Continuant/Projection", "Entity/Node/Continuant/Atom", "Entity/Node/Continuant/Atom.Substance", "Structural Entity", "Entity/Node/Continuant/History/Journal", "Entity/Relation"]
version: 8
updated_at: "2026-10-19 15:53:12 +0400"
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
  source_atom_revision: 8
  source_sha256: e723e17015d11756e663e944418a19a6e3431f9cf49e23c5edafdf842d366a51
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
