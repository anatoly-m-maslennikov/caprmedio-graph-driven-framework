---
atom_id: CA-R-2535
ref_id: CA-R-2535
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
tier: 3
status: active
version: 3
updated_at: '2026-11-12T19:19:43.082639+00:00'
carrier_destination:
  file:
    name: CA-R-2535-CORE_META_MODEL-DECLARATION--declare-projection.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Declare Projection

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import Continuant

class Projection(Continuant):
    pass

declare_entity(
    entity_class=Projection,
    entity_name="Projection",
    model_relation_constraints={"IS_PROPERTY_OF": {"targets_per_source": 0}},
)
```

## Semantics

A Projection is a derived view of source Atoms. It does not establish or override their Claims.
