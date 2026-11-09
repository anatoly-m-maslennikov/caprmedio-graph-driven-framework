---
atom_id: CA-M-368@13
ref_id: CA-M-368@13
container:
  scope_unit: CA-SU-19
role: Method
form: Eng Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
  dependencies:
  - Subject/CAPRMEDIO/Carrier/Git Commit
  - Subject/CAPRMEDIO/Carrier/Git Repository
  - Subject/CAPRMEDIO/Carrier/Pull Request
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution
tier: 4
relations:
  method_for:
  - CA-R-1925
  - CA-R-1926
  - CA-R-1927
status: Archived
version: 13
updated_at: 2026-10-27 19:59:42 +0400
carrier_destination:
  file:
    name: CA-M-368@13-PROJECT_TOOLS-ENG_DECISION--bind-public-remote-effects-to-one-pr-identity.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-19_FEATURE_PROJECT_TOOLS/05_method/archive
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
author: Anatoly Maslennikov
---
# Summary

Bind public remote effects to one PR identity

## Scope

the selected `amm/dev` push and `main` PR maintenance sequence.

## Claim

**the Operator** **must** use admitted native bindings to prove the immutable pushed commit and retain exactly one matching open PR identity through its create/update and any final refresh.

## Details

The bindings may use local subprocess facilities after their own admission; this Method adds no MCP prerequisite. It excludes merge and makes an identity change a stop condition.
