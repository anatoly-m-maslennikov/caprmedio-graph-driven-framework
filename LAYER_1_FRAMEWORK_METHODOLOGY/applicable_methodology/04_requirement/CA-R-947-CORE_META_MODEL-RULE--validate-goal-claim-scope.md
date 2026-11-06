---
atom_id: CA-R-947
ref_id: CA-R-947
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Target Scope Unit
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Goal)
  - CAPRMEDIO_MODEL <+ Atom.Local Scope Unit
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Project
tier: 6
relations:
  child_of:
  - CA-R-925@37
  - CA-R-926
  - CA-R-2747
status: Active
version: 41
updated_at: 2026-11-04 09:19:08 +0400
carrier_destination:
  file:
    name: CA-R-947-CORE_META_MODEL-RULE--validate-goal-claim-scope.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-947-CORE_META_MODEL-RULE--validate-goal-claim-scope.md
  source_atom_id: CA-R-947
  source_atom_revision: 41
  source_sha256: 288bc9ede4f004602e31815e6b4620b40914cb1a06bd149e0ee2d45b245a4034
  original_relations_sha256: 91c7b81a93565ea551702b0fc17328a97f5b2ffe919fd4c28fb189c6d4a73e22
---
## Summary
Validate Goal Claim Scope

## Claim

### Prose Claim


Goal Atoms.


a Goal Atom **must** identify **`=1`** Claim Target Scope Unit that is a direct child of its Atom Scope Unit according **to** authoritative Project Structure, **or** the Project Scope Unit **if** its Atom Scope **contains** no Scope Unit. a Goal reference assigns a purpose **and** **must not** independently declare **or** change the target's Name, parent, order, **or** Carrier binding.
