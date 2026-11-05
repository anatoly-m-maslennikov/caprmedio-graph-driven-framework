---
atom_id: CA-R-2604
ref_id: CA-R-2604
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL<+Operator//InstanceBinding
tier: 3
status: Active
version: 3
updated_at: 2026-11-04 21:11:03 +0400
carrier_destination:
  file:
    name: CA-R-2604-DECLARATION--declare-cfel-operator.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2604-CORE_META_MODEL-DECLARATION--declare-cfel-operator.md
  source_atom_id: CA-R-2604
  source_atom_revision: 3
  source_sha256: 7f08e169debf641dd8956671de194e9935c6eeae72aebd3c6f9a649526775411
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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

Bind an existing selected instance or read its bound Property; it creates nothing. A variable introduced by a standalone typed instance selector such as `Kind//$x;` remains in scope for following statements in the same CFEL fenced block. A variable introduced in an IF condition is in scope within that condition and its matching THEN group only; it is not in scope in following statements. If an outer variable is already bound, a new binding inside IF must use a different variable name; references to the outer variable retain its existing identity.
