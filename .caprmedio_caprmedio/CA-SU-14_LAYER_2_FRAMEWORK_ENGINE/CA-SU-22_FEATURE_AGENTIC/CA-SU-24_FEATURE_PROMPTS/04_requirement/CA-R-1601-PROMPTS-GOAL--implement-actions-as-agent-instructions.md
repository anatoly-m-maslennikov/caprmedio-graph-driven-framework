---
atom_id: CA-R-1601
ref_id: CA-R-1601
container:
  scope_unit: CA-SU-24
role: Requirement
form: Goal
topics:
  {"main_subject": "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Authoring/Prompt Authoring", "dependencies": ["CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Action"]}
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

Implement Actions as Agent Instructions

## Claim

### Prose Claim

ACTION_PROMPTS **must** own self-contained agent-facing prompt implementations of methodology Actions. An ACTION_PROMPT supplies executable instructions **and** invocation context but does **not** own the Action meaning, Workflow state, Step transition, **or** Operator authority.
