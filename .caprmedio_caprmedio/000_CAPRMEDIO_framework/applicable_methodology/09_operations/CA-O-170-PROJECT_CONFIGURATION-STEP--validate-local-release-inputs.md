---
atom_id: CA-O-170
ref_id: CA-O-170
container:
  scope_unit: CA-SU-13
role: Operations
form: Step
topics:
  main_subject: 'Subject/caprmedio/Step//Release Version/Step: validate local inputs'
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
tier: 3
relations:
  part_of:
  - CA-O-164
  invokes:
  - CA-O-165
status: Active
version: 10
updated_at: 2026-10-27 19:59:47 +0400
carrier_destination:
  file:
    name: CA-O-170-PROJECT_CONFIGURATION-STEP--validate-local-release-inputs.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations
current_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/CA-O-170-PROJECT_CONFIGURATION-STEP--validate-local-release-inputs.md
  source_atom_id: CA-O-170
  source_atom_revision: 10
  source_sha256: a33118f2bfdaaf047e61dbd8151f2b6bb2aef1dbda1c0dcd42730a7653ce8fc0
  original_relations_sha256: b43e5560a9819a6ec044ecaad8542d3e8b7fc358b1edde7dc3d0cb9767d1ec07
---
# Summary

Validate local release inputs

## Step

This Step invokes CA-O-165 once with phase `validate` to check current active Core Meta-Model, installed extension, Project Configuration sources, and delivery paths.

## Details

Missing, inactive, ambiguous, or mismatched inputs stop before tests or delivery effects and are reported for manual handling. This Step does not copy, compile, install, publish, or retry.
