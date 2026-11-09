---
atom_id: CA-E-613
ref_id: CA-E-613
container:
  scope_unit: CA-SU-27
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
status: Active
version: 15
updated_at: 2026-11-09 15:54:30 +0400
carrier_destination:
  file:
    name: CA-E-613-FRAMEWORK_DELIVERY-EVAL_CASE--validate-actual-version-history-pr-link.md
    path: .caprmedio_caprmedio/CA-SU-27_LAYER_5_FRAMEWORK_DELIVERY/06_evaluation
current_scope_unit: FRAMEWORK_DELIVERY
claim_target_scope_unit: FRAMEWORK_DELIVERY
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
