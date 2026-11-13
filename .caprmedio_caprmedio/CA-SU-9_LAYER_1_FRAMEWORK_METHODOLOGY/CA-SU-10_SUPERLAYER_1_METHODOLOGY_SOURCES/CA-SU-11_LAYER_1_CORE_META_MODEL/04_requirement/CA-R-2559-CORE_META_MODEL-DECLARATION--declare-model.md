---
atom_id: CA-R-2559
ref_id: CA-R-2559
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL
tier: 3
status: active
version: 3
updated_at: '2026-11-12T20:21:33.885135+00:00'
carrier_destination:
  file:
    name: CA-R-2559-CORE_META_MODEL-DECLARATION--declare-model.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Declare MODEL

## Claim

### Prose Claim



- A local MODEL inherits CAPRMEDIO's MODEL.
- MODEL inheritance is distinct from Node narrowing.
- Local overrides replace matching inherited rules in the local MODEL.
- Local overrides preserve the base MODEL's rules.
- Unmodified inherited Declarations are reused.

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import Node

class Model(Node):
    pass

declare_entity(
    entity_class=Model,
    entity_name='MODEL',
    model_relation_constraints={"IS_PROPERTY_OF": {"targets_per_source": 0}},
    classifications={"Container": "yes"},
)
```

## Semantics

MODEL declares Node kinds, Relations, Properties, and rules.
