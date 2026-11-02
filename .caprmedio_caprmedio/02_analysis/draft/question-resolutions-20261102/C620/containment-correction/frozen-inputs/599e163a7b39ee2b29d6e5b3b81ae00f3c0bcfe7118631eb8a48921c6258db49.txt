---
cce_version: cce_1
cce_form: evaluation
version: 24
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-E-001
  evaluation_for:
  - CA-M-270
  - CA-M-262
subjects:
  active: Entity/Aspect/Engineering/Verification/Test Design
  passive:
  - Atom/(.Role := Requirement)
  - Atom/(.Role := Method)
  - Atom/(.Role := Evaluation)
  - Atom/(.Role := Delivery)
  - Entity/Aspect/Engineering/Verification/Test Design
  - Project
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-442
status: Active
current_scope_unit: caprmedio
tier: 3
role: Evaluation
form: Eval Policy
---
## Summary
Evaluate refactoring verification readiness

## Claim

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
