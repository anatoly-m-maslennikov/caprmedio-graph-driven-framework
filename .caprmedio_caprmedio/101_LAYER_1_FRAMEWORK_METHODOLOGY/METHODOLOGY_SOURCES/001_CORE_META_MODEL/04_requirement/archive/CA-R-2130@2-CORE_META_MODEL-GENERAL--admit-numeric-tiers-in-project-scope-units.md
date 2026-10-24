---
subjects:
  governs: Subject/Domain/Node/Continuant/Atom.Tier
  depends_on:
  - Subject/Domain/Node/Continuant/Project
  - Subject/Domain/Node/Continuant/Atom.Tier
relations:
  child_of:
    - CA-R-917
    - CA-R-2126
    - CA-R-2127
    - CA-R-2128
    - CA-R-2129
version: 2
updated_at: 2026-10-23 23:17:14 +0400
atom_id: "CA-R-2130@2"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
type: "Rule"
tier: 2
status: "Archived"
author: "Anatoly Maslennikov"
---
# Summary

Admit Numeric Tiers in Project Scope Units

## Scope

ordinary Atoms owned by Project Scope Units.

## Claim

a Project Scope Unit **must** admit an integer Tier **>=0** for every ordinary Atom it owns. The explicit Project Goal case carries Tier `-1` under CA-R-2132. The initial display names are 0 Principle, 1 Core, 2 General, and 3 Standard; higher integer Tiers remain admissible without an upper bound when selected by the Project's authority.

Principle is admitted only in the Project under CA-R-1443. This range rule imposes no Content-Role or Type-to-Tier restriction.

## Details

