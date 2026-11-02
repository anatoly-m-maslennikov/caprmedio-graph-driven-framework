---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: OPERATOR_PROMPTS/Goal
  depends_on:
  - PROMPTS
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
version: 3
updated_at: 2026-10-23 03:18:40 +0400
relations: {}
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-1602@3
status: Archived
---
# Request Operator Decisions and Input

OPERATOR_PROMPTS **must** own user-facing prompts that request an Operator decision, authorization, clarification, **or** input. They **must not** be treated as agent-executable Action implementations **or** as substitutes for the Operator's response.
