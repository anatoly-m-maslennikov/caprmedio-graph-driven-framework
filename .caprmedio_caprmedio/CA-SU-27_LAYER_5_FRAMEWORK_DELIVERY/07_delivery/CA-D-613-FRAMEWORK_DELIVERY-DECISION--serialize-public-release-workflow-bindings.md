---
atom_id: CA-D-613
ref_id: CA-D-613
container:
  scope_unit: CA-SU-27
role: Delivery
form: Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control
tier: 3
status: active
version: 20
updated_at: '2026-11-12T17:10:15.004765+00:00'
carrier_destination:
  file:
    name: CA-D-613-FRAMEWORK_DELIVERY-DECISION--serialize-public-release-workflow-bindings.md
    path: .caprmedio_caprmedio/CA-SU-27_LAYER_5_FRAMEWORK_DELIVERY/07_delivery
current_scope_unit: FRAMEWORK_DELIVERY
claim_target_scope_unit: FRAMEWORK_DELIVERY
author: Anatoly Maslennikov
relations: {}
---
## Summary

Serialize public-release Workflow bindings

## Claim scope

The Operation identities and execution boundary of one public release.

## Claim

### Prose Claim

Public Release finds the matching open PR, or creates a Draft PR from the already-published branch. Without an actual matching PR URL, stop before pushing. Prepare the PR materials and newest-first Version History with that URL, then commit the candidate and run the full required test suite on that exact commit.

After the suite passes and the checkout still matches the tested commit, push that SHA once. Verify the matching PR's head SHA, update its prepared body and mark it ready for CI. Stop on failed tests, changed inputs, a mismatched PR head or an uncertain remote effect. Report effects already completed. Do not merge or replay the push.
