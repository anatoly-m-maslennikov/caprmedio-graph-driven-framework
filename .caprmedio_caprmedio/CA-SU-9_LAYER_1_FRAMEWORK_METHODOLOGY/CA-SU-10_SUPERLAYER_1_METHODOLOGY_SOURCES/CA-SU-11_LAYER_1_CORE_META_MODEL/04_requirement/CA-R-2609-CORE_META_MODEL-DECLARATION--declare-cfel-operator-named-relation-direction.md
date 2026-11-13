---
atom_id: CA-R-2609
ref_id: CA-R-2609
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL<+Operator//NamedRelationDirection
tier: 3
status: active
version: 3
updated_at: '2026-11-13T05:29:21.318804+00:00'
carrier_destination:
  file:
    name: CA-R-2609-CORE_META_MODEL-DECLARATION--declare-cfel-operator-named-relation-direction.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Declare CFEL operator named Relation direction

## Claim

### Prose Claim

`Source ((RELATION)) Target` is forward and `Target <((RELATION)) Source` is reverse writing of the same canonical Relation fact. Counts stay on written endpoints; reverse normalization swaps canonical Host/Target and count slots. The declared Relation name is matched exactly. This CFEL operator is distinct from the named graph Relation. It grants no inverse permission and creates no second stored fact.
### Formal Claim

```python
# model
set_value(address='Operator//NamedRelationDirection', value='"((RELATION)) / <((RELATION))"')
```

