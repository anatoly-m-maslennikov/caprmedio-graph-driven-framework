---
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan'
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: AI Agent'
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan.Label'
version: 18
updated_at: 2026-10-26 05:59:45 +0400
relations: {}
atom_id: CA-R-1589@18
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Rule
---
# Summary

Bound executable leaf Plans

## Scope

executable Plans with **none** direct decompositions.

## Claim

**every** executable Plan with **none** direct decompositions **must** bound its own work **to** an estimate of **<=15** minutes for **=1** assigned AI Agent, with sufficient inputs, required output, verification, **and** no unresolved Operator decision; a composite Plan **may** have a larger roll-up estimate. the rule applies independently of Label.

## Details
