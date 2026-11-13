---
atom_id: CA-R-2579
ref_id: CA-R-2579
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Event Record.object_output.updated_at
tier: 3
status: active
version: 3
updated_at: '2026-11-12T12:33:04.158402+00:00'
carrier_destination:
  file:
    name: CA-R-2579-CORE_META_MODEL-DECLARATION--declare-event-record-object-output-updated-at.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Declare Event Record.object_output.updated_at

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from datetime import datetime

declare_entity(
    entity_name='updated_at',
    relation_name='IS_PROPERTY_OF',
    base_path='Event Record.object_output',
    value_format=datetime,
    property_occurrence_cardinality=1,
    value_cardinality=1,
    dependent_property_cardinality=0,
)
```

