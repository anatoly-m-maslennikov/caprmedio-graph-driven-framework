---
atom_id: CA-E-442
ref_id: CA-E-442
container:
  scope_unit: CA-SU-00
role: Evaluation
form: Eval Policy
topics:
  main_subject: "CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Quality <+ Verification <+ Test Design"
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Method)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Evaluation)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Delivery)
  - "CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Quality <+ Verification <+ Test Design"
  - CAPRMEDIO_MODEL <+ Project
tier: 3
relations:
  child_of:
  - CA-E-001
  evaluation_for:
  - CA-M-270
  - CA-M-262
status: Active
version: 26
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-E-442-CAPRMEDIO-EVAL_POLICY--evaluate-refactoring-verification-readiness.md
    path: .caprmedio_caprmedio/06_evaluation
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: caprmedio
---
## Summary
Evaluate refactoring verification readiness

## Claim

### Prose Claim


the refactoring-verification Evaluation **must** return `fail` **if**

- the target Implementation changes **before** applicable verification is prepared **and** the existing Implementation baseline is recorded,
- baseline inputs are incomplete **or** uncontrolled,
- an existing defect becomes expected correctness **without** governing authority,
- the candidate is **not** checked against the governing RMED **and** baseline,
- **or** required release gates are bypassed.

**when** canary testing applies, it **must** return `fail` **if**

- criteria were **not** prepared **before** refactoring
- **or** the canary is reported as executed **without** running the candidate during an authorized controlled rollout.

absence of an inapplicable testing technique **or** of an old-Implementation baseline for a fresh reconstruction **must not** by itself cause failure. baseline observations **must not** replace RMED as authority.
