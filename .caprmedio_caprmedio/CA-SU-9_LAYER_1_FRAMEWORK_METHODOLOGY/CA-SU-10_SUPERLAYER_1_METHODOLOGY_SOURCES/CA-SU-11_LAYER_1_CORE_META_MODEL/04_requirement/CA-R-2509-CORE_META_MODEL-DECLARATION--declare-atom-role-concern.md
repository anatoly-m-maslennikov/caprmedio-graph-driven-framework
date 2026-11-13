---
atom_id: CA-R-2509
ref_id: CA-R-2509
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Concern)
tier: 3
status: active
version: 5
updated_at: '2026-11-12T17:23:54+00:00'
carrier_destination:
  file:
    name: CA-R-2509-CORE_META_MODEL-DECLARATION--declare-atom-role-concern.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Declare Atom/(.Role := Concern)

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import Atom

class Concern(Atom):
    pass

declare_entity(entity_class=Concern, entity_name='Concern', qualification_property_path="Atom.Header.Context.Role", classifications={"Role Order Number": 1})
```

## Semantics

A Concern identifies a question, conflict, or problem.
