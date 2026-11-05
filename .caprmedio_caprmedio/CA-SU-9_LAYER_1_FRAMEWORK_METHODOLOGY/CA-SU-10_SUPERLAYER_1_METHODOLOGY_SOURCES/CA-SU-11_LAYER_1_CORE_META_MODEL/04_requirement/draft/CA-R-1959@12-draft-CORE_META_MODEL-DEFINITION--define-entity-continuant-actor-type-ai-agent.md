---
atom_id: CA-R-1959@12-draft
ref_id: CA-R-1959@12-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Entity Definition
topics:
  main_subject: Entity/Object/Continuant/Actor/AI Agent
  dependencies:
  - Entity/Object/Continuant/Actor
  - Entity/Object/Continuant/Actor/AI Agent.Permissions
tier: 3
relations:
  child_of:
  - CA-R-1174
status: Draft
version: 12
updated_at: 2026-10-30 08:45:17 +0400
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
author: Anatoly Maslennikov
---
## Summary

Define Entity/Continuant/Actor/Type: AI Agent

## Claim scope

AI Agents.

## Claim

an AI Agent **means** an Actor that performs delegated work using an AI model.

## Details

Historical context: Candidate #6 retained AI Agent under Actor. The current permission target is `Entity/Object/Continuant/Actor/AI Agent.Permissions`. CA-R-852 and CA-R-1552 govern those permissions but do not define the Actor kind. This definition grants no additional authority.
