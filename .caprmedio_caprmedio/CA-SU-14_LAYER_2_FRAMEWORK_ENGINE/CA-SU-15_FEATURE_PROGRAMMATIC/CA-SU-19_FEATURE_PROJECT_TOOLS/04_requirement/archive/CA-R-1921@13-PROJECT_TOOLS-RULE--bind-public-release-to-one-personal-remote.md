---
atom_id: CA-R-1921@13
ref_id: CA-R-1921@13
container:
  scope_unit: CA-SU-19
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
  dependencies:
  - Subject/CAPRMEDIO/Carrier/Git Repository
  - Subject/CAPRMEDIO/Carrier/Git Branch
tier: 3
status: Archived
version: 13
updated_at: 2026-10-27 20:00:05 +0400
carrier_destination:
  file:
    name: CA-R-1921@13-PROJECT_TOOLS-RULE--bind-public-release-to-one-personal-remote.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-19_FEATURE_PROJECT_TOOLS/04_requirement/archive
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
author: Anatoly Maslennikov
---
# Summary

Bind public release to one personal remote

## Scope

the selected remote boundary of one public release.

## Claim

**the Operator** **must** bind one public-release invocation to an explicit personal remote identity and the exact `amm/dev` to `main` branch direction.

## Details

The binding contains no credential or secret. A different remote, owner, head, base, or branch direction is out of scope and stops the invocation.
