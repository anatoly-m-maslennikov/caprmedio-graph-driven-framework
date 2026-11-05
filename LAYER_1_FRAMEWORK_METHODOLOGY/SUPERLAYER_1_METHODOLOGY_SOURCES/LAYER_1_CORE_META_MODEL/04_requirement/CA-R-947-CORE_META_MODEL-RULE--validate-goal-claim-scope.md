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
---
## Summary
Validate Goal Claim Scope

## Claim

### Prose Claim


Goal Atoms.


a Goal Atom **must** identify **`=1`** Claim Target Scope Unit that is a direct child of its Atom Scope Unit according **to** authoritative Project Structure, **or** the Project Scope Unit **if** its Atom Scope **contains** no Scope Unit. a Goal reference assigns a purpose **and** **must not** independently declare **or** change the target's Name, parent, order, **or** Carrier binding.
