---
cce_version: cce_1
cce_form: evaluation
version: 26
updated_at: 2026-10-29 09:35:50 +0400
relations:
  child_of:
  - CA-E-001
  evaluation_for:
  - CA-O-016
  - CA-O-017
  - CA-O-018
  - CA-O-019
  - CA-O-020
  - CA-O-021
  - CA-M-239
subjects:
  governs: Entity/Object/Occurrent/Execution
  depends_on:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Method'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Evaluation'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Delivery'
  - Entity/Aspect/Engineering/Verification
  - Entity/Object/Continuant/Governing Objects/Atom.ID
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-439@26
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: PROJECT_CONFIGURATION
type: Eval Policy
tier: 4
claim_target_scope_unit: caprmedio
---
## Summary
Evaluate the Evaluation-first implementation loop

## Claim

within the caprmedio Project, the implementation-loop Evaluation **must** return `fail` **if**

- unchanged mode, RMED, **and** complete execution inputs yield different applicable tasks **or** ordering,
- a consumer runs **before** its prerequisite,
- Atom ID overrides a prerequisite,
- a cycle is admitted,
- feasible Evaluation-preparation precedence is omitted **or** left implicit,
- **or** an absolute E-first barrier prevents preparation of an Evaluation prerequisite.

it **must** also return `fail` **if**

- applicable Methods **or** Delivery boundaries are omitted from Evaluation **or** Requirement implementation,
- Atom ID resolves a Method conflict,
- preparation of an Evaluation is reported as its execution,
- **or** completion is reported with **any** applicable Evaluation failed, blocked, **or** unevaluated.

repeated evaluate-fix execution **and** runtime loops alone **must not** be rejected as prerequisite cycles.
