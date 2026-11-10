---
atom_id: CA-R-1607
ref_id: CA-R-1607@12
container:
  scope_unit: CA-SU-14
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Container
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Method)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Evaluation)
  - CAPRMEDIO_MODEL <+ Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Authoring/Prompt Authoring
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Authoring/Code Authoring
tier: 1
status: Archived
version: 12
updated_at: 2026-10-27 19:59:59 +0400
cce_version: cce_1
cce_form: obligation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: FRAMEWORK_ENGINE
carrier_destination:
  file:
    name: CA-R-1607@12-FRAMEWORK_ENGINE-RULE--separate-code-and-prompt-method-evaluation-authority.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/04_requirement/archive
---
## Summary

Separate Code and Prompt Method-Evaluation Authority

## Claim

### Prose Claim

A Method **or** Evaluation that applies only to executable code **must** be owned by TOOLS **or** its applicable code Scope Unit. A Method **or** Evaluation that applies only to prompt implementations **must** be owned by PROMPTS, ACTION_PROMPTS, OPERATOR_PROMPTS, **or** its applicable prompt Scope Unit. Cross-implementation authority **must** remain at the lowest common Scope Unit and state both implementation classes explicitly.
