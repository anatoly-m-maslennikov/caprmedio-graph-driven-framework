---
atom_id: CA-R-2617
role: Requirement
form: Declaration
status: Active
version: 2
updated_at: 2026-11-03 20:00:05 +0400
current_scope_unit: CORE_META_MODEL
tier: 3
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//CONTAINS
relations: {}
carrier_destination:
  file:
    name: CA-R-2617-CORE_META_MODEL-DECLARATION--declare-contains.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
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
