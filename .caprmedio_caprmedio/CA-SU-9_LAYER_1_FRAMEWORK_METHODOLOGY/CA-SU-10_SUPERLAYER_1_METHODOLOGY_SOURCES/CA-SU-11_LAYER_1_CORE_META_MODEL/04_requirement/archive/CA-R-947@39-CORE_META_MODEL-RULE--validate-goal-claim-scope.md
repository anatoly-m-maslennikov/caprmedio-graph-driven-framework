---
subjects:
  active: Entity/Object/Continuant/Governing Objects/Atom.Target Scope Unit
  passive:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement/Type: Goal'
  - Entity/Object/Continuant/Governing Objects/Atom.Local Scope Unit
  - Scope Unit
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Structure
  - Project
version: 39
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-R-925@37
  - CA-R-926
  - CA-R-927
atom_id: CA-R-947@39
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
tier: 6
role: Requirement
form: Rule
---
## Summary
Validate Goal Claim Scope

## Claim scope

Goal Atoms.

## Claim

a Goal Atom **must** identify **`=1`** Claim Target Scope Unit that is a direct child of its Atom Scope Unit according **to** authoritative Project Structure, **or** the Project Scope Unit **if** its Atom Scope **contains** no Scope Unit. a Goal reference assigns a purpose **and** **must not** independently declare **or** change the target's Name, parent, order, **or** Carrier binding.
