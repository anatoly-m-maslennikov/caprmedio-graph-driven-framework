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
---
## Summary

Define Git Branch Carrier

## Claim

### Formal Claim

```CFEL
Carrier/Git Branch
```

### Prose Claim

A Git Branch is a repository-owned Carrier identifying a branch head.

## Semantics

A Git Repository contains its Git Branches; this is containment, not specialization.
