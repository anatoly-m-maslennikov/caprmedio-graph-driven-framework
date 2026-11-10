---
atom_id: CA-E-361
ref_id: CA-E-361
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
    <+ Execution Control
  dependencies:
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture
    <+ Component Structure
tier: 5
relations:
  evaluation_for:
  - CA-M-425
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
    name: CA-E-361-PROGRAMMATIC-EVAL_CASE--require-an-object-for-a-persistent-effect-owner.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation
---

## Summary

Require an object for a persistent effect owner

## Claim



### Prose Claim
one effect that owns identity, state, an invariant, a resource, a lifecycle, **or**
a replaceable adapter across calls is applied through a specifically named
object method.

## Details

### Test case

evaluate one standalone function that acquires a resource **and** retains its
lifecycle state for a later call.

### Acceptance criteria

pass **only** **when** the function is rejected **and** the persistent responsibility is
allocated **to** one object with explicit acquisition, use, **and** release boundaries.

### Failure disposition

reject the effect boundary **until** its persistent owner is explicit.

### Sources

- [CA-M-425 — Separate deterministic transformations from effects and lifecycle](../05_method/CA-M-425-PROGRAMMATIC-DIRECT_POLICY--separate-deterministic-transformations-from-effects-and-lifecycle.md)
