---
subjects:
  active: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Goal)'
  passive:
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit.Parent
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit.Children
version: 39
updated_at: 2026-11-02 19:44:26 +0400
relations:
  child_of:
  - CA-R-925@37
atom_id: CA-R-926
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 5
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-926-CORE_META_MODEL-RULE--let-direct-parents-define-non-project-goals.md
  source_atom_id: CA-R-926
  source_atom_revision: 39
  source_sha256: 88b4ca286f527aa9cbf0cb0242a523bc12a1f827d12088c9d48d033da9b40786
  original_relations_sha256: dd57d219aa140ba8b8c8278982e1d4f4e92c8575d8f69e445395c034eaf3ac3e
---
## Summary
Let Direct Parents Define Non-Project Goals

## Claim

### Prose Claim


Non-Project Scope Units.


**every** non-Project Scope Unit **must** have **`>=1`** accepted Goal Atom owned by its declared direct parent Scope Unit. this is a Goal-coverage obligation, **not** the source of the child's structural identity; a missing accepted Goal is a reported gap **and** **must not** remove **or** conceal the declared Scope Unit.
