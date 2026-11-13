---
atom_id: CA-R-815
ref_id: CA-R-815
container:
  scope_unit: CA-SU-00
role: Requirement
form: Goal
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Product
  dependencies:
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_STRUCTURE <+ Entity/Object/Continuant/Selection//PROJECT_PRIORITY_MODEL
tier: 4
relations:
  child_of:
  - CA-R-2157
status: active
version: 36
updated_at: '2026-11-13T12:06:38.894034+00:00'
cce_version: cce_1
cce_form: obligation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: caprmedio
claim_target_scope_unit: FRAMEWORK_ENGINE
destination:
  file:
    name: CA-R-815-GOAL--follow-the-operator-s-priorities.md
    path: .caprmedio_caprmedio/04_requirement
---
## Summary
Follow the Operator's priorities

## Claim

### Prose Claim


the CAPRMEDIO Framework Instance **must** support implementing **every** admissible priority model established by the Operator for possible Project trade-offs.

Trade-off parameters may include Project velocity, delivered-result performance, correctness beyond mandatory requirements, and flexibility (how much effort later changes would take). These are examples, not a closed list. Mandatory requirements remain binding.
