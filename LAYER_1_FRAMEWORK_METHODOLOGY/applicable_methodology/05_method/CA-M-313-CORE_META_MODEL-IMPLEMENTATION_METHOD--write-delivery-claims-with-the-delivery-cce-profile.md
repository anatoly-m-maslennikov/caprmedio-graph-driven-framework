---
atom_id: CA-M-313
ref_id: CA-M-313
container:
  scope_unit: CA-SU-11
role: Method
form: Implementation Method
topics:
  main_subject: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role: Delivery).Content.Claim'
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Delivery)
  - CAPRMEDIO_MODEL <+ Carrier
  - CAPRMEDIO_MODEL <+ Atom.Header.Topics
  - CAPRMEDIO_MODEL <+ Term
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
tier: 6
relations:
  child_of:
  - CA-M-307
status: Active
version: 26
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-M-313-CORE_META_MODEL-IMPLEMENTATION_METHOD--write-delivery-claims-with-the-delivery-cce-profile.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method/CA-M-313-CORE_META_MODEL-IMPLEMENTATION_METHOD--write-delivery-claims-with-the-delivery-cce-profile.md
  source_atom_id: CA-M-313
  source_atom_revision: 26
  source_sha256: 36c4d9fa6e683a484d93b84753c68a567ae8b901123cb2dda7ff056543ec857a
  original_relations_sha256: 1037ec3e9bee824bbe0013d533c233bc31238f593358d3400af78e5150b7d7f4
---
## Summary

Write Delivery Claims with the Delivery CCE Profile

## Claim

### Prose Claim


authoring Delivery Substance with the applicable Delivery CCE Role Profile.


a Delivery Substance **must** use the applicable Delivery CCE Role Profile with these authoring conventions:

1. name the governed Entity or Carrier and state its representation, storage or placement constraint directly.
2. include format, content, address, placement or lifecycle conditions **when** they are relevant to that contribution.
3. choose CCE Operators to express the applicable modality, conditions, quantities and comparisons.
4. use admitted typed Relations when the contribution expresses a representation binding.
5. keep the Substance about its governed Subject; reference separately governed contributions instead of redefining them.

## Details

Entity, property and Carrier-kind definitions belong to Requirement. Delivery uses those definitions to specify representation. Do not invent a filename, format or lifecycle condition merely to fill a template. YAML fields and Markdown sections can represent properties inside one File Carrier without a separate binding record for each property.
