---
atom_id: CA-R-3007
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Form := Scope Unit Declaration)
tier: 3
ref_id: CA-R-3007@2
status: Archived
version: 2
updated_at: "2026-11-07 15:18:44 +0400"
carrier_destination:
  file:
    name: CA-R-3007@2-CORE_META_MODEL-DECLARATION--declare-project-scope-unit-declaration-form.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/archive
---

## Summary

Declare Project Scope Unit Declaration Form

## Claim

### Prose Claim

Scope Unit Declaration is the Requirement Form for the Project-root Scope Unit Declaration. Its active Subject identifies a Project Scope Unit. Non-Project Scope Units use Scope Delegation.

### Formal Claim

```CFEL
# instances
Atom/(.Header.Form := Scope Unit Declaration)//$root_scope_declaration;
$root_scope_declaration.Header.Role:: [in (Requirement)]{::1};
$root_scope_declaration ((HAS_ACTIVE_SUBJECT)) Scope Unit/Project//$project;
```
