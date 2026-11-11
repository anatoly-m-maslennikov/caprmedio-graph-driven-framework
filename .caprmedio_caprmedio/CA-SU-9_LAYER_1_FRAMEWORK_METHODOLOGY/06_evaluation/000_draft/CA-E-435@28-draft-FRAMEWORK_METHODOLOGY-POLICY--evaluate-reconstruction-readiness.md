---
atom_id: CA-E-435
ref_id: CA-E-435@28-draft
container:
  scope_unit: CA-SU-9
role: Evaluation
form: Eval Policy
topics:
  main_subject: "CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Quality <+ Verification <+ Static Analysis"
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Requirement)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Method)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Evaluation)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Delivery)
  - CAPRMEDIO_MODEL <+ Project
tier: 4
relations:
  child_of:
  - CA-E-001
  evaluation_for:
  - CA-M-261
  - CA-M-262
status: Draft
version: 28
updated_at: "2026-11-11 18:12:55 +0400"
carrier_destination:
  file:
    name: CA-E-435@28-draft-FRAMEWORK_METHODOLOGY-POLICY--evaluate-reconstruction-readiness.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/06_evaluation/000_draft
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: FRAMEWORK_METHODOLOGY
---
## Summary
Evaluate reconstruction readiness

## Claim

### Prose Claim


the reconstruction readiness Evaluation **must** return `fail` **if** rebuilding required behavior **or** evaluating the rebuilt result needs authority recovered from the previous Implementation **or** specification work **before** reconstruction; **if** a language change is selected, **then** evaluate readiness against the current RMED **after** its affected Method **and** Delivery updates. absence of a prebuilt alternative **must not** by itself cause failure.

the Evaluation **must not** report runtime equivalence **if** equal complete runtime inputs under unchanged RMED produce different outputs, relevant starting state **or** configuration **or** time **or** randomness **or** external-service responses are omitted from the comparison, applicable Method **or** Delivery constraints are violated, **or** an authorized RMED change is hidden inside the unchanged baseline. source-code differences alone **must not** cause failure. a fixed task order **or** readiness review **without** runtime evidence **must not** be reported as proof of equivalent reconstruction.
