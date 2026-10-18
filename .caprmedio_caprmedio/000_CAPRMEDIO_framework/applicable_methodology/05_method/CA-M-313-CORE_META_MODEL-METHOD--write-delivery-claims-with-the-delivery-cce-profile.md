---
subjects:
  governs: "Entity/Continuant/Node/Atom/Content Role: Delivery.Substance"
  depends_on:
  - "Entity/Continuant/Node/Atom/Content Role: Delivery"
  - Entity/Carrier
  - "Entity/Continuant/Node/Atom.Subjects"
  - "Entity/Continuant/Node/Term"
  - "Entity/Continuant/Relation"
version: 9
updated_at: "2026-10-18 03:34:20 +0400"
relations:
  child_of:
    - CA-M-307
  relates_to:
    - CA-R-1342
atom_id: "CA-M-313"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/05_method/CA-M-313-CORE_META_MODEL-METHOD--write-delivery-claims-with-the-delivery-cce-profile.md
  source_atom_id: CA-M-313
  source_atom_revision: 9
  source_sha256: d1069a91de748f190a6feca595da3113b95b781a18e30e04a4b2d6522b4558fe
  original_relations_sha256: df4e705715370cdf548abfbeba9ae0eed904bc3f2977ebc87988f011e0ad7418
---
# Summary

Write Delivery Claims with the Delivery CCE Profile

## Scope

authoring Delivery Substance with the applicable Delivery CCE Role Profile.

## Claim

a Delivery Substance **must** use the applicable Delivery CCE Role Profile with these authoring conventions:

1. name the governed Entity or Carrier and state its representation, storage or placement constraint directly.
2. include format, content, address, placement or lifecycle conditions **when** they are relevant to that contribution.
3. choose CCE Operators to express the applicable modality, conditions, quantities and comparisons.
4. use admitted typed Relations when the contribution expresses a representation binding.
5. keep the Substance about its governed Subject; reference separately governed contributions instead of redefining them.

## Details

Entity, property and Carrier-kind definitions belong to Requirement. Delivery uses those definitions to specify representation. Do not invent a filename, format or lifecycle condition merely to fill a template. YAML fields and Markdown sections can represent properties inside one File Carrier without a separate binding record for each property.

