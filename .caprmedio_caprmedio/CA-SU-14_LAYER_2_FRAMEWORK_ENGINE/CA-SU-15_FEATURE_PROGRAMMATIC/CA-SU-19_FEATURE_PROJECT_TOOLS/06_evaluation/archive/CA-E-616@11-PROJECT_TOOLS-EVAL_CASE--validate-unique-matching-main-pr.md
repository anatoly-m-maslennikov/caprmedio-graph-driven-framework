---
atom_id: CA-E-616@11
ref_id: CA-E-616@11
container:
  scope_unit: CA-SU-19
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
  dependencies:
  - Subject/CAPRMEDIO/Carrier/Pull Request
  - Subject/CAPRMEDIO/Carrier/Git Repository
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Quality/Verification
tier: 5
relations:
  evaluation_for:
  - CA-R-1926
  - CA-M-368
status: Archived
version: 11
updated_at: 2026-10-27 19:59:38 +0400
carrier_destination:
  file:
    name: CA-E-616@11-PROJECT_TOOLS-EVAL_CASE--validate-unique-matching-main-pr.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-19_FEATURE_PROJECT_TOOLS/06_evaluation/archive
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
author: Anatoly Maslennikov
---
# Summary

Validate unique matching `main` PR

## Scope

one public-release PR discovery and update.

## Claim

**the Operator** **must** verify that zero matching PRs permits creation only after the initial push, one matching PR is reused, and duplicate, retargeted, closed, or URL-changed results stop before further material preparation or remote effects.

## Details

The final refresh must retain the same actual PR URL returned by the initial upsert.
