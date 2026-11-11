---
atom_id: CA-M-266
ref_id: CA-M-266@27-draft
container:
  scope_unit: CA-SU-9
role: Method
form: Implementation Method
topics:
  main_subject: "CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Effect Authorization"
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Requirement)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Method)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Evaluation)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Delivery)
  - CAPRMEDIO_MODEL <+ Project
tier: 3
relations:
  child_of:
  - CA-M-261
status: Draft
version: 27
updated_at: "2026-11-11 18:12:55 +0400"
carrier_destination:
  file:
    name: CA-M-266@27-draft-FRAMEWORK_METHODOLOGY-IMPLEMENTATION_METHOD--follow-the-operator-selected-implementation-mode.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/05_method/000_draft
cce_version: cce_1
cce_form: method
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: FRAMEWORK_METHODOLOGY
---
## Summary
Follow the Operator-selected implementation mode

## Claim

### Prose Claim


**to** implement within a Task, follow the Operator-selected mode: evaluate **and** fix, full rebuild, refactoring, **or** another authorized approach. keep the selected mode within the Task permissions **and** governing RMED; permission for a full rebuild **must not** be inferred from an evaluation-and-fix request. the reconstruction equivalence governed by CA-M-262 applies regardless of mode **and** does **not** require identical code **or** a no-change rerun.
