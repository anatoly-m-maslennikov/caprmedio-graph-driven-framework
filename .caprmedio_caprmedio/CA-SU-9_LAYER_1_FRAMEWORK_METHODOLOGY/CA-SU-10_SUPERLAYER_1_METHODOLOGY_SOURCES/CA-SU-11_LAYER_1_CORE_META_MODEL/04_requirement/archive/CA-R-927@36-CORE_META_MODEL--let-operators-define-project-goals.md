---
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Project
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom.Target Scope Unit
  - Subject/Graph Node/Domain/Continuant/Atom.Author
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Requirement/Type: Project Goal'
  - Subject/Graph Node/Domain/Continuant/Atom.Local Scope Unit
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Domain/Continuant/Project
version: 36
updated_at: 2026-10-25 17:32:27 +0400
relations:
  child_of:
  - CA-R-925
atom_id: CA-R-927@36
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
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
