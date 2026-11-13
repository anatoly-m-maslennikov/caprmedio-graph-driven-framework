---
atom_id: CA-R-2463
ref_id: CA-R-2463
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)
tier: 3
status: active
version: 7
updated_at: '2026-11-12T12:33:04.158402+00:00'
carrier_destination:
  file:
    name: CA-R-2463-CORE_META_MODEL-DECLARATION--declare-operations.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---

## Summary

Declare Operations

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import Atom

class Operations(Atom):
    pass

declare_entity(
    entity_class=Operations,
    entity_name='Operations',
    qualification_property_path='Atom.Header.Context.Role',
    classifications={'Role Order Number': 9},
)
```

## Semantics

An Operations Atom specifies work to perform and how it is coordinated, including its sequence, inputs and outputs.
