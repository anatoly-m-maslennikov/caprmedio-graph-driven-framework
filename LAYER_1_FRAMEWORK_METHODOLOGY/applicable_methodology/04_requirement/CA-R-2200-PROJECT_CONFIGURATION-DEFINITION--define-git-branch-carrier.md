---
atom_id: CA-R-2200
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Carrier/Git Branch
version: 6
updated_at: 2026-11-03 23:25:51 +0400
relations: {}
tier: 1
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/CA-R-2200-PROJECT_CONFIGURATION-DEFINITION--define-git-branch-carrier.md
  source_atom_id: CA-R-2200
  source_atom_revision: 6
  source_sha256: 2c2dff0fb5096737abc02e985312434622dbd068591b0ad8d920c751228e39ac
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define Git Branch Carrier

## Claim

### Formal Claim

```CFEL
# model
Carrier/Git Branch
```

### Prose Claim

A Git Branch is a repository-owned Carrier identifying a branch head.

## Semantics

A Git Repository contains its Git Branches; this is containment, not specialization.
