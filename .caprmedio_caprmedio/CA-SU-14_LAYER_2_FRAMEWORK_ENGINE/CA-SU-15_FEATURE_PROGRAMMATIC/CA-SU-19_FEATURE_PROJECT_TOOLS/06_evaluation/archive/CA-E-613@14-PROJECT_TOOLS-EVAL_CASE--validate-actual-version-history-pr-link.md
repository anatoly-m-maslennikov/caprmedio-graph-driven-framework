---
atom_id: CA-E-613@14
ref_id: CA-E-613@14
container:
  scope_unit: CA-SU-19
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
  dependencies:
  - Subject/CAPRMEDIO/Carrier/Pull Request
tier: 5
relations:
  evaluation_for:
  - CA-R-1923
  - CA-M-366
status: Archived
version: 14
updated_at: 2026-10-27 19:59:38 +0400
carrier_destination:
  file:
    name: CA-E-613@14-PROJECT_TOOLS-EVAL_CASE--validate-actual-version-history-pr-link.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-19_FEATURE_PROJECT_TOOLS/06_evaluation/archive
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
author: Anatoly Maslennikov
---
# Summary

Validate actual Version History PR link

## Scope

one public Version History entry.

## Claim

**the Operator** **must** verify that an existing matching PR is linked before the initial public push, while a newly created PR causes finalization with its returned URL and never accepts a guessed URL or placeholder.

## Details

The entry contains only the concise selected-Version summary and that actual hyperlink.
