---
atom_id: CA-O-196
ref_id: CA-O-196
container:
  scope_unit: CA-SU-27
role: Operations
form: Action
topics:
  main_subject: Subject/CAPRMEDIO/Carrier/Pull Request
  dependencies:
  - Subject/CAPRMEDIO/Carrier/Git Commit
  - Subject/CAPRMEDIO/Carrier/Git Repository
  - Subject/CAPRMEDIO/Carrier/Pull Request
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
tier: 3
status: Active
version: 11
updated_at: 2026-11-09 15:54:30 +0400
carrier_destination:
  file:
    name: CA-O-196-FRAMEWORK_DELIVERY-ACTION--push-the-gated-public-closure-and-upsert-main-pr.md
    path: .caprmedio_caprmedio/CA-SU-27_LAYER_5_FRAMEWORK_DELIVERY/09_operations
current_scope_unit: FRAMEWORK_DELIVERY
author: Anatoly Maslennikov
relations: {}
---

# Summary

Push the gated public closure and upsert `main` PR

## Action

Push the gated public closure and upsert `main` PR **means** the native, explicitly authorized remote effect that records an immutable `amm/dev` commit/push proof and one actual matching open `main` PR identity.

## Details

This Action accepts only the selected personal remote scope. Its Tool-call effect references are evidence on this Action Run; a new PR URL is not assumed until the remote result returns it. Merge is excluded.
