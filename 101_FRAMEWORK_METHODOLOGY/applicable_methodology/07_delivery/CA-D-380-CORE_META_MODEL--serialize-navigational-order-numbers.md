---
subjects:
  governs: "Entity/Node/Continuant/Scope Unit.Navigational Order Number"
  depends_on:
    ["Entity/Carrier", "Entity/Node/Continuant/Scope Unit", "Entity/Node/Continuant/Project.Structure"]
version: 10
updated_at: "2026-10-19 15:55:39 +0400"
relations: {}
atom_id: "CA-D-380"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-380-CORE_META_MODEL--serialize-navigational-order-numbers.md
  source_atom_id: CA-D-380
  source_atom_revision: 10
  source_sha256: 2824ae9cff0184dd3677432198acf3ebe76e1bdb6ad834962f171410349b7e1a
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize Navigational Order Numbers

## Scope

Carrier renderings of a Navigational Order Number.

## Claim

**every** Carrier rendering of a Navigational Order Number **must** use decimal digits. the default directory-name rendering of a non-Project Scope Unit **must** use **`>=2`** digits; a typed TOML integer stores the numeric value **without** leading-zero padding.

## Details
