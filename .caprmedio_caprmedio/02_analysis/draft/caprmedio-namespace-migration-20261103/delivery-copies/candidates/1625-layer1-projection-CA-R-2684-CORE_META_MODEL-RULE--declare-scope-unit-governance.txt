---
atom_id: CA-R-2684
status: Active
tier: 3
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom/(.Role := Requirement)/(.Form := Scope Unit Declaration)
  passive:
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Requirement)
  - CAPRMEDIO <+ MODEL <+ Scope Unit
version: 1
updated_at: 2026-11-02 19:17:40 +0400
relations: {}
form: Rule
role: Requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2684-CORE_META_MODEL-RULE--declare-scope-unit-governance.md
  source_atom_id: CA-R-2684
  source_atom_revision: 1
  source_sha256: 44da6f2be2c56c17afd4353bbe036129e802e2696ff62fb7ae5f08fd88c3e656
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define Scope Unit Declaration form

## Claim

Scope Unit Declaration is a Requirement Form. A Scope Unit Declaration Atom has Role = Requirement and Form = Scope Unit Declaration. Its active Subject (`subjects.active`) identifies the specific Scope Unit being declared, rather than the generic Scope Unit kind.

The Declaration is external to its declared Scope Unit. It may carry external Scope Constraints. “External” is relative to the governed Scope Unit; it does not create another Scope Unit or Entity.

The form does not define how many Declarations a Scope Unit has, its fields, folder names, Goals, or Contracts. Those rules belong to their dedicated Requirements, Methods, Evaluations and Delivery Atoms.

### Formal claim

```
(Atom//.Role = Requirement & .Form = Scope Unit Declaration & .subjects.active = Scope Unit//)
```
