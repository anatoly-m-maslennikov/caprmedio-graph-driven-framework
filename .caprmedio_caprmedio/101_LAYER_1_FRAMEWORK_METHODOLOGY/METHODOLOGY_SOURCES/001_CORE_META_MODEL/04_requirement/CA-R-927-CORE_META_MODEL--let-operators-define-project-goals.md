---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Target Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Author
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Requirement/Type: Project Goal'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Local Scope Unit
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
version: 37
updated_at: 2026-10-27 20:00:12 +0400
relations:
  child_of:
  - CA-R-925
atom_id: CA-R-927
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 5
type: Rule
---
# Summary

Let Operators Define Project Goals

## Scope

Project Scope Units.

## Claim

**every** Project **must** be the Target Scope Unit of **`>=1`** accepted Requirement Atom of Type Project Goal. The Project Goal's current/local owner **must** be its Operator Actor, not the Project Scope Unit. This is the exception to ordinary Scope Unit ownership; the Operator **must not** be registered as a Scope Unit. Other Goal Atoms target non-Project Scope Units and use ordinary ownership.

## Details
