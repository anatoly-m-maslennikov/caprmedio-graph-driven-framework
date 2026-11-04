---
atom_id: CA-R-2765
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Method)/(.Header.Form := Term Definition)
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Method)
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
tier: 3
role: Requirement
form: Declaration
version: 5
updated_at: 2026-11-04 23:07:00 +0400
carrier_destination:
  file:
    name: CA-R-2765-CORE_META_MODEL-DECLARATION--declare-term-definition-as-a-method-form.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2765-CORE_META_MODEL-DECLARATION--declare-term-definition-as-a-method-form.md
  source_atom_id: CA-R-2765
  source_atom_revision: 5
  source_sha256: 06c5863629ae52cc481f2b2472dec3cb2e1bfcf1fd2d109f470a98f07809ef62
  original_relations_sha256: e367927d209b7bdecd9da53dd0dc693193d074370738c97b4bc15988d6240196
---
## Summary

Declare Term Definition as a Method Form

## Claim

### Formal Claim

```CFEL
# model
Atom/(.Header.Role := Method).Header.Form: Term Definition;
Atom/(.Header.Role := Method)/(.Header.Form := Term Definition)
```
