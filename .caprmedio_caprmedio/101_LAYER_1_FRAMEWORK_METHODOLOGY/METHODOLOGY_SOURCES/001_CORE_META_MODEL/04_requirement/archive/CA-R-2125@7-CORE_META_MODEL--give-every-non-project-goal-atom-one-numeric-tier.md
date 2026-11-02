---
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom.Tier
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement/Type: Goal'
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project
  - Entity/Object/Continuant/Governing Objects/Atom.Tier
version: 7
updated_at: 2026-10-29 07:45:28 +0400
relations: {}
atom_id: CA-R-2125@7
content_role: Requirement
type: Rule
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
tier: 1
status: Archived
author: Anatoly Maslennikov
---
## Summary
Give Every Non-Project-Goal Atom One Numeric Tier

## Claim scope
Atom other than a Project Goal Atom.

## Claim

**every** non-Project-Goal Atom **must** carry exactly one integer Tier. An ordinary Atom owned by the Project uses an integer Tier **>=0**; an Atom owned by a non-Project Scope Unit uses an integer Tier **>=1**. Project Goal is the separate explicit Tier `-1` case under CA-R-2132.

This rule defines owner-relative ranges, not a finite set of values. Higher integers remain admissible and may be assigned or raised when required by the approved governing-relation ordering. No Content-Role or Type-to-Tier restriction is imposed.

## Details
