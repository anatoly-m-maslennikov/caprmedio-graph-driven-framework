---
atom_id: CA-R-1980
ref_id: CA-R-1980
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project.Settings.Framework Control-Root Locator
tier: 3
relations:
  child_of:
  - CA-R-1176
status: active
version: 17
updated_at: '2026-11-12T17:23:54+00:00'
carrier_destination:
  file:
    name: CA-R-1980-CORE_META_MODEL-DECLARATION--define-project-framework-settings-framework-control-root-locator.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Project.Framework Settings.Framework Control-Root Locator

## Claim

### Prose Claim


the Project's framework control-root reference in Framework Settings.



### Formal Claim

```python
# model
from caprmedio.formal_claims import Cardinality, declare_entity

declare_entity(
    entity_name='Framework Control-Root Locator',
    relation_name='IS_PROPERTY_OF',
    base_path='Project.Settings',
    value_cardinality=Cardinality(minimum=0, maximum=1),
    value_format='str',
    dependent_property_cardinality=0,
)
```

## Details

Evidence: CA-D-370 requires the locator to resolve to the Directory Carrier prescribed by CA-D-317 without selecting another authority root. Candidate #6 keeps concrete CAPRMEDIO mechanisms in Project Configuration. This definition adds no path or alternative authority root; those remain Delivery rules.
