---
subjects:
  governs: "Entity/Node/Continuant/Atom/Content Role: Requirement/Type: Demand.Target Scope Unit"
  depends_on:
    ["Entity/Node/Continuant/Atom.Owning Scope Unit", "Entity/Node/Continuant/Atom.Target Scope Unit"]
version: 20
updated_at: "2026-10-19 15:52:46 +0400"
relations: {}
atom_id: "CA-R-1294"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1294-CORE_META_MODEL-CORE-REQUIREMENT--derive-demand-direction-without-another-relation-kind.md
  source_atom_id: CA-R-1294
  source_atom_revision: 20
  source_sha256: acab525b8123719be885585c19ad4848278635f0f22727d18db2770a0d5e9009
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Derive Demand Direction without Another Relation Kind

## Scope

Demand Atom directions.

## Claim

a Demand Atom **must not** introduce a graph Relation Kind for its direction because its Consumer Atom Scope Unit **and** Producer Claim Target Scope Unit references determine that direction.

## Details
