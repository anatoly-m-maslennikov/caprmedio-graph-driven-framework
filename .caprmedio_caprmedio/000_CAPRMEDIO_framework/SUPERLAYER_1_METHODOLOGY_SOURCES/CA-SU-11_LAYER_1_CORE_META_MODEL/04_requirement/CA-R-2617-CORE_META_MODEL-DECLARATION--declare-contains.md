---
atom_id: CA-R-2617
ref_id: CA-R-2617
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//CONTAINS
tier: 3
status: Active
version: 2
updated_at: 2026-11-03 20:00:05 +0400
carrier_destination:
  file:
    name: CA-R-2617-CORE_META_MODEL-DECLARATION--declare-contains.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
---
## Summary

Declare CONTAINS

## Claim

### Formal Claim

```CFEL
# model
Relation//CONTAINS <((HAS_INVERSE)) Relation//IS_CONTAINED_BY;

alias(Relation//CONTAINS) == "<+"
```
