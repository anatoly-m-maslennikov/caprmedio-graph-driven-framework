---
subjects:
  active: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement/Type:
    Goal'
  passive:
  - Scope Unit
  - Atom.Content
  - Entity/Object/Continuant/Structural Unit/Scope Unit.Parent
  - Entity/Object/Continuant/Structural Unit/Scope Unit.Children
version: 39
updated_at: 2026-11-02 19:44:26 +0400
relations:
  child_of:
  - CA-R-925@37
atom_id: CA-R-926
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 5
role: Requirement
form: Rule
---
## Summary
Let Direct Parents Define Non-Project Goals

## Claim scope

Non-Project Scope Units.

## Claim

**every** non-Project Scope Unit **must** have **`>=1`** accepted Goal Atom owned by its declared direct parent Scope Unit. this is a Goal-coverage obligation, **not** the source of the child's structural identity; a missing accepted Goal is a reported gap **and** **must not** remove **or** conceal the declared Scope Unit.
