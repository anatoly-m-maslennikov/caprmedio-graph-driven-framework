---
subjects:
  active: 'Entity/Object/Continuant/Governing Objects/Atom/(.Content Role: Delivery).Content.Claim'
  passive:
  - Atom/(.Role := Delivery)
  - Carrier
  - Atom.Subjects
  - Term
  - CFEL <+ Relation
version: 26
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-M-307
atom_id: CA-M-313
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 6
role: Method
form: Implementation Method
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method/CA-M-313-CORE_META_MODEL-IMPLEMENTATION_METHOD--write-delivery-claims-with-the-delivery-cce-profile.md
  source_atom_id: CA-M-313
  source_atom_revision: 26
  source_sha256: 49d8549c0c1276dd9243211f44fc0d6020ce2a382d9ef80a4ac725097d93a94e
  original_relations_sha256: 1037ec3e9bee824bbe0013d533c233bc31238f593358d3400af78e5150b7d7f4
---
## Summary

Write Delivery Claims with the Delivery CCE Profile

## Claim scope

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
