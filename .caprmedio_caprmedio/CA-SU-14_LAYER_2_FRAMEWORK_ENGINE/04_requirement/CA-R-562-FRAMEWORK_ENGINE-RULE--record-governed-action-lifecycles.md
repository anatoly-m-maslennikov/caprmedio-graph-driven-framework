---
atom_id: CA-R-562
ref_id: CA-R-562
container:
  scope_unit: CA-SU-14
role: Requirement
form: Rule
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
    <+ Execution Control
  dependencies:
  - MODEL//CAPRMEDIO <+ Journal
  - MODEL//CAPRMEDIO <+ Event Record
  - MODEL//CAPRMEDIO <+ Execution/Workflow Run
tier: 1
relations: {}
status: Active
version: 15
updated_at: 2026-11-10 20:47:54 +0400
subject_scopes:
- session-engine
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: FRAMEWORK_ENGINE
carrier_destination:
  file:
    name: CA-R-562-FRAMEWORK_ENGINE-RULE--record-governed-action-lifecycles.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/04_requirement
---
## Summary

Record governed action lifecycles

## Claim

### Prose Claim

the session engine **and** **every** Skill that performs governed work **must** use deterministic Tools **to** record its start **and** terminal outcome **and** **to** reconcile missing Work Journal coverage **after** session initialization **or** context recovery.
