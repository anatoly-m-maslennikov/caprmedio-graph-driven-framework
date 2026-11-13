---
atom_id: CA-R-2524
ref_id: CA-R-2524@4-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project
tier: 3
status: Draft
version: 4
updated_at: 2026-11-05 12:58:42 +0400
carrier_destination:
  file:
    name: CA-R-2524@4-draft-CORE_META_MODEL-DECLARATION--declare-project.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft
---

## Summary

Declare Project

## Claim

### Prose Claim


A Project uses CAPRMEDIO's MODEL.


### Formal Claim

```python
# model
subject_path(address='Scope Unit/Project')
classify(address='Project', axis='Container', value='yes', grouped=True)
relation(source='Project', name='NARROWER_THAN', target='Scope Unit')
# instances
population(address='Scope Unit/Project//$scope_unit', count='1')
relation(source='Project//$project', name='IS_CONTAINED_BY', target='Scope Unit//$scope_unit_2', source_count='0')
set_value(address='Project//$project_2.order.ordered', value=False)
property_rule(address='Project//$project_3.order.number', value_format='', values='0')
```

## Semantics

A Project is the root Scope Unit. The Project is not renamed or moved through Scope Unit operations. It has a stable Scope Unit ID. The shared model makes it Unordered with no order.number; individual Project Declarations inherit these facts.
