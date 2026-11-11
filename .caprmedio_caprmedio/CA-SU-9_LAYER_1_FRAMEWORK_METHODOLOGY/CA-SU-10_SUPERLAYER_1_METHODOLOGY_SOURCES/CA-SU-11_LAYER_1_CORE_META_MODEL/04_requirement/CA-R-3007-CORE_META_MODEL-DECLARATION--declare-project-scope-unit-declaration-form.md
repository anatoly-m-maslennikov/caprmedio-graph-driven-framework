---
atom_id: CA-R-3007
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Form := Scope Unit Declaration)
tier: 3
ref_id: CA-R-3007
status: Active
version: 3
updated_at: '2026-11-11 14:06:22 +0400'
carrier_destination:
  file:
    name: CA-R-3007-CORE_META_MODEL-DECLARATION--declare-project-scope-unit-declaration-form.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---

## Summary

Declare Project Scope Unit Declaration Form

## Claim

### Prose Claim

Scope Unit Declaration is the Requirement Form for the Project-root Scope Unit Declaration. Its active Subject identifies a Project Scope Unit. Non-Project Scope Units use Scope Delegation.

### Formal Claim

```CFEL
# model
Atom.Header.Context.Form :: Scope Unit Declaration;

# instances
FOR EACH $a[<Atom>, (.Header.Context.Form = Scope Unit Declaration)]:
(
    $a.Header.Context.Role:: [in (Requirement)]{::1};
    $a ((HAS_ACTIVE_SUBJECT)) Scope Unit/Project//$project;
)
```
