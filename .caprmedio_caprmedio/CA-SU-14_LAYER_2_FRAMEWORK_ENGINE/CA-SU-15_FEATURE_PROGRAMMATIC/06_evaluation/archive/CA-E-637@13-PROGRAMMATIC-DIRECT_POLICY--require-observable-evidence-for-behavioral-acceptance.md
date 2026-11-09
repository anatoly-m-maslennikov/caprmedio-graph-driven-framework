---
identity:
  atom_id: CA-E-637@13
  ref_id: CA-E-637@13
context:
  container:
    scope_unit: CA-SU-15
  role: Evaluation
  form: Direct Policy
  topics:
    main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Quality/Verification/Test
      Design
  tier: 1
state:
  status: Archived
  version: 13
  updated_at: 2026-11-09 00:09:26 +0400
destination:
  file:
    name: CA-E-637@13-PROGRAMMATIC-DIRECT_POLICY--require-observable-evidence-for-behavioral-acceptance.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation/archive
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---
# Summary

Require observable evidence for behavioral acceptance

## Scope

The foundational evidence boundary for behavioral software Evaluation of PROGRAMMATIC components.

## Claim

Given the applicable Spec and declared failure predicates, behavioral software Evaluation **may** support acceptance **only when** **every** predicate is covered by **`>=1`** reproducible check. No check **may** make acceptance depend solely on replaceable private Implementation structure **when** a semantic **or** public behavior boundary can expose the predicate.

## Details

These necessary evidence conditions do not select a portfolio, cost ranking or fixed test-scope ratio.

## Sources

- [CA-E-389@11 — historical extraction basis](archive/CA-E-389-PROGRAMMATIC-CORE-EVAL_APPROACH--combine-complementary-software-behavior-evidence@11.md)
