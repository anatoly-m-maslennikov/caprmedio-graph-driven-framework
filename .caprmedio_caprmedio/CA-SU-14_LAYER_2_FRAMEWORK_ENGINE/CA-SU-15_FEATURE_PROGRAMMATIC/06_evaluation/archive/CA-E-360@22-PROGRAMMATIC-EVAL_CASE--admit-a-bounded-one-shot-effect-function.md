---
atom_id: CA-E-360
ref_id: CA-E-360@22
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution
    Control
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Component
    Structure
tier: 5
relations:
  evaluation_for:
  - CA-M-425
  derived_from:
  - CA-A-053
status: Archived
version: 22
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
    name: CA-E-360@22-PROGRAMMATIC-EVAL_CASE--admit-a-bounded-one-shot-effect-function.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation/archive
---

## Summary

Admit a bounded one-shot effect function

## Claim

### Prose Claim

one bounded one-shot effect **may** be a function **when** **every** dependency **and**
boundary is explicit **and** no identity **or** ownership persists across calls.

## Details

### Test case

evaluate one specifically named function that applies one file effect from an
explicit target **and** dependency **and** returns a typed outcome **without** retained
state.

### Acceptance criteria

pass **only** **when** the function's target, dependency, input, outcome, **and** failure
boundary are explicit **and** it owns no state, invariant, resource, lifecycle, **or**
adapter across calls.

### Failure disposition

reject the function **or** allocate an object **when** **any** persistent ownership is
required.

### Sources

- [CA-M-425 — Separate deterministic transformations from effects and lifecycle](../05_method/CA-M-425-PROGRAMMATIC-DIRECT_POLICY--separate-deterministic-transformations-from-effects-and-lifecycle.md)
