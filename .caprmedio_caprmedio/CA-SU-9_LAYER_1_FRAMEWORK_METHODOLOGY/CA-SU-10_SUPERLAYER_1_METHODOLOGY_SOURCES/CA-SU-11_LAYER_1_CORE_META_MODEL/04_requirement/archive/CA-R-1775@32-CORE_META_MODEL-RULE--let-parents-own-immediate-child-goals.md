---
version: 32
updated_at: 2026-10-30 01:32:01 +0400
relations:
  child_of:
  - CA-M-447
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement/Type: Goal'
  depends_on:
  - Entity/Object/Continuant/Structural Unit/Scope Unit
  - Entity/Object/Continuant/Governing Objects/Atom
  - Entity/Object/Continuant/Selection
atom_id: CA-R-1775@32
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
---
## Summary

Let Parents Own Immediate Child Goals

## Claim scope

parent Scope Units and their immediate child Scope Units.

## Claim

**every** parent Scope Unit **must** own the Goal Atoms for its immediate child Scope Units under CA-R-926; those Goal Atoms belong **to** the parent's Owned Atoms **and** the child's Targeting Atoms **without** transferring their ownership.
