---
atom_id: CA-E-356
ref_id: CA-E-356
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
    <+ Authoring <+ Code Authoring
tier: 5
relations:
  evaluation_for:
  - CA-M-407
  DERIVED_FROM:
  - CA-A-053
status: Active
version: 23
updated_at: 2026-11-10 20:47:54 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
destination:
  file:
    name: CA-E-356-PROGRAMMATIC-EVAL_CASE--reject-a-class-used-only-as-a-function-namespace.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation
---
## Summary

Reject a class used only as a function namespace

## Claim



### Prose Claim
#### Claim checked

one deterministic responsibility that needs no identity **or** owned state is
implemented as specifically named functions **in** a module rather than as a class
used **only** for grouping.

#### Test case

evaluate one changed class whose methods are **all** static deterministic
transformations **and** whose instances own no state, invariant, resource,
lifecycle, **or** adapter.

#### Acceptance criteria

pass **only** **when** the class is rejected **and** the transformations are allocated **to**
specifically named functions **in** one cohesive module.

#### Failure disposition

reject the changed allocation **until** the namespace-only class is removed.

#### Sources

- [CA-M-407 — Allocate deterministic transformations to functions](../05_method/CA-M-407-PROGRAMMATIC-ENG_POLICY--allocate-deterministic-transformations-to-functions.md)
