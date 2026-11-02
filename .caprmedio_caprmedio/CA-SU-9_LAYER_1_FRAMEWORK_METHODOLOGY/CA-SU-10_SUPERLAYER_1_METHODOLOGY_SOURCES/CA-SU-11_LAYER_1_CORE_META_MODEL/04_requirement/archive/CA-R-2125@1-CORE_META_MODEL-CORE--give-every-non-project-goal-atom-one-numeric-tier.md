---
subjects:
  governs: "Subject/Domain/Node/Continuant/Atom.Tier"
  depends_on:
    ["Subject/Domain/Node/Continuant/Atom", "Subject/Domain/Node/Continuant/Atom/Content Role: Requirement/Type: Goal", "Subject/Domain/Node/Continuant/Project", "Subject/Domain/Node/Continuant/Atom.Tier"]
version: 1
updated_at: 2026-10-23 23:13:47 +0400
relations: {}
atom_id: "CA-R-2125@1"
content_role: "Requirement"
type: "Rule"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
tier: 1
status: "Archived"
author: "Anatoly Maslennikov"
---
# Summary
Give Every Non-Project-Goal Atom One Numeric Tier

## Scope
Atom other than a Project Goal Atom.

## Claim

**every** non-Project-Goal Atom **must** have **`=1`** integer Tier. An ordinary Atom owned by the Project uses an integer Tier **>=0**; an Atom owned by a non-Project Scope Unit uses an integer Tier **>=1**. Project Goal is the separate explicit Tier `-1` case under CA-R-2132 and is not an omitted Tier.

This rule defines owner-relative ranges, not a finite set of values. The initial display names are 0 Principle, 1 Core, 2 General, and 3 Standard; higher integers remain admissible when the owning Scope Unit admits them. No Content-Role or Type-to-Tier restriction is imposed.

## Details

