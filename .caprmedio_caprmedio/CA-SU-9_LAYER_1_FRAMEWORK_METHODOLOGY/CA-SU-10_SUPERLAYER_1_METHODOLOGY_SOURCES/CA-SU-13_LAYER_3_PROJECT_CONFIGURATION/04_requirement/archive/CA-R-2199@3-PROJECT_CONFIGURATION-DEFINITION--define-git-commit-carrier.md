---
atom_id: CA-R-2199@3
content_role: Requirement
type: Definition
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Entity/Carrier/Git Commit
version: 3
updated_at: 2026-10-29 07:17:27 +0400
relations: {}
tier: 1
---
# Summary

Define Git Commit Carrier

## Claim

A Git Commit **means** an immutable Carrier representing a committed repository snapshot and its commit metadata.

## Semantics

Its native commit identity is interpreted within its repository context. Author, signer and source facts remain provenance.
