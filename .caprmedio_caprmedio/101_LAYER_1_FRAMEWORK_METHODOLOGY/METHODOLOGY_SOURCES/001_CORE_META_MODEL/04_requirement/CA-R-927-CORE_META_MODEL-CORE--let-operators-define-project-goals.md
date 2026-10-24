---
subjects:
  governs: Subject/Domain/Node/Continuant/Project
  depends_on:
  - Subject/Domain/Node/Continuant/Atom.Target Scope Unit
  - Subject/Domain/Node/Continuant/Atom.Author
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Requirement/Type: Project Goal'
  - Subject/Domain/Node/Continuant/Atom.Local Scope Unit
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Subject/Domain/Node/Continuant/Project
version: 34
updated_at: 2026-10-24 02:14:24 +0400
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
