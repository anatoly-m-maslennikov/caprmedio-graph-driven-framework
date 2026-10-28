---
version: 28
updated_at: 2026-10-27 20:00:03 +0400
relations:
  child_of:
  - CA-M-001
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Requirement/Type: Goal'
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Selection
atom_id: CA-R-1775
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Let Parents Own Immediate Child Goals

## Scope

parent Scope Units and their immediate child Scope Units.

## Claim

**every** parent Scope Unit **must** own the Goal Atoms for its immediate child Scope Units under CA-R-926; those Goal Atoms belong **to** the parent's Owned Atoms **and** the child's Targeting Atoms **without** transferring their ownership.

## Details
