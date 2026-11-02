---
subjects:
  governs: Entity/Object/Continuant/Structural Unit/Scope Unit/Project
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom.Target Scope Unit
  - Entity/Object/Continuant/Governing Objects/Atom.Author
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement/Type: Project Goal'
  - Entity/Object/Continuant/Governing Objects/Atom.Local Scope Unit
  - Entity/Object/Continuant/Actor/Operator
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project
version: 40
updated_at: 2026-10-29 10:13:50 +0400
relations:
  child_of:
  - CA-R-925
atom_id: CA-R-927@40
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 5
type: Rule
---
## Summary

Let Operators Define Project Goals

## Claim scope

Project Scope Units.

## Claim

**every** Project **must** be the Target Scope Unit of **`>=1`** accepted Requirement Atom of Type Project Goal. The Project Goal's current/local owner **must** be its Operator Actor, not the Project Scope Unit. This is the exception to ordinary Scope Unit ownership; the Operator **must not** be registered as a Scope Unit. Other Goal Atoms target non-Project Scope Units and use ordinary ownership.
