---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom.Target Scope Unit
  passive:
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement/Type: Goal'
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom.Local Scope Unit
  - CAPRMEDIO <+ MODEL <+ Scope Unit
  - CAPRMEDIO <+ MODEL <+ Project
version: 40
updated_at: 2026-11-02 19:44:26 +0400
relations:
  child_of:
  - CA-R-925@37
  - CA-R-926
  - CA-R-927
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
  source_atom_revision: 40
  source_sha256: 836297c36b26c85fe1efe5aa18fb8c8db39987ae18049d594752c1e6b879f0e0
  original_relations_sha256: 87c5d2564d549a62992e5e7c204533361943879345c214fc121400c321658e40
---
## Summary
Validate Goal Claim Scope

## Claim scope

Goal Atoms.

## Claim

a Goal Atom **must** identify **`=1`** Claim Target Scope Unit that is a direct child of its Atom Scope Unit according **to** authoritative Project Structure, **or** the Project Scope Unit **if** its Atom Scope **contains** no Scope Unit. a Goal reference assigns a purpose **and** **must not** independently declare **or** change the target's Name, parent, order, **or** Carrier binding.
