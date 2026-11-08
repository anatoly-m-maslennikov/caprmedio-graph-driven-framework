---
identity:
  atom_id: CA-E-638
  ref_id: CA-E-638@13-draft
context:
  container:
    scope_unit: CA-SU-15
  role: Evaluation
  form: Direct Policy
  topics:
    main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification/Dynamic
      Testing
  tier: 1
state:
  status: Draft
  version: 13
  updated_at: 2026-11-08 20:40:58 +0400
destination:
  file:
    name: CA-E-638@13-draft-PROGRAMMATIC-DIRECT_POLICY--bound-and-recover-canary-exposure.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation/draft/engine-refinement-20261108
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---
# Summary

Bound and recover canary exposure

## Scope

Canary Evaluation of a changed PROGRAMMATIC component against a production-like or live workload.

## Claim

Canary Evaluation **may** be admitted **only when** the cohort **or** shadow surface isolates exposure; exposure is bounded; immediate stop is available; **and** rollback has been tested against the applicable state boundary. Canary evidence supplements rather than replaces required pre-deployment evidence.

## Details

These are necessary safety conditions, not a complete canary technique specification.

## Sources

- [CA-E-536@2 — historical extraction basis](archive/CA-E-536-PROGRAMMATIC-CORE-EVAL_APPROACH--admit-safe-canary-evaluation@2.md)
