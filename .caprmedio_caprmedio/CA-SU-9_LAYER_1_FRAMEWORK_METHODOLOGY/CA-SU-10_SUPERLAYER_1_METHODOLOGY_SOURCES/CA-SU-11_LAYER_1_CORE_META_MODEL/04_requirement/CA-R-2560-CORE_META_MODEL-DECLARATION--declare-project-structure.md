---
atom_id: CA-R-2560
ref_id: CA-R-2560
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ PROJECT STRUCTURE
tier: 3
status: active
version: 3
updated_at: '2026-11-12T20:21:37.628721+00:00'
carrier_destination:
  file:
    name: CA-R-2560-CORE_META_MODEL-DECLARATION--declare-project-structure.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Declare PROJECT STRUCTURE

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import Node

class ProjectStructure(Node):
    pass

declare_entity(
    entity_class=ProjectStructure,
    entity_name='PROJECT STRUCTURE',
    model_relation_constraints={"IS_PROPERTY_OF": {"targets_per_source": 0}},
    classifications={"Container": "yes"},
)
```

## Semantics

PROJECT STRUCTURE describes the actual structure of a Project, including its Scope Units, Aspects, and other declared components.
