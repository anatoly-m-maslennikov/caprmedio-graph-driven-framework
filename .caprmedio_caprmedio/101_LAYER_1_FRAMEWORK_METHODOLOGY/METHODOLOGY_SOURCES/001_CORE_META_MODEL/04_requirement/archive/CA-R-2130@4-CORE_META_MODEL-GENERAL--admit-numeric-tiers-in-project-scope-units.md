---
subjects:
  governs: Subject/Domain/Node/Continuant/Atom.Tier
  depends_on:
  - Subject/Domain/Node/Continuant/Project
  - Subject/Domain/Node/Continuant/Atom.Tier
relations:
  child_of:
  - CA-R-917
version: 4
updated_at: 2026-10-24 02:14:24 +0400
atom_id: CA-R-2130@4
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
type: Rule
tier: 3
status: Archived
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
