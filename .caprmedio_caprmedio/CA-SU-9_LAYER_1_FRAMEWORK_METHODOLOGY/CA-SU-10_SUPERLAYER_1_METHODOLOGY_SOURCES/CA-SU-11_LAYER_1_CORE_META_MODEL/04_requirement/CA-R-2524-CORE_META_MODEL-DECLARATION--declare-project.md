---
atom_id: CA-R-2524
ref_id: CA-R-2524
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project
tier: 3
status: active
version: 7
updated_at: '2026-11-12T12:33:04.158402+00:00'
container:
  scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-R-2524-CORE_META_MODEL-DECLARATION--declare-project.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---

## Summary

Declare Project

## Claim

### Prose Claim

A Project uses CAPRMEDIO's MODEL.

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import ScopeUnit

class Project(ScopeUnit):
    pass

declare_entity(
    entity_class=Project,
    entity_name='Project',
    classifications={'Container': 'yes'},
    instance_population_cardinality=1,
    instance_population_scope='project',
    instance_relation_constraints={'IS_CONTAINED_BY': {'target_entity_paths': ('Scope Unit',), 'targets_per_source': 0}},
    required_instance_property_values={'order.ordered': False},
    instance_property_constraints={'order.number': {'value_cardinality': 0}},
)
```

## Semantics

A Project is the root Scope Unit. It is not renamed or moved through Scope Unit operations. Its one stable Scope Unit ID is governed by CA-R-2526. The shared model makes Project unordered with no order.number; individual Project Declarations inherit these facts.
