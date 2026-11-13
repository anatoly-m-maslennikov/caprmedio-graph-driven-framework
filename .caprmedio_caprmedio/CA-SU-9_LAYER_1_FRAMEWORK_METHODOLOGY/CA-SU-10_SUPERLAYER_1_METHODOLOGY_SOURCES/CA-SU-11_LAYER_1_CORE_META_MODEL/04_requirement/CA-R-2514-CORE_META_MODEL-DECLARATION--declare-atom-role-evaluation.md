---
atom_id: CA-R-2514
ref_id: CA-R-2514
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Evaluation)
tier: 3
status: active
version: 7
updated_at: '2026-11-12T12:33:04.158402+00:00'
carrier_destination:
  file:
    name: CA-R-2514-CORE_META_MODEL-DECLARATION--declare-atom-role-evaluation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---

## Summary

Declare Atom/(.Role := Evaluation)

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import Atom

class Evaluation(Atom):
    pass

declare_entity(
    entity_class=Evaluation,
    entity_name='Evaluation',
    qualification_property_path='Atom.Header.Context.Role',
    classifications={'Role Order Number': 6},
)
```

## Semantics

An Evaluation specifies falsifiable checks and how their evidence is interpreted to determine whether required results are achieved.
