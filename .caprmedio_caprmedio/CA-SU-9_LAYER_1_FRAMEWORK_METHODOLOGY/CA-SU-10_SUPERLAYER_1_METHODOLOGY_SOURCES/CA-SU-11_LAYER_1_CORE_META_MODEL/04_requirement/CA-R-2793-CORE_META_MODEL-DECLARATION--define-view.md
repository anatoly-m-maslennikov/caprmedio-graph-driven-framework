---
identity:
  atom_id: CA-R-2793
  ref_id: CA-R-2793
context:
  container:
    scope_unit: CA-SU-11
  role: Requirement
  form: Declaration
  topics:
    main_subject: MODEL//CAPRMEDIO <+ (View, View.id, View.sql, View.name)
  tier: 3
state:
  status: active
  version: 5
  updated_at: '2026-11-13T04:14:36.994022+00:00'
destination:
  file:
    name: CA-R-2793-CORE_META_MODEL-DECLARATION--define-view.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
author: Anatoly Maslennikov
---
## Summary

Define View

## Claim

### Prose Claim

A View is a Workbench SQL document in one Workspace. It has one stable string ID, one complete SQL query and may have one name. A View can be edited, run, fetched, focused, renamed, removed or saved through the Workspace operations.

### Formal Claim

```python
from dataclasses import dataclass, field
from caprmedio.formal_claims import Cardinality, declare_entity

@dataclass
class View:
    id: str = field(metadata={
        "property_occurrence_cardinality": 1,
        "value_cardinality": 1,
    })
    sql: str = field(metadata={
        "property_occurrence_cardinality": 1,
        "value_cardinality": 1,
    })
    name: str = field(metadata={
        "property_occurrence_cardinality": Cardinality(minimum=0, maximum=1),
        "value_cardinality": Cardinality(minimum=0, maximum=1),
    })

declare_entity(entity_name="View", entity_class=View)
```
