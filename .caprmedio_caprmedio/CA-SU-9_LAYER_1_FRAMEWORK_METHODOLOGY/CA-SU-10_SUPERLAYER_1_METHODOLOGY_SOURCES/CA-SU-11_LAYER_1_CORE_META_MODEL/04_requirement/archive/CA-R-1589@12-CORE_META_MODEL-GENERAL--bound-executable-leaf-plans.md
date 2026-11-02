---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  - 'Subject/Domain/Node/Continuant/Actor/Type: AI Agent'
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - 'Entity/Node/Continuant/Atom/Content Role: Plan.Label'
version: 12
updated_at: 2026-10-23 03:14:50 +0400
relations:
  relates_to:
  - CA-R-1575
  - CA-R-1584
atom_id: CA-R-1589@12
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: General
status: Archived
author: Anatoly Maslennikov
global_tier: 10
---
# Summary

Bound executable leaf Plans

## Scope

executable Plans with **none** direct decompositions.

## Claim

**every** executable Plan with **none** direct decompositions **must** bound its own work **to** an estimate of **<=15** minutes for **=1** assigned AI Agent, with sufficient inputs, required output, verification, **and** no unresolved Operator decision; a composite Plan **may** have a larger roll-up estimate. the rule applies independently of Label.

## Details
