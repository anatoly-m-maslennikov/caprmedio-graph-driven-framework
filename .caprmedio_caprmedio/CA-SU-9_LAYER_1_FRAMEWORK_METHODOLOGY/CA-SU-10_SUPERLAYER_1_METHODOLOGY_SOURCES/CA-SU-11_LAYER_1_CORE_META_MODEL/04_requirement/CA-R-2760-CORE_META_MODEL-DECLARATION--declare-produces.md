---
atom_id: CA-R-2760
ref_id: CA-R-2760
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//PRODUCES
tier: 1
status: active
version: 1
updated_at: 2026-11-04 16:07:35 +0400
carrier_destination:
  file:
    name: CA-R-2760-CORE_META_MODEL-DECLARATION--declare-produces.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Declare PRODUCES

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_relation

declare_relation(
    relation_name='PRODUCES',
    source_endpoint={"level": "instances", "entity_paths": ('Execution',)},
    target_endpoint={"level": "instances", "entity_paths": ('Event',)},
    inverse_alias='IS_PRODUCED_BY',
)
```

## Semantics

PRODUCES links an Execution to an Event it produced.
