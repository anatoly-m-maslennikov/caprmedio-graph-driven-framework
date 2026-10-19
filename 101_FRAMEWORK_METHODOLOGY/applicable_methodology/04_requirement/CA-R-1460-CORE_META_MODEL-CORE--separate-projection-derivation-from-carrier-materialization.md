---
subjects:
  governs: "Entity/Continuant/Projection"
  depends_on:
    ["Entity/Carrier", "Type", "Entity/Continuant/Object/Atom.Substance"]
version: 7
updated_at: "2026-10-15 18:43:18 +0000"
relations: {}
atom_id: "CA-R-1460"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1460-CORE_META_MODEL-CORE--separate-projection-derivation-from-carrier-materialization.md
  source_atom_id: CA-R-1460
  source_atom_revision: 7
  source_sha256: d385cf4baef7bac86511e0a6b2b8dbaa1675299bba8dec101c31dc22dbfff1da
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Separate Projection derivation from Carrier materialization

## Scope

the derivation of a Projection and its Carrier materialization.

## Claim

the governing derivation logic of a Projection **must** remain distinct from its Carrier materialization strategy. whether **and** how its result is represented **or** persisted **in** Carriers does **not**, by itself, define the transformation **or** content-preservation behavior of that derivation, its semantic Type, **or** its refresh behavior; those remain determined by their applicable governing Claims. describing a derivation as direct **or** content-preserving does **not** select a persistence strategy.

## Details
