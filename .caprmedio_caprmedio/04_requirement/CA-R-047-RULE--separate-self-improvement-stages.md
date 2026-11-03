---
version: 37
updated_at: 2026-11-02 18:35:20 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
  - CA-R-1423
subjects:
  active: CAPRMEDIO_MODEL <+ Project
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := "Analysis & Advisory")
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Package/Project Implementation
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Delivery)
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Product
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Method)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Evaluation)
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Journal
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/History/Journal > Event Record
cce_version: cce_1
cce_form: obligation
current_scope_unit: caprmedio
status: Active
atom_id: CA-R-047
tier: 1
role: Requirement
form: Rule
---
## Summary

Separate self-improvement stages

## Claim

### Prose Claim


a CAPRMEDIO self-improvement cycle **must** keep the following participating contributions distinct **and** traceably related:

- observations recorded **in** the Journal;
- Analysis & Advisory;
- Tasks;
- changes **to** Plan, Requirement, Method, Evaluation, Delivery, **and** Operations authority;
- Implementation;
- Delivery;
- follow-up Evaluation.

reusable Operations definitions remain distinct from the Journal Records of their executions **and** observations under CAPRMEDIO-META-REQU-092.
