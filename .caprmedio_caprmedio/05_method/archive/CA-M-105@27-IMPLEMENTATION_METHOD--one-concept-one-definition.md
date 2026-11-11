---
atom_id: CA-M-105
ref_id: CA-M-105@27
container:
  scope_unit: CA-SU-00
role: Method
form: Implementation Method
topics:
  main_subject: CAPRMEDIO_MODEL <+ Entity
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity
  - CAPRMEDIO_MODEL <+ Term//Property
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
tier: 1
relations:
  child_of:
  - CA-M-446
  - CA-M-006
status: archived
version: 27
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-M-105@27-IMPLEMENTATION_METHOD--one-concept-one-definition.md
    path: .caprmedio_caprmedio/05_method/archive
cce_version: cce_1
cce_form: method
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: caprmedio
---
## Summary

One concept, one definition

## Claim

### Prose Claim


**to** represent a kind of information **in** the Project, use **`=1`** canonical Entity, including a Property, for that kind **in** the same context:

1. reuse its existing canonical definition instead of introducing another Entity **or** Property for the same information.
2. treat mappings, explanations, **and** realizations as representations of that definition rather than additional canonical definitions.
3. **if** choosing between competing canonical definitions requires an unresolved decision, **then** stop the affected mapping **or** adaptation **and** return the alternatives **and** their evidence **to** the Operator.
