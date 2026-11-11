---
atom_id: CA-R-3007
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Form := Scope Unit Declaration)
tier: 3
ref_id: CA-R-3007
status: Active
version: 2
updated_at: "2026-11-07 15:18:44 +0400"
carrier_destination:
  file:
    name: CA-R-3007-CORE_META_MODEL-DECLARATION--declare-project-scope-unit-declaration-form.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-3007-CORE_META_MODEL-DECLARATION--declare-project-scope-unit-declaration-form.md
  source_atom_id: CA-R-3007
  source_atom_revision: 2
  source_sha256: 959ea802612833afa410ae6fba2924191e500a5ef385dc459fbe186660b62832
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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
