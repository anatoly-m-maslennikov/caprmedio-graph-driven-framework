---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Target Scope Unit
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Goal)
  - CAPRMEDIO_MODEL <+ Atom.Local Scope Unit
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Project
version: 41
updated_at: 2026-11-04 09:19:08 +0400
relations:
  child_of:
  - CA-R-925@37
  - CA-R-926
  - CA-R-2747
atom_id: CA-R-947
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 6
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-947-CORE_META_MODEL-RULE--validate-goal-claim-scope.md
  source_atom_id: CA-R-947
  source_atom_revision: 41
  source_sha256: 5f003496c43bb35e9e7c949d0f1e264ae08530d6353529b2e94b1f943f65859d
  original_relations_sha256: 91c7b81a93565ea551702b0fc17328a97f5b2ffe919fd4c28fb189c6d4a73e22
---
## Summary
Validate Goal Claim Scope

## Claim

### Prose Claim


Goal Atoms.


a Goal Atom **must** identify **`=1`** Claim Target Scope Unit that is a direct child of its Atom Scope Unit according **to** authoritative Project Structure, **or** the Project Scope Unit **if** its Atom Scope **contains** no Scope Unit. a Goal reference assigns a purpose **and** **must not** independently declare **or** change the target's Name, parent, order, **or** Carrier binding.
