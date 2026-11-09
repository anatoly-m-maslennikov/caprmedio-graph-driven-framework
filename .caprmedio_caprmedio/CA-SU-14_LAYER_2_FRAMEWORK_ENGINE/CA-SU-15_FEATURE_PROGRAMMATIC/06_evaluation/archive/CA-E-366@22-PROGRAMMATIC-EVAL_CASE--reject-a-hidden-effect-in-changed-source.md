---
atom_id: CA-E-366@22
ref_id: CA-E-366@22
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
  - CA-M-425
  derived_from:
  - CA-A-053
status: Archived
version: 22
updated_at: 2026-10-27 19:59:33 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
destination:
  file:
    name: CA-E-366@22-PROGRAMMATIC-EVAL_CASE--reject-a-hidden-effect-in-changed-source.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation/archive
---
# Reject a hidden effect in changed source

## Claim checked

one changed effect function declares its complete effect boundary **or** allocates
persistent ownership **to** an object.

## Test case

evaluate one changed function that reads the process environment implicitly
**before** writing its declared target.

## Acceptance criteria

pass **only** **when** the function is rejected **until** the environment observation is
an explicit input **or** an owned adapter boundary.

## Failure disposition

block the changed unit **until** the hidden observation is removed.

## Sources

- [CA-M-425 — Separate deterministic transformations from effects and lifecycle](../05_method/CA-M-425-PROGRAMMATIC-ENG_POLICY--separate-deterministic-transformations-from-effects-and-lifecycle.md)
