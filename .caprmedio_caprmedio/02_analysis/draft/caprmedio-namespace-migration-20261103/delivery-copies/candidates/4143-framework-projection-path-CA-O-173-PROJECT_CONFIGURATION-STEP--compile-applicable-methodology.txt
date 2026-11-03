---
atom_id: CA-O-173
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
subjects:
  governs: 'Subject/caprmedio/Step//Release Version/Step: compile applicable Methodology'
  depends_on:
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
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/CA-O-173-PROJECT_CONFIGURATION-STEP--compile-applicable-methodology.md
  source_atom_id: CA-O-173
  source_atom_revision: 16
  source_sha256: ef98c90ad5bdfd7b1b35a20768449a10a77adcf5d501577dfd1ba04c0d95f734
  original_relations_sha256: a4287f08702e809c2bc900193cc22bbb07dea32a402f5e63b0ea5a6a852a1aeb
---
# Summary

Compile applicable Methodology

## Step

This Step invokes CA-O-166 once with phase `compile` for `LAYER_1_FRAMEWORK_METHODOLOGY/` and the canonical compiler. Its output remains in that derived product; it does not write the installed Framework.

## Details

This is not another compiler graph. An incomplete product, unavailable Tool/layout, or output mismatch stops before installation and is reported for manual handling.
