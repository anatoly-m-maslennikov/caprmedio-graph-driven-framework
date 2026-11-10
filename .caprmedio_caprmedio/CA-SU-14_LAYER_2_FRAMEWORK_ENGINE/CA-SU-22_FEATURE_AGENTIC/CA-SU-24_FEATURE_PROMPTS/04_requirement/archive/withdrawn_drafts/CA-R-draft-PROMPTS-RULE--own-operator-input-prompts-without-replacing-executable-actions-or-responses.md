---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Interaction/Decision
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Authoring/Prompt Authoring
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
version: 1
updated_at: 2026-10-29 20:32:25 +0400
relations: {}
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-draft
status: Draft
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: PROMPTS
type: Rule
tier: 1
---
## Summary

Own Operator input prompts without replacing executable Actions or responses

## Claim scope

The obligation described by the Claim.

## Claim

OPERATOR_PROMPTS **must** own user-facing prompts that request an Operator decision, authorization, clarification, **or** input. They **must not** be treated as agent-executable Action implementations **or** as substitutes for the Operator's response.
