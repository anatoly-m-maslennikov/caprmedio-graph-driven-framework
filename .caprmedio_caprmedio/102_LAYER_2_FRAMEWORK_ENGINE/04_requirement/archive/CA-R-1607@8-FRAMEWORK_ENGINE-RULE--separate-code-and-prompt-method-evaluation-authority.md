---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Method'
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Evaluation'
  - 'Subject/Domain/Node/Continuant/Scope Unit: TOOLS'
  - PROMPTS
version: 8
updated_at: 2026-10-24 11:58:20 +0400
relations: {}
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-1607@8
status: Archived
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: FRAMEWORK_ENGINE
type: Rule
tier: 1
---
# Separate Code and Prompt Method-Evaluation Authority

A Method **or** Evaluation that applies only to executable code **must** be owned by TOOLS **or** its applicable code Scope Unit. A Method **or** Evaluation that applies only to prompt implementations **must** be owned by PROMPTS, ACTION_PROMPTS, OPERATOR_PROMPTS, **or** its applicable prompt Scope Unit. Cross-implementation authority **must** remain at the lowest common Scope Unit and state both implementation classes explicitly.
