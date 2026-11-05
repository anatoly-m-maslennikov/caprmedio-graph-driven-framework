---
atom_id: CA-O-173
ref_id: CA-O-173
role: Operations
form: Step
current_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
topics:
  main_subject: 'Subject/caprmedio/Step//Release Version/Step: compile applicable Methodology'
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Applicable Methodology'
  - Subject/CAPRMEDIO/Carrier
version: 16
updated_at: 2026-11-02 19:46:47 +0400
relations:
  part_of:
  - CA-O-164
  invokes:
  - CA-O-166
tier: 3
container:
  scope_unit: CA-SU-13
carrier_destination:
  file:
    name: CA-O-173-PROJECT_CONFIGURATION-STEP--compile-applicable-methodology.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations
---
# Summary

Compile applicable Methodology

## Step

This Step invokes CA-O-166 once with phase `compile` for `LAYER_1_FRAMEWORK_METHODOLOGY/` and the canonical compiler. Its output remains in that derived product; it does not write the installed Framework.

## Details

This is not another compiler graph. An incomplete product, unavailable Tool/layout, or output mismatch stops before installation and is reported for manual handling.
