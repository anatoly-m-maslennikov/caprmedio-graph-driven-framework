---
atom_id: CA-R-2542
ref_id: CA-R-2542
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Actor
tier: 3
status: active
version: 3
updated_at: '2026-11-12T17:40:07+00:00'
carrier_destination:
  file:
    name: CA-R-2542-CORE_META_MODEL-DECLARATION--declare-actor.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Declare Actor

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import Continuant

class Actor(Continuant):
    pass

declare_entity(entity_class=Actor, entity_name='Actor')
```

## Semantics

An Actor participates in Project work.
