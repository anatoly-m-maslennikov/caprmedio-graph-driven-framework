---
atom_id: CA-R-2481
ref_id: CA-R-2481
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Declaration)
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom
version: 2
updated_at: 2026-11-02 00:18:22 +0400
tier: 3
role: Requirement
form: Rule
container:
  scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-R-2481-CORE_META_MODEL-RULE--use-role-and-form-for-declaration-atoms.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Use Role and Form for Declaration Atoms

## Claim

### Prose Claim


The proposed authored representation and formal paths of a Node Declaration.


The proposed Atom schema **must** distinguish Role from Form. The current Atom `content_role` field maps to the proposed `role` value, and the current `type` field maps to the proposed `form` value. A Declaration Atom has `role: Requirement` and `form: Declaration`; Declaration is a Form under the Requirement Role, not a new Role value. In Subject addresses, express that pair as `Atom/(.Header.Role := Requirement)/(.Header.Form := Declaration)`. Use `Form` for the form qualifier in place of a legacy nested `Role: X` or `Type: X` qualifier.

Role identifies the contribution. Form identifies its authoring form and does not override or duplicate Role.
