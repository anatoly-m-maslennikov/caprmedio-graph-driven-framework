---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan'
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: AI Agent'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan.Label'
version: 20
updated_at: 2026-10-27 19:59:58 +0400
relations: {}
atom_id: CA-R-1589
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 2
type: Rule
---
# Summary

Bound executable leaf Plans

## Scope

executable Plans with **none** directly contained Plan Atoms.

## Claim

**every** executable Plan with **none** directly contained Plan Atoms **must** bound its own work **to** an estimate of **<=15** minutes for **=1** assigned AI Agent, with sufficient inputs, required output, verification, **and** no unresolved Operator decision; a Plan with contained children **may** have a larger roll-up estimate. the rule applies independently of Label.

## Details
