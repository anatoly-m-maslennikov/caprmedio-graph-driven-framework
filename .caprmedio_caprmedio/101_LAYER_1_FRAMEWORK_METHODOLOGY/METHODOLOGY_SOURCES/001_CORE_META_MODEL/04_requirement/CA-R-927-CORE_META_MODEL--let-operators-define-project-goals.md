---
subjects:
  active: Project
  passive:
  - Entity/Object/Continuant/Governing Objects/Atom.Target Scope Unit
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement/Type: Project Goal'
  - Entity/Object/Continuant/Governing Objects/Atom.Local Scope Unit
  - Entity/Object/Continuant/Actor/Operator
  - Project
version: 41
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-R-925@37
atom_id: CA-R-927
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 5
role: Requirement
form: Rule
---
## Summary

Let Operators Define Project Goals

## Claim scope

Project Scope Units.

## Claim

**every** Project **must** be the Target Scope Unit of **`>=1`** accepted Requirement Atom of Type Project Goal. The Project Goal's current/local owner **must** be its Operator Actor, not the Project Scope Unit. This is the exception to ordinary Scope Unit ownership; the Operator **must not** be registered as a Scope Unit. Other Goal Atoms target non-Project Scope Units and use ordinary ownership.
