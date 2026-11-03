---
cce_version: cce_1
cce_form: evaluation
version: 29
updated_at: 2026-11-02 18:35:20 +0400
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
  active: CAPRMEDIO <+ MODEL <+ Entity/Object/Occurrent/Execution
  passive:
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Requirement)
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Method)
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Evaluation)
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Delivery)
  - CAPRMEDIO <+ STRUCTURE <+ Aspects <+ Engineering <+ Verification
  - CAPRMEDIO <+ MODEL <+ Atom.ID
  - CAPRMEDIO <+ MODEL <+ Project
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-439
status: Active
current_scope_unit: PROJECT_CONFIGURATION
tier: 4
claim_target_scope_unit: caprmedio
role: Evaluation
form: Eval Policy
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/06_evaluation/CA-E-439-PROJECT_CONFIGURATION-POLICY--evaluate-the-evaluation-first-implementation-loop.md
  source_atom_id: CA-E-439
  source_atom_revision: 29
  source_sha256: 623729fbd7eb15c2200257b286932b3950ae5c3dccf28ff5a4b0fb8d023a067f
  original_relations_sha256: e4a42269e4336082dc660022de5b35d2793f7baa25bf13da7892b2584b1286c3
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
