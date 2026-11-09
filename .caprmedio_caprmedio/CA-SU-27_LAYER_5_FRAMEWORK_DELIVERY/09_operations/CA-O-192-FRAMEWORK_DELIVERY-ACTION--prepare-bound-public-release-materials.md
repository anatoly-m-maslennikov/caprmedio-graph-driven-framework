---
atom_id: CA-O-192
ref_id: CA-O-192
container:
  scope_unit: CA-SU-27
role: Operations
form: Action
topics:
  main_subject: Subject/caprmedio/Action//Prepare bound public release materials
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Documentation
  - Subject/CAPRMEDIO/Carrier/Pull Request
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Release.ID
tier: 3
status: Active
version: 16
updated_at: 2026-11-09 15:54:30 +0400
carrier_destination:
  file:
    name: CA-O-192-FRAMEWORK_DELIVERY-ACTION--prepare-bound-public-release-materials.md
    path: .caprmedio_caprmedio/CA-SU-27_LAYER_5_FRAMEWORK_DELIVERY/09_operations
current_scope_unit: FRAMEWORK_DELIVERY
author: Anatoly Maslennikov
relations: {}
---

# Summary

Prepare bound public-release materials

## Action

Prepare bound public-release materials **means** the sole content prompt for one selected Version and source snapshot. It returns the full public PR body and concise Version History summary.

## Details

The PR body distinguishes What’s new and What’s fixed. README, Version History edits, and all remote effects are mechanical later work. If the actual URL is not yet known, CA-O-198 appends it after PR creation; no placeholder is valid. A different Version or changed code, Methodology, or package requires a fresh full suite before public release.
