---
atom_id: CA-R-2554
ref_id: CA-R-2554
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit.structural_level
tier: 3
status: active
version: 3
updated_at: '2026-11-12T18:51:56.607337+00:00'
carrier_destination:
  file:
    name: CA-R-2554-CORE_META_MODEL-DECLARATION--declare-scope-unit-structural-level.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---

## Summary

Declare Scope Unit.structural_level

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import ScopeUnit

def check_structural_level(unit: ScopeUnit) -> bool:
    if unit.structural_level is None:
        return False
    if unit.container is None:
        return unit.structural_level == 0
    return (
        unit.container.structural_level is not None
        and unit.structural_level == unit.container.structural_level + 1
    )

declare_entity(
    entity_name="structural_level",
    relation_name="IS_PROPERTY_OF",
    base_path="Scope Unit",
    property_occurrence_cardinality=1,
    value_format=int,
    value_cardinality=1,
    dependent_property_cardinality=0,
    minimum_value=0,
    instance_check=check_structural_level,
)
```

