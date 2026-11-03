---
atom_id: CA-R-2199
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Carrier/Git Commit
version: 5
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 1
role: Requirement
form: Entity Definition
---
## Summary

Define Git Commit Carrier

## Claim

A Git Commit **means** an immutable Carrier representing a committed repository snapshot and its commit metadata.

## Semantics

Its native commit identity is interpreted within its repository context. Author, signer and source facts remain provenance.
