---
atom_id: CA-R-1602
ref_id: CA-R-1602
container:
  scope_unit: CA-SU-24
role: Requirement
form: Goal
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Interaction <+ Decision
  dependencies:
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Authoring
    <+ Prompt Authoring
  - MODEL//CAPRMEDIO <+ Actor/Operator
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
    name: CA-R-1602-PROMPTS-GOAL--request-operator-decisions-and-input.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-22_FEATURE_AGENTIC/CA-SU-24_FEATURE_PROMPTS/04_requirement
---
## Summary

Request Operator Decisions and Input

## Claim

### Prose Claim

OPERATOR_PROMPTS **must** own user-facing prompts that request an Operator decision, authorization, clarification, **or** input. They **must not** be treated as agent-executable Action implementations **or** as substitutes for the Operator's response.
