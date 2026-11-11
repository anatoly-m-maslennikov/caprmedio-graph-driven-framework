---
atom_id: CA-R-1607
ref_id: CA-R-1607
container:
  scope_unit: CA-SU-14
role: Requirement
form: Rule
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
    <+ Architecture <+ Component Structure
  dependencies:
  - MODEL//CAPRMEDIO <+ Atom/(.Header.Context.Role := Method)
  - MODEL//CAPRMEDIO <+ Atom/(.Header.Context.Role := Evaluation)
  - MODEL//CAPRMEDIO <+ Scope Unit
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Authoring
    <+ Prompt Authoring
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Authoring
    <+ Code Authoring
  - MODEL//CAPRMEDIO <+ Atom.Header.Context.Container
tier: 1
status: Active
version: 13
updated_at: 2026-11-10 20:47:54 +0400
cce_version: cce_1
cce_form: obligation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: FRAMEWORK_ENGINE
carrier_destination:
  file:
    name: CA-R-1607-FRAMEWORK_ENGINE-RULE--separate-code-and-prompt-method-evaluation-authority.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/04_requirement
---
## Summary

Separate Code and Prompt Method-Evaluation Authority

## Claim

### Prose Claim

A Method **or** Evaluation that applies only to executable code **must** be owned by PROGRAMMATIC **or** its applicable code Scope Unit. A Method **or** Evaluation that applies only to prompt implementations **must** be owned by PROMPTS **or** its applicable prompt Scope Unit. Cross-implementation authority **must** remain at the lowest common Scope Unit and state both implementation classes explicitly.
