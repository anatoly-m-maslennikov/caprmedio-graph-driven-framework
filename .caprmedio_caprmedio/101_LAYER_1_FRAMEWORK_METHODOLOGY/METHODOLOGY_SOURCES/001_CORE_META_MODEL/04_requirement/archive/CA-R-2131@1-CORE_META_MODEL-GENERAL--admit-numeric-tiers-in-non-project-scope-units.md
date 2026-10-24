---
subjects:
  governs: Subject/Domain/Node/Continuant/Atom.Tier
  depends_on:
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Domain/Node/Continuant/Atom.Tier
version: 1
updated_at: 2026-10-23 23:13:47 +0400
relations: {}
atom_id: "CA-R-2131@1"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
type: "Rule"
tier: 2
status: "Archived"
author: "Anatoly Maslennikov"
---
# Summary

Admit Numeric Tiers in Non-Project Scope Units

## Scope

ordinary Atoms owned by non-Project Scope Units.

## Claim

a non-Project Scope Unit **must** admit an integer Tier **>=1** for every ordinary Atom it owns. The initial display names are 1 Core, 2 General, and 3 Standard; higher integer Tiers remain admissible without an upper bound when selected by the Scope Unit's authority.

Principle is not admitted outside the Project under CA-R-1443. This range rule imposes no Content-Role or Type-to-Tier restriction.

## Details

