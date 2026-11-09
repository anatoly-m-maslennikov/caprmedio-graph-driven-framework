---
atom_id: CA-R-1602
ref_id: CA-R-1602
container:
  scope_unit: CA-SU-24
role: Requirement
form: Goal
topics:
  {"main_subject": "Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Interaction/Decision", "dependencies": ["Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Authoring/Prompt Authoring", "CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator"]}
tier: 1
status: Active
version: 14
updated_at: 2026-10-27 19:59:58 +0400
cce_version: cce_1
cce_form: obligation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: PROMPTS
---
## Summary

Request Operator Decisions and Input

## Claim

### Prose Claim

OPERATOR_PROMPTS **must** own user-facing prompts that request an Operator decision, authorization, clarification, **or** input. They **must not** be treated as agent-executable Action implementations **or** as substitutes for the Operator's response.
