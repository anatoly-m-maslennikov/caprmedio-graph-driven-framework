---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Tier
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Tier
version: 5
updated_at: 2026-10-27 20:00:07 +0400
relations: {}
atom_id: CA-R-2131
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
type: Rule
tier: 2
status: Active
author: Anatoly Maslennikov
---
# Summary

Admit Numeric Tiers in Non-Project Scope Units

## Scope

ordinary Atoms owned by non-Project Scope Units.

## Claim

a non-Project Scope Unit **must** admit an integer Tier **>=1** for every ordinary Atom it owns. Higher integer Tiers remain admissible without an upper bound and may be assigned or raised when required by the approved governing-relation ordering.

This range rule imposes no Content-Role or Type-to-Tier restriction.

## Details
