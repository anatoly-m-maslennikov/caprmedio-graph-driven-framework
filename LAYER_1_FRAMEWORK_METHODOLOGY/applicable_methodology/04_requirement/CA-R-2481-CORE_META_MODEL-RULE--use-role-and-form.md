---
atom_id: CA-R-2481
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: Atom/(.Role := Requirement)/(.Form := Declaration)
  passive:
  - Atom
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2481-CORE_META_MODEL-RULE--use-role-and-form.md
  source_atom_id: CA-R-2481
  source_atom_revision: 2
  source_sha256: 3bf88dc5974200938d933c59b48637443c47a6c78bb67c431136ccff53766b9a
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Use Role and Form for Declaration Atoms

## Claim scope

The proposed authored representation and formal paths of a Node Declaration.

## Claim

The proposed Atom schema **must** distinguish Role from Form. The current Atom `content_role` field maps to the proposed `role` value, and the current `type` field maps to the proposed `form` value. A Declaration Atom has `role: Requirement` and `form: Declaration`; Declaration is a Form under the Requirement Role, not a new Role value. In Subject addresses, express that pair as `Atom/(.Role := Requirement)/(.Form := Declaration)`. Use `Form` for the form qualifier in place of a legacy nested `Role: X` or `Type: X` qualifier.

Role identifies the contribution. Form identifies its authoring form and does not override or duplicate Role.
