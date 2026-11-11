---
atom_id: CA-R-2200
ref_id: CA-R-2200
container:
  scope_unit: CA-SU-13
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Carrier/Git Branch
tier: 1
status: Active
version: 7
updated_at: '2026-11-11 16:04:42 +0400'
carrier_destination:
  file:
    name: CA-R-2200-PROJECT_CONFIGURATION-DECLARATION--define-git-branch-carrier.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
---
## Summary

Define Git Branch Carrier

## Claim

### Prose Claim

A Git Branch is a repository-owned Carrier identifying a branch head.

### Formal Claim

```CFEL
# model
Carrier/Git Branch ((NARROWER_THAN)) Carrier;
```

## Semantics

A Git Repository contains its Git Branches; this is containment, not specialization.
