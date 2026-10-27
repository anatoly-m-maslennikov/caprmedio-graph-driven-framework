---
cce_version: cce_1
cce_form: obligation
version: 24
updated_at: 2026-10-25 17:32:27 +0400
relations:
  child_of:
  - CA-R-2157
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Actor/Type: AI Agent.Permissions'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: AI Agent'
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Engineering/AI Agent Delegation
  - Subject/Graph Node/Engineering/Framework Instance
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-846@24
status: Archived
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: caprmedio
type: Goal
tier: 4
claim_target_scope_unit: FRAMEWORK_ENGINE
---
# Let the Operator control AI permissions

CAPRMEDIO **must** let the Operator create AI Agent Delegations **and** mandatory authorization rules for **every** identified AI Agent **and** inspect, limit, modify, suspend, **and** revoke **every** such delegation **or** rule.
