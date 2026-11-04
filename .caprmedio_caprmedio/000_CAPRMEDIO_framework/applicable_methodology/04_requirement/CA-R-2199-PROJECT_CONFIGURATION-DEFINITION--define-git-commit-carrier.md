---
atom_id: CA-R-2199
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Carrier/Git Commit
version: 6
updated_at: 2026-11-03 23:25:51 +0400
relations: {}
tier: 1
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/CA-R-2199-PROJECT_CONFIGURATION-DEFINITION--define-git-commit-carrier.md
  source_atom_id: CA-R-2199
  source_atom_revision: 6
  source_sha256: 35ecfa5f7bfa50f2126188ec86bedf45765c921bf6bc11c0333599d2595e72f6
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define Git Commit Carrier

## Claim

### Formal Claim

```CFEL
# model
Carrier/Git Commit
```

### Prose Claim

A Git Commit is an immutable Carrier representing a committed repository snapshot and its commit metadata.

## Semantics

Its native identity is interpreted within its repository context. Author, signer and source facts remain provenance.
