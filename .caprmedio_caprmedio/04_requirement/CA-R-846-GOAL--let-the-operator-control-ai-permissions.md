---
cce_version: cce_1
cce_form: obligation
version: 31
updated_at: 2026-11-02 18:35:20 +0400
relations:
  child_of:
  - CA-R-2157
topics:
  main_subject: CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/AI Agent.Permissions
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/AI Agent
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Execution Control <+ Effect Authorization
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Product
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-846
ref_id: CA-R-846
status: Active
current_scope_unit: caprmedio
tier: 4
claim_target_scope_unit: FRAMEWORK_ENGINE
role: Requirement
form: Goal
container:
  scope_unit: CA-SU-00
---
## Summary
Let the Operator control AI permissions

## Claim

### Prose Claim


CAPRMEDIO **must** let the Operator create AI Agent Delegations **and** mandatory authorization rules for **every** identified AI Agent **and** inspect, limit, modify, suspend, **and** revoke **every** such delegation **or** rule.
