---
atom_id: CA-R-2684
status: Active
tier: 3
subjects:
  active: Atom/(.Role := Requirement)/(.Form := Scope Unit Declaration)
  passive:
  - Atom/(.Role := Requirement)
  - Scope Unit
version: 1
updated_at: 2026-11-02 19:17:40 +0400
relations: {}
form: Rule
role: Requirement
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
