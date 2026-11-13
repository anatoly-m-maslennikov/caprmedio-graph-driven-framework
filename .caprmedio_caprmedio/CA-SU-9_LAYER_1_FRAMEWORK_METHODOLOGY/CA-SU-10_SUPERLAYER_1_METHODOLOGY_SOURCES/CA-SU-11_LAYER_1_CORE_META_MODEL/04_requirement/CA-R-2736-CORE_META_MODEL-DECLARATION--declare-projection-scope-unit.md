---
atom_id: CA-R-2736
ref_id: CA-R-2736
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection.Scope Unit
tier: 3
status: active
version: 2
updated_at: '2026-11-12T23:17:21.180957+00:00'
carrier_destination:
  file:
    name: CA-R-2736-CORE_META_MODEL-DECLARATION--declare-projection-scope-unit.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---

## Summary

Declare Projection.Scope Unit

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import ScopeUnit

declare_entity(
    entity_name="Scope Unit",
    relation_name="IS_PROPERTY_OF",
    base_path="Projection",
    property_occurrence_cardinality=1,
    value_format=ScopeUnit,
    value_cardinality=1,
    dependent_property_cardinality=0,
)
```

