---
identity:
  atom_id: CA-R-3128
  ref_id: CA-R-3128
context:
  role: requirement
  form: declaration
  container:
    scope_unit: CA-SU-11
  tier: 3
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Scope Unit.Paths
state:
  version: 1
  status: active
  updated_at: '2026-11-12T22:03:59.156641+00:00'
destination:
  file:
    name: CA-R-3128-CORE_META_MODEL-DECLARATION--declare-scope-unit-paths.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Declare Scope Unit Paths

## Claim

### Prose Claim

Paths groups the Scope Unit’s two physical folder paths. Each path is relative to the Project root.

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity

declare_entity(
    entity_name="Paths",
    relation_name="IS_PROPERTY_OF",
    base_path="Scope Unit",
    property_occurrence_cardinality=1,
    value_cardinality=0,
    dependent_property_cardinality=2,
    allowed_dependent_property_names=("Authority", "Delivery"),
)
```
