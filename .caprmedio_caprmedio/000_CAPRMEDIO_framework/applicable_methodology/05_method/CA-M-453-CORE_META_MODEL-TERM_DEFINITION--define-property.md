---
atom_id: CA-M-453
status: Active
tier: 1
version: 6
updated_at: 2026-11-04 23:01:11 +0400
subjects:
  active: CAPRMEDIO_MODEL <+ Term//Property
  passive:
  - CAPRMEDIO_MODEL <+ Term
  - CAPRMEDIO_MODEL <+ Term//Entity
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_PROPERTY_OF
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Method)/(.Header.Form := Term Definition)
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
role: Method
form: Term Definition
carrier_destination:
  file:
    name: CA-M-453-CORE_META_MODEL-TERM_DEFINITION--define-property.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method/CA-M-453-CORE_META_MODEL-TERM_DEFINITION--define-property.md
  source_atom_id: CA-M-453
  source_atom_revision: 6
  source_sha256: 05aa611f0737b1abd55cde20d63328d12bbfec4d105a7b333cdf8472c5c5fa90
  original_relations_sha256: e367927d209b7bdecd9da53dd0dc693193d074370738c97b4bc15988d6240196
---
## Summary

Define Property

## Claim

### Prose Claim

Property means an Entity whose identity depends on exactly one immediate bearer through the direct IS_PROPERTY_OF Relation.
