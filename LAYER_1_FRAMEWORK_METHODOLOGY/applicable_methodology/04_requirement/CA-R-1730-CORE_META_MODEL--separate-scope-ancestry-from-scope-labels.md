---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Scope Unit
  passive:
  - CAPRMEDIO <+ MODEL <+ Scope Unit.Path
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit.Parent
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit.Children
  - CAPRMEDIO <+ MODEL <+ Scope Unit.Label
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO <+ MODEL <+ Scope Unit
version: 40
updated_at: 2026-11-02 19:44:26 +0400
relations:
  child_of:
  - CA-R-1776
atom_id: CA-R-1730
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1730-CORE_META_MODEL--separate-scope-ancestry-from-scope-labels.md
  source_atom_id: CA-R-1730
  source_atom_revision: 40
  source_sha256: 1cbd20df7f989b8d9fd842732942b9d164607cc6f5a6fe53ec84342834564cf8
  original_relations_sha256: 1aee20d21b9ce38a56336862dc1f3d576ad4e3123506d524cd0d5ea4cd2829ab
---
## Summary

Separate scope ancestry from scope labels

## Claim scope

Scope Unit ancestry **and** Scope Unit Labels.

## Claim

Scope Unit ancestry **must** follow declared Scope Unit parentage. CAPRMEDIO **must not** author or persist a Structural Level property; an optional derived depth or path rendering **must not** independently override that parentage under CA-R-1485.

the Operator **may** choose **any** suitable Scope Unit Label, including `Layer`, `Feature`, `group`, `supergroup`, **or** `sub-feature`, **without** changing the unit's ancestry, authority, precedence, **or** Relation semantics. Labels **and** readability fields do **not** replace the active authority for those distinctions.
