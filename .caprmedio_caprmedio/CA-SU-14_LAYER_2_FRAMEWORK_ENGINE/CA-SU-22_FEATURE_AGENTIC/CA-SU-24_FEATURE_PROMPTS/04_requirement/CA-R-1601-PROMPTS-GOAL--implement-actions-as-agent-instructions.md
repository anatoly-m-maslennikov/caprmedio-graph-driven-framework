---
atom_id: CA-R-1601
ref_id: CA-R-1601
container:
  scope_unit: CA-SU-24
role: Requirement
form: Goal
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
    <+ Authoring <+ Prompt Authoring
  dependencies:
  - MODEL//CAPRMEDIO <+ Atom/(.Header.Context.Role := Operations)/Action
tier: 1
status: Active
version: 15
updated_at: 2026-11-10 20:47:54 +0400
cce_version: cce_1
cce_form: obligation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: PROMPTS
destination:
  file:
    name: CA-R-1601-PROMPTS-GOAL--implement-actions-as-agent-instructions.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-22_FEATURE_AGENTIC/CA-SU-24_FEATURE_PROMPTS/04_requirement
---
## Summary

Implement Actions as Agent Instructions

## Claim

### Prose Claim

ACTION_PROMPTS **must** own self-contained agent-facing prompt implementations of methodology Actions. An ACTION_PROMPT supplies executable instructions **and** invocation context but does **not** own the Action meaning, Workflow state, Step transition, **or** Operator authority.
