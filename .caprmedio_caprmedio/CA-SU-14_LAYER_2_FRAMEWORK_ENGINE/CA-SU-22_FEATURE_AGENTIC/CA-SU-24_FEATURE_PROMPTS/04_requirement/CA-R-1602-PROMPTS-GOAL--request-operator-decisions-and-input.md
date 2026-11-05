---
cce_version: cce_1
cce_form: obligation
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Interaction/Decision
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Authoring/Prompt Authoring
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
version: 14
updated_at: 2026-10-27 19:59:58 +0400
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-1602
ref_id: CA-R-1602
status: Active
role: Requirement
author: Anatoly Maslennikov
current_scope_unit: PROMPTS
form: Goal
tier: 1
container:
  scope_unit: CA-SU-24
---
# Request Operator Decisions and Input

OPERATOR_PROMPTS **must** own user-facing prompts that request an Operator decision, authorization, clarification, **or** input. They **must not** be treated as agent-executable Action implementations **or** as substitutes for the Operator's response.
