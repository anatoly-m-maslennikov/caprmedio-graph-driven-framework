---
atom_id: CA-O-170
ref_id: CA-O-170
container:
  scope_unit: CA-SU-27
role: Operations
form: Step
topics:
  main_subject: 'Subject/caprmedio/Step//Release Version/Step: validate local inputs'
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
tier: 3
relations:
  part_of:
  - CA-O-164
  invokes:
  - CA-O-165
status: Active
version: 11
updated_at: 2026-11-09 15:54:30 +0400
carrier_destination:
  file:
    name: CA-O-170-FRAMEWORK_DELIVERY-STEP--validate-local-release-inputs.md
    path: .caprmedio_caprmedio/CA-SU-27_LAYER_5_FRAMEWORK_DELIVERY/09_operations
current_scope_unit: FRAMEWORK_DELIVERY
author: Anatoly Maslennikov
---

# Summary

Validate local release inputs

## Step

This Step invokes CA-O-165 once with phase `validate` to check current active Core Meta-Model, installed extension, Project Configuration sources, and delivery paths.

## Details

Missing, inactive, ambiguous, or mismatched inputs stop before tests or delivery effects and are reported for manual handling. This Step does not copy, compile, install, publish, or retry.
