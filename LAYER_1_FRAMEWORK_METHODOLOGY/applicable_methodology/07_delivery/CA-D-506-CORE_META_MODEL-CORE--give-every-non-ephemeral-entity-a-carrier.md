---
atom_id: "CA-D-506"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
global_tier: 9
status: "Active"
version: 3
updated_at: "2026-10-15 18:52:27 +0000"
author: "Anatoly Maslennikov"
subjects:
  governs: "Non-ephemeral Entity"
  depends_on:
    ["Entity", "Entity/Carrier", "Property"]
relations: {}
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-506-CORE_META_MODEL-CORE--give-every-non-ephemeral-entity-a-carrier.md
  source_atom_id: CA-D-506
  source_atom_revision: 3
  source_sha256: 422262333bc6a6c9bea217ac1463869833fe7d3641f6a6c8764ba52d4c991873
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Give every non-ephemeral Entity a Carrier

## Scope

non-ephemeral Entities.

## Claim

**every** non-ephemeral Entity **must** have **`>=1`** Carrier through its Entity/Carrier binding.

## Details

a binding **may** use a shared Carrier **or** a location within it. a carried Property does **not** require a separate file merely because it is an Entity.
