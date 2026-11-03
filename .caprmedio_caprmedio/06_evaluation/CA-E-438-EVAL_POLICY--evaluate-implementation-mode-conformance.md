---
cce_version: cce_1
cce_form: evaluation
version: 29
updated_at: 2026-11-02 08:06:47 +0400
relations:
  child_of:
  - CA-E-001
  evaluation_for:
  - CA-M-266
  - CA-M-262
subjects:
  active: CAPRMEDIO_MODEL <+ Package/Implementation
  passive:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_MODEL <+ Atom/(.Role := Plan)
  - CAPRMEDIO_MODEL <+ Package/Implementation
  - CAPRMEDIO_MODEL <+ Atom/(.Role := Evaluation)
  - CAPRMEDIO_MODEL <+ Atom/(.Role := Requirement)
  - CAPRMEDIO_MODEL <+ Atom/(.Role := Method)
  - CAPRMEDIO_MODEL <+ Atom/(.Role := Delivery)
  - CAPRMEDIO_MODEL <+ Project
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-438
status: Active
current_scope_unit: caprmedio
tier: 3
role: Evaluation
form: Eval Policy
---
## Summary
Evaluate implementation mode conformance

## Claim

the implementation mode Evaluation **must** return `fail` **if**

- execution replaces the Operator-selected mode **without** authorization,
- treats an evaluation-and-fix request as permission for a full rebuild,
- exceeds Task permissions,
- **or** exempts the selected mode from the governing RMED.

authorized rewriting **or** different source-code bytes **must not** by themselves cause failure **when** reconstruction equivalence under CA-M-262 is preserved.
