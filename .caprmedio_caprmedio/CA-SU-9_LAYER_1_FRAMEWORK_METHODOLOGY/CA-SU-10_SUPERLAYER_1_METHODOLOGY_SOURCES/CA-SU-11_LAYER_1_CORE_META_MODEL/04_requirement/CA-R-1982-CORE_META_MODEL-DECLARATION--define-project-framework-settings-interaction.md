---
atom_id: CA-R-1982
ref_id: CA-R-1982
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project.Settings.Interaction
tier: 3
relations:
  child_of:
  - CA-R-1176
status: active
version: 16
updated_at: '2026-11-12T17:23:54+00:00'
carrier_destination:
  file:
    name: CA-R-1982-CORE_META_MODEL-DECLARATION--define-project-framework-settings-interaction.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Project.Framework Settings.Interaction

## Claim

### Prose Claim


the Interaction grouping in the Project's Framework Settings.



### Formal Claim

```python
# model
from caprmedio.formal_claims import Cardinality, declare_entity

declare_entity(
    entity_name='Interaction',
    relation_name='IS_PROPERTY_OF',
    base_path='Project.Settings',
    property_occurrence_cardinality=Cardinality(minimum=0, maximum=1),
    value_cardinality=0,
    dependent_property_cardinality=1,
    allowed_dependent_property_names=('Reporting Mode',),
)
```

## Details

Evidence: CA-R-1628 defines reporting-mode values; CA-R-1439 limits effects to presentation; CA-R-1440 preserves mandatory information. These define the child setting and its constraints, not the parent grouping. Candidate #6 keeps concrete CAPRMEDIO mechanisms in Project Configuration. This grouping adds no authorization, workflow, validation or safety behavior.
