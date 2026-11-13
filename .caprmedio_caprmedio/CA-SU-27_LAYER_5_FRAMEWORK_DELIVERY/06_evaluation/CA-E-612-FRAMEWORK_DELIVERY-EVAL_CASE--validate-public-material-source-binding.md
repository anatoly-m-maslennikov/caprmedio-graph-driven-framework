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
status: active
version: 19
updated_at: '2026-11-12T17:10:08.584172+00:00'
carrier_destination:
  file:
    name: CA-E-612-FRAMEWORK_DELIVERY-EVAL_CASE--validate-public-material-source-binding.md
    path: .caprmedio_caprmedio/CA-SU-27_LAYER_5_FRAMEWORK_DELIVERY/06_evaluation
current_scope_unit: FRAMEWORK_DELIVERY
claim_target_scope_unit: FRAMEWORK_DELIVERY
author: Anatoly Maslennikov
---
## Summary

Validate public material source binding

## Claim scope

one selected public documentation closure.

## Claim

### Prose Claim

Verify the README, full PR body, Version History and selected Version are the exact prepared public materials that were tested. The PR body has `New` and `Fixed` sections. The newest Version is first in Version History and has the actual matching PR URL. Reject substituted bytes, a different Version or PR, and a guessed link.
