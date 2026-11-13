---
atom_id: CA-R-2604
ref_id: CA-R-2604@5-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL<+Operator//InstanceBinding
tier: 3
status: draft
version: 5
updated_at: '2026-11-13T07:05:38.647579+00:00'
carrier_destination:
  file:
    name: CA-R-2604@5-draft-CORE_META_MODEL-DECLARATION--declare-cfel-operator.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft
---

## Summary

Declare CFEL operator $

## Claim

### Formal Claim

```python
# model
set_value(address='Operator//InstanceBinding', value='"$"')
```

## Semantics

Bind an existing selected instance or read its bound Property; it creates nothing. A variable introduced by a standalone typed instance selector such as `Kind//$x;` remains in scope for following statements in the same CFEL fenced block. A variable introduced in an IF condition is in scope within that condition and its matching THEN group only; it is not in scope in following statements. If an outer variable is already bound, a new binding inside IF must use a different variable name; references to the outer variable retain its existing identity.
