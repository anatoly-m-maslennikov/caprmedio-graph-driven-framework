---
atom_id: CA-E-617@11
ref_id: CA-E-617@11
container:
  scope_unit: CA-SU-19
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - Subject/CAPRMEDIO/Carrier/Pull Request
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Quality/Verification
tier: 5
relations:
  evaluation_for:
  - CA-R-1927
  - CA-M-368
status: Archived
version: 11
updated_at: 2026-10-27 19:59:38 +0400
carrier_destination:
  file:
    name: CA-E-617@11-PROJECT_TOOLS-EVAL_CASE--validate-public-release-does-not-merge.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-19_FEATURE_PROJECT_TOOLS/06_evaluation/archive
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
author: Anatoly Maslennikov
---
# Summary

Validate public release does not merge

## Scope

one public-release effect declaration.

## Claim

**the Operator** **must** verify that the native public-release binding exposes no merge, approval, target-retargeting, protected-branch update, tag, or deployment effect and ends with an open PR result only.

## Details

The absence of merge is verified from the declared binding and mocked effect trace, not inferred from intent.
