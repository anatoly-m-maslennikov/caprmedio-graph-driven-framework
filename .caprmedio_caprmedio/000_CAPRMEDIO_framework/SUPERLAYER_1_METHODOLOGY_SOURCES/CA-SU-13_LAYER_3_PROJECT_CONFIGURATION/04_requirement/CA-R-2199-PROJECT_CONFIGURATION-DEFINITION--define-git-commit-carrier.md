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
