---
atom_id: CA-R-1926@12
ref_id: CA-R-1926@12
container:
  scope_unit: CA-SU-19
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
  dependencies:
  - Subject/CAPRMEDIO/Carrier/Pull Request.ID
  - Subject/CAPRMEDIO/Carrier/Git Branch
  - Subject/CAPRMEDIO/Carrier/Git Repository
tier: 3
status: Archived
version: 12
updated_at: 2026-10-27 20:00:05 +0400
carrier_destination:
  file:
    name: CA-R-1926@12-PROJECT_TOOLS-RULE--maintain-one-matching-open-main-pr.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-19_FEATURE_PROJECT_TOOLS/04_requirement/archive
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
author: Anatoly Maslennikov
---
# Summary

Maintain one matching open `main` PR

## Scope

one public release Pull Request boundary.

## Claim

**the Operator** **must** discover, create, or update exactly one actual open PR from the selected `amm/dev` head to `main` on the selected personal remote.

## Details

Zero matches permits create after the actual initial push. More than one match, a changed existing identity, or an unsafe/nonmatching URL blocks the Workflow.
