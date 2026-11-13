---
atom_id: CA-R-2616
ref_id: CA-R-2616
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL<+Operator
tier: 3
status: active
version: 3
updated_at: '2026-11-13T05:35:36.099791+00:00'
carrier_destination:
  file:
    name: CA-R-2616-CORE_META_MODEL-DECLARATION--declare-cfel-operator.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Declare CFEL Operator

## Claim

### Prose Claim


A CFEL Operator is one declared language component with one token or bounded construct meaning. Each individual operator-instance Declaration supplies its own token semantics. A CFEL Operator is distinct from a graph Relation and does not create a Node, Relation fact, Property occurrence, Carrier fact, or runtime operation. Its declared operator descriptor may be a graph endpoint where a Relation signature admits declared model entities; a glyph or literal operand is not another model entity.


### Formal Claim

```python
# model
composition(container="CFEL", parts=("Operator",))
```

## Semantics

CFEL<+Operator//Name identifies a declared CFEL operator by semantic name.
Graph Relations and their canonical, derived, inverse, and counterpart semantics
remain in Relation Declarations; punctuation alone does not admit a counterpart.
