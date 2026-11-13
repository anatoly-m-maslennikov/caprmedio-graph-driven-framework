---
atom_id: CA-M-366
ref_id: CA-M-366
container:
  scope_unit: CA-SU-27
role: Method
form: Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Documentation
  - Subject/CAPRMEDIO/Carrier/Pull Request
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History
tier: 4
relations:
  method_for:
  - CA-R-1923
status: active
version: 20
updated_at: '2026-11-12T17:10:04.026422+00:00'
carrier_destination:
  file:
    name: CA-M-366-FRAMEWORK_DELIVERY-DECISION--prepare-public-materials-with-an-actual-pr-link.md
    path: .caprmedio_caprmedio/CA-SU-27_LAYER_5_FRAMEWORK_DELIVERY/05_method
current_scope_unit: FRAMEWORK_DELIVERY
claim_target_scope_unit: FRAMEWORK_DELIVERY
author: Anatoly Maslennikov
---
## Summary

Prepare public materials with an actual PR link

## Claim scope

the selected public documentation closure.

## Claim

### Prose Claim

Prepare README, one full PR body and concise Version History bullets from the selected Version. Use `New` and `Fixed` in the PR body. Discover the matching open PR or create a Draft PR from the already-published branch before preparing Version History. Use its actual URL and put the new Version first. If a matching PR cannot be obtained, stop before pushing.
