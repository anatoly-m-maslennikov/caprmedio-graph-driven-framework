---
atom_id: CA-R-2526
ref_id: CA-R-2526
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit.ID
tier: 3
status: Active
version: 4
updated_at: 2026-11-04 05:21:15 +0400
---
## Summary

Declare Scope Unit ID

## Claim

### Formal Claim

```CFEL
# model
Scope Unit.ID:: [string]{::0..1};

Scope Unit.ID.*[]{::0};

# instances
IF (Scope Unit//$unit not in (Scope Unit/Project//$scope_unit))
THEN ($unit.ID{::1})
```

## Semantics

A non-root Scope Unit keeps its ID through moves and renames. The ID distinguishes those operations from removing that Scope Unit. The Project root has no Scope Unit ID because it cannot be moved or renamed through Scope Unit operations.
