---
atom_id: CA-R-2532
ref_id: CA-R-2532
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project.Settings
tier: 3
status: active
version: 9
updated_at: '2026-11-12T17:23:54+00:00'
carrier_destination:
  file:
    name: CA-R-2532-CORE_META_MODEL-DECLARATION--declare-project-settings.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Declare Project.Settings

## Claim

### Formal Claim

```python
# model
from caprmedio.formal_claims import Cardinality, declare_entity

declare_entity(
    entity_name='Settings',
    relation_name='IS_PROPERTY_OF',
    base_path='Project',
    property_occurrence_cardinality=1,
    value_cardinality=0,
    dependent_property_cardinality=Cardinality(minimum=3, maximum=11),
    allowed_dependent_property_names=('Name', 'Prefix', 'AI Agent Confidence Threshold', 'Artifact Timestamp Timezone', 'Code-Root Locators', 'Confidence', 'Framework Control-Root Locator', 'Interaction', 'Authority Modes', 'Implementation Retry Limit', 'RMED Review'),
)
```

