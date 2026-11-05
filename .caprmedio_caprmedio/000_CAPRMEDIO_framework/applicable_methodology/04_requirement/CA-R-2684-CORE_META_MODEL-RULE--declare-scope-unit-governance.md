---
atom_id: CA-R-2684
ref_id: CA-R-2684
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Scope Unit Declaration)
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)
  - CAPRMEDIO_MODEL <+ Scope Unit
tier: 3
status: Active
version: 1
updated_at: 2026-11-02 19:17:40 +0400
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2684-CORE_META_MODEL-RULE--declare-scope-unit-governance.md
  source_atom_id: CA-R-2684
  source_atom_revision: 1
  source_sha256: a95da42f912b9f5754d77a1ac3cc120e378efe48f48a03008b4056cfedc2ced0
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define Scope Unit Declaration form

## Claim

### Prose Claim


Scope Unit Declaration is a Requirement Form. A Scope Unit Declaration Atom has Role = Requirement and Form = Scope Unit Declaration. Its active Subject (`subjects.active`) identifies the specific Scope Unit being declared, rather than the generic Scope Unit kind.

The Declaration is external to its declared Scope Unit. It may carry external Scope Constraints. “External” is relative to the governed Scope Unit; it does not create another Scope Unit or Entity.

The form does not define how many Declarations a Scope Unit has, its fields, folder names, Goals, or Contracts. Those rules belong to their dedicated Requirements, Methods, Evaluations and Delivery Atoms.


```
(Atom//.Role = Requirement & .Form = Scope Unit Declaration & .subjects.active = Scope Unit//)
```
