---
atom_id: CA-R-1927
ref_id: CA-R-1927
container:
  scope_unit: CA-SU-27
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - Subject/CAPRMEDIO/Carrier/Pull Request
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery/Git Commits
tier: 3
status: Active
version: 13
updated_at: 2026-11-09 15:54:30 +0400
carrier_destination:
  file:
    name: CA-R-1927-FRAMEWORK_DELIVERY-RULE--exclude-merge-from-public-release-workflow.md
    path: .caprmedio_caprmedio/CA-SU-27_LAYER_5_FRAMEWORK_DELIVERY/04_requirement
current_scope_unit: FRAMEWORK_DELIVERY
claim_target_scope_unit: FRAMEWORK_DELIVERY
author: Anatoly Maslennikov
relations: {}
---

# Summary

Exclude merge from public-release Workflow

## Scope

one public-release Workflow execution.

## Claim

**the Operator** **must not** merge, approve, retarget, or otherwise adopt the public PR through this Workflow.

## Details

The terminal public result is an actual open or updated PR with evidence, not a release merge, protected-branch update, tag, or deployment.
