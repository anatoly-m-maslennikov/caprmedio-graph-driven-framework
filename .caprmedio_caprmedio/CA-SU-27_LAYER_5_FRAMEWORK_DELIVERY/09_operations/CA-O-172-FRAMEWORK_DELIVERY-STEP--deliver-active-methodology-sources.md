---
atom_id: CA-O-172
ref_id: CA-O-172
container:
  scope_unit: CA-SU-27
role: Operations
form: Step
topics:
  main_subject: 'Subject/caprmedio/Step//Release Version/Step: deliver active sources'
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Release.ID
tier: 3
relations:
  part_of:
  - CA-O-164
  invokes:
  - CA-O-166
status: Active
version: 15
updated_at: 2026-11-09 15:54:30 +0400
carrier_destination:
  file:
    name: CA-O-172-FRAMEWORK_DELIVERY-STEP--deliver-active-methodology-sources.md
    path: .caprmedio_caprmedio/CA-SU-27_LAYER_5_FRAMEWORK_DELIVERY/09_operations
current_scope_unit: FRAMEWORK_DELIVERY
author: Anatoly Maslennikov
---

# Summary

Deliver active Methodology sources

## Step

This Step invokes CA-O-166 once with phase `deliver_sources`, clearing replaceable product members and copying only the current active Core Meta-Model, installed extension, and Project Configuration sources into `LAYER_1_FRAMEWORK_METHODOLOGY/`.

## Details

It preserves protected product settings, does not broaden source membership, and does not compile, install, test, publish, or retry. A source or destination mismatch stops and is reported for manual handling.
