---
atom_id: CA-R-2604
ref_id: CA-R-2604@4-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL<+Operator//InstanceBinding
tier: 3
status: Draft
version: 4
updated_at: 2026-11-05 03:25:14 +0400
carrier_destination:
  file:
    name: CA-R-2604@4-draft-DECLARATION--declare-cfel-operator.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft
---

## Summary

Declare CFEL operator $

## Claim

### Formal Claim

```CFEL
# model
Operator//InstanceBinding == "$"
```

## Semantics

Bind an existing selected instance or read its bound Property; it creates nothing. `<Kind>` references a declared Model kind. `$x[<Kind>, (conditions)]` is the successor spelling of `Kind//$x`: it binds an existing instance of that kind as a named participant, subject to grouped conditions evaluated against that participant. `$<Kind>` is the anonymous successor spelling of `Kind//`. Repeated anonymous selections use the same domain but do not assert that their referents are identical or different; use a named participant to assert the same selected identity. These expressions create nothing and do not turn a model entity into a data-layer fact. `Journal//{:1}` and its successor forms `$<Journal>{::1}` and `$journal[<Journal>]{::1}` each constrain the selected logical Journal instance population within the Current Project to exactly one; they do not create that instance. A variable introduced by a standalone typed instance selector such as `Kind//$x;` or `$x[<Kind>];` remains in scope for following statements in the same CFEL fenced block. A variable introduced in an IF condition is in scope within that condition and its matching THEN group only; it is not in scope in following statements. If an outer variable is already bound, a new binding inside IF must use a different variable name; references to the outer variable retain its existing identity.
