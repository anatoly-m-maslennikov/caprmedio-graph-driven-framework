---
atom_id: CA-E-615
ref_id: CA-E-615
container:
  scope_unit: CA-SU-27
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation/Code/Tool
  dependencies:
  - Subject/CAPRMEDIO/Carrier/Git Commit
  - Subject/CAPRMEDIO/Carrier/Pull Request
tier: 5
relations:
  evaluation_for:
  - CA-R-1925
  - CA-M-368
status: active
version: 16
updated_at: '2026-11-12T17:10:11.668804+00:00'
carrier_destination:
  file:
    name: CA-E-615-FRAMEWORK_DELIVERY-EVAL_CASE--exercise-successful-public-release-with-mocked-remote-effects.md
    path: .caprmedio_caprmedio/CA-SU-27_LAYER_5_FRAMEWORK_DELIVERY/06_evaluation
current_scope_unit: FRAMEWORK_DELIVERY
claim_target_scope_unit: FRAMEWORK_DELIVERY
author: Anatoly Maslennikov
---
## Summary

Exercise successful public release with mocked remote effects

## Claim scope

the successful path of one public release.

## Claim

### Prose Claim

Run the Public Release against a disposable Project with mocked remote effects. Cover an existing matching PR and creation of a new Draft PR. In both cases, the actual PR URL is written into Version History before committing and testing. Verify the full suite passes before the sole push of the tested SHA. Mark the same PR ready for CI only after confirming its head is that SHA. Verify no push when the PR cannot be obtained, the candidate changes, or required tests fail. An uncertain push or wrong PR head stops without replay.
