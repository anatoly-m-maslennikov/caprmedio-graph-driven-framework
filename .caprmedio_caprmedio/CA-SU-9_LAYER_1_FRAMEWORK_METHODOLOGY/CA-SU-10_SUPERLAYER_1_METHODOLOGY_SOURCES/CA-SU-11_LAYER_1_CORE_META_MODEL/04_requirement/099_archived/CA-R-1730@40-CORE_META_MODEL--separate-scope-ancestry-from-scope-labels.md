---
atom_id: CA-R-1730
ref_id: CA-R-1730@40
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit
  dependencies:
  - CAPRMEDIO_MODEL <+ Scope Unit.Path
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit.Parent
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit.Children
  - CAPRMEDIO_MODEL <+ Scope Unit.Label
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_MODEL <+ Scope Unit
tier: 2
relations:
  child_of:
  - CA-R-1776
status: archived
version: 40
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-R-1730@40-CORE_META_MODEL--separate-scope-ancestry-from-scope-labels.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Separate scope ancestry from scope labels

## Claim

### Prose Claim


Scope Unit ancestry **and** Scope Unit Labels.


Scope Unit ancestry **must** follow declared Scope Unit parentage. CAPRMEDIO **must not** author or persist a Structural Level property; an optional derived depth or path rendering **must not** independently override that parentage under CA-R-1485.

the Operator **may** choose **any** suitable Scope Unit Label, including `Layer`, `Feature`, `group`, `supergroup`, **or** `sub-feature`, **without** changing the unit's ancestry, authority, precedence, **or** Relation semantics. Labels **and** readability fields do **not** replace the active authority for those distinctions.
