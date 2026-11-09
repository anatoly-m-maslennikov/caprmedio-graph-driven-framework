---
atom_id: CA-R-1920@12
ref_id: CA-R-1920@12
container:
  scope_unit: CA-SU-19
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
tier: 3
status: Archived
version: 12
updated_at: 2026-10-27 20:00:05 +0400
carrier_destination:
  file:
    name: CA-R-1920@12-PROJECT_TOOLS-RULE--require-explicit-operator-invocation-for-public-release.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-19_FEATURE_PROJECT_TOOLS/04_requirement/archive
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
author: Anatoly Maslennikov
---
# Summary

Require explicit Operator invocation for public release

## Scope

one public-release Workflow invocation.

## Claim

**the Operator** **must** explicitly authorize the exact selected public-release request, definition manifest, source-currentness proof, effect set, and personal remote before a public commit, push, or PR effect begins.

## Details

Preview, preparation, and planning do not authorize execution. Missing, stale, or differently bound authorization stops before any remote effect.
