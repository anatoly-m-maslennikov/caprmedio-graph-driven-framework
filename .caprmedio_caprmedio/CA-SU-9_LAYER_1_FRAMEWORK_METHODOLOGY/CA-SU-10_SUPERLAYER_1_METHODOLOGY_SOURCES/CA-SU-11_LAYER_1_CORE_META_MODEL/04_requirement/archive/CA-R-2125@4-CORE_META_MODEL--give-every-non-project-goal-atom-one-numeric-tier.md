---
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Atom.Tier
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Requirement/Type: Goal'
  - Subject/Graph Node/Domain/Continuant/Project
  - Subject/Graph Node/Domain/Continuant/Atom.Tier
version: 4
updated_at: 2026-10-25 17:32:27 +0400
relations: {}
atom_id: CA-R-2125@4
content_role: Requirement
type: Rule
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
tier: 1
status: Archived
author: Anatoly Maslennikov
---
# Summary
Give Every Non-Project-Goal Atom One Numeric Tier

## Scope
Atom other than a Project Goal Atom.

## Claim

**every** non-Project-Goal Atom **must** carry exactly one integer Tier. An ordinary Atom owned by the Project uses an integer Tier **>=0**; an Atom owned by a non-Project Scope Unit uses an integer Tier **>=1**. Project Goal is the separate explicit Tier `-1` case under CA-R-2132.

This rule defines owner-relative ranges, not a finite set of values. Higher integers remain admissible and may be assigned or raised when required by the approved governing-relation ordering. No Content-Role or Type-to-Tier restriction is imposed.

## Details
