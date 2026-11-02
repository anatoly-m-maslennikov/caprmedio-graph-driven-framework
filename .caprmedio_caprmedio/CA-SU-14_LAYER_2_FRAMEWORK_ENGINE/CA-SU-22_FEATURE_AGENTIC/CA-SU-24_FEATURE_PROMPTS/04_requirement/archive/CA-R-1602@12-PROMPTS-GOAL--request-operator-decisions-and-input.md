---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: Subject/Graph Node/UX/Operator Decision Prompt Interface
  depends_on:
  - Subject/Graph Node/Engineering/Prompt
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
version: 12
updated_at: 2026-10-26 00:46:35 +0400
relations: {}
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-1602@12
status: Archived
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: PROMPTS
type: Goal
tier: 1
---
# Request Operator Decisions and Input

OPERATOR_PROMPTS **must** own user-facing prompts that request an Operator decision, authorization, clarification, **or** input. They **must not** be treated as agent-executable Action implementations **or** as substitutes for the Operator's response.
