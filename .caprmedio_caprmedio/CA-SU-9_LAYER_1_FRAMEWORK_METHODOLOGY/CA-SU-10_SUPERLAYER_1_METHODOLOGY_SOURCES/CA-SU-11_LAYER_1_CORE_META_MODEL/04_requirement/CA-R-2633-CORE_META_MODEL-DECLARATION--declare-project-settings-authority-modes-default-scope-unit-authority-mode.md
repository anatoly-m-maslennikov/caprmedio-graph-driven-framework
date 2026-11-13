---
atom_id: CA-R-2633
ref_id: CA-R-2633
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project.Settings.Authority Modes.Default Scope
    Unit Authority Mode
tier: 3
status: active
version: 3
updated_at: '2026-11-12T17:23:54+00:00'
carrier_destination:
  file:
    name: CA-R-2633-CORE_META_MODEL-DECLARATION--declare-project-settings-authority-modes-default-scope-unit-authority-mode.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---

## Summary

Declare Project.Settings.Authority Modes.Default Scope Unit Authority Mode

## Claim

### Prose Claim


The permitted values are `strict` and `casual`. The effective selection follows the applicable authority-mode resolution.

### Formal Claim

```python
# model
from caprmedio.formal_claims import declare_entity

declare_entity(
    entity_name='Default Scope Unit Authority Mode',
    relation_name='IS_PROPERTY_OF',
    base_path='Project.Settings.Authority Modes',
    property_occurrence_cardinality=1,
    value_cardinality=1,
    dependent_property_cardinality=0,
)
```

