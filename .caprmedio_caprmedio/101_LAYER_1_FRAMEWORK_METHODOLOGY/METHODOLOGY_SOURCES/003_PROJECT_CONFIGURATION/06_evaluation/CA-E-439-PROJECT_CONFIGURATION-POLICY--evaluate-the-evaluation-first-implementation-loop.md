---
cce_version: cce_1
cce_form: evaluation
version: 23
updated_at: 2026-10-27 19:59:35 +0400
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
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Execution
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Requirement'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Method'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Delivery'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.ID
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-439
status: Active
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: PROJECT_CONFIGURATION
type: Policy
tier: 4
claim_target_scope_unit: caprmedio
---
# Evaluate the Evaluation-first implementation loop

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
