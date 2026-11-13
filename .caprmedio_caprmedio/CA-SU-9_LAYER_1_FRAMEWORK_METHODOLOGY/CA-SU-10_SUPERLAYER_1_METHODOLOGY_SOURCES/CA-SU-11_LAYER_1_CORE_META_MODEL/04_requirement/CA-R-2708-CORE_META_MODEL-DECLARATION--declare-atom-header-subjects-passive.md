---
atom_id: CA-R-2708
ref_id: CA-R-2708
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Context.Topics.Dependencies
tier: 3
status: active
version: 2
updated_at: '2026-11-13T02:05:10.331403+00:00'
carrier_destination:
  file:
    name: CA-R-2708-CORE_META_MODEL-DECLARATION--declare-atom-header-subjects-passive.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Declare Atom.Header.Subjects.Passive

## Claim

### Prose Claim

Dependencies identify direct contextual dependencies.

### Formal Claim

```python
from caprmedio.formal_claims import Cardinality, declare_entity
from caprmedio.model import Atom

def dependencies_are_distinct(atom: Atom) -> bool:
    return len(atom.dependencies) == len(set(atom.dependencies))

declare_entity(
    entity_name="Dependencies",
    relation_name="IS_PROPERTY_OF",
    base_path="Atom.Header.Context.Topics",
    property_occurrence_cardinality=Cardinality(minimum=0, maximum=1),
    value_format=str,
    value_cardinality=Cardinality(minimum=0, maximum=None),
    dependent_property_cardinality=0,
    instance_check=dependencies_are_distinct,
)
```
