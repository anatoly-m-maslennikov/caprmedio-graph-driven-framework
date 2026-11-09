---
atom_id: CA-O-185
ref_id: CA-O-185
container:
  scope_unit: CA-SU-27
role: Operations
form: Step
topics:
  main_subject: 'Subject/caprmedio/Step//Release Version/Step: run closed candidate
    Unit gate'
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Quality/Verification
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Selection//Methodology Sources
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
tier: 3
relations:
  part_of:
  - CA-O-164
  invokes:
  - CA-O-168
status: Active
version: 12
updated_at: 2026-11-09 15:54:30 +0400
carrier_destination:
  file:
    name: CA-O-185-FRAMEWORK_DELIVERY-STEP--run-the-closed-candidate-unit-gate.md
    path: .caprmedio_caprmedio/CA-SU-27_LAYER_5_FRAMEWORK_DELIVERY/09_operations
current_scope_unit: FRAMEWORK_DELIVERY
author: Anatoly Maslennikov
---

# Summary

Run the closed candidate Unit gate

## Step

This Step invokes CA-O-168 once with phase `closed_unit_gate`, binding CA-O-175's exact private compiled candidate, frozen active-source boundary, and declared Unit/source partition.

## Details

Every declared Unit/source testcase must terminal-pass for the frozen candidate; skipped, excluded, missing, focused, cached, or historical results are non-pass. Host-capable Candidate E2E remains CA-O-182, and CA-O-184 alone aggregates the complete Release Gate. This Step does not clear, copy, compile, install, publish, or retry.
