---
atom_id: CA-R-2749
ref_id: CA-R-2749
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Execution
tier: 3
status: active
version: 1
updated_at: 2026-11-05 01:38:59 +0400
carrier_destination:
  file:
    name: CA-R-2749-CORE_META_MODEL-DECLARATION--declare-execution.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Declare Execution

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity, Cardinality
from caprmedio.model import Occurrent

class Execution(Occurrent):
    pass

declare_entity(
    entity_class=Execution,
    entity_name='Execution',
    instance_relation_constraints={
        'IS_EXECUTED_BY': {"target_entity_paths": ('Runtime',), "targets_per_source": Cardinality(minimum=1, maximum=None)},
        'PRODUCES': {"target_entity_paths": ('Event',), "targets_per_source": Cardinality(minimum=0, maximum=None)},
    },
)
```

## Semantics

An Execution is the actual performance of work.
