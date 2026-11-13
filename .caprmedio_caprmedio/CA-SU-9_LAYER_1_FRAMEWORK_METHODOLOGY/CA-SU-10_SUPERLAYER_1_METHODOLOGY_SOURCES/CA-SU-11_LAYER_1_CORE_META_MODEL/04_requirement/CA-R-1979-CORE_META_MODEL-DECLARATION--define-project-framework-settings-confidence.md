---
atom_id: CA-R-1979
ref_id: CA-R-1979
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project.Settings.Confidence
tier: 3
relations:
  child_of:
  - CA-R-1176
status: active
version: 17
updated_at: '2026-11-12T17:23:54+00:00'
carrier_destination:
  file:
    name: CA-R-1979-CORE_META_MODEL-DECLARATION--define-project-framework-settings-confidence.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Project.Framework Settings.Confidence

## Claim

### Prose Claim


the Confidence grouping in the Project's Framework Settings.



### Formal Claim

```python
# model
from caprmedio.formal_claims import Cardinality, declare_entity

declare_entity(
    entity_name='Confidence',
    relation_name='IS_PROPERTY_OF',
    base_path='Project.Settings',
    property_occurrence_cardinality=Cardinality(minimum=0, maximum=1),
    value_cardinality=0,
    dependent_property_cardinality=Cardinality(minimum=0, maximum=2),
    allowed_dependent_property_names=('Necessary Information Threshold', 'Semantic Resolution Threshold'),
    dependent_property_value_format='int',
)
```

## Details

Evidence: CA-R-1652 defines the necessary-information threshold default; CA-R-380 defines the semantic-resolution threshold default. These define the child settings, not the parent grouping. Candidate #6 decision 8 retains Settings as the default source, and decision 18 distinguishes Project settings from the framework's name. This grouping adds no threshold, override layer or mandatory value. Concrete CAPRMEDIO setting definitions belong in Project Configuration.
