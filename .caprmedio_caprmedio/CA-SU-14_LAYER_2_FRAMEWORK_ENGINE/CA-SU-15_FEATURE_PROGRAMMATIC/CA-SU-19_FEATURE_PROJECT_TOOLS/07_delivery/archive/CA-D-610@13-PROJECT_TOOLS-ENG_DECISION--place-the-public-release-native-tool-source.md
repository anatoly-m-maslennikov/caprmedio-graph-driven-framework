---
atom_id: CA-D-610@13
ref_id: CA-D-610@13
container:
  scope_unit: CA-SU-19
role: Delivery
form: Eng Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Storage/Directory
    Layout
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation/Code/Tool
  - Subject/CAPRMEDIO/Carrier
tier: 4
relations:
  delivery_for:
  - CA-R-1920
status: Archived
version: 13
updated_at: 2026-11-02 19:46:47 +0400
carrier_destination:
  file:
    name: CA-D-610@13-PROJECT_TOOLS-ENG_DECISION--place-the-public-release-native-tool-source.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-19_FEATURE_PROJECT_TOOLS/07_delivery/archive
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
author: Anatoly Maslennikov
---
# Summary

Place the public-release native Tool source

## Scope

the authoritative source carrier for the native public-release Tool.

## Claim

the native public-release Tool **must** be carried at `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_PROJECT_TOOLS/PUBLIC_RELEASE/public_release.py` with its package-local tests under `PUBLIC_RELEASE/tests/`.

## Details

The carrier is source material for package installation and discovery after the package registry admits it. Its presence alone does not claim an installed launcher or MCP route.
