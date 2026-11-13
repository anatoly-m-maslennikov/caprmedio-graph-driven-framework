---
atom_id: CA-R-2617
ref_id: CA-R-2617@4-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//CONTAINS
tier: 3
status: draft
version: 4
updated_at: '2026-11-13T07:37:38.992804+00:00'
carrier_destination:
  file:
    name: CA-R-2617@4-draft-CORE_META_MODEL-DECLARATION--declare-contains.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft
current_scope_unit: CORE_META_MODEL
---
## Summary

Declare CONTAINS

## Claim

### Formal Claim

```python
# model
relation(source='Relation//CONTAINS', name='HAS_INVERSE', target='Relation//IS_CONTAINED_BY', reverse=True)
set_value(address='alias(Relation//CONTAINS)', value='<+')

```
