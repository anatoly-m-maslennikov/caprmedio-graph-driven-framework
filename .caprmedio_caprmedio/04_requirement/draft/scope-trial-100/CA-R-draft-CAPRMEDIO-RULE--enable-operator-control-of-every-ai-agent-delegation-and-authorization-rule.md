---
cce_version: cce_1
cce_form: obligation
version: 1
updated_at: 2026-10-29 20:32:25 +0400
relations:
  child_of:
  - CA-R-2157
subjects:
  governs: Entity/Object/Continuant/Actor/AI Agent.Permissions
  depends_on:
  - Entity/Object/Continuant/Actor/AI Agent
  - Entity/Object/Continuant/Actor/Operator
  - Entity/Aspect/Engineering/Execution Control/Effect Authorization
  - 'Entity/Aspect/Product: CAPRMEDIO Framework'
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-draft
status: Draft
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: caprmedio
type: Rule
tier: 4
claim_target_scope_unit: FRAMEWORK_ENGINE
---
## Summary

Enable Operator control of every AI Agent delegation and authorization rule

## Claim scope

The obligation described by the Claim.

## Claim

CAPRMEDIO **must** let the Operator create AI Agent Delegations **and** mandatory authorization rules for **every** identified AI Agent **and** inspect, limit, modify, suspend, **and** revoke **every** such delegation **or** rule.
