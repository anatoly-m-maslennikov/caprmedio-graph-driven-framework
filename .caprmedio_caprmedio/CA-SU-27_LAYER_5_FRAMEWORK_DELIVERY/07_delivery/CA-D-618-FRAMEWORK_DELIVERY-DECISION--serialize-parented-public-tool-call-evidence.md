---
atom_id: CA-D-618
ref_id: CA-D-618
container:
  scope_unit: CA-SU-27
role: Delivery
form: Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal.Record
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Serialization
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution
tier: 4
relations:
  delivery_for:
  - CA-R-1928
status: Active
version: 11
updated_at: 2026-11-09 15:54:30 +0400
carrier_destination:
  file:
    name: CA-D-618-FRAMEWORK_DELIVERY-DECISION--serialize-parented-public-tool-call-evidence.md
    path: .caprmedio_caprmedio/CA-SU-27_LAYER_5_FRAMEWORK_DELIVERY/07_delivery
current_scope_unit: FRAMEWORK_DELIVERY
claim_target_scope_unit: FRAMEWORK_DELIVERY
author: Anatoly Maslennikov
---

# Summary

Serialize parented public Tool-call evidence

## Scope

Tool-call evidence of one public-release Action.

## Claim

public-release Tool-call evidence **must** serialize input, result, effect, and report references under the actual parent Step and Action Run records of the existing schema-v5 Journal.

## Details

This Delivery adds neither a Tool Run kind nor a new Journal event schema. Started, terminal, and recording-pending states remain the shared schema meanings.
