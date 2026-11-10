---
atom_id: CA-E-366
ref_id: CA-E-366
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
    <+ Execution Control
  dependencies:
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution
    Control <+ Effect Authorization
tier: 5
relations:
  evaluation_for:
  - CA-M-425
  DERIVED_FROM:
  - CA-A-053
status: Active
version: 24
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
    name: CA-E-366-PROGRAMMATIC-EVAL_CASE--reject-a-hidden-effect-in-changed-source.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation
---

## Summary

Reject a hidden effect in changed source

## Claim

### Prose Claim

one changed effect function declares its complete effect boundary **or** allocates
persistent ownership **to** an object.

## Details

### Test case


Evaluate a changed function that reads the process environment implicitly before writing its declared target, or performs a persistence, Run or Journal write while presented as pure computation.

### Acceptance criteria


Pass only when hidden environment observation is rejected until it is an explicit input or an owned adapter boundary. Persistence and execution recording must be delegated to the declared authorized effect owner or executor; generated output is not durable terminal completion.

### Failure disposition

block the changed unit **until** the hidden observation is removed.

### Sources

- [CA-M-425 — Separate deterministic transformations from effects and lifecycle](../05_method/CA-M-425-PROGRAMMATIC-DIRECT_POLICY--separate-deterministic-transformations-from-effects-and-lifecycle.md)
