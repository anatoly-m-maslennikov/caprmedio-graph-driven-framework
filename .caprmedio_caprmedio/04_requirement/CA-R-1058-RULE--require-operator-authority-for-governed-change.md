---
atom_id: CA-R-1058
ref_id: CA-R-1058
container:
  scope_unit: CA-SU-00
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Product
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/AI Agent
tier: 5
relations:
  child_of:
  - CA-R-004
  - CA-R-827
  - CA-R-846
  - CA-R-2157
  - CA-R-2158
status: Active
version: 39
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-R-1058-CAPRMEDIO-RULE--require-operator-authority-for-governed-change.md
    path: .caprmedio_caprmedio/04_requirement
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
cce_version: cce_1
cce_form: obligation
current_scope_unit: caprmedio
---
## Summary
Require operator authority for governed change

## Claim

### Prose Claim


CAPRMEDIO **must** establish **or** change governed Project meaning **only** through explicit per-action acceptance by the Operator **or** active authority explicitly delegated by the Operator **to** the identified AI Agent performing the change.
