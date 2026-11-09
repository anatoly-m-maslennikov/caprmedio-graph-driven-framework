---
atom_id: CA-E-616
ref_id: CA-E-616
container:
  scope_unit: CA-SU-27
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
  dependencies:
  - Subject/CAPRMEDIO/Carrier/Pull Request
  - Subject/CAPRMEDIO/Carrier/Git Repository
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Quality/Verification
tier: 5
relations:
  evaluation_for:
  - CA-R-1926
  - CA-M-368
status: Active
version: 12
updated_at: 2026-11-09 15:54:30 +0400
carrier_destination:
  file:
    name: CA-E-616-FRAMEWORK_DELIVERY-EVAL_CASE--validate-unique-matching-main-pr.md
    path: .caprmedio_caprmedio/CA-SU-27_LAYER_5_FRAMEWORK_DELIVERY/06_evaluation
current_scope_unit: FRAMEWORK_DELIVERY
claim_target_scope_unit: FRAMEWORK_DELIVERY
author: Anatoly Maslennikov
---

# Summary

Validate unique matching `main` PR

## Scope

one public-release PR discovery and update.

## Claim

**the Operator** **must** verify that zero matching PRs permits creation only after the initial push, one matching PR is reused, and duplicate, retargeted, closed, or URL-changed results stop before further material preparation or remote effects.

## Details

The final refresh must retain the same actual PR URL returned by the initial upsert.
