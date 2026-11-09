---
atom_id: CA-E-617
ref_id: CA-E-617
container:
  scope_unit: CA-SU-27
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - Subject/CAPRMEDIO/Carrier/Pull Request
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Quality/Verification
tier: 5
relations:
  evaluation_for:
  - CA-R-1927
  - CA-M-368
status: Active
version: 12
updated_at: 2026-11-09 15:54:30 +0400
carrier_destination:
  file:
    name: CA-E-617-FRAMEWORK_DELIVERY-EVAL_CASE--validate-public-release-does-not-merge.md
    path: .caprmedio_caprmedio/CA-SU-27_LAYER_5_FRAMEWORK_DELIVERY/06_evaluation
current_scope_unit: FRAMEWORK_DELIVERY
claim_target_scope_unit: FRAMEWORK_DELIVERY
author: Anatoly Maslennikov
---

# Summary

Validate public release does not merge

## Scope

one public-release effect declaration.

## Claim

**the Operator** **must** verify that the native public-release binding exposes no merge, approval, target-retargeting, protected-branch update, tag, or deployment effect and ends with an open PR result only.

## Details

The absence of merge is verified from the declared binding and mocked effect trace, not inferred from intent.
