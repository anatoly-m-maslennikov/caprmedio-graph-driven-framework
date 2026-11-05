---
cce_version: cce_1
cce_form: obligation
topics:
  main_subject: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Method'
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit: TOOLS'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Authoring/Prompt Authoring
version: 12
updated_at: 2026-10-27 19:59:59 +0400
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-1607
ref_id: CA-R-1607
status: Active
role: Requirement
author: Anatoly Maslennikov
current_scope_unit: FRAMEWORK_ENGINE
form: Rule
tier: 1
container:
  scope_unit: CA-SU-14
---
# Separate Code and Prompt Method-Evaluation Authority

A Method **or** Evaluation that applies only to executable code **must** be owned by TOOLS **or** its applicable code Scope Unit. A Method **or** Evaluation that applies only to prompt implementations **must** be owned by PROMPTS, ACTION_PROMPTS, OPERATOR_PROMPTS, **or** its applicable prompt Scope Unit. Cross-implementation authority **must** remain at the lowest common Scope Unit and state both implementation classes explicitly.
