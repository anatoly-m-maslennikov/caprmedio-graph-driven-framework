---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: Subject/Engineering/Action Prompts.Goal
  depends_on:
  - PROMPTS
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
version: 6
updated_at: 2026-10-24 01:28:26 +0400
relations: {}
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-1601@6
status: Archived
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: PROMPTS
type: Goal
---
# Implement Actions as Agent Instructions

ACTION_PROMPTS **must** own self-contained agent-facing prompt implementations of methodology Actions. An ACTION_PROMPT supplies executable instructions **and** invocation context but does **not** own the Action meaning, Workflow state, Step transition, **or** Operator authority.
