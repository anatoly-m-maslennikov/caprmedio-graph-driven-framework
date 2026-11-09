---
atom_id: CA-E-260
ref_id: CA-E-260
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution
    Control
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control/Effect
    Authorization
tier: 5
relations:
  evaluation_for:
  - CA-M-404
  - CA-M-425
  derived_from:
  - CA-A-053
status: Active
version: 25
updated_at: 2026-11-09 14:19:14 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
destination:
  file:
    name: CA-E-260-PROGRAMMATIC-EVAL_CASE--verify-decision-precedes-effect-application.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation
---

## Summary

Verify decision precedes effect application

## Claim

### Prose Claim

one PROGRAMMATIC effect is applied **only** **after** a deterministic decision supplies
its target, ordering, **and** expected outcome.

## Details

### Applicable conditions

apply **when** a component combines a decision with an external effect,
asynchronous work, **or** lifecycle transition.

### Test case

evaluate one effect request by observing its decision result **before** allowing
the declared effect owner **to** apply it.

### Acceptance criteria


pass **only** **when** the decision result **contains** the target, ordering, **and** expected
outcome, **and** the effect owner reports completion facts **without** adding,
reordering, **or** suppressing a decision.

Verify that completion facts return to the decision boundary and actual execution recording remains with its declared executor. Generated output or a completion fact alone does not claim durable terminal completion.

### Failure disposition

stop the operation **and** return the missing decision boundary **to** its owner.

### Sources

- [CA-M-425 — Separate deterministic transformations from effects and lifecycle](../05_method/CA-M-425-PROGRAMMATIC-DIRECT_POLICY--separate-deterministic-transformations-from-effects-and-lifecycle.md)
