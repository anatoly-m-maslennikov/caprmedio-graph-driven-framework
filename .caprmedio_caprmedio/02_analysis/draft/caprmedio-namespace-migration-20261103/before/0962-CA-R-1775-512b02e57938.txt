---
version: 33
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-M-447
subjects:
  active: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement/Type: Goal'
  passive:
  - Scope Unit
  - Atom
  - Entity/Object/Continuant/Selection
atom_id: CA-R-1775
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
---
## Summary

Let Parents Own Immediate Child Goals

## Claim scope

parent Scope Units and their immediate child Scope Units.

## Claim

**every** parent Scope Unit **must** own the Goal Atoms for its immediate child Scope Units under CA-R-926; those Goal Atoms belong **to** the parent's Owned Atoms **and** the child's Targeting Atoms **without** transferring their ownership.
