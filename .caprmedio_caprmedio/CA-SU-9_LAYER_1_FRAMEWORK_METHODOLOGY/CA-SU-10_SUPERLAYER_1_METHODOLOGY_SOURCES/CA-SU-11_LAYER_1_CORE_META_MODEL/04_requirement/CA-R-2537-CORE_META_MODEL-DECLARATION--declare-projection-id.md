---
atom_id: CA-R-2537
ref_id: CA-R-2537
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection.ID
tier: 3
status: active
version: 4
updated_at: '2026-11-13T03:54:21.584142+00:00'
carrier_destination:
  file:
    name: CA-R-2537-CORE_META_MODEL-DECLARATION--declare-projection-id.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Declare Projection.ID

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity

declare_entity(
    entity_name="ID", relation_name="IS_PROPERTY_OF", base_path="Projection",
    property_occurrence_cardinality=1, value_format=str, value_cardinality=1,
    dependent_property_cardinality=0,
    population_functional_dependencies=(
        {"keys": ("Form", "Scope Unit"), "dependents": ("ID",)},
        {"keys": ("ID",), "dependents": ("Form", "Scope Unit")},
    ),
)
```

