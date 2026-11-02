---
subjects:
  governs: "Structural Entity"
  depends_on:
    ["Structural Entity", "Entity/Carrier/Directory Carrier", "Entity/Node/Continuant/Scope Unit", "Entity/Node/Continuant/Project.Structure"]
version: 8
updated_at: "2026-10-19 15:55:52 +0400"
relations: {"relates_to": ["CA-R-1956", "CA-D-312", "CA-R-1484"]}
atom_id: "CA-D-465"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-465-CORE_META_MODEL-STANDARD--carry-each-materialized-structural-entity-with-a-directory-carrier.md
  source_atom_id: CA-D-465
  source_atom_revision: 8
  source_sha256: 7e4e93c7bc89aa75d745407cff1feea6403f5a2771ab23b067529eabdb9293d9
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Carry Each Materialized Structural Entity with a Directory Carrier

## Scope

materialized Structural Entities and Scope Units established by Project Structure.

## Claim

**every** materialized Structural Entity **must** be carried by **`>=1`** Directory Carrier; a Scope Unit established by Project Structure **may** remain unmaterialized under CA-R-1484-CORE_META_MODEL-GENERAL-REQUIREMENT--establish-scope-units-through-project-structure-declarations without losing its declaration **or** identity.

## Details
