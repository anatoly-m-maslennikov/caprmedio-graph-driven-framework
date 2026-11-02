---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Delivery.Substance'
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Delivery'
  - Subject/Engineering/Carrier
  - Subject/Domain/Node/Continuant/Atom.Subjects
  - Subject/Domain/Node/Continuant/Term
  - Subject/Graph/Relation
version: 15
updated_at: 2026-10-24 01:37:42 +0400
relations:
  child_of:
  - CA-M-307
  relates_to:
  - CA-R-1342
atom_id: CA-M-313@15
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Implementation Method
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

