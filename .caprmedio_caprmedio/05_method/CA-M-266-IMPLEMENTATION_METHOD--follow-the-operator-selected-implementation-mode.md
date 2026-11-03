---
cce_version: cce_1
cce_form: method
version: 25
updated_at: 2026-11-02 18:35:20 +0400
relations:
  child_of:
  - CA-M-261
subjects:
  active: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Execution Control <+ Effect Authorization
  passive:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Method)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Evaluation)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Delivery)
  - CAPRMEDIO_MODEL <+ Project
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-M-266
status: Active
current_scope_unit: caprmedio
tier: 2
role: Method
form: Implementation Method
---
## Summary
Follow the Operator-selected implementation mode

## Claim

### Prose Claim


**to** implement within a Task, follow the Operator-selected mode: evaluate **and** fix, full rebuild, refactoring, **or** another authorized approach. keep the selected mode within the Task permissions **and** governing RMED; permission for a full rebuild **must not** be inferred from an evaluation-and-fix request. the reconstruction equivalence governed by CA-M-262 applies regardless of mode **and** does **not** require identical code **or** a no-change rerun.
