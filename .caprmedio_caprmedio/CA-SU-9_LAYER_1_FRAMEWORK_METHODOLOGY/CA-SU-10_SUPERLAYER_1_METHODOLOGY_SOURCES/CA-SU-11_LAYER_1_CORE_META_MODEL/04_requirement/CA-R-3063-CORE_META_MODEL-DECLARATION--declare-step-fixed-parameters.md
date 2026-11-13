---
atom_id: CA-R-3063
ref_id: CA-R-3063
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Step.Fixed Parameters
tier: 3
status: active
version: 3
updated_at: '2026-11-12T23:10:08.677592+00:00'
carrier_destination:
  file:
    name: CA-R-3063-CORE_META_MODEL-DECLARATION--declare-step-fixed-parameters.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---

## Summary

Declare Step.Fixed Parameters

## Claim

### Prose Claim

A Step may declare fixed parameter values for its invocation. A fixed value is one permitted source of a binding.

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity

declare_entity(entity_name='Fixed Parameters', relation_name="IS_PROPERTY_OF", base_path='Atom/(.Header.Context.Role:=Operations)/Step')
```
