---
atom_id: CA-O-182
ref_id: CA-O-182
container:
  scope_unit: CA-SU-27
role: Operations
form: Step
topics:
  main_subject: 'Subject/caprmedio/Step//Release Version/Step: run host-capable Candidate
    E2E'
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Quality/Verification
  - Subject/CAPRMEDIO/Carrier/Docker Image
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
tier: 3
relations:
  part_of:
  - CA-O-164
  invokes:
  - CA-O-181
status: Active
version: 11
updated_at: 2026-11-09 15:54:30 +0400
carrier_destination:
  file:
    name: CA-O-182-FRAMEWORK_DELIVERY-STEP--run-host-capable-candidate-e2e.md
    path: .caprmedio_caprmedio/CA-SU-27_LAYER_5_FRAMEWORK_DELIVERY/09_operations
current_scope_unit: FRAMEWORK_DELIVERY
author: Anatoly Maslennikov
---

# Summary

Run host-capable Candidate E2E

## Step

This Step invokes CA-O-181 once after CA-O-186's immutable image canary, binding the exact candidate/package/image/N identity and explicit host-capable controller authorization.

## Details

Absent host capability is non-pass, not a fallback to the frozen Docker worker. Failed, partial, stale, unsafe or missing-recording results stop before Full Gate aggregation, promotion and retirement without replay.
