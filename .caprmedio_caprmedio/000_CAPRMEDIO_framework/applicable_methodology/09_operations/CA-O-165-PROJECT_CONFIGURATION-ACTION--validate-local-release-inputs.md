---
atom_id: CA-O-165
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Subject/caprmedio/Action//Validate local release inputs
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Selection//Methodology Sources
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Release.ID
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification
version: 22
updated_at: 2026-11-02 19:46:47 +0400
relations: {}
tier: 3
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/CA-O-165-PROJECT_CONFIGURATION-ACTION--validate-local-release-inputs.md
  source_atom_id: CA-O-165
  source_atom_revision: 22
  source_sha256: e9291b3b7b13019b376d0cf785f576c33f477f0541cdafb473f86e34a7270e31
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Validate local release inputs

## Action

Validate local release inputs **means** the Action that checks the explicit local-release inputs and configured delivery paths for file/path safety before the declared local validation scope. The complete discovered suite remains the default; a focused scope requires the explicit current Operator record admitted by CA-O-164.

## Scope

The Action checks the configured source and delivery paths, Project Structure, protected settings, compiler, and target paths `LAYER_1_FRAMEWORK_METHODOLOGY/` and `.caprmedio_caprmedio/000_CAPRMEDIO_framework/` for ordinary input and file/path safety. It does not separately validate Active Atom metadata, placement or relations; release verification uses the declared scope and records whether it is complete or focused.

## Details

Missing, ambiguous or unsafe required input stops before tests or delivery writes and is reported for manual handling. This Action does not copy or clear product or installed contents, compile, install, push, or open a PR.
