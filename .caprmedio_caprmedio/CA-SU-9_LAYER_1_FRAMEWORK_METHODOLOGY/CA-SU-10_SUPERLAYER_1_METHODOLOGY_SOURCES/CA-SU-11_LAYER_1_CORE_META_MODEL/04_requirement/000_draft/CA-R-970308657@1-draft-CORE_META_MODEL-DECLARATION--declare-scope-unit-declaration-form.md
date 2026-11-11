---
identity:
  id: CA-R-970308657
  ref_id: CA-R-970308657@1-draft
context:
  container:
    scope_unit: CA-SU-11
  role: requirement
  form: declaration
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Form := Scope Unit Declaration)
  tier: 3
relations:
  is_replacement_for:
  - CA-R-3007
state:
  status: draft
  version: 1
  updated_at: '2026-11-11T16:37:55+04:00'
destination:
  file:
    name: CA-R-970308657@1-draft-CORE_META_MODEL-DECLARATION--declare-scope-unit-declaration-form.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft
---


## Summary

Declare Scope Unit Declaration Form

## Claim

### Prose Claim

Scope Unit Declaration is a Requirement Form. Its active Subject identifies one Scope Unit within the Project. Its Formal Claim states the unit’s stable ID, Name and ordering state. It states order.number when ordered. Label is optional. A non-Project Declaration states the unit’s direct Parent. The Project Declaration identifies the Project root and its unordered state.

### Formal Claim

```CFEL
# model
Atom.Header.Context.Form :: Scope Unit Declaration;

# instances
FOR EACH $a[<Atom>, (.Header.Context.Form = Scope Unit Declaration)]:
(
    $a.Header.Context.Role:: [in (Requirement)]{::1};
    $a ((HAS_ACTIVE_SUBJECT)) Scope Unit//$unit;
)
```
