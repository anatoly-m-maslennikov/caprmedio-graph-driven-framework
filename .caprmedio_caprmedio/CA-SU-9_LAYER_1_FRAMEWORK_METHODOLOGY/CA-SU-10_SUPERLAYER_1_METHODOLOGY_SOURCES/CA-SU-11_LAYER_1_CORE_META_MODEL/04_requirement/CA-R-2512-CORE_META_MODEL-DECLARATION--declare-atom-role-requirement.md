---
atom_id: CA-R-2512
ref_id: CA-R-2512
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Requirement)
tier: 3
status: active
version: 7
updated_at: '2026-11-12T12:33:04.158402+00:00'
carrier_destination:
  file:
    name: CA-R-2512-CORE_META_MODEL-DECLARATION--declare-atom-role-requirement.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---

## Summary

Declare Atom/(.Role := Requirement)

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import Atom

class Requirement(Atom):
    pass

declare_entity(
    entity_class=Requirement,
    entity_name='Requirement',
    qualification_property_path='Atom.Header.Context.Role',
    classifications={'Role Order Number': 4},
)
```

## Semantics

A Requirement states a required outcome, behavior, property or constraint, or defines a governed model and its constraints. It applies across Aspects, including domain behavior, engineering performance, evaluation effectiveness and delivery reliability.
