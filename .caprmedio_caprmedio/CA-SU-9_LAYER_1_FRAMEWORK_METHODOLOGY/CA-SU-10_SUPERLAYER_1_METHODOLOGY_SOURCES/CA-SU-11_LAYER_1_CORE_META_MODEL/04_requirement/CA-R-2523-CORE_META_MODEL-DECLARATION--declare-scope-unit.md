---
atom_id: CA-R-2523
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Scope Unit
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---

## Summary

Declare Scope Unit

## Claim

```CFEL
Scope Unit >| (Container == yes);
Scope Unit//{:0..1}((IS_CONTAINED_BY)) Scope Unit//;
Scope Unit//{:0+}((CONTAINS)) Scope Unit//;
IF (Scope Unit//$unit not in (Scope Unit/Project//))
THEN ($unit {==1}((IS_CONTAINED_BY)) Scope Unit//);
Scope Unit ((NARROWER_THAN)) @Continuant
```

## Semantics

A Scope Unit defines a boundary of responsibility for Atoms.
