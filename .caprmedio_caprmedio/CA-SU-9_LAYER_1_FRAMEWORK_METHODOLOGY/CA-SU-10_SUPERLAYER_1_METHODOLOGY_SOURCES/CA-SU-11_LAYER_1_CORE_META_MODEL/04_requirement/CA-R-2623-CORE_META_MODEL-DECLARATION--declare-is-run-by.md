---
atom_id: CA-R-2623
ref_id: CA-R-2623
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_RUN_BY
tier: 3
status: active
version: 5
updated_at: '2026-11-13T06:26:10.910372+00:00'
carrier_destination:
  file:
    name: CA-R-2623-CORE_META_MODEL-DECLARATION--declare-is-run-by.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
---
## Summary

Declare IS_RUN_BY

## Claim

### Formal Claim

```python
# model
relation(source='Relation//IS_RUN_BY', name='HAS_INVERSE', target='Relation//RUNS', reverse=True)
```
