---
atom_id: CA-R-2418
current_scope_unit: CORE_META_MODEL
status: Active
tier: 1
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_CARRIED_BY
relations: {}
version: 5
updated_at: 2026-11-03 20:00:05 +0400
claim_target_scope_unit: CORE_META_MODEL
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2418-CORE_META_MODEL-DECLARATION--define-is-carried-by-relation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Define IS_CARRIED_BY Relation

## Claim

### Formal Claim

```CFEL
# model
Relation//IS_CARRIED_BY <((HAS_INVERSE)) Relation//CARRIES
```
