---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: OPERATOR_PROMPTS/Goal
  depends_on:
  - PROMPTS
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
version: 6
updated_at: 2026-10-24 01:28:26 +0400
relations: {}
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-1602@6
status: Archived
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: PROMPTS
type: Goal
---
# Request Operator Decisions and Input

OPERATOR_PROMPTS **must** own user-facing prompts that request an Operator decision, authorization, clarification, **or** input. They **must not** be treated as agent-executable Action implementations **or** as substitutes for the Operator's response.
