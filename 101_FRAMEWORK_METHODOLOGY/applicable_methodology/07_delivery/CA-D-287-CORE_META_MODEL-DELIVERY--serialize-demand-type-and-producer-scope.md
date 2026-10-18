---
subjects:
  governs: "Entity/Carrier/File Carrier.Filename"
  depends_on:
    ["Entity/Continuant/Node/Atom/Content Role: Requirement/Type: Demand.Target Scope Unit"]
version: 15
updated_at: "2026-10-18 03:34:34 +0400"
relations: {}
atom_id: "CA-D-287"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-287-CORE_META_MODEL-DELIVERY--serialize-demand-type-and-producer-scope.md
  source_atom_id: CA-D-287
  source_atom_revision: 15
  source_sha256: fa5bdee2e3c2e3695ab7e074e684b0f2b066ff7b0a8d50595049213402da57ba
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize Demand Type and Producer Scope

## Scope

Demand Atom filenames.

## Claim

**every** Demand Atom filename **must** serialize its Type **and** Producer Scope as `DEMANDS_FROM-<PRODUCER_SCOPE>`.

## Details
