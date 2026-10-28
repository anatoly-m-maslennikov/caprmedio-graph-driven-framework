---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Tier
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Tier
relations:
  child_of:
  - CA-R-917
version: 7
updated_at: 2026-10-27 20:00:07 +0400
atom_id: CA-R-2130
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
type: Rule
tier: 3
status: Active
author: Anatoly Maslennikov
---
# Summary

Admit Numeric Tiers in Project Scope Units

## Scope

ordinary Atoms owned by Project Scope Units.

## Claim

a Project Scope Unit **must** admit an integer Tier **>=0** for every ordinary Atom it owns. The explicit Project Goal case carries Tier `-1` under CA-R-2132. Higher integer Tiers remain admissible without an upper bound and may be assigned or raised when required by the approved governing-relation ordering.

This range rule imposes no Content-Role or Type-to-Tier restriction.

## Details
