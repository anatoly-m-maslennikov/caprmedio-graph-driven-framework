---
atom_id: CA-E-612
ref_id: CA-E-612
container:
  scope_unit: CA-SU-27
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Documentation
  - Subject/CAPRMEDIO/Carrier/Pull Request
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History
tier: 5
relations:
  evaluation_for:
  - CA-M-366
status: Active
version: 18
updated_at: 2026-11-09 15:54:30 +0400
carrier_destination:
  file:
    name: CA-E-612-FRAMEWORK_DELIVERY-EVAL_CASE--validate-public-material-source-binding.md
    path: .caprmedio_caprmedio/CA-SU-27_LAYER_5_FRAMEWORK_DELIVERY/06_evaluation
current_scope_unit: FRAMEWORK_DELIVERY
claim_target_scope_unit: FRAMEWORK_DELIVERY
author: Anatoly Maslennikov
---

# Summary

Validate public material source binding

## Scope

one selected public documentation closure.

## Claim

**the Operator** **must** verify that README, full PR body, Version History carrier and selected Version remain the exact prepared public material bindings and reject substituted carrier, Version, document bytes or PR identity.

## Details

The golden successful case contains distinct What's new and What's fixed PR sections. Adding only the actual matching PR URL to the already-generated concise Version History summary may change those metadata bytes while preserving the selected Version and all non-metadata source/material bindings. A substituted raw document byte, substantive summary rewrite, guessed or unrelated PR identity, or changed non-metadata binding is refused. This tests actual prepared material binding, not a retired CA-D-566 snapshot or a newly invented Source Proof serialization.
