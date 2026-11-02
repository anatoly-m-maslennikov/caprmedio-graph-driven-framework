---
subjects:
  governs: "Entity/Carrier/File Carrier.Filename"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Requirement/Type: Demand.Target Scope Unit"]
version: 16
updated_at: "2026-10-19 15:55:22 +0400"
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
  source_atom_revision: 16
  source_sha256: e7972624f3619e10458cdf855e5aea287f7aa35e02b58649e1cb65a25097581d
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize Demand Type and Producer Scope

## Scope

Demand Atom filenames.

## Claim

**every** Demand Atom filename **must** serialize its Type **and** Producer Scope as `DEMANDS_FROM-<PRODUCER_SCOPE>`.

## Details
