---
atom_id: CA-R-2620
ref_id: CA-R-2620
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//HAS_NARROWER
tier: 3
status: active
version: 3
updated_at: '2026-11-13T05:35:54.631909+00:00'
carrier_destination:
  file:
    name: CA-R-2620-CORE_META_MODEL-DECLARATION--declare-has-narrower.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
---
## Summary

Declare HAS_NARROWER

## Claim

### Formal Claim

```python
# model
relation(source="Relation//HAS_NARROWER", name="HAS_INVERSE", target="Relation//NARROWER_THAN", reverse=True)
```
