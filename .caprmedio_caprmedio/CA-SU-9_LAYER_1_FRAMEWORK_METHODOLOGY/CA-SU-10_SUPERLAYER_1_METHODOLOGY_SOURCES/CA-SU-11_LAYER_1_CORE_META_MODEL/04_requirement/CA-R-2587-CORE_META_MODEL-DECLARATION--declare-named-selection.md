---
atom_id: CA-R-2587
ref_id: CA-R-2587
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Named Selection
tier: 3
status: active
version: 3
updated_at: '2026-11-12T19:19:39.079406+00:00'
carrier_destination:
  file:
    name: CA-R-2587-CORE_META_MODEL-DECLARATION--declare-named-selection.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Declare Named Selection

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import Continuant

class NamedSelection(Continuant):
    pass

declare_entity(
    entity_class=NamedSelection,
    entity_name="Named Selection",
    model_relation_constraints={"IS_PROPERTY_OF": {"targets_per_source": 0}},
)
```

## Semantics

A Named Selection names criteria for choosing members. Selected members retain their identity.
