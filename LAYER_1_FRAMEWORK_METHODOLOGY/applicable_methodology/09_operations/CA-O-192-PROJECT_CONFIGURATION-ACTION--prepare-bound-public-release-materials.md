---
atom_id: CA-O-192
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Subject/caprmedio/Action//Prepare bound public release materials
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Documentation
  - Subject/CAPRMEDIO/Carrier/Pull Request
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Release.ID
version: 15
updated_at: 2026-10-27 19:59:47 +0400
relations: {}
tier: 3
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/CA-O-192-PROJECT_CONFIGURATION-ACTION--prepare-bound-public-release-materials.md
  source_atom_id: CA-O-192
  source_atom_revision: 15
  source_sha256: 8ae5941190b44f66c6eba0b4a152ba11dc376129702a548de885ccd1d5529c74
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Prepare bound public-release materials

## Action

Prepare bound public-release materials **means** the sole content prompt for one selected Version and source snapshot. It returns the full public PR body and concise Version History summary.

## Details

The PR body distinguishes What’s new and What’s fixed. README, Version History edits, and all remote effects are mechanical later work. If the actual URL is not yet known, CA-O-198 appends it after PR creation; no placeholder is valid. A different Version or changed code, Methodology, or package requires a fresh full suite before public release.
