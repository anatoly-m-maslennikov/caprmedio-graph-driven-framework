---
identity:
  atom_id: CA-E-637
  ref_id: CA-E-637
context:
  container:
    scope_unit: CA-SU-15
  role: Evaluation
  form: Direct Policy
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality
      <+ Verification <+ Test Design
  tier: 1
state:
  status: Active
  version: 15
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-E-637-PROGRAMMATIC-DIRECT_POLICY--require-observable-evidence-for-behavioral-acceptance.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---

## Summary

Require observable evidence for behavioral acceptance

## Claim

### Prose Claim

Given the applicable Spec and declared failure predicates, behavioral software Evaluation **may** support acceptance **only when** **every** predicate is covered by **`>=1`** reproducible check. No check **may** make acceptance depend solely on replaceable private Implementation structure **when** a semantic **or** public behavior boundary can expose the predicate.

## Details

### Scope

The foundational evidence boundary for behavioral software Evaluation of PROGRAMMATIC components.

These necessary evidence conditions do not select a portfolio, cost ranking or fixed test-scope ratio.

### Sources

- [CA-E-389@11 — historical extraction basis](archive/CA-E-389-PROGRAMMATIC-CORE-EVAL_APPROACH--combine-complementary-software-behavior-evidence@11.md)
