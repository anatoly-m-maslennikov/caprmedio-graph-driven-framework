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
version: 6
updated_at: 2026-11-03 23:25:51 +0400
carrier_destination:
  file:
    name: CA-R-2200-PROJECT_CONFIGURATION-DECLARATION--define-git-branch-carrier.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/CA-R-2200-PROJECT_CONFIGURATION-DEFINITION--define-git-branch-carrier.md
  source_atom_id: CA-R-2200
  source_atom_revision: 6
  source_sha256: 8f4c6ba6ab906fab8026cce68c5c7a82ab76aa779e3886ffdf93c9d89fc913a2
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define Git Branch Carrier

## Claim

### Prose Claim

A Git Branch is a repository-owned Carrier identifying a branch head.

### Formal Claim

```CFEL
# model
Carrier/Git Branch
```

## Semantics

A Git Repository contains its Git Branches; this is containment, not specialization.
