---
atom_id: CA-R-1958
ref_id: CA-R-1958
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Carrier
tier: 1
relations:
  child_of:
  - CA-R-1174
status: active
version: 17
updated_at: '2026-11-12T17:40:07+00:00'
carrier_destination:
  file:
    name: CA-R-1958-CORE_META_MODEL-DECLARATION--define-entity-carrier.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Entity/Carrier

## Claim

### Prose Claim

A Carrier is a storage representation distinct from the Object it represents. An Object is an instance of any model Entity.

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity

class Carrier:
    pass

declare_entity(entity_class=Carrier, entity_name='Carrier')
```

