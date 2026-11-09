---
atom_id: CA-O-173
ref_id: CA-O-173
container:
  scope_unit: CA-SU-27
role: Operations
form: Step
topics:
  main_subject: 'Subject/caprmedio/Step//Release Version/Step: compile applicable
    Methodology'
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Applicable Methodology'
  - Subject/CAPRMEDIO/Carrier
tier: 3
relations:
  part_of:
  - CA-O-164
  invokes:
  - CA-O-166
status: Active
version: 17
updated_at: 2026-11-09 15:54:30 +0400
carrier_destination:
  file:
    name: CA-O-173-FRAMEWORK_DELIVERY-STEP--compile-applicable-methodology.md
    path: .caprmedio_caprmedio/CA-SU-27_LAYER_5_FRAMEWORK_DELIVERY/09_operations
current_scope_unit: FRAMEWORK_DELIVERY
author: Anatoly Maslennikov
---

# Summary

Compile applicable Methodology

## Step

This Step invokes CA-O-166 once with phase `compile` for `LAYER_1_FRAMEWORK_METHODOLOGY/` and the canonical compiler. Its output remains in that derived product; it does not write the installed Framework.

## Details

This is not another compiler graph. An incomplete product, unavailable Tool/layout, or output mismatch stops before installation and is reported for manual handling.
