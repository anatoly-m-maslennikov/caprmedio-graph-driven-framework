---
subjects:
  governs: "Entity/Continuant/Node/Atom/Content Role: Plan"
  depends_on:
    ["Entity/Continuant/Node/Atom/Content Role: Plan", "Entity/Continuant/Node/Actor/Type: AI Agent", "Entity/Continuant/Node/Actor/Type: Operator", "Entity/Continuant/Node/Atom/Content Role: Plan.Label"]
version: 9
updated_at: "2026-10-18 03:33:43 +0400"
relations: {"relates_to": ["CA-R-1575", "CA-R-1584"]}
atom_id: "CA-R-1589"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1589-CORE_META_MODEL-GENERAL--bound-executable-leaf-plans.md
  source_atom_id: CA-R-1589
  source_atom_revision: 9
  source_sha256: 73a2a5ba3383b829d54e57af3f08a3a6143f9dec7b58705ee6743e259db3fbf6
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Bound executable leaf Plans

## Scope

executable Plans with **none** direct decompositions.

## Claim

**every** executable Plan with **none** direct decompositions **must** bound its own work **to** an estimate of **<=15** minutes for **=1** assigned AI Agent, with sufficient inputs, required output, verification, **and** no unresolved Operator decision; a composite Plan **may** have a larger roll-up estimate. the rule applies independently of Label.

## Details
