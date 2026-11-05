---
atom_id: CA-R-2199
ref_id: CA-R-2199
container:
  scope_unit: CA-SU-13
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Carrier/Git Commit
tier: 1
status: Active
version: 6
updated_at: 2026-11-03 23:25:51 +0400
carrier_destination:
  file:
    name: CA-R-2199-PROJECT_CONFIGURATION-DECLARATION--define-git-commit-carrier.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/CA-R-2199-PROJECT_CONFIGURATION-DEFINITION--define-git-commit-carrier.md
  source_atom_id: CA-R-2199
  source_atom_revision: 6
  source_sha256: a2adb784da1616932699b3a2901c6e27f150b6e39e239852d0c7a3052c3dba11
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define Git Commit Carrier

## Claim

### Prose Claim

A Git Commit is an immutable Carrier representing a committed repository snapshot and its commit metadata.

### Formal Claim

```CFEL
# model
Carrier/Git Commit
```

## Semantics

Its native identity is interpreted within its repository context. Author, signer and source facts remain provenance.
