---
atom_id: CA-R-2199
content_role: Requirement
type: Definition
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Subject/CAPRMEDIO/Carrier/Git Commit
version: 2
updated_at: 2026-10-27 20:00:09 +0400
relations: {}
tier: 1
---
# Summary

Define Git Commit Carrier

## Claim

A Git Commit **means** an immutable Carrier representing a committed repository snapshot and its commit metadata.

## Semantics

Its native commit identity is interpreted within its repository context. Author, signer and source facts remain provenance.
