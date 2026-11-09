---
atom_id: CA-E-611@11
ref_id: CA-E-611@11
container:
  scope_unit: CA-SU-19
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
  dependencies:
  - Subject/CAPRMEDIO/Carrier/Git Repository
  - Subject/CAPRMEDIO/Carrier/Git Branch
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Quality/Verification
tier: 5
relations:
  evaluation_for:
  - CA-R-1921
  - CA-M-365
status: Archived
version: 11
updated_at: 2026-10-27 19:59:38 +0400
carrier_destination:
  file:
    name: CA-E-611@11-PROJECT_TOOLS-EVAL_CASE--validate-personal-remote-and-branch-boundary.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-19_FEATURE_PROJECT_TOOLS/06_evaluation/archive
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
author: Anatoly Maslennikov
---
# Summary

Validate personal remote and branch boundary

## Scope

the remote and branch fields of one public-release request.

## Claim

**the Operator** **must** verify that only an explicit personal remote with `amm/dev` head and `main` base is admitted, while missing remote identity, another scope, or any branch change is refused before effects.

## Details

The case verifies configuration boundaries, not remote credentials or GitHub access.
