---
atom_id: CA-E-435
ref_id: CA-E-435
container:
  scope_unit: CA-SU-00
role: Evaluation
form: Eval Policy
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Verification <+ Static Analysis
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Method)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Evaluation)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Delivery)
  - CAPRMEDIO_MODEL <+ Project
tier: 3
relations:
  child_of:
  - CA-E-001
  evaluation_for:
  - CA-M-261
  - CA-M-262
status: Active
version: 26
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-E-435-CAPRMEDIO-EVAL_POLICY--evaluate-reconstruction-readiness.md
    path: .caprmedio_caprmedio/06_evaluation
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: caprmedio
---
## Summary
Evaluate reconstruction readiness

## Claim

### Prose Claim


the reconstruction readiness Evaluation **must** return `fail` **if** rebuilding required behavior **or** evaluating the rebuilt result needs authority recovered from the previous Implementation **or** specification work **before** reconstruction; **if** a language change is selected, **then** evaluate readiness against the current RMED **after** its affected Method **and** Delivery updates. absence of a prebuilt alternative **must not** by itself cause failure.

the Evaluation **must not** report runtime equivalence **if** equal complete runtime inputs under unchanged RMED produce different outputs, relevant starting state **or** configuration **or** time **or** randomness **or** external-service responses are omitted from the comparison, applicable Method **or** Delivery constraints are violated, **or** an authorized RMED change is hidden inside the unchanged baseline. source-code differences alone **must not** cause failure. a fixed task order **or** readiness review **without** runtime evidence **must not** be reported as proof of equivalent reconstruction.
