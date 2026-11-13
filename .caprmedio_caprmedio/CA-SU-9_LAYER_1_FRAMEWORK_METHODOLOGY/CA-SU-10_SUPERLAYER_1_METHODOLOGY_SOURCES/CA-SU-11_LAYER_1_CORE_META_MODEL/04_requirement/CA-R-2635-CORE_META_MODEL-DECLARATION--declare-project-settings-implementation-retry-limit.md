---
atom_id: CA-R-2635
ref_id: CA-R-2635
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project.Settings.Implementation Retry Limit
tier: 3
status: active
version: 3
updated_at: '2026-11-12T17:23:54+00:00'
carrier_destination:
  file:
    name: CA-R-2635-CORE_META_MODEL-DECLARATION--declare-project-settings-implementation-retry-limit.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---

## Summary

Declare Project.Settings.Implementation Retry Limit

## Claim

### Prose Claim


An omitted value follows the governed default resolution. A value is an integer at least zero. Zero permits no retries after the initial failure. The limit does not grant repair permission or bypass authority or confidence rules.

### Formal Claim

```python
# model
from caprmedio.formal_claims import Cardinality, declare_entity

declare_entity(
    entity_name='Implementation Retry Limit',
    relation_name='IS_PROPERTY_OF',
    base_path='Project.Settings',
    value_cardinality=Cardinality(minimum=0, maximum=1),
    value_format='int',
    dependent_property_cardinality=0,
)
```

