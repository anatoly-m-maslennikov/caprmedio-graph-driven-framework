---
atom_id: CA-R-2619
ref_id: CA-R-2619
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//HAS_INSTANCE
tier: 3
status: active
version: 3
updated_at: '2026-11-13T05:35:52.255000+00:00'
carrier_destination:
  file:
    name: CA-R-2619-CORE_META_MODEL-DECLARATION--declare-has-instance.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
---
## Summary

Declare HAS_INSTANCE

## Claim

### Formal Claim

```python
# model
relation(source="Relation//HAS_INSTANCE", name="HAS_INVERSE", target="Relation//INSTANCE_OF", reverse=True)
```
