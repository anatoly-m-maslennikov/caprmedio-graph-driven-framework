---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Target Scope Unit
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Requirement/Type: Goal'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Local Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Structure
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
version: 35
updated_at: 2026-10-27 20:00:12 +0400
relations:
  child_of:
  - CA-R-925
  - CA-R-926
  - CA-R-927
atom_id: CA-R-947
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 6
type: Rule
---
# Summary
Validate Goal Claim Scope

## Scope

Goal Atoms.

## Claim

a Goal Atom **must** identify **`=1`** Claim Target Scope Unit that is a direct child of its Atom Scope Unit according **to** authoritative Project Structure, **or** the Project Scope Unit **if** its Atom Scope **contains** no Scope Unit. a Goal reference assigns a purpose **and** **must not** independently declare **or** change the target's Name, parent, order, **or** Carrier binding.

## Details
