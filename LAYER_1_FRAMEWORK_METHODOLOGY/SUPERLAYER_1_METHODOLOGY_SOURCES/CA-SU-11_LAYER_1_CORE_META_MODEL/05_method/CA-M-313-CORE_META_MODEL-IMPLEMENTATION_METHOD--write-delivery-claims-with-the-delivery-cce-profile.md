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
