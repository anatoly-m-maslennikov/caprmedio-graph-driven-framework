---
cce_version: cce_1
cce_form: method
version: 27
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-M-446
  - CA-M-006
subjects:
  active: CAPRMEDIO_MODEL <+ Entity
  passive:
  - CAPRMEDIO_MODEL <+ Entity
  - CAPRMEDIO_MODEL <+ Term//Property
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-M-105
status: Active
current_scope_unit: caprmedio
tier: 1
role: Method
form: Implementation Method
---
## Summary

One concept, one definition

## Claim

### Prose Claim


**to** represent a kind of information **in** the Project, use **`=1`** canonical Entity, including a Property, for that kind **in** the same context:

1. reuse its existing canonical definition instead of introducing another Entity **or** Property for the same information.
2. treat mappings, explanations, **and** realizations as representations of that definition rather than additional canonical definitions.
3. **if** choosing between competing canonical definitions requires an unresolved decision, **then** stop the affected mapping **or** adaptation **and** return the alternatives **and** their evidence **to** the Operator.
