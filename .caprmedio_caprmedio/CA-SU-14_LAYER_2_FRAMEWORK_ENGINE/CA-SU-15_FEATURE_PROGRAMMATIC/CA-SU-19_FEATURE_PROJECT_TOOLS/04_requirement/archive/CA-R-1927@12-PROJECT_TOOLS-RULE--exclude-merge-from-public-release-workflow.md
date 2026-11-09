---
atom_id: CA-R-1927@12
ref_id: CA-R-1927@12
container:
  scope_unit: CA-SU-19
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
status: Archived
version: 12
updated_at: 2026-10-27 20:00:05 +0400
carrier_destination:
  file:
    name: CA-R-1927@12-PROJECT_TOOLS-RULE--exclude-merge-from-public-release-workflow.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-19_FEATURE_PROJECT_TOOLS/04_requirement/archive
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
author: Anatoly Maslennikov
---
# Summary

Exclude merge from public-release Workflow

## Scope

one public-release Workflow execution.

## Claim

**the Operator** **must not** merge, approve, retarget, or otherwise adopt the public PR through this Workflow.

## Details

The terminal public result is an actual open or updated PR with evidence, not a release merge, protected-branch update, tag, or deployment.
